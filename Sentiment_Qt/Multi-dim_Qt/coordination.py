import nltk
import pprint
from os import walk

class Splitter(object):
        def __init__(self):
                self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
                self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

        def split(self, text):
                sentences = self.nltk_splitter.tokenize(text)
                tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
                return tokenized_sentences

class DictionaryRator(object):
	def __init__(self, dictionary_path):
		dfile = open(dictionary_path, 'r')
		self.words = []
		self.valence_avg = []
		self.valence_stddev = []
		self.arousal_avg = []
		self.arousal_stddev = []
		while 1:
			line = dfile.readline()
			if not line:
				break
			#print line.split()
			contents = line.split()
			self.words.append(contents[0])
			self.valence_avg.append(float(contents[2]))
			self.valence_stddev.append(float(contents[3][1:-1]))
			self.arousal_avg.append(float(contents[4]))
			self.arousal_stddev.append(float(contents[5][1:-1]))
		#pprint.pprint(words)

	def print_dictionary(self):
		length = len(self.words)
		print length
		for i in range(0, length):
			print (self.words[i], self.valence_avg[i], self.valence_stddev[i], self.arousal_avg[i], self.arousal_stddev[i])

	def find(self, word):
		for i in range(0, len(self.words)):
			if word == self.words[i]:
				return i
		return -1

	def sentence_score(self, sentence, valence, valence_w, arousal, arousal_w):
		if not sentence:
			return valence, arousal
		else:
			#print sentence
			word = sentence[0]
			pos = self.find(word)
			if pos >= 0:
				valence = valence * valence_w + self.valence_avg[pos] / self.valence_stddev[pos]
				valence_w = valence_w + 1 / self.valence_stddev[pos]
				valence = valence / valence_w
				arousal = arousal * arousal_w + self.arousal_avg[pos] / self.arousal_stddev[pos]
				arousal_w = arousal_w + 1 / self.arousal_stddev[pos]
				arousal = arousal / arousal_w
			return self.sentence_score(sentence[1:], valence, valence_w, arousal, arousal_w)
	
	def sentiment_score(self, review):
		v = 0
		a = 0
		i = 0
		for sentence in review:
			(x , y) = self.sentence_score(sentence, 0, 0, 0, 0)
			#print x, y
			if x>0 and y>0:
				v += x
				a += y
				i += 1
		if i == 0:
			return (5, 5)
		else:
			return v / i, a / i
		


out = open("output", 'w')
splitter = Splitter()
rator = DictionaryRator('ANEW.txt')

yelp_path = "twitter"
for (dirpath, dirnames, filenames) in walk(yelp_path):
	shop = dirpath[len(yelp_path) + 1 :]
	for filename in filenames:
		f = open(dirpath + '/' + filename, 'r')
		print dirpath + '/' + filename
		#out.write(dirpath + '/' + filename + '\n')
		review = ""
		while 1:
			line = f.readline()
			if not line:
				break
			review = review + line.decode('ascii', 'ignore')
		#print review
		splitted_sentences = splitter.split(review)
		#print shop + ' ' + repr(rator.sentiment_score(splitted_sentences))
		out.write( repr(rator.sentiment_score(splitted_sentences)) + '\n' )
		out.write( shop + '\n' )

out.close()


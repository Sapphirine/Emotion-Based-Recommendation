import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;

import java.io.*;


public class Twitterdata {
	public static void main(String[] args) throws TwitterException, IOException{
		
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true)
		  .setOAuthConsumerKey("***")
		  .setOAuthConsumerSecret("***")
		  .setOAuthAccessToken("***")
		  .setOAuthAccessTokenSecret("***");
//		TwitterFactory tf = new TwitterFactory(cb.build());
//		Twitter twitter = tf.getInstance();
		
		
	    StatusListener listener = new StatusListener(){
	    	@Override
	        public void onStatus(Status status) {        	
	            
	            try{
	            BufferedWriter name=new BufferedWriter(new FileWriter(new File("username.txt"),true));
	            BufferedWriter text=new BufferedWriter(new FileWriter(new File("text.txt"),true));
	            if(status.getText().length()>100){
	            System.out.println(status.getUser().getName() + " : " + status.getText());
	            name.write(status.getUser().getName() + "\n");	            
	            text.write(status.getText()+"\n");	 
	            }
	            name.close();
	            text.close();
	            
	            }catch(Exception ex){
	            	System.out.println("exception in wirte file");
	            }
	        }
	        public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) {}
	        public void onTrackLimitationNotice(int numberOfLimitedStatuses) {}
	        public void onException(Exception ex) {
	            ex.printStackTrace();
	        }
			@Override
			public void onScrubGeo(long arg0, long arg1) {
				// TODO Auto-generated method stub
				
			}
			@Override
			public void onStallWarning(StallWarning arg0) {
				// TODO Auto-generated method stub
				
			}
	    };
	    
/*	    FilterQuery tweetFilterQuery = new FilterQuery(); // See 
	    tweetFilterQuery.track(new String[]{"Food", "Restaurant","Happy","Sad"}); // OR on keywords
	    tweetFilterQuery.locations(new double[][]{new double[]{-74,40,-73,41},
	                    }); // See https://dev.twitter.com/docs/streaming-apis/parameters#locations for proper location doc. 
	    //Note that not all tweets have location metadata set.
	    tweetFilterQuery.language(new String[]{"en"}); // Note that language does not work properly on Norwegian tweets 
	    TwitterStream twitterStream = new TwitterStreamFactory().getInstance();
	    twitterStream.addListener(listener);
	    // sample() method internally creates a thread which manipulates TwitterStream and calls these adequate listener methods continuously.
	   // twitterStream.sample();
	    twitterStream.filter(tweetFilterQuery);
	    */
	    
	    TwitterStream twitterStream = new TwitterStreamFactory(cb.build()).getInstance();
	    twitterStream.addListener(listener);
	    FilterQuery tweetFilterQuery = new FilterQuery(); // See 
	    tweetFilterQuery.track(new String[]{"Bieber", "Teletubbies"}); // OR on keywords
	    tweetFilterQuery.locations(new double[][]{new double[]{-126.562500,30.448674},
	                    new double[]{-61.171875,44.087585
	                    }}); // See https://dev.twitter.com/docs/streaming-apis/parameters#locations for proper location doc. 
	    //Note that not all tweets have location metadata set.
	    tweetFilterQuery.language(new String[]{"en"});
	    twitterStream.filter(tweetFilterQuery);
	}
	
	
}

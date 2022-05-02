#the code below allows us to get 1 tweet from twitter
#we are using this code to see if and what we can scrape from twitter

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "covid"
limit = 1
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet))  #vars function to see all the attributes of this tweet
    break #break the for loop

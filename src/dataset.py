#Importing neccessary libraries to read the dataset
import json
import pandas as pd

# Input data files are available in the "./dataset/" directory.
# Read the input raw data and parse only the necessary columns from the json file.

def main():
    """
    This function reads the raw twitter dataset and takes no arguments.
    Returns dataframe obtained from populate_tweet_df()
    """
    tweet_file = ("../dataset/tweets_parisagreement_09-03-2020.txt")
    tweets = []
    with open(tweet_file, 'r') as file:
        for line in file.readlines():
            tweets.append(json.loads(line))
    return populate_tweet_df(tweets)

def populate_tweet_df(tweets):
    """
    This function takes tweets list as argument and returns a dataframe of the tweets.
    """
    df = pd.DataFrame()
    df['text'] = [tweet['text'] for tweet in tweets if (tweet['lang'] == 'en')]
    # df['text'] = list(map(lambda tweet:tweet['text'], filter(lambda tweet: tweet['lang']=='en', tweets)))
    return df

if __name__ == '__main__':
    tweets_df = main()
    tweets_df.to_csv("../dataset/tweets.csv", index=False)

import SentimentData as sdc
import TweetAnalysisUtil as ta
import TwitterClient as tc
from OSCRunner import OSCRunner as osc
from datetime import datetime as dta
from time import sleep
import sys

def runSent(sent_data, query):
    """

    :param sent_data: The filename for the sentiment dictionary
    :param query: The query to search
    :return: A list containing the positive percentage and the negative percentage
    """
    dt = dta.now()
    day = str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)
    log_file = query + day + ".txt"
    client = tc.TwitterClient()
    client.connect()
    tweets = ta.parseSearchResultsForText(client.search(query))

    pos_count = 0
    neg_count = 0
    for tweet_text in tweets:
        if ta.isApplicable(tweet_text, sent_data, 2):
            mean_valence = ta.calculateTweetValence(tweet_text, sent_data)
            if (mean_valence > 5.5):
                #NOTE: 5.5 IS COMPLETELY ARBITRARY. RECOMMEND IMPLEMENTING SYSTEM TO DETERMINE AVERAGE
                #FOR A SPECIFIC SEARCH QUERY AND DECIDE AGAINST THAT
                pos_count += 1
            if (mean_valence < 5.5):
                neg_count += 1
    pos_per = int((pos_count / (pos_count + neg_count)) * 100)
    neg_per = int((neg_count / (pos_count + neg_count)) * 100)
    return [pos_per, neg_per]

def main(argv):
    usg_str = "usage: python Engine.py [query] [sentiment dictionary file] [sleep value]"
    if len(argv) != 4:
        print(usg_str)
        exit(0)

    query = argv[1]
    sent_file = argv[2]
    sleep_val = int(argv[3])

    sd = sdc.SentimentData(sent_file)
    hold_data = sd.getSentimentData()

    osc_runner = osc("127.0.0.1", 6448, "/wek/inputs")
    osc_runner.instantiate_udp()

    while True:
        data = runSent(hold_data, query)
        #data[0] is the positivity percentage
        osc_runner.send_message(data[0] / 100)
        sleep(sleep_val)

main(sys.argv)
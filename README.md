# Feature Extraction Project - Week 5

Jonathan Meade  
CSCI-4830  
Dr. Ben Shapiro  

## Usage

Please note that you must get a Twitter consumer API key to plug into Engine.py, available [here](https://apps.twitter.com).  
Simply run the script with  
```
python Engine.py [search query] [sentiment dictionary] [sleep time between queries]
```

## Project Goals

The goals of my project were to take a stream of real-time tweets from Twitter about a given subject and train an algorithim to display a certain color depending
on the overall sentiment of the tweets which were being published about said subject at the time.  

## Tools and Libraries Used
* Python 3.6.4
* [Tweepy](https://www.tweepy.org)

## Accomplishments

I was able to produce an output which displayed brighter colors when the overall sentiment about a topic was positive
and darker hues when the overall sentiment was negative.

## ML Choices
### Algorithm
I chose to use a linear regression model because of the nature of the features that I extracted. They all stay inside
of a defined range between 0 and 1. I also intended to build a regression model that changed its output on a linear
scale, and, taking that into consideration, the model that would construct a linear equation based on the
input data was by far the best choice.

Please note that the positivity ranking extractor uses a naive algorithm itself and does not weight words based on the
severity with which people react to the words.

### Inputs
The algorithm was trained on the following inputs:
* Positive: ['candy':avg 88% pos, 'dog':avg 84% pos, 'happy':avg 96% pos, 'smile':avg 96% pos]
* Negative: ['hurt':avg 14% pos,'crisis':avg 25% pos, 'tragedy':avg 13% pos]

## Example Tests
Testing against the keyword 'beautiful' produces this lovely pink color
![beautiful_pink](https://raw.githubusercontent.com/meadej/I-FeatExt-Meade/master/readme_imgs/beautiful.PNG)

Testing against the keyword 'weed' (a surprisingly controversial topic on Twitter) produces this middle of the ground
orange

![weed_orange](https://raw.githubusercontent.com/meadej/I-FeatExt-Meade/master/readme_imgs/weed.PNG)


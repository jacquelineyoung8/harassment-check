
import json
import csv 
from watson_developer_cloud import AlchemyLanguageV1


def checkForBadWords(text):
	text_list = text.split()
	bad_words = []
	bad_words.append(False) #0th element is true or false, the rest are the bad words 
	with open('Terms-to-Block.csv', 'rb') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader: 
				for word in text_list: 
					if word == row[1][0:len(row[1])-1]: #compare word in text string to a bad word
						bad_words.append(word)

	if len(bad_words) > 1: 
		bad_words[0] = True 
	return bad_words

mean_tweets = ["you are such a dumb shit", "crooked hillary is not qualified to be president", "oriental women are more attractive", "black men are more dangerous", "dogs are better than cats"]

bad_tweets = []
for tweet in mean_tweets:
	alchemy_language = AlchemyLanguageV1(api_key='352784ebf5a02644225cb5eda97e76da20788915')
	response = json.dumps(
  alchemy_language.emotion(
    text=tweet),
  indent=2)

	response =json.loads(response)
# 	if float(response["docEmotions"]["anger"])> 0.25 or float(response["docEmotions"]["disgust"]) > 0.25: 
# 		bad_tweets.append(tweet)
# print bad_tweets
	print tweet 
	print checkForBadWords(tweet)



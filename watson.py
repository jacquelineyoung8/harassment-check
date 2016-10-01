
import json
import csv 
from watson_developer_cloud import AlchemyLanguageV1


def checkForBadWords(text):
	'''returns a list w/ the zeroth element as True (for containing a bad word) and False for not containing a bad word, 
	if True, the list will also contain the bad words that occured in the text'''
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


def checkForRacialSlurs(text): 
	text_list = text.split()
	bad_words = []
	bad_words.append(False) #0th element is true or false, the rest are the bad words 
	with open('racial_slurs.csv', 'rb') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader: 
				for word in text_list: 
					if word == row[0].lower(): #compare word in text string to a racial discriminatory word
						bad_words.append(word)
	if len(bad_words) > 1: 
		bad_words[0] = True 
	return bad_words


def findDisgustedAngry(text): 
	'''returns true if the text is disgusted and angry'''
	alchemy_language = AlchemyLanguageV1(api_key='352784ebf5a02644225cb5eda97e76da20788915')
	response = alchemy_language.emotion(text=text)
	if float(response["docEmotions"]["anger"])> 0.25 and float(response["docEmotions"]["disgust"]) > 0.25: 
		return True
	else: 
		return False

def createDict():
	advice_dict = {}
	with open('our_advice.tsv', 'rb') as advice:
		for line in advice: 
			line_dict = line.split("	")
			advice_dict[line_dict[0]] = line_dict[1]
	return advice_dict

def everything(text):
	# if findDisgustedAngry(text): 
 #  		print (text + " seems angry and disgusted")
 #  	if checkForBadWords(text)[0]:
 #  		print (text + " contains some bad words")
 	my_advice = createDict()
 	all_bad = []
 	racial_slurs = checkForRacialSlurs(text)
 	bad_words = checkForBadWords(text)
 	both_lists = racial_slurs + bad_words
 	for bad_word in both_lists: 
 		if bad_word != True or bad_word != False: 
 			all_bad.append(bad_word)
 	for word in all_bad: 
 		if word in my_advice.keys(): 
 			return my_advice[word]

print everything('you are a slut')





#everything("you're a dumb slut")





# Imports for ocr
import json
import requests
import re

# Imports for text analysis
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions

image_url = 'https://i.pinimg.com/originals/2f/a9/38/2fa938ef1403574d42553b5ede952bb4.png'
# image_url = ''
text = ''

def config(url):
	global image_url, text
	# image_url = url
	# Config for ocr
	API_ENDPOINT = 'https://api.havenondemand.com/1/api/sync/ocrdocument/v1'
	apikey = '31fa3841-77d5-453b-8ef4-e78c192ecd75'
	PARAMS = {'apikey': apikey, 'url': image_url}
	r = requests.get(url=API_ENDPOINT, params= PARAMS)
	data = r.json()
	text = data['text_block'][0]['text']

# Config for text analysis
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='e624d94c-0e1d-449c-a0c3-4e6ba839918b',
  password='axlca4eonzhv',
  version='2018-03-16')

# phone_regex_in = re.compile(r'((\+*)((0[ -]+)*|(91 )*)(\d{12}+|\d{10}+))|\d{5}([- ]*)\d{6}')
# # phone_regex_rest = re.compile(r'''(
# 	(\d{3}|\(\d{3}\))?                # area code
# 	(\s|-|\.)?                        # separator
# 	(\d{3})                           # first 3 digits
# 	(\s|-|\.)                         # separator
# 	(\d{4})                           # last 4 digits
# 	(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
# 	)''', re.VERBOSE)

# emailRegex = re.compile(r'''(
# 	[a-zA-Z0-9._%+-]+      # username
# 	@                      # @ symbol
# 	[a-zA-Z0-9.-]+         # domain name
# 	(\.[a-zA-Z]{2,4})      # dot-something
# 	)''', re.VERBOSE)

# job_regex = re.compile(r'work|skills|experience|projects|expertise', re.IGNORECASE)
# lines = text.split('\n')

def get_response(text):
	response = natural_language_understanding.analyze(
						text = text,
						features=Features(
						entities=EntitiesOptions(
						  emotion=True,
						  sentiment=True,
						  limit=2),
						keywords=KeywordsOptions(
						  emotion=True,
						  sentiment=True,
						  limit=2)))
	return response['keywords']

# for line in lines:
# 	searchText = job_regex.search(line)
# 	if searchText:
# 		keywords = get_response(line)
# 		for word in keywords:
# 			print(word['text'])


# print(email.group())

def getFinalText():
	# global email, lines, job_regex
	global text
	emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+      # username
	@                      # @ symbol
	[a-zA-Z0-9.-]+         # domain name
	(\.[a-zA-Z]{2,4})      # dot-something
	)''', re.VERBOSE)
	email = emailRegex.search(text)

	job_regex = re.compile(r'work|skills|experience|projects|expertise', re.IGNORECASE)
	
	lines = text.split('\n')

	finalText = ''
	for line in lines:
		searchText = job_regex.search(line)
		if searchText:
			keywords = get_response(line)
			for word in keywords:
				print(word['text'])
				finalText = finalText + word['text'] + ', ' 
	finalText = finalText + '\nEmail: ' + email.group()
	return finalText 




from __future__ import print_function
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, RequestContext
import MySQLdb
import datetime as dt
from datetime import datetime
from twperson.models import UserTw, Status

# Create your views here.
from django.core.management.base import BaseCommand, CommandError
from twperson.models import UserTw, Status
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
# Create your views here.
ckey="NhKXNHp5u9yTtNZdmHGs5NCtd"
csecret="LKHqoFsCCAnPZGe9IXEkwpCv0LQVvdtvRJSqPkKnKpuILr22ml"
atoken="523419774-rXzTBTkVQW6XqO7vimDhSf5l6TgAPiJAwuyiN13t"
asecret="yncMCCkfPPwz0d22BfszVVamKiQ5b1Os7fkn4mCTNduqx"
# Create your views here.

# Personality Insights credentials and URL
#
# You can obtain these credentials by binding a PI service to an application in bluemix and 
# and clicking the "show credentials" link on the service in the application dashboard.
# Or you can use "cf env <application name>" from the command line to get the credentials.

pi_url = ''
pi_username = ''
pi_password = ''



from twitter import Twitter, OAuth, TwitterHTTPError
import os

from alchemyapi import AlchemyAPI
import qsstats
from django.db.models import Count, Sum



#import datetime
from datetime import datetime
from datetime import timedelta





def search_tweets(q, count=5, result_type="recent"):
	"""
	    Returns a list of tweets matching a certain phrase (hashtag, word, etc.)
	"""
	t = Twitter(auth=OAuth(atoken, asecret, ckey, csecret))

	return t.search.tweets(q=q, result_type=result_type, count=count)


def user_timeline(q, count=5, result_type="recent"):
	"""
	    Returns a list of tweets matching a certain phrase (hashtag, word, etc.)
	"""
	t = Twitter(auth=OAuth(atoken, asecret, ckey, csecret))

	return t.statuses.user_timeline(screen_name=q, result_type=result_type, count=count)


#!/usr/bin/env python

#	Copyright 2013 AlchemyAPI
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


def dashboard(request):
	tweets_hashtag = search_tweets('DondeComienzaelCambio')
	count           = tweets_hashtag['search_metadata']['count']
	for user in range(int(count)):
		if not tweets_hashtag['statuses'][int(user)]['text'].startswith('RT'):
			user_text 			= tweets_hashtag['statuses'][int(user)]['text'].encode('ascii', 'ignore')
			created_at 			= tweets_hashtag['statuses'][int(user)]['created_at'].encode('ascii', 'ignore')
			#'Wed Oct 21 19:28:39 +0000 2015'
			clean_timestamp 	= datetime.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y')
			offset_hours 		= -3 #offset in hours for EST timezone
			#account for offset from UTC using timedelta                               
			created_at_local 	= clean_timestamp + timedelta(hours=offset_hours)
			
			user_id 			= tweets_hashtag['statuses'][int(user)]['user']['id']
			user_screen_name 	= tweets_hashtag['statuses'][int(user)]['user']['screen_name'].encode('ascii', 'ignore')
			user_description 	= tweets_hashtag['statuses'][int(user)]['user']['description']
			user_timelinen		= user_timeline(user_screen_name)
			user_timelinen		= [tweet['text'].encode('ascii', 'ignore') for tweet in user_timelinen if not tweet['text'].encode('ascii', 'ignore').startswith('RT')]
			#obtener personalidad desde los twittes 
			#for timeline in range(len(timelines)):
			#    print timelines[timeline]['text']
			#userTw, created = UserTw.objects.get_or_create(screen_name=user_screen_name, screen_id=user_id, description=user_description, timeline=user_timelinen)
			
			#llamar a watson
			#TODO add personality from watson "keywords": [{"relevance": "0.904619","text": "Justin Bieber"}
			#TODO add tweets from twitter 
			"""
			pi_content_items = { 'contentItems' : user_timelinen }

			personality = requests.post(config.pi_url + '/v2/profile', 
				auth=(config.pi_username, config.pi_password),
				headers = {
					'content-type': 'application/json',
					'accept': 'application/json'
				},
				data=json.dumps(pi_content_items)
			)
			"""
			personality = """{
							"id": "*UNKNOWN*",
							"source": "*UNKNOWN*",
							"word_count": 2196,
							"tree": {
							    "id": "r",
							    "name": "root",
							    "children": [
							      {
							          "id": "needs",
							          "name": "Needs",
							          "children": [
							            {
							                "id": "Practicality_parent",
							                "name": "Practicality",
							                "category": "needs",
							                "percentage": 0.9839864449532627,
							                "children": [
							                  {
							                      "id": "Challenge",
							                      "name": "Challenge",
							                      "category": "needs",
							                      "percentage": 0.6584166017026339,
							                      "sampling_error": 0.602517824
							                  },
							                  {
							                      "id": "Closeness",
							                      "name": "Closeness",
							                      "category": "needs",
							                      "percentage": 0.924529448337046,
							                      "sampling_error": 0.696857696
							                  },
							                  {
							                      "id": "Curiosity",
							                      "name": "Curiosity",
							                      "category": "needs",
							                      "percentage": 0.836074789385127,
							                      "sampling_error": 0.6318680640000001
							                  },
							                  {
							                      "id": "Excitement",
							                      "name": "Excitement",
							                      "category": "needs",
							                      "percentage": 0.8576434327454714,
							                      "sampling_error": 0.62010672
							                  },
							                  {
							                      "id": "Harmony",
							                      "name": "Harmony",
							                      "category": "needs",
							                      "percentage": 0.981853123726956,
							                      "sampling_error": 0.686543104
							                  },
							                  {
							                      "id": "Ideal",
							                      "name": "Ideal",
							                      "category": "needs",
							                      "percentage": 0.3425618908848262,
							                      "sampling_error": 0.603128032
							                  },
							                  {
							                      "id": "Liberty",
							                      "name": "Liberty",
							                      "category": "needs",
							                      "percentage": 0.3936046680718908,
							                      "sampling_error": 0.572532448
							                  },
							                  {
							                      "id": "Love",
							                      "name": "Love",
							                      "category": "needs",
							                      "percentage": 0.5237755189252377,
							                      "sampling_error": 0.721777024
							                  },
							                  {
							                      "id": "Practicality",
							                      "name": "Practicality",
							                      "category": "needs",
							                      "percentage": 0.9839864449532627,
							                      "sampling_error": 0.65719744
							                  },
							                  {
							                      "id": "Self-expression",
							                      "name": "Self-expression",
							                      "category": "needs",
							                      "percentage": 0.03828102978032242,
							                      "sampling_error": 0.64546576
							                  },
							                  {
							                      "id": "Stability",
							                      "name": "Stability",
							                      "category": "needs",
							                      "percentage": 0.7025224350455281,
							                      "sampling_error": 0.67650368
							                  },
							                  {
							                      "id": "Structure",
							                      "name": "Structure",
							                      "category": "needs",
							                      "percentage": 0.6938192628712627,
							                      "sampling_error": 0.026310336
							                  }
							                ]
							            }
							          ]
							      }
							    ]
							  }
							}"""
			personality = json.loads(personality)
			for nivel1 in personality['tree']['children']:
				for nivel2 in nivel1['children']:
					necesidades = nivel2['children']
					for children in nivel2['children']:
						if children['name'] == 'Challenge':
							challenge = children['percentage']
						if children['name'] == 'Closeness':
							closeness = children['percentage']
						if children['name'] == 'Curiosity':
							curiosity = children['percentage']
						if children['name'] == 'Excitement':
							excitement = children['percentage']
						if children['name'] == 'Harmony':
							harmony = children['percentage']
						if children['name'] == 'Ideal':
							ideal = children['percentage']
						if children['name'] == 'Liberty':
							liberty = children['percentage']
						if children['name'] == 'Love':
							love = children['percentage']
						if children['name'] == 'Practicality':
							practicality = children['percentage']
						if children['name'] == 'Self-expression':
							selfexpression = children['percentage']
						if children['name'] == 'Stability':
							stability = children['percentage']
						if children['name'] == 'Structure':
							structure = children['percentage']


						#necesidades.append(children)
						#necesidades = necesidad_tipo['children']
			userTw, created = UserTw.objects.update_or_create(
				screen_id=user_id,
				defaults={
					'screen_name': user_screen_name,
					'description': user_description,
					'timeline': user_timelinen,
					'personality': necesidades,
					'challenge': challenge,
					'closeness': closeness,
					'curiosity': curiosity,
					'excitement': excitement,
					'harmony': harmony,
					'ideal': ideal,
					'liberty': liberty,
					'love': love,
					'practicality': practicality,
					'selfexpression': selfexpression,
					'stability': stability,
					'structure': structure,
					'created': created_at_local,
					},
			)
			
			
			#llamar a alchemy
			#TODO add keyworkd from alchemylanguage "keywords": [{"relevance": "0.904619","text": "Justin Bieber"}
			#TODO add docSentiment from alchemylanguage "docSentiment": [{"score": "0.522221","type": "positive"}
			#TODO add tweets from twitter 
			# Create the AlchemyAPI Object
			alchemyapi = AlchemyAPI()

			response = alchemyapi.keywords('text', user_text, {'sentiment': 1})

			if response['status'] == 'OK':
				#print('## Response Object ##')
				#response = json.dumps(response, indent=4)

				## Keywords ##
				for keyword in response['keywords']:
					keywords = keyword['text'].encode('utf-8')
					if 'sentiment' in keyword:
						sentiment = keyword['sentiment']['type']
					else:
						sentiment = 'No disponible'

			status, created = Status.objects.get_or_create(text=user_text, usertw=user_screen_name, keywords=keywords, sentiment=sentiment, created_tw=created_at_local)
	users = UserTw.objects.all()
	status 	= Status.objects.all()


	#grafico usuarios registrados en la ultima semana
	GOOGLE_API_KEY = 'AIzaSyC5Lo0yTl79GUfvIfzEpfV3HhdFyG79OWY'
	qs = UserTw.objects.all()
	qss = qsstats.QuerySetStats(qs, 'created')
	hoy = dt.date.today()
	hace_1_semanas = hoy - dt.timedelta(weeks=1)
	usuarios_total = qs.count()
	usuarios_stats = qss.time_series(hace_1_semanas, hoy)
	#

	context = {"users": users, "status": status, "usuarios_stats": usuarios_stats, "usuarios_total":usuarios_total}
	return render(request, "index.html", context)


def home(request):
	users = UserTw.objects.all().count
	status 	= Status.objects.all().count
	context = {"users": users, "status": status}

	return render(request, "home.html", context)

import json
from graphqlclient import GraphQLClient

from Utility.Constants import *

def getEventSets(eventID, page=1, perPage=100):
	# Creating a graphql client and providing the OSUCorvallisMelee admin auth token
	client = GraphQLClient('https://api.start.gg/gql/' + apiVersion)
	client.inject_token('Bearer ' + startGGToken)

	# building the query, setting arguments, and executing the query
	queryResult = client.execute('''
	query EventSets($eventId: ID!, $page: Int!, $perPage: Int!) {
		event(id: $eventId) {
			id
			name
			sets(
				page: $page
			  	perPage: $perPage
			  	sortType: STANDARD
			) {
				pageInfo {
					total
			  	}
			  	nodes {
					id
					slots {
				  		id
				  		entrant {
							id
							name
				  		}
					}
			  	}
			}
		}
	}
	''',
	{
		"eventId": eventID,
		"page": page,
		"perPage": perPage
	})

	# loading the query result into a dictionary
	resultsDict = json.loads(queryResult)

	# now we need to parse the data into something more usable for future functions
	# dictionary: 	key - set id,
	# 				value - tuple (p1 set ID, p1 dict, p2 set ID, p2 dict)
	setsDict = dict()

	# getting the sets dictionary
	setsPlayedArry = resultsDict['data']['event']['sets']['nodes']

	for node in setsPlayedArry:
		# getting the assigned set ID
		setID = node['id']

		# getting the players in the set
		playersArry = node['slots']
		player1SetID = playersArry[0]['id']
		player1Info = playersArry[0]['entrant']
		player2SetID = playersArry[1]['id']
		player2Info = playersArry[1]['entrant']

		# loading the set information into the working dictionary
		setsDict[setID] = (player1SetID, player1Info, player2SetID, player2Info)

	return setsDict



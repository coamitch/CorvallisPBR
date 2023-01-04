import json
from graphqlclient import GraphQLClient

from Utility.Constants import *

def retrieveEventData(eventID: int, page=1, perPage=100):
	# Creating a graphql client and providing the OSUCorvallisMelee admin auth token
	client = GraphQLClient('https://api.start.gg/gql/' + apiVersion)
	client.inject_token('Bearer ' + startGGToken)
	
	# building the query, setting arguments, and executing the query
	queryResult = client.execute('''
	query EventSets($eventId: ID!, $page: Int!, $perPage: Int!) {
		event(id: $eventId) {
			id
			name
			tournament {
				name
			}
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
		"page"   : page,
		"perPage": perPage
	})
	
	# loading the query result into a dictionary for easier parsing
	return json.loads(queryResult)
	
def retrieveGameCount(setID: int):
	# Creating a graphql client and providing the OSUCorvallisMelee admin auth token
	client = GraphQLClient('https://api.start.gg/gql/' + apiVersion)
	client.inject_token('Bearer ' + startGGToken)
	
	# building the query, setting arguments, and executing the query
	queryResult = client.execute('''
	query set($setId: ID!) {
		set(id: $setId) {
			id
			slots {
				id
				standing {
					id
					placement
					stats {
						score {
							label
							value
						}
					}
				}
			}
		}
	}
	''',
	{
		"setId": setID,
	})
	
	return json.loads(queryResult)

def unpackTournament(eventID: int):
	# getting the event sets associated with the event ID
	eventData = retrieveEventData(eventID)
	
	# getting the sets dictionary
	setsPlayedArry = eventData['data']['event']['sets']['nodes']

	# creating a working dictionary to store the tournament data
	tournamentDict = dict()

	for node in setsPlayedArry:
		# getting the assigned set ID and game counts
		setID = node['id']
		gameCountRslts = retrieveGameCount(setID)
		workingArry = gameCountRslts['data']['set']['slots']
		
		# getting the players in the set
		playersArry = node['slots']

		player1SetID = playersArry[0]['id']
		player1Info = playersArry[0]['entrant']
		player1GameCount = workingArry[0]['standing']['stats']['score']['value']
		
		player2SetID = playersArry[1]['id']
		player2Info = playersArry[1]['entrant']
		player2GameCount = workingArry[1]['standing']['stats']['score']['value']


		# TODO: if the tournament doesn't have a winner then this check has to change
		# 	ex. fpf8 amateur bracket grand finals 
		if player1GameCount > player2GameCount:
			winnerID = player1Info['id']
		else:
			winnerID = player2Info['id']

		# creating a working dictionary to store the current set
		setDict = dict()
		
		# loading the information into the working dictionary
		setDict['player1'] = {'setID': player1SetID, 'playerInfo': player1Info, 'gamesWon': player1GameCount}
		setDict['player2'] = {'setID': player2SetID, 'playerInfo': player2Info, 'gamesWon': player2GameCount}
		setDict['winnerID'] = winnerID

		tournamentDict[setID] = setDict
		
	# saving the event and tournament names
	tournamentName = eventData['data']['event']['tournament']['name']
	eventName = eventData['data']['event']['name']

	return tournamentDict, tournamentName, eventName
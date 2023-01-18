import json
from graphqlclient import GraphQLClient

from Utility.Constants import *

def retrieveTournament(tournamentSlug):
	# Creating a graphql client and providing the OSUCorvallisMelee admin auth token
	client = GraphQLClient('https://api.start.gg/gql/' + apiVersion)
	client.inject_token('Bearer ' + startGGToken)

	# building the query, setting arguments, and executing the query
	queryResult = client.execute('''
		query TournamentQuery($slug: String!) {
			tournament(slug: $slug) {
				id
				name
				numAttendees
				events {
					id
				}
			}
		}
		''',
		{
			"slug": tournamentSlug
		})

	# loading the query result into a dictionary for easier parsing
	return json.loads(queryResult)

def unpackTournament(tournamentQueryRslt: dict):
	# getting event dictionary result from the query
	tournamentInfoDict = tournamentQueryRslt['data']['tournament']

	# creating a working dictionary to store the tournament data
	tournamentDict = dict()
	
	# storing general event information
	tournamentDict['id'] = tournamentInfoDict['id']
	tournamentDict['name'] = tournamentInfoDict['name']
	tournamentDict['numAttendees'] = tournamentInfoDict['numAttendees']
	tournamentDict['events'] = dict()

	# iterating through all the events
	for event in tournamentInfoDict['events']:
		# getting the event id
		eventID = event['id']

		# loading empty event dicts with key = event ID
		tournamentDict['events'][eventID] = dict()

	# returning the tournament dictionary
	return tournamentDict

def retrieveEventData(eventID: int, page=1, perPage=100):
	# Creating a graphql client and providing the OSUCorvallisMelee admin auth token
	client = GraphQLClient('https://api.start.gg/gql/' + apiVersion)
	client.inject_token('Bearer ' + startGGToken)
	
	# building the query, setting arguments, and executing the query
	queryResult = client.execute('''
	query EventData($eventId: ID!, $page: Int!, $perPage: Int!) {
		event(id: $eventId) {
			id
			name
			numEntrants
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

def unpackEvent(eventQueryRslt: dict):
	# getting event dictionary result from query
	eventInfoDict = eventQueryRslt['data']['event']

	# creating a working dictionary to store the tournament data
	eventDict = dict()

	# storing general event information
	eventDict['id'] = eventInfoDict['id']
	eventDict['name'] = eventInfoDict['name']
	eventDict['numEntrants'] = eventInfoDict['numEntrants']

	# storing set information
	# getting a list of all the sets played 
	setsPlayedArry = eventInfoDict['sets']['nodes']
	
	# iterating through all the sets played and storing information
	for node in setsPlayedArry:
		# getting the assigned set ID and game counts
		setID = node['id']

		# retrieving the game counts for the current set ID and unpacking the query result
		setInfoQueryRslt = retrieveSetInfo(setID)
		setDict = unpackSetInfo(setInfoQueryRslt)

		# storing the set in the event dictionary with key = set ID
		eventDict[setID] = setDict

	return eventDict

def retrieveSetInfo(setID: int):
	# Creating a graphql client and providing the OSUCorvallisMelee admin auth token
	client = GraphQLClient('https://api.start.gg/gql/' + apiVersion)
	client.inject_token('Bearer ' + startGGToken)

	# building the query, setting arguments, and executing the query
	queryResult = client.execute('''
	query SetInfo($setId: ID!) {
		set(id: $setId) {
			id
			round
			totalGames
			winnerId
			slots {
				id
				entrant {
					id
					name
				}
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

def unpackSetInfo(setInfoQueryRslt: dict):
	setInfoDict = setInfoQueryRslt['data']['set']

	# creating a working dictionary to store the current set
	setDict = dict()

	# storing general set information
	setDict['id'] = setInfoDict['id']
	setDict['round'] = setInfoDict['round']
	setDict['totalGames'] = setInfoDict['totalGames']
	setDict['winnerID'] = setInfoDict['winnerId']

	# getting the set slots (players in the set)
	playersArry = setInfoDict['slots']

	# iterating through the set players and storing their information
	for i in range(len(playersArry)):
		# creating a working dictionary to store player information
		setDict[f'player{i+1}'] = dict()

		# populating the working dictionary
		setDict[f'player{i+1}']['id'] = playersArry[i]['id']
		setDict[f'player{i+1}']['entrant'] = playersArry[i]['entrant']
		setDict[f'player{i+1}']['placement'] = playersArry[i]['standing']['placement']
		setDict[f'player{i+1}']['gamesWon'] = playersArry[i]['standing']['stats']['score']['value']

	# returning the populated set dictionary
	return setDict


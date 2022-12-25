import json
from graphqlclient import GraphQLClient

from Utility.Constants import *

# Create a GraphQL client using the defined transport
client = GraphQLClient('https://api.start.gg/gql/' + apiVersion)
client.inject_token('Bearer ' + startGGToken)

# Provide a GraphQL query
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
	"eventId": 828045,
	"page": 1,
	"perPage": 100
})

# loading the query result
setData = json.loads(queryResult)

print(setData)

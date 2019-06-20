import requests
import boto3

from dataworld import team


"""
Here is an example of the various json requests we are calling into for reference 


Scoreboard Data for a single matchup
====================================================================================
{}Json
    {}LeagueSchedule
        []scheduleitems
            {}0
                []matchups
                    {}0
                        []awayTeamScores
                        {}awayTeam
                            teamId
                            waiver rank    
                            













"""

# setting up some variables
class League(object):

    dynamodb = boto3.resource('dynamodb')
    dynamoTable = dynamodb.Table('test_table')

    def __init__(self, id_league, year_current, year_birth):
        self.id_league = id_league
        self.year_current = year_current
        self.year_birth = year_birth
        self.teams = []
        self._data_get()
        self._data_parse()
        self.teams_build()

    def _data_get(self):
        self.data = []
        for year in range(self.year_birth, self.year_current):
            print(year)
            r = requests.get('http://games.espn.com/ffl/api/v2/schedule',
                            params={'leagueId': self.id_league, 'seasonId': year},


            dynamoTable.put_item(r)

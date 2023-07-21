import requests
import json
import datetime

#wide-use variables DO NOT ALTER
TBAKEY = {
    'X-TBA-Auth-Key': 'XVHY1zwGfejtWKREuLSV7my72QA1F5990BXbQs2bbr16D8KyZotXhmCXB8V9N4Ny',
}
YEAR = datetime.date.today().year
CONFIRMATIONKEY = "FNC86f7YbsiPMq0p"

#get json of general team information with int param of team number from TBA API
def tba_team_info(teamNumber):
  response = requests.get("https://www.thebluealliance.com/api/v3/team/frc" + str(teamNumber), params=TBAKEY)
  return response.json()

#get json of team event information for the season with int param of team number from TBA API
def tba_team_event_info(teamNumber):
  response = requests.get("https://www.thebluealliance.com/api/v3/team/frc" + str(teamNumber) + "/events/" + YEAR, params=TBAKEY)
  return response.json()

#get json of team event keys for the season with int param of team number from TBA API
def tba_team_event_keys(teamNumber):
  response = requests.get("https://www.thebluealliance.com/api/v3/team/frc" + str(teamNumber) + "/events/" + YEAR + "/keys", params=TBAKEY)
  return response.json()

#get json of team match information for the season with int param of team number from TBA API
def tba_team_match_info(teamNumber):
  response = requests.get("https://www.thebluealliance.com/api/v3/team/frc" + str(teamNumber) + "/matches/" + YEAR, params=TBAKEY)
  return response.json()

#get json of event predictions for the season with string param of event key from TBA API
def tba_event_predictions(eventKey):
  response = requests.get("https://www.thebluealliance.com/api/v3/event/" + eventKey + "/predictions", params=TBAKEY)
  return response.json()

#get json of specific team performace information with int param of team number from Statbotics API
def statbotics_team_info(teamNumber):
  response = requests.get("https://api.statbotics.io/v2/team_year/" + str(teamNumber) + "/" + str(YEAR))
  return response.json()

#get json of specific team match information with int param of team number from Statbotics API
def statbotics_team_match_info(teamNumber):
  response = requests.get("https://api.statbotics.io/v2/matches/team/" + str(teamNumber) + "/year/" + str(YEAR))
  return response.json()

#get json of all teams and basic information from Statbotics API [no param]
def teams():
  response = requests.get("https://api.statbotics.io/v2/teams")
  return response.json()
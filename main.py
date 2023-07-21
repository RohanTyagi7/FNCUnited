from typing import Union
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json
import datetime
import info
import data
import scouts

app = FastAPI(
  title="FNC United",
  docs_url="/docs", 
  redoc_url=None,
)

favicon_path = 'FNCU.png'
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#team information model
class Team(BaseModel):
    number: int
    score: float
    match: str
    competition: str
    alliance: str
    top: int
    mid: int
    low: int
    cubes: int
    cones: int
    cycleTime: float
    cycles: int
    chargeStation: str
    defense: bool
    defenseScale: int
    autonTop: int
    autonMid: int
    autonLow: int
    autonChargeStation: str
    notes: str
    scoutId: int
    topTimes: dict
    midTimes: dict
    lowTimes: dict

#root hook
@app.get("/", tags=["Default"])
def read_root():
    return data.get()
  
@app.get('/status', tags=["Default"])
def status():
  return {"status":200}

@app.get('/team/{team_num}', tags=["Team Information"])
def get_all_team_information(team_num: int):
  datas = [{}]
  count = 0
  score = 0
  top = 0
  mid = 0
  low = 0
  cubes = 0
  cones = 0
  cycles = 0
  cycleTime = 0
  defenseScale = 0
  autonTop = 0
  autonMid = 0
  autonLow = 0
  for x in data.get():
    if x!= {} and x['number'] == team_num:
      count += 1
      score += x['score']
      top += x['top']
      mid += x['mid']
      low += x['low']
      cubes += x['cubes']
      cones += x['cones']
      cycles += x['cycles']
      cycleTime += x['cycleTime']
      defenseScale += x['defenseScale']
      autonTop += x['autonTop']
      autonMid += x['autonMid']
      autonLow += x['autonLow']
      if datas == [{}]:
        datas = json.loads("[" + json.dumps(x) + "]")
      else:
        datas = json.loads(json.dumps(data)[0:len(json.dumps(data))-1] + "," + json.dumps(x) + "]")
  try:
    score /= count
    top /= count
    mid /= count
    low /= count
    cubes /= count
    cones /= count
    cycles /= count
    cycleTime /= count
    defenseScale /= count
    autonTop /= count
    autonMid /= count
    autonLow /= count
    return({"TBA": info.tba_team_info(team_num), "Statbotics": info.statbotics_team_match_info(team_num), "FNCU": {"score": score, "top": top, "mid": mid, "low": low, "cubes": cubes, "cones": cones, "cycles": cycles, "cycleTime": cycleTime, "defenseScale": defenseScale, "autonTop": autonTop, "autonMid": autonMid, "autonLow": autonLow, "matches":datas}})
  except:
    return({"TBA": info.tba_team_info(team_num), "Statbotics": info.statbotics_team_match_info(team_num), "FNCU": {}})

@app.get('/teams', tags=["Team Information"])
def get_all_teams():
  data = info.teams()
  return data

@app.post('/add/team/{team_num}', tags=["Team Information"])
def add_team_information(team_num: int, item: Team):
  data.add(json.loads(json.dumps(item.__dict__)))
  return data.get()

#Rohan
@app.get('/predict/{match}', tags=["Event Information"])
def predict_match(match: str):
  return {"hello":"world"}

#Ethan
@app.get('/event/{event}', tags=["Event Information"])
def event_information(event: str):
  return {"hello":"world"}

#Rohan
@app.get('/team/{team}/event', tags=["Team Information"])
def event_information_for_team(team: str):
  return {"hello":"world"}

#Ethan
@app.get('/event/{match}', tags=["Event Information"])
def match_information_for_an_event(match: str):
  return {"hello":"world"}

#log in
@app.get('/login/{username}/{password}/{team}', tags=["Scout Account"])
def log_in_user(username: str, password: str, team: int):
  for x in scouts.get():
    if x != {} and x['username'] == username and str(scouts.unscramble(x['password'], x['key']), "utf-8") == password and x['team'] == team:
      return x
  return {}

#sign up
@app.get('/signup/{username}/{password}/{team}', tags=["Scout Account"])
def sign_up_user(username: str, password: str, team: int):
  for x in scouts.get():
    if x != {} and x['username'] == username:
      return {}
  return scouts.add(scouts.json_param(username, password, team))


#example of a get API hook without query
"""@app.get('/get/{item_id}')
def get_all_team_information(item_id: int):
  return {"hello":"world"}"""

#example of a post API hook with "Team" information hook as query
"""@app.post('/add/{item_id}')
def add_team_information(item_id: int, item: Team):
    return {"hello":"world"}"""

#run port DO NOT ALTER
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
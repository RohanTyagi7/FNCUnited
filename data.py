import requests
import json
import datetime

#wide-use variables DO NOT ALTER
TBAKEY = {
    'X-TBA-Auth-Key': 'XVHY1zwGfejtWKREuLSV7my72QA1F5990BXbQs2bbr16D8KyZotXhmCXB8V9N4Ny',
}
YEAR = datetime.date.today().year
CONFIRMATIONKEY = "FNC86f7YbsiPMq0p"

#get all json stored int json bin [no param]
def get():
  f = open('data.json')
  return json.load(f)

#find index of json object in json bin through json parameter
def index(data):
  count = 0
  list = []
  jsonData = get()
  for item in jsonData:
    if item == data:
      list.append(count)
    count += 1
  if list == []:
    return -1
  else:
    return list

#replace all json in bin with new json parameter
def post(data):
  with open('data.json', 'r+') as f:
    dataset = json.load(f)
    if json.dumps(data) == "[]":
      data = json.loads("[{}]")
    dataset = data
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

#add new json to existing json in bin through json parameter
def add(data):
  if(json.dumps(get()) != "[{}]"):
    jsonData = json.loads(json.dumps(get())[0:len(json.dumps(get()))-1] + "," + json.dumps(data) + "]")
    post(jsonData)
  else:
    post(json.loads("[" + json.dumps(data) + "]"))

#remove specific json from existing json in bin through json parameter
def remove(data):
  jsonData = get()
  jsonData.remove(data)
  post(jsonData)

#remove all json from json bin
def remove_all(confirm):
  if(confirm == CONFIRMATIONKEY):
    post([{}])
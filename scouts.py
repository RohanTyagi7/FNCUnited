import json
import datetime
from cryptography.fernet import Fernet
import random

#wide-use variables DO NOT ALTER
CONFIRMATIONKEY = "FNC86f7YbsiPMq0p"

#get all json stored int json bin [no param]
def get():
  f = open('scouts.json')
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

#scramble/encrypt password with one unique altered user-based key, returns [encrypted_text, user_based_key]
def scramble(password):
  key = Fernet.generate_key()
  cipher_suite = Fernet(key)
  encoded_text = cipher_suite.encrypt(bytes(password,"utf-8"))
  key = bytes("f" + str(random.randint(1,9)) + str(key[7:], "utf-8") + "t" + str(random.randint(1,9)) + str(key[0:7], "utf-8"), "utf-8")
  return [str(encoded_text, "utf-8"), key]

#uncramble/unencrypt password with one unique user-based key and one general server-based key, returns decrypted text
def unscramble(password, key):
  key = key[len(key)-7:] + key[2:len(key)-9]
  cipher_suite = Fernet(bytes(key,"utf-8"))
  decoded_text = cipher_suite.decrypt(password)
  return decoded_text

#replace all json in bin with new json parameter
def post(data):
  with open('users.json', 'r+') as f:
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
    return data
  else:
    post(json.loads("[" + json.dumps(data) + "]"))
    return(json.loads("[" + json.dumps(data) + "]"))

#remove specific json from existing json in bin through json parameter
def remove(data):
  jsonData = get()
  jsonData.remove(data)
  post(jsonData)

#remove all json from json bin
def remove_all(confirm):
  if(confirm == CONFIRMATIONKEY):
    post([{}])

def json_param(username, password, team):
  x = scramble(password)
  return {'username': username, 'password':x[0], 'creationDate':datetime.datetime.now().strftime("%x"), 'key': str(x[1],"utf-8"), 'rating': 5.0, 'team': team}

#provide amount of items in json bin
def length():
  x = 0
  for i in get():
    if i is not {}:
      x += 1
  return x
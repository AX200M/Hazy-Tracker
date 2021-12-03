import requests
import os
import time 
from time import sleep

def his():
    url = "https://covid-193.p.rapidapi.com/history"

    country = input("which country would you like to search for? ")
    day = input("Which date would you like to look at (YYYY-MM-DD)? ")
    querystring = {"country":country,"day":day}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "04ad1050c2msh6cad7306ab54c46p1c134fjsncc6fe8663bcf"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def stats():
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "04ad1050c2msh6cad7306ab54c46p1c134fjsncc6fe8663bcf"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def count():
    url = "https://covid-193.p.rapidapi.com/countries"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "04ad1050c2msh6cad7306ab54c46p1c134fjsncc6fe8663bcf"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


#main
print("""
  _    _                   _______             _             
 | |  | |                 |__   __|           | |            
 | |__| | __ _ _____   _     | |_ __ __ _  ___| | _____ _ __ 
 |  __  |/ _` |_  / | | |    | | '__/ _` |/ __| |/ / _ \ '__|
 | |  | | (_| |/ /| |_| |    | | | | (_| | (__|   <  __/ |   
 |_|  |_|\__,_/___|\__, |    |_|_|  \__,_|\___|_|\_\___|_|   
                    __/ |                                    
                   |___/                                     
""")

time.sleep(1)

choose = input(" [1] Hisory \n [2] Statistics \n [3] Country \n \n >> ")

if choose == "1":
    his()
elif choose == "2":
    stats()
elif choose == "3":
    count()
else:
    print("Please enter a correct number...")
    (os).clear
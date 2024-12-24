"""
********************************************************************************
* Project Name:  Exercise Tracker with Google Sheet
* Description:   Exercise Tracker is a Python-based application that uses the Nutritionix API to analyze your workout and the Sheety API to log the exercise data into a Google Sheet. 
* Author:        ziqkimi308
* Created:       2024-12-24
* Updated:       2024-12-24
* Version:       1.0
********************************************************************************
"""

import requests
import datetime as dt

# ------------------------------------------------- CONSTANT ------------------------------------------------------------ #
# ------------- EXERCISE API ------------- #
APP_ID = ""
API_KEY = ""
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
MY_WEIGHT = 
MY_HEIGHT = 
MY_AGE = 

# ------------ SHEETY API -------------- #
SHEETY_SPREADSHEET = ""
SHEETY_ADDROW_ENDPOINT = ""
SHEETY_BEARER_TOKEN = ""

# ----------------------------------------------- EXERCISE SETUP --------------------------------------------------------- #
exercise_headers = {
	"x-app-id": APP_ID,
	"x-app-key": API_KEY,
}

exercise_parameters = {
	"query": input("Which exercise you did? : "),
	"weight_kg": MY_WEIGHT,
	"height_cm": MY_HEIGHT,
	"age": MY_AGE
}

exercise_response = requests.post(url=EXERCISE_ENDPOINT, headers=exercise_headers, json=exercise_parameters)
exercise_data = exercise_response.json()
print(f"Result from exercise request:\n{exercise_data}")

# --------------------------------------------- SHEETY ADD ROW SETUP --------------------------------------------------- #
# Create parameters for sheety add row
sheety_headers = {
	"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

date_today = dt.datetime.now().date().strftime("%d/%m/%Y")
time_now = dt.datetime.now().time().strftime("%X")

for exercise in exercise_data["exercises"]:
	sheety_param = {
		"sheet1": {
			"date": date_today,
			"time": time_now,
			"exercise": exercise["name"].title(),
			"duration": round(exercise["duration_min"]),
			"calories": exercise["nf_calories"]
		}
	}

	sheety_addrow_response = requests.post(url=SHEETY_ADDROW_ENDPOINT, json=sheety_param, headers=sheety_headers)
	print(f"Result from Google Sheet:\n{sheety_addrow_response.text}")
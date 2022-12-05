# https://developer.tomtom.com/routing-api/documentation/routing/calculate-route
import json
import requests
import os
import sys

BASE_URL = "https://api.tomtom.com/routing/1/calculateRoute/"

class TravelInfo:
  def __init__(self, travel_data):
      self.travelTimeInMinutes = round(travel_data.get("routes")[0].get("summary").get("travelTimeInSeconds") / 60)

class Config:
  def __init__(self, json):
    self.start = json.get("start").replace(" ", "")
    self.destinations = []
    for d in json.get("destinations"):
      self.destinations.append(Destination(d))

class Destination:
  def __init__(self, json):
    self.name = json.get("name")
    self.coordinates = json.get("coordinates").replace(" ", "")

def get_travel_time(coordinates, apikey):
    response = requests.get(f"{BASE_URL}{coordinates}/json?key={apikey}")
    travel_data = response.json()

    return TravelInfo(travel_data).travelTimeInMinutes

def get_config():
  with open(os.path.join(sys.path[0], "coordinates.json"), "r") as f:
    config = json.load(f)
    return Config(config)

def get_apikey():
  with open(os.path.join(sys.path[0], "apikey"), "r") as f:
    return f.readline()

def get_travel_times():
  apikey = get_apikey()
  config = get_config()
  travel_times = []
  for d in config.destinations:
    coordinate_pair = f"{config.start}:{d.coordinates}"
    time = get_travel_time(coordinate_pair, apikey)
    travel_times.append(f"{d.name}: {time} min")
  return travel_times

print(get_travel_times())
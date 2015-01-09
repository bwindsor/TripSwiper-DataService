from config import Config
import json
from models import Event
from parse_rest.datatypes import GeoPoint
from datetime import datetime
import requests

DEFAULT_LAT = "40.8075"
DEFAULT_LONG = "-73.9619"
DEFAULT_RAD = "5000"
BASE_REQUEST = "http://api.nytimes.com/svc/events/v2/listings.json?"
DEFAULT_PHOTO = "http://kerryhannon.com/wp-content/uploads/2013/11/the-new-york-times-logo.jpg"

def getTodaysDate():
  i = datetime.now()
  return i.strftime('%Y-%m-%d:%Y-%m-%d')

def isInvalidAttribute(string):
      return not string or all(c.isspace() for c in string)

class NewYorkTimes(object):
  def __init__(self):
    config = Config()
    self.api_key = config.getNYTKey()

  def getEventsForToday(self, latitude=DEFAULT_LAT, longitude=DEFAULT_LONG, radius=DEFAULT_RAD):
    query_string = self.queryString(latitude, longitude, radius)
    print query_string
    events = requests.get(query_string).json()
    parse_events = []
    for event in events['results']:
      print event
      json_object = NewYorkTimes.objectFromJSON(event)
      if json_object:
        parse_events.append(json_object)
      else:
        print "SOMETHING FUCKED UP"
    return parse_events

  def queryString(self, latitude, longitude, radius):
    query = BASE_REQUEST
    query += "ll=" + latitude + "," + longitude + "&"
    query += "radius=" + radius + "&"
    query += "date_range=" + getTodaysDate() + "&"
    query += "api-key=" + self.api_key
    return query

  @staticmethod
  def objectFromJSON(event):
    try:
      parse_event = Event()
      if isInvalidAttribute(event['event_name']):
        return
      parse_event.title = event['event_name']
      if isInvalidAttribute(event['web_description']):
        return
      parse_event.description = event['web_description']
      if isInvalidAttribute(str(event['event_id'])):
        return
      parse_event.eventId = str(event['event_id'])
      try:
        parse_event.location = GeoPoint(latitude=float(event['geocode_latitude']), longitude=float(event['geocode_longitude']))
      except:
        print "Invalid lat/long"
      if isInvalidAttribute(event['street_address']):
        return
      parse_event.address = event['street_address']
      if isInvalidAttribute(event['venue_name']):
        return
      parse_event.venueName = event['venue_name']
      if isInvalidAttribute(event['date_time_description']):
        return
      parse_event.startTime = event['date_time_description']
      parse_event.photoURL = DEFAULT_PHOTO
      if isInvalidAttribute(event['category']):
        return
      parse_event.venueName = event['category']
      return parse_event
    except KeyError:
      print "We missed a key!"



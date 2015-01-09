from config import Config
import json
from models import Event
from parse_rest.datatypes import GeoPoint

EVENT_SEARCH = "/events/search"
CATEGORIES_SEARCH = "/categories/list"
NEW_YORK = "New York, NY"
TODAY = "Today"

def isInvalidAttribute(string):
      return not string or all(c.isspace() for c in string)

def getPhotoURL(event):
  try:
    return event['image']['medium']['url']
  except:
    return

class Eventful(object):
  def __init__(self):
    config = Config()
    self.eventful = config.registerEventfulAPI()

  def getEventsForToday(self, category):
    return self.eventful.call(EVENT_SEARCH, location=NEW_YORK, date=TODAY, page_size=50, category=category)

  def getCategories(self):
    categories = open('eventful_categories.json')
    return json.load(categories)

  @staticmethod
  def objectFromJSON(event, category):
    try:
      parse_event = Event()
      if isInvalidAttribute(event['title']):
        return
      parse_event.title = event['title']
      if isInvalidAttribute(event['description']):
        return
      parse_event.description = event['description']
      if isInvalidAttribute(event['id']):
        return
      parse_event.eventId = event['id']
      try:
        parse_event.location = GeoPoint(latitude=float(event['latitude']), longitude=float(event['longitude']))
      except:
        print "Invalid lat/long"
      if isInvalidAttribute(event['venue_address']):
        return
      parse_event.address = event['venue_address']
      if isInvalidAttribute(event['venue_name']):
        return
      parse_event.venueName = event['venue_name']
      if isInvalidAttribute(event['start_time']):
        return
      parse_event.startTime = event['start_time']
      if not getPhotoURL(event):
        return
      parse_event.photoURL = getPhotoURL(event)
      parse_event.category = category
      return parse_event
    except KeyError:
      print "We missed a key!"

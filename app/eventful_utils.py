from config import Config
import json
from models import Event
from parse_rest.datatypes import GeoPoint

EVENT_SEARCH = "/events/search"
CATEGORIES_SEARCH = "/categories/list"
NEW_YORK = "New York, NY"
TODAY = "Today"


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
      parse_event.title = event['title']
      print parse_event.title
      parse_event.description = event['description']
      parse_event.eventId = event['id']
      parse_event.location = GeoPoint(latitude=event['latitude'], longitude=event['longitude'])
      parse_event.address = event['venue_address']
      parse_event.venueName = event['venue_name']
      parse_event.startTime = event['start_time']
      parse_event.category = category
      return parse_event
    except KeyError:
      print "We missed a key!"

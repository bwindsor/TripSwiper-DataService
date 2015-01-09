from eventful_utils import Eventful
from config import Config
from parse_rest.connection import ParseBatcher
import sys

def configureParse():
  config = Config()
  config.registerParseApp()

def postEvents(events, category):
  try:
    parse_events = []
    for event in events['event']:
      parse_event = Eventful.objectFromJSON(event,category)
      parse_events.append(parse_event)
    batcher = ParseBatcher()
    batcher.batch_save(parse_events)
  except KeyError:
    print "Something went wrong!"
    sys.exit()

if __name__ == "__main__":
  Config().registerParseApp()
  eventful = Eventful()
  categories = eventful.getCategories()
  for key in categories.keys():
    postEvents(eventful.getEventsForToday(key)['events'], categories[key])



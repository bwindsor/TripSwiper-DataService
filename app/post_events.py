from eventful_utils import Eventful
from config import Config
from parse_rest.connection import ParseBatcher
import sys, traceback

def configureParse():
  config = Config()
  config.registerParseApp()

def postEvents(events, category):
  parse_events = []
  for event in events['event']:
    parse_event = Eventful.objectFromJSON(event,category)
    if parse_event:
      parse_events.append(parse_event)
  batcher = ParseBatcher()
  batcher.batch_save(parse_events)

if __name__ == "__main__":
  Config().registerParseApp()
  eventful = Eventful()
  categories = eventful.getCategories()
  for key in categories.keys():
    postEvents(eventful.getEventsForToday(key)['events'], categories[key])




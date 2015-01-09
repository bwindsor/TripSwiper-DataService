from new_york_times_utils import NewYorkTimes
from config import Config
from parse_rest.connection import ParseBatcher
import sys, traceback

def postEvents(events):
  print events

if __name__ == "__main__":
  Config().registerParseApp()
  nyt = NewYorkTimes()
  postEvents(nyt.getEventsForToday())

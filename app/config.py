from parse_rest.connection import register
import json, sys, eventful

PARSE_APP_ID = 'parse_app_id'
PARSE_REST_API_KEY = 'parse_rest_api_key'
PARSE_MASTER_KEY = 'parse_master_key'

EVENTFUL_API_KEY = 'eventful_api_key'

NEW_YORK_TIMES_API_KEY = 'new_york_times_api_key'

class Config(object):
  def __init__(self):
    self.api_keys = self.loadAPIKeys()

  def loadAPIKeys(self):
    api_data = open('api_keys.json')
    return json.load(api_data)

  def registerParseApp(self):
    try:
      register(self.api_keys[PARSE_APP_ID], self.api_keys[PARSE_REST_API_KEY], 
        master_key=self.api_keys[PARSE_MASTER_KEY])
    except KeyError:
      print "Please create your api_keys.json file with proper keys"
      sys.exit()
    except:
      print "Something else went wrong. Please look into this."
      sys.exit()

  def registerEventfulAPI(self):
    return eventful.API(self.api_keys[EVENTFUL_API_KEY])

  def getNYTKey(self):
    return self.api_keys[NEW_YORK_TIMES_API_KEY]




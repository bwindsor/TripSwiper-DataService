from parse_rest.connection import register
import json
import sys

PARSE_APP_ID = 'parse_app_id'
PARSE_REST_API_KEY = 'parse_rest_api_key'
PARSE_MASTER_KEY = 'parse_master_key'

def loadAPIKeys():
  api_data = open('api_keys.json')
  return json.load(api_data)

def registerParseApp():
  api_keys = loadAPIKeys()
  print api_keys
  try:
    register(api_keys[PARSE_APP_ID], api_keys[PARSE_REST_API_KEY], master_key=api_keys[PARSE_MASTER_KEY])
  except KeyError:
    print "Please create your api_keys.json file with proper keys"
    sys.exit()
  except:
    print "Something else went wrong. Please look into this."
    sys.exit()



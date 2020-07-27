#!/usr/bin/python3
# NX-OS API Route Table Parser
# Nicholas Schmidt
# 04 Jun 2020

# API Processing imports
import requests
import json

# Command line parsing imports
import argparse

# Command line validating imports
from django.core.validators import URLValidator

# Object Definitions

# Functions

# Do API
# Send a json payload via the requests API
def do_api_unpw(do_api_unpw_user, do_api_unpw_password, do_api_unpw_url, do_api_unpw_payload): 
      # Perform NX-API Processing - conditional basic or certificate authentication
      try: 
            do_api_unpw_headers = {'content-type':'application/json'}
            do_api_unpw_r = requests.post(do_api_unpw_url,data=json.dumps(do_api_unpw_payload), headers=do_api_unpw_headers,auth=(do_api_unpw_user,do_api_unpw_password))
            # We'll be discarding the actual `Response` object after this, but we do want to get HTTP status for erro handling
            response_code = do_api_unpw_r.status_code
            do_api_unpw_r.raise_for_status() #trigger an exception before trying to convert or read data. This should allow us to get good error info
            return do_api_unpw_r.json() #if HTTP status is good, i.e. a 100/200 status code, we're going to convert the response into a json dict
      except:
            if httperrors.get(response_code):
                  print('HTTP Status Error ' + str(response_code) + ' ' + httperrors.get(response_code)[max(min(args.verbosity,1),0)])
                  exit() #interpet the error, then close out so we don't have to put all the rest of our code in an except statement
            else:
                  print('Unhandled HTTP Error ' + str(response_code) + '!' )
                  exit() #interpet the error, then close out so we don't have to put all the rest of our code in an except statement
def do_api_cert(do_api_cert_client, do_api_cert_pkey, do_api_cert_ca, do_api_cert_user, do_api_cert_password, do_api_cert_url, do_api_cert_payload):
      try: 
            do_api_unpw_headers = {'content-type':'application/json'}
            do_api_cert_r = requests.post(do_api_cert_url,data=json.dumps(do_api_cert_payload), headers=do_api_unpw_headers,auth=(do_api_cert_user,do_api_cert_password),cert=(do_api_cert_client,do_api_cert_pkey),verify=do_api_cert_ca)
            # We'll be discarding the actual `Response` object after this, but we do want to get HTTP status for erro handling
            response_code = do_api_cert_r.status_code
            do_api_cert_r.raise_for_status() #trigger an exception before trying to convert or read data. This should allow us to get good error info
            return do_api_cert_r.json() #if HTTP status is good, i.e. a 100/200 status code, we're going to convert the response into a json dict
      except:
            if httperrors.get(response_code):
                  print ('HTTP Status Error ' + str(response_code) + ' ' + httperrors.get(response_code)[max(min(args.verbosity,1),0)])
                  exit() #interpet the error, then close out so we don't have to put all the rest of our code in an except statement
            else:
                  print ('Unhandled HTTP Error ' + str(response_code) + '!' )
                  exit() #interpet the error, then close out so we don't have to put all the rest of our code in an except statement

#### Open a json payload file
def get_json_from_file(get_json_from_file_name):
      # Attempt to load a json file, and lint it
      try:
            with open(get_json_from_file_name) as json_file:
                  return json.load(json_file)
      except ValueError as err:
            print('Python thinks you have a json formatting issue. Please run your payload input through a json linter.')
            print(err)
            exit()
      except IOError as err:
            print('A File I/O error has occurred. Please check your file path!')
            print(err)
            exit()
      except:
            print('An unexpected error has occurred!')
            exit()

# References

# Set HTTP Error + Verbosity table. Due to the use of max(min()), verbosity count becomes a numerical range that caps off and prevents array issues
# Credit where due - https://gist.github.com/bl4de/3086cf26081110383631 by bl4de
httperrors = {
  100: ('Continue', 'Request received, please continue'),
  101: ('Switching Protocols',
        'Switching to new protocol; obey Upgrade header'),

  200: ('OK', 'Request fulfilled, document follows'),
  201: ('Created', 'Document created, URL follows'),
  202: ('Accepted',
        'Request accepted, processing continues off-line'),
  203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
  204: ('No Content', 'Request fulfilled, nothing follows'),
  205: ('Reset Content', 'Clear input form for further input.'),
  206: ('Partial Content', 'Partial content follows.'),

  300: ('Multiple Choices',
        'Object has several resources -- see URI list'),
  301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
  302: ('Found', 'Object moved temporarily -- see URI list'),
  303: ('See Other', 'Object moved -- see Method and URL list'),
  304: ('Not Modified',
        'Document has not changed since given time'),
  305: ('Use Proxy',
        'You must use proxy specified in Location to access this '
        'resource.'),
  307: ('Temporary Redirect',
        'Object moved temporarily -- see URI list'),

  400: ('Bad Request',
        'Bad request syntax or unsupported method'),
  401: ('Unauthorized',
        'No permission -- see authorization schemes'),
  402: ('Payment Required',
        'No payment -- see charging schemes'),
  403: ('Forbidden',
        'Request forbidden -- authorization will not help'),
  404: ('Not Found', 'Nothing matches the given URI'),
  405: ('Method Not Allowed',
        'Specified method is invalid for this server.'),
  406: ('Not Acceptable', 'URI not available in preferred format.'),
  407: ('Proxy Authentication Required', 'You must authenticate with '
        'this proxy before proceeding.'),
  408: ('Request Timeout', 'Request timed out; try again later.'),
  409: ('Conflict', 'Request conflict.'),
  410: ('Gone',
        'URI no longer exists and has been permanently removed.'),
  411: ('Length Required', 'Client must specify Content-Length.'),
  412: ('Precondition Failed', 'Precondition in headers is false.'),
  413: ('Request Entity Too Large', 'Entity is too large.'),
  414: ('Request-URI Too Long', 'URI is too long.'),
  415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
  416: ('Requested Range Not Satisfiable',
        'Cannot satisfy request range.'),
  417: ('Expectation Failed',
        'Expect condition could not be satisfied.'),

  500: ('Internal Server Error', 'Server got itself in trouble'),
  501: ('Not Implemented',
        'Server does not support this operation'),
  502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
  503: ('Service Unavailable',
        'The server cannot process the request due to a high load'),
  504: ('Gateway Timeout',
        'The gateway server did not receive a timely response'),
  505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
}

# Arguments Parsing
parser = argparse.ArgumentParser(description='Fetch all routing tables via NX-API')
parser.add_argument('-v', '--verbosity', action='count', default=0, help='Output Verbosity')
parser.add_argument('-f', help='Select JSON Payload file')
subparsers = parser.add_subparsers(help='Use Basic or CA Authentication')
unpw = subparsers.add_parser('basic', help='Use Basic Authentication')
unpw.add_argument('-u', help='NX-API Username')
unpw.add_argument('-p', help='NX-API Password')
cert = subparsers.add_parser('ca', help='Use Certificate Authentication')
cert.add_argument('--cert', help='NX-API Client Certificate. Required if using CA Authentication')
cert.add_argument('--privkey', help='NX-API Client Certificate Private Key. Required if using CA Authentication')
cert.add_argument('--ca', help='NX-API Client Certificate CA. Optional if using CA Authentication')
parser.add_argument('nxapi_endpoint', help='The NX-API Endpoint to target with this API call')

args = parser.parse_args()

# Ensure that NX-API Endpoint is a valid one
validate = URLValidator()
try:
  validate(args.nxapi_endpoint)
except:
  print('Invalid URL. Please try a valid URL. Example: "http://10.1.1.1/ins"')
  exit()

# Get system information, ensure that you have a good endpoint
## JSON Payload to check version data
precheck_payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show version",
    "output_format": "json"
  }
}
precheck = do_api_unpw(args.u, args.p, args.nxapi_endpoint, precheck_payload)
try:
      print('Found NX-API Endpoint! System Name: ' + precheck['ins_api']['outputs']['output']['body']['host_name'])
      print('Chassis: ' + precheck['ins_api']['outputs']['output']['body']['chassis_id'])
      print('Version: ' + precheck['ins_api']['outputs']['output']['body']['nxos_ver_str'])
except:
      print('API Endpoint did not respond to test query with valid data. Please try again on a valid NX-API endpoint.')

# Create a JSON file if a developer wants to use this from the python code (it's sometimes easier)
#with open('payload_show_ip_route_vrf_all.json', 'w') as outfile:
#    json.dump(payload, outfile)

route_tables = do_api_unpw(args.u,args.p,args.nxapi_endpoint,get_json_from_file(args.f))

# Begin Processing API Data - Parsing Route Tables
## Debugging shouldn't require code changes, let's use our verbosity switches
if max(min(args.verbosity,1),0) >= 1:
      print (route_tables) #print raw json response

# iterate through all route tables, and print them
for i in route_tables['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']:
      print(i['vrf-name-out'] + ': ')
      for ii in i['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix']: 
            print(ii)
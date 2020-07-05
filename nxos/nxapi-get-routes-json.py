### NX-OS API Route Table Parser
### Nicholas Schmidt
### 04 Jun 2020

# API Processing imports
import requests
import json

# Command line parsing imports
import argparse

# Command line validating imports
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Arguments Parsing
parser = argparse.ArgumentParser(description='Fetch all routing tables via NX-API')
parser.add_argument('-v', '--verbosity', action='count', default=0, help='Output Verbosity')
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

# Import/Test arguments
# Endpoint
#print(args.nxapi_endpoint)
# User
#print(args.u)
# Password (I know. this needs to be fixed later.)
#print(args.p)
# Certificate Auth - Enable CA Auth
#print(args.verbosity)
# Auth Certificate - Select Certificate
#print(args.cert)
# Private Key
#print(args.privkey)
# Auth Certificate Authority
#print(args.ca)

# Set NX-API Credential Variables
client_cert_auth=False
switchuser=args.u
switchpassword=args.p
client_cert='PATH_TO_CLIENT_CERT_FILE'
client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

# Set NX-API URL and payload
# Note: default API URI endpoint for NX-OS is /ins
url=args.nxapi_endpoint
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip route vrf all",
    "output_format": "json"
  }
}

# Perform NX-API Processing - conditional based on certificate authentication
try: 
  if client_cert_auth is False:
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword))
  else:
    url='https://10.7.28.99/ins'
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert)
  #response_json = response
  response.raise_for_status()
except:
  httperrors = {
    401: ' HTTP Authentication Failed!'
  }
  if httperrors.get(response.status_code):
    print ('HTTP Status Error ' + str(response.status_code) + httperrors.get(response.status_code))
  else:
    print ('Unhandled HTTP Error ' + str(response.status_code) + '!' )
# Do things with what was received by the API!
#print(json.dumps(response, indent=1, sort_keys=True))
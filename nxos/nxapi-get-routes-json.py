import requests
import json

"""
Modify these please
"""
#For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
#For basic authentication using username & pwd, set 'client_cert_auth' to False.
client_cert_auth=False
switchuser='admin'
switchpassword='admin'
client_cert='PATH_TO_CLIENT_CERT_FILE'
client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='http://10.7.28.99/ins'
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

if client_cert_auth is False:
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    print json.dumps(response, indent=1, sort_keys=True)
else:
    url='https://10.7.28.99/ins'
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert).json()
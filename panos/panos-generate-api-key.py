#!/usr/bin/python3
# PAN-OS API API Keygen
# PAN-OS OP-CMDs are not supported via REST, only CRUD. This will generate an API key for use with a future function.
# Actions will be functionalized so that every API call can theoretically use an ephemeral key, or re-use.
# Nicholas Schmidt
# 27 Jul 2020

# API Processing imports
import requests
import json

# XML has vulnerabilities, use DefusedXML libraries instead to offload security mitigations to the project
# https://pypi.org/project/defusedxml/#defusedxml
import defusedxml

# Command line parsing imports
import argparse

# Command line validating imports
from django.core.validators import URLValidator

# Object Definitions

# Functions

# Do API GET
def do_api_get_unpw(do_api_unpw_user, do_api_unpw_password, do_api_unpw_url, do_api_certvalidation):
    # Perform API Processing - conditional basic authentication
    try:
        do_api_unpw_headers = {'content-type': 'application/xml'}
        do_api_unpw_r = requests.get(do_api_unpw_url, headers=do_api_unpw_headers, verify=do_api_certvalidation)
        # We'll be discarding the actual `Response` object after this, but we do want to get HTTP status for erro handling
        response_code = do_api_unpw_r.status_code
        do_api_unpw_r.raise_for_status()  # trigger an exception before trying to convert or read data. This should allow us to get good error info
        return do_api_unpw_r.json()  # if HTTP status is good, i.e. a 100/200 status code, we're going to convert the response into a json dict
    except:
        if httperrors.get(response_code):
            print('HTTP Status Error ' + str(response_code) + ' ' + httperrors.get(response_code)[max(min(args.verbosity, 1), 0)])
            exit()  # interpet the error, then close out so we don't have to put all the rest of our code in an except statement
        else:
            print('Unhandled HTTP Error ' + str(response_code) + '!')
            exit()  # interpet the error, then close out so we don't have to put all the rest of our code in an except statement


# Do API GET with Auth Key
# Send a xml payload via the requests API
def do_api_get_key(do_api_post_auth_key, do_api_post_url, do_api_post_payload, do_api_certvalidation):
    # Perform API Processing - conditional basic authentication
    try:
        do_api_post_headers = {'content-type': 'application/xml'}
        do_api_post_r = requests.get(do_api_post_url + do_api_post_payload + '&key=' + do_api_post_auth_key, headers=do_api_post_headers, verify=do_api_certvalidation)
        # We'll be discarding the actual `Response` object after this, but we do want to get HTTP status for erro handling
        response_code = do_api_post_r.status_code
        do_api_post_r.raise_for_status()  # trigger an exception before trying to convert or read data. This should allow us to get good error info
        return do_api_post_r.json()  # if HTTP status is good, i.e. a 100/200 status code, we're going to convert the response into a json dict
    except:
        if httperrors.get(response_code):
            print('HTTP Status Error ' + str(response_code) + ' ' + httperrors.get(response_code)[max(min(args.verbosity, 1), 0)])
            exit()  # interpet the error, then close out so we don't have to put all the rest of our code in an except statement
        else:
            print('Unhandled HTTP Error ' + str(response_code) + '!')
            exit()  # interpet the error, then close out so we don't have to put all the rest of our code in an except statement


# Do API POST with Auth Key
# Send a xml payload via the requests API
def do_api_post_key(do_api_post_auth_key, do_api_post_url, do_api_post_payload, do_api_certvalidation):
    # Perform API Processing - conditional basic authentication
    try:
        do_api_post_headers = {'content-type': 'application/xml'}
        do_api_post_r = requests.post(do_api_post_url + do_api_post_payload + '&key=' + do_api_post_auth_key, headers=do_api_post_headers, verify=do_api_certvalidation)
        # We'll be discarding the actual `Response` object after this, but we do want to get HTTP status for erro handling
        response_code = do_api_post_r.status_code
        do_api_post_r.raise_for_status()  # trigger an exception before trying to convert or read data. This should allow us to get good error info
        return do_api_post_r.json()  # if HTTP status is good, i.e. a 100/200 status code, we're going to convert the response into a json dict
    except:
        if httperrors.get(response_code):
            print('HTTP Status Error ' + str(response_code) + ' ' + httperrors.get(response_code)[max(min(args.verbosity, 1), 0)])
            exit()  # interpet the error, then close out so we don't have to put all the rest of our code in an except statement
        else:
            print('Unhandled HTTP Error ' + str(response_code) + '!')
            exit()  # interpet the error, then close out so we don't have to put all the rest of our code in an except statement


# DO API GET for API Key
def do_api_get_auth_key(do_api_get_auth_key_user, do_api_get_auth_key_password, do_api_get_auth_key_url, do_api_get_auth_key_certvalidation):
    return do_api_get_unpw(do_api_get_auth_key_user, do_api_get_auth_key_password, 
                            '/?type=keygen&user=' + do_api_get_auth_key_user + '&password=' + do_api_get_auth_key_password,
                            do_api_get_auth_key_certvalidation)


# Open an xml payload file
def get_xml_from_file(get_xml_from_file_name):
    # Attempt to load a json file, and lint it
    try:
        with open(get_xml_from_file_name) as xml_file:
            return defusedxml.ElementTree.parse(xml_file)
    except ValueError as err:
        print('Python thinks you have a xml formatting issue. Please run your payload input through a xml linter.')
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
parser = argparse.ArgumentParser(description='Fetch via API')
parser.add_argument('-v', '--verbosity', action='count', default=0, help='Output Verbosity')
parser.add_argument('-f', help='Select XML Payload file')
parser.add_argument('-k', action='store_false', default=True, help='Ignore Certificate Errors')
subparsers = parser.add_subparsers(help='Use Basic or Key Authentication')
unpw = subparsers.add_parser('basic', help='Use Basic Authentication')
unpw.add_argument('-u', help='Username')
unpw.add_argument('-p', help='Password')
cert = subparsers.add_parser('key', help='Use Key Authentication')
cert.add_argument('--auth_key', help='Authentication Key')
parser.add_argument('api_endpoint', help='The API Endpoint to target with this API call. PAN-OS XML API is at https://<ip>/api')

args = parser.parse_args()
# Ensure that API Endpoint is a valid one
validate = URLValidator()
try:
    validate(args.api_endpoint)
except:
    print('Invalid URL. Please try a valid URL. Example: "https://10.0.0.0/api"')
    exit()

# Let's try getting an API key first
    session_auth_key = do_api_get_auth_key(args.u, args.p, args.api_endpoint, args.k)
    print(session_auth_key)

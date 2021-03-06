"""
"""
from os.path import join
import requests

class EZIDActor(object):
    def __init__(self):
        # this NUST be a https since EZID API only allows sending authentication via basic authentication
        # leave this URL as-is. NEVER change it to http because if you do you are violating security policy!
        self.api_host = "https://ezid.cdlib.org/id/"

    def post_data(self, identifier, post_data, username, password):
        url = join(self.api_host, identifier)
        auth_handler = requests.auth.HTTPBasicAuth(username, password)
        post_data_string = self._post_data_to_change_target(post_data).encode("utf-8")
        headers = {'Content-Type': 'text/plain'}
        resp = requests.post(url, data=post_data_string,
                             auth=auth_handler, headers=headers)
        if resp.status_code == 200:
            return 'Ok'
        else:
            return 'null'

    def get_data(self, identifier):
        url = join(self.api_host, identifier)
        resp = requests.post(url)
        if resp.status_code == 200:
            return resp.text 
        else:
            return 'null'

    def _post_data_to_change_target(self, new_location):
        request_string = "_target: {}".format(new_location)
        return request_string


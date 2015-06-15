"""This code collects lthe test logs from jenkins and
   stroes those test logs into elasticsearch"""

import requests
from requests.auth import HTTPBasicAuth
import json
from githubMapping import githubMapping
from elasticsearch import Elasticsearch
es = Elasticsearch()


class GithubManager(object):

    """This is the main class for xunit."""

    def __init__(self, job_url, user, password):
        """constructor, for collecting project credentials.
           Project: github repo name, user: your user_name for github
           password: you password for github, job_url: Github url,
           """
        self.job_url = job_url
        self.user = user
        self.password = password
        self.es = Elasticsearch()

        requests.put("http://localhost:9200/" + self.user,
                     data=json.dumps(githubMapping))

    def get_response(self, response_json):
        """ collecting response, building url
        and getting the values from the url"""

        print response_json

        for k in response_json:

            self.index_pull_request(k['title'],
                                    k['state'],
                                    k['head']['repo']['description'],
                                    k['head']['repo']['name'],
                                    k['head']['repo']['default_branch'])

    def index_pull_request(self, title, state, description,
                           name, default_branch):
        """ creating index"""

        pull_request = {
            "title": title,
            "state": state,
            "description": description,
            "name": name,
            "default_branch": default_branch

        }
        self.es.index(index=self.user, id=1,
                      doc_type="pullrequest", body=pull_request)

    def get_pull(self):
        """ response from github in json format """
        # self.get_response(self.get_pull())
        response_json = self.call_github(self.job_url +
                                         'repos/proverma/cloudscope/pulls')
        return response_json

    def call_github(self, job_url):
        """ github authorization"""

        r = requests.get(job_url,
                         auth=HTTPBasicAuth(self.user, self.password))
        return r.json()

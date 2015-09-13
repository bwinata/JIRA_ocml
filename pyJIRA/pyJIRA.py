#!/bin/python

from pyJIRA_consts import *
from pyJIRA_dict import *

import simplejson as json
from restkit import request, BasicAuth, Resource

class JIRA:
    auth = BasicAuth ("", "")
    url = ""
    username = ""
    password = ""

    # -- Contructor
    def __init__ (self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

    # -- Private Functions
    def __authenticate (self):
        if self.username == "" or self.password == "" or self.url == "":
            return JIRA_ERROR_CREDENTIALS_MISSING
        else:
            self.auth = BasicAuth (self.username, self.password)
            return JIRA_SUCCESS

    def __get_json_response (self, resource):
        try:
            response = resource.get (headers = {'Content-type' : 'application/json'})
        except Exception, ex:
            print "Exception: %s" % ex.msg;

        if response.status_int != 200:
            print "ERROR: status %s" % response.status_int
            return False, response
        else:
            return True, response

    def __get_ticket_resource (self, username, ticket_type):
        ticket_resource = Resource (self.url + JIRA_REST_PATH + "search?jql=assignee=" + username + "%20and%20" + "issuetype='%s'&fields=summary" % (ticket_type), filters=[self.auth])
        return ticket_resource

    def __get_ticket_list (self, username, ticket_type):
        ticket_list = []
        if self.__authenticate () == JIRA_SUCCESS:
            status, resp = self.__get_json_response (self.__get_ticket_resource (username, ticket_type))
            if status == True:
                issues = json.loads (resp.body_string ())
                for issue in issues['issues']:
                    ticket_list.append ("%s : %s" % (issue['key'], issue['fields']['summary']))

        return ticket_list

    # -- Public Functions
    def check_ticket_valid (self, ticket):
        if ticket in JIRA_TYPES_DICT.keys ():
            return True, JIRA_TYPES_DICT[ticket]
        else:
            return False, -1

    def get_issues (self, username):
        return self.__get_ticket_list (username, "Bug")

    def get_tasks (self, username):
        return self.__get_ticket_list (username, "Task")

    def get_features (self, username):
        return self.__get_ticket_list (username, "New%20Feature")

    def get_improvements (self, username):
        return self.__get_ticket_list (username, "Improvement")

    def get_epics (self, username):
        return self.__get_ticket_list (username, "Epic")

    def get_stories (self, username):
        return self.__get_ticket_list (username, "Story")

    def get_rmas (self, username):
        return self.__get_ticket_list (username, "RMA")

    def get_tests (self, username):
        return self.__get_ticket_list (username, "Test")

    def get_ticket (self, ticket, username):
        

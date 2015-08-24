#!/bin/python

import simplejson as json
from restkit import request, BasicAuth, Resource

JIRA_SUCCESS = 0
JIRA_ERROR_CREDENTIALS_MISSING = 100
JIRA_ERROR_CREDENTIALS_INVALID = 200

JIRA_BUG            = 0
JIRA_NEW_FEATURE    = 1
JIRA_IMPROVEMENT    = 2
JIRA_EPIC           = 3
JIRA_STORY          = 4
JIRA_RMA            = 5
JIRA_TEST           = 6
JIRA_TASK           = 7

JIRA_ERROR_DICT = {
    JIRA_ERROR_CREDENTIALS_MISSING: "Credentials are missing. Please try again",
    JIRA_ERROR_CREDENTIALS_INVALID: "Credentials are invalid. Please try again"
}

JIRA_TYPES_DICT = {
    "bug"       : JIRA_BUG,
    "new_feat"  : JIRA_NEW_FEATURE,
    "improve"   : JIRA_IMPROVEMENT,
    "epic"      : JIRA_EPIC,
    "story"     : JIRA_STORY,
    "rma"       : JIRA_RMA,
    "test"      : JIRA_TEST,
    "task"      : JIRA_TASK
}

class JIRA:
    rest_path = "/rest/api/2/"
    auth = BasicAuth ("", "")
    url = ""
    username = ""
    password = ""

    # Contructor
    def __init__ (self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

    # Private Functions
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


    # Public Functions
    def get_issues (self, username):
        issue_list = []
        if self.__authenticate () == JIRA_SUCCESS:
            resource = Resource (self.url + self.rest_path + "search?jql=assignee=" + username + "%20and%20" + "issuetype=Bug&fields=summary", filters=[self.auth])
            status, resp = self.__get_json_response (resource)
            if status == True:
                issues = json.loads (resp.body_string ())
                for issue in issues['issues']:
                    issue_list.append ("%s : %s" % (issue['key'], issue['fields']['summary']))

        return issue_list

    def get_tasks (self, username):
        task_list = []
        if self.__authenticate () == JIRA_SUCCESS:
            resource = Resource (self.url + self.rest_path + "search?jql=assignee=" + username + "%20and%20" + "issuetype=Task&fields=summary", filters=[self.auth])

            status, resp = self.__get_json_response (resource)
            if status == True:
                tasks = json.loads (resp.body_string ())
                for task in tasks['issues']:
                    task_list.append ("%s : %s" % (task['key'], task['fields']['summary']))

        return task_list


    def find_ticket (self, username, ticket):
        ticket_dict = {}
        if self.__authenticate () == JIRA_SUCCESS:


    def start (self):
        print "Starting JIRA service..."

    def stop (self):
        print "Stopping JIRA service..."

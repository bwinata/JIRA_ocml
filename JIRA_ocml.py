#!/bin/python

import time
import sys

from cmd import Cmd
from threading import Thread
from pyJIRA import pyJIRA

STRING_PROMPT_DEFAULT = "jcl>> "
STRING_PROMPT_INTRO = "JIRA On the Command Line 1.0\n============================"

ARG_LIMIT_COMMAND_LS    = 2
ARG_LIMIT_COMMAND_OPEN  = 2

USAGE_COMMAND_LS    = "Usage: ls <ticket type> <user>"
USAGE_COMMAND_OPEN  = "Usage: open <ticket number>"

class JIRA_ocml (Cmd):

    # -- Constructor
    def __init__ (self):
        Cmd.__init__ (self);
        self.J = pyJIRA.JIRA ("bwinata", "Evolve_729183", "https://xeranet.atlassian.net")
        self.prompt = STRING_PROMPT_DEFAULT
        self.intro = STRING_PROMPT_INTRO

    # -- Private
    def __check_ticket_valid (self, ticket):
        return self.J.check_ticket_valid (ticket)

    def __display_ticket_list (self, username, ticket_list, ticket_type):
        num = len (ticket_list)
        if num > 0:
            print "============================================================="
            print "List of %s - %s" % (username, ticket_type)
            for issue_cnt in range (num):
                print "--------------------------------------------------------------"
                print ticket_list[issue_cnt]
        else:
            print "Woops: No %s available for %s" % (ticket_type, username)

    def __display_ticket (self):


    def __list_bugs (self, username):
        issues = self.J.get_issues (username)
        self.__display_ticket_list (username, issues, "Bugs")

    def __list_tasks (self, username):
        tasks = self.J.get_tasks (username)
        self.__display_ticket_list (username, tasks, "Tasks")

    def __list_new_features (self, username):
        features = self.J.get_features (username)
        self.__display_ticket_list (username, features, "New Features")

    def __list_improvements (self, username):
        improves = self.J.get_improvements (username)
        self.__display_ticket_list (username, improves, "Improvements")

    def __list_epics (self, username):
        epics = self.J.get_epics (username)
        self.__display_ticket_list (username, epics, "Epics")

    def __list_stories (self, username):
        stories = self.J.get_stories (username)
        self.__display_ticket_list (username, stories, "Stories")

    def __list_rmas (self, username):
        rmas = self.J.get_rmas (username)
        self.__display_ticket_list (username, rmas, "RMAs")

    def __list_tests (self, username):
        tests = self.J.get_tests (username)
        self.__display_ticket_list (username, tests, "Tests")

    def __open_ticket (self, opt='-b', ticket):


    JIRA_func_dict = {
        pyJIRA.JIRA_BUG            : __list_bugs,
        pyJIRA.JIRA_NEW_FEATURE    : __list_new_features,
        pyJIRA.JIRA_IMPROVEMENT    : __list_improvements,
        pyJIRA.JIRA_EPIC           : __list_epics,
        pyJIRA.JIRA_STORY          : __list_stories,
        pyJIRA.JIRA_RMA            : __list_rmas,
        pyJIRA.JIRA_TEST           : __list_tests,
        pyJIRA.JIRA_TASK           : __list_tasks
    }

    # -- Public Functiosn
    # Overload function in Cmd class to flush command line after each command
    def emptyline (self):
        pass

    def do_ls (self, ticket_type):
        ticket = ticket_type.split ()
        if len (ticket) == ARG_LIMIT_COMMAND_LS:
            status, value = self.__check_ticket_valid (ticket[0])
            if status == True:
                self.JIRA_func_dict[value] (self, ticket[1])
            else:
                print USAGE_COMMAND_LS
        else:
            print USAGE_COMMAND_LS

    def do_open (self, ticket):
        ticket = ticket_type.split ()
        if len (ticket) == ARG_LIMIT_COMMAND_OPEN:
            self.__open_ticket (ticket[1], ticket[2])
        else if len (ticket) == ARG_LIMIT_COMMAND_OPEN - 1:
            self.__open_ticket (ticket[1])
        else:
            print USAGE_COMMAND_OPEN

    def do_create (self, title):
        print "Create"

    def do_comment (self, ticket):
        print "Comment"

    def do_EOF(self, line):
        return True

def main ():
    jira = JIRA_ocml ()
    jira.cmdloop ()

if __name__ == "__main__":
    main ()

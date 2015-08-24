#!/bin/python

import sys
import getopt
import pyJIRA

def JIRA_cmd_list_issues (jira, username):
    issues = jira.get_issues (username)
    num_issues = len (issues)

    if num_issues > 0:
        print "============================================================="
        print "List of Bugs - %s" % username
        for issue_cnt in range (num_issues):
            print "--------------------------------------------------------------"
            print issues[issue_cnt]
    else:
        print "Woops: No bugs available for %s" % username


def JIRA_cmd_list_tasks (jira, username):
    tasks = jira.get_tasks (username)
    num_tasks = len (tasks)

    if num_tasks > 0:
        print "============================================================="
        print "List of Tasks - %s" % username
        for task_cnt in range (num_tasks):
            print "--------------------------------------------------------------"
            print tasks[task_cnt]
    else:
        print "Woops: No tasks available for %s" % username


def JIRA_cmd_list_new_features ():
    return

def JIRA_cmd_list_improvements ():
    return

def JIRA_cmd_list_epics ():
    return

def JIRA_cmd_list_stories ():
    return

def JIRA_cmd_list_rmas ():
    return

def JIRA_cmd_list_tests ():
    return



def JIRA_usage ():
    print "Usage: Invalid paramters. Try again"


JIRA_func_dict = {
    pyJIRA.JIRA_BUG            : JIRA_cmd_list_issues,
    pyJIRA.JIRA_NEW_FEATURE    : JIRA_cmd_list_new_features,
    pyJIRA.JIRA_IMPROVEMENT    : JIRA_cmd_list_improvements,
    pyJIRA.JIRA_EPIC           : JIRA_cmd_list_epics,
    pyJIRA.JIRA_STORY          : JIRA_cmd_list_stories,
    pyJIRA.JIRA_RMA            : JIRA_cmd_list_rmas,
    pyJIRA.JIRA_TEST           : JIRA_cmd_list_tests,
    pyJIRA.JIRA_TASK           : JIRA_cmd_list_tasks
}

def main ():
    j = pyJIRA.JIRA ("bwinata", "Evolve_729183", "https://xeranet.atlassian.net")

    try:
        opts, args = getopt.getopt (sys.argv[1:], "l:f:o:c:")
    except getopt.GetoptError as e:
        JIRA_usage ()
        sys.exit (2)

    for o, a in opts:
        if o == '-l' and len (sys.argv) == 4:
            if a in pyJIRA.JIRA_TYPES_DICT.keys ():
                value = pyJIRA.JIRA_TYPES_DICT[a]
                JIRA_func_dict[value] (j, sys.argv[3])
                break
            else:
                JIRA_usage ()
        else:
            JIRA_usage ()

    #JIRA_cmd_list_issues (j, "bwinata")
    #JIRA_cmd_list_tasks (j, "bwinata")



if __name__ == "__main__":
    main ()

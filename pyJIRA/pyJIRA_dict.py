#!/bin/python

from pyJIRA_consts import *

JIRA_ERROR_DICT = {
    JIRA_ERROR_CREDENTIALS_MISSING: "Credentials are missing. Please try again",
    JIRA_ERROR_CREDENTIALS_INVALID: "Credentials are invalid. Please try again"
}

JIRA_TYPES_DICT = {
    "bugs"          : JIRA_BUG,
    "feats"         : JIRA_NEW_FEATURE,
    "improves"      : JIRA_IMPROVEMENT,
    "epics"         : JIRA_EPIC,
    "stories"       : JIRA_STORY,
    "rmas"          : JIRA_RMA,
    "tests"         : JIRA_TEST,
    "tasks"         : JIRA_TASK
}

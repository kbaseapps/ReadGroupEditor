# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
import os
import uuid

# silence whining
import requests
requests.packages.urllib3.disable_warnings()

from biokbase.workspace.client import Workspace as workspaceService
from SetAPI.SetAPIClient import SetAPI
#END_HEADER


class ReadsSetEditor:
    '''
    Module Name:
    ReadsSetEditor

    Module Description:
    A KBase module: ReadSetEditor
This sample module contains one small method - save_read_set.
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.1.0"
    GIT_URL = "ssh://git@github.com/eapearson/ReadsSetEditor"
    GIT_COMMIT_HASH = "4db5400faeaf1c2e58fb7ca291e68602b2615201"

    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.servicewizardURL = config['service-wizard-url']
        #END_CONSTRUCTOR
        pass

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

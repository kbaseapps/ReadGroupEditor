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


class ReadGroupEditor:
    '''
    Module Name:
    ReadGroupEditor

    Module Description:
    A KBase module: ReadGroupEditor
This sample module contains one small method - save_read_group.
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbaseapps/ReadGroupEditor"
    GIT_COMMIT_HASH = "a0b903922b0a52faa1de779bd6bfd17f815c2332"
    
    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        #END_CONSTRUCTOR
        pass
    

    def save_read_set(self, ctx, params):
        """
        :param params: instance of type "save_read_set_params" (** **  Method
           for adding Reads objects to a ReadsSet) -> structure: parameter
           "workspace_name" of String, parameter "output_readset_name" of
           String, parameter "input_reads_list" of list of String, parameter
           "desc" of String
        :returns: instance of type "save_read_set_output" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN save_read_set
        #END save_read_set

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method save_read_set return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

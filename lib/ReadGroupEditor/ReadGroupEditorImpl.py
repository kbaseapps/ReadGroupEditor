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
    GIT_COMMIT_HASH = "12d38b7b32b6fbb78e455126ea741f055b8da940"
    
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
    

    def save_read_group(self, ctx, params):
        """
        :param params: instance of type "save_read_group_params" (** ** 
           Method for adding Reads objects to a Reads Group) -> structure:
           parameter "workspace_name" of String, parameter
           "output_readgroup_name" of String, parameter "input_reads_list" of
           list of String, parameter "desc" of String
        :returns: instance of type "save_read_group_output" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN save_read_group

        console = []
        invalid_msgs = []
        #self.log(console,'Running save_read_group with params=')
        #self.log(console, "\n"+pformat(params))
        report = ''
#        report = 'Running KButil_Add_Genomes_to_GenomeSet with params='
#        report += "\n"+pformat(params)

        #### do some basic checks
        #
        if 'workspace_name' not in params:
            raise ValueError('workspace_name parameter is required')
        if 'desc' not in params:
            raise ValueError('desc parameter is required')
        if 'input_reads_list' not in params:
            raise ValueError('input_reads_list parameter is required')
        #if 'input_readsset_name' not in params:
        #    raise ValueError('input_readsset_name parameter is optional')
        if 'output_readsgroup_name' not in params:
            raise ValueError('output_readsgroup_name parameter is required')


        # Build ReadSet
        #
        elements = dict()

        savereadssetparams = {}
        savereadssetparams['workspace_name'] = params['workspace_name']
        savereadssetparams['output_object_name'] = params['output_readset_name']
        readsetdata = {}
        if(params['desc'] is not None):
            readsetdata['description'] = params['desc']
        readsetdata['items'] = []

        print "WS "+params['workspace_name']
        print "READS "+str(params['input_reads_list'])
        # add new reads
        for reads_name in params['input_reads_list']:
            readssetitem = {}
            readssetitem['ref'] = params['workspace_name']+'/'+reads_name
            readssetitem['label'] = ''
            readsetdata['items'].append(readssetitem)

        savereadssetparams['data'] = readsetdata

        # load the method provenance from the context object
        #
        #self.log(console,"Setting Provenance")  # DEBUG
        provenance = [{}]
        if 'provenance' in ctx:
            provenance = ctx['provenance']
        # add additional info to provenance here, in this case the input data object reference
        try:
            prov_defined = provenance[0]['input_ws_objects']
        except:
            provenance[0]['input_ws_objects'] = []
        for reads_name in params['input_reads_list']:
            provenance[0]['input_ws_objects'].append(params['workspace_name']+'/'+reads_name)
        provenance[0]['service'] = 'ReadGroupEditor'
        provenance[0]['method'] = 'save_read_group'


        # Save output object
        #
        #if len(invalid_msgs) == 0:
        #    self.log(console,"Saving ReadsSet")

        set_api = SetAPI(url=self.servicewizardURL,token= ctx['token'])
        #set_api._service_ver = "dev"
        set_api.save_reads_set_v1(savereadssetparams)

        # build output report object
        #
        #self.log(console,"BUILDING REPORT")  # DEBUG
        if len(invalid_msgs) == 0:
            #self.log(console,"reads in output group "+params['output_readset_name']+": "+str(len(elements.keys())))
            report += 'reads in output set '+params['output_readgroup_name']+': '+str(len(elements.keys()))+"\n"
            reportObj = {
                'objects_created':[{'ref':params['workspace_name']+'/'+params['output_readgroup_name'], 'description':'save_read_group'}],
                'text_message':report
                }
        else:
            report += "FAILURE:\n\n"+"\n".join(invalid_msgs)+"\n"
            reportObj = {
                'objects_created':[],
                'text_message':report
                }
        reportName = 'save_read_group_report_' + str(hex(uuid.getnode()))
        ws = workspaceService(self.workspaceURL, token=ctx['token'])
        report_obj_info = ws.save_objects({
                'workspace': params['workspace_name'],
                'objects':[
                    {
                        'type':'KBaseReport.Report',
                        'data': reportObj,
                        'name': reportName,
                        'meta': {},
                        'hidden': 1,
                        'provenance': provenance
                    }
                ]
            })[0]


        # Build report and return
        #
        #self.log(console,"BUILDING RETURN OBJECT")
        returnVal = { 'report_name': reportName,
                      'report_ref': str(report_obj_info[6]) +
                                    '/' + str(report_obj_info[0]) +
                                    '/' + str(report_obj_info[4]),
                      }
        #self.log(console,"save_read_group DONE") 

        #END save_read_group

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method save_read_group return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

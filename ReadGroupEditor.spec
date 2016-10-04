/*
A KBase module: ReadGroupEditor
This sample module contains one small method - save_read_group.
*/

module ReadGroupEditor {

    typedef string workspace_name;
    typedef string output_readset_name;

    /*
    **
    **  Method for adding Reads objects to a ReadsSet
    */
    typedef structure {
        string workspace_name;
        string  output_readset_name;
        list <string> input_reads_list;
        string desc;
    } save_read_set_params;

    typedef structure {
        string report_name;
        string  report_ref;
    } save_read_set_output;

    funcdef save_read_set (save_read_set_params params)  returns (save_read_set_output) authentication required;

};

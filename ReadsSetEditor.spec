/*
A KBase module: ReadSetEditor
This sample module contains one small method - save_read_set.
*/

module ReadsSetEditor {

    typedef string workspace_name;
    typedef string output_readset_name;

    /*
    **
    **  Method for adding Reads objects to a Reads Set
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

    /* dummy method ... this is never actually invoked, rather SetAPI/save_reads_set_v1 is */
    funcdef save_reads_set_v1() returns (UnspecifiedObject outputs) authentication required;

};

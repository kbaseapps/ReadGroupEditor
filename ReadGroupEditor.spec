/*
A KBase module: ReadGroupEditor
This sample module contains one small method - save_read_group.
*/

module ReadGroupEditor {

    typedef string workspace_name;
    typedef string data_obj_name;
    typedef string data_obj_ref;

     /* KButil_Add_Genomes_to_GenomeSet()
    **
    **  Method for adding Reads objects to a ReadsSet
    */
    typedef structure {
        workspace_name workspace_name;
        data_obj_name  input_reads_names;
        data_obj_name  input_readsset_name;
        data_obj_name  output_readset_name;
        string desc;
    } save_read_group_params;

    typedef structure {
        data_obj_name report_name;
        data_obj_ref  report_ref;
    } save_read_group_output;

    funcdef save_read_group (save_read_group_params params)  returns (save_read_group_output) authentication required;

};

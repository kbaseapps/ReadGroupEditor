
package us.kbase.readsseteditor;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: save_read_set_params</p>
 * <pre>
 * **
 * **  Method for adding Reads objects to a Reads Set
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "output_readset_name",
    "input_reads_list",
    "desc"
})
public class SaveReadSetParams {

    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    @JsonProperty("output_readset_name")
    private java.lang.String outputReadsetName;
    @JsonProperty("input_reads_list")
    private List<String> inputReadsList;
    @JsonProperty("desc")
    private java.lang.String desc;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("workspace_name")
    public java.lang.String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public SaveReadSetParams withWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("output_readset_name")
    public java.lang.String getOutputReadsetName() {
        return outputReadsetName;
    }

    @JsonProperty("output_readset_name")
    public void setOutputReadsetName(java.lang.String outputReadsetName) {
        this.outputReadsetName = outputReadsetName;
    }

    public SaveReadSetParams withOutputReadsetName(java.lang.String outputReadsetName) {
        this.outputReadsetName = outputReadsetName;
        return this;
    }

    @JsonProperty("input_reads_list")
    public List<String> getInputReadsList() {
        return inputReadsList;
    }

    @JsonProperty("input_reads_list")
    public void setInputReadsList(List<String> inputReadsList) {
        this.inputReadsList = inputReadsList;
    }

    public SaveReadSetParams withInputReadsList(List<String> inputReadsList) {
        this.inputReadsList = inputReadsList;
        return this;
    }

    @JsonProperty("desc")
    public java.lang.String getDesc() {
        return desc;
    }

    @JsonProperty("desc")
    public void setDesc(java.lang.String desc) {
        this.desc = desc;
    }

    public SaveReadSetParams withDesc(java.lang.String desc) {
        this.desc = desc;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((((("SaveReadSetParams"+" [workspaceName=")+ workspaceName)+", outputReadsetName=")+ outputReadsetName)+", inputReadsList=")+ inputReadsList)+", desc=")+ desc)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

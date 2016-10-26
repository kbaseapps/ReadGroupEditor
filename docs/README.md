# README

## About

This module exists to supply the reads_set_editor method, which is used to build a Reads Set Editor in the Narrative UI.

The method spec contains just enough information to provide for the method to appear in the Narrative app panel, and for the Narrative back end code to route the editor output to the SetAPI save_reads_set_v1 method.

Note that the specification of the target dynamic service, SetAPI, is encoded in the method spec.


## Workarounds


### validation errors

Due to the "misuse" of the ui spec.json service mapping to refer to the SetAPI dynamic service, kb-sdk validate will complain:

```
 unknown method "save_reads_set_v1" defined within path [behavior/service-mapping/method] in spec.json
```

Even if you create a dummy method in the top level spec (via funcdef), the validator will complain about the module name not matching.

The good news is that the module will still build and deploy!
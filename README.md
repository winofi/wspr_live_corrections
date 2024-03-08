# DRAFT DOCUMENT NOT ACTUALLY IMPLEMENTED
# Correcting wspr
There are many known errors inside the Wspr (wsprnet.org) dataset. This repository contains a collection of known issues which are applied to the wspr.live database. 

### Automated (fast) wspr.live spot validation process
Incoming spots are validated against "fast" checks defined in folder live_checks. They are simple plausibility checks written in python not using any context but the actual spot. If any of this checks return a negative result the spot is marked as -10 in the validation_state column. If all validations are positive they get a validation score of 10. 

### Asynchronous "slow" spot validation. 
They are defined as SQL statements inside the manual_corrections folder and get directly applied against the dataset to correct errors or mark spots as bad if they are false decodes. 
Check files are named using a unique number and are executed in ascending order. The number of the last check executed is stored inside the applied_checks table.  

#### Correction rules
* The correction file has to contain an explanation of what is wrong in the corresponding spots. If available the source of the knowledge must be specified. 
* If there is a decoding or configuration error (for example the rx frequency is wrong) the corresponding fields get corrected and the spot validation_state is set to 20 (or -9 if they are a known telemetry coding scheme). 
* If spots are known false decodes, they are marked as -20.
* If spots are known valid they might be marked as 30. 

### Validation State (column "validation_state" in rx table):
| Validation State | Desciption |
|-----|-----|
| -20 | Known bad spot (this spot is known to be a bad decode) |
| -10 | Generic validation failed (might still be a valid spot like balloon telemetry) |
| -9 | corrected "non normal" wspr spot |
| 0 | Not validated |
| 10 | Validated against generic validation checks |
| 20 | Corrected to be valid |
| 30 | Manually validated by transmitting and receiving station |

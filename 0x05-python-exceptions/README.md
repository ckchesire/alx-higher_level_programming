# 0x05. Python - Exceptions 
Errors are generally critical issues that cause program termination, while exceptions are specific runtime errors that can be caught and handled to allow the program to continue. 

Exceptions occur when something goes wrong during execution, such as 
- invalid input, 
- file handling issues,
- network failures,.etc. 

They are managed using `try`, `except`, `else`, and `finally` blocks to gracefully handle and recover from errors, ensuring the program remains robust. Raising exceptions helps signal issues in a controlled way, and catching exceptions prevents crashes while providing user-friendly error handling. 

Clean-up actions, often handled in the `finally` block, ensure that resources like files or connections are properly released, regardless of exceptions.

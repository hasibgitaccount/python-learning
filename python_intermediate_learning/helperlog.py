import logging
log = logging.getLogger(__name__) # its good practice to use double underscore.
# so this create a logger with the name of the file(module)
# then we can use the logger to log something.

log.info('hello from helper')
# then we need to go to our main file(module), here the log file.


# now not to print it

import logging
logger = logging.getLogger(__name__) # its good practice to use double underscore.
# so this create a logger with the name of the file(module)
# then we can use the logger to log something.

# here we need to write it false to not get printed that log in log file(module).
# logger.propagate = False        # lets just comment it.
logger.info('hello from helper')
# then we need to go to our main file(module), here the log file.
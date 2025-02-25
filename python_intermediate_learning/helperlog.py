import logging
log = logging.getLogger(__name__) # its good practice to use double underscore.
# so this create a logger with the name of the file(module)
# then we can use the logger to log something.
log.info('hello from helper')
# then we need to go to our main file(module), here the log file.
# python already comes with a powerful build in logging module. so you can quickly add logging to your application by simply saying import logging.
import logging
# in this course we will have a quick look at the different block level, the different configuration options, how to log in different modules, how to use different lock handlers, how to capture stack traces in your log and how to use rotating file handler.

# after importing logging we can import five different log levels.
'''
1. logging.debug (this is a debug message)
2. logging.info (this is an info message)
3. logging.warning (this is a warning message)
4. logging.error (this is an error message)
5. logging.critical (this is a critical message)
'''

# the indicate the severity of the events
'''logging.debug ('this is a debug message')
logging.info ('this is an info message')
logging.warning ('this is a warning message')
logging.error ('this is an error message')
logging.critical ('this is a critical message')''' # by default only warning and after it will be printed.

# if we want to change this then we can do that by setting up the basic configuration. and we need to do it right after importing the logging module.
import logging
logging.basicConfig

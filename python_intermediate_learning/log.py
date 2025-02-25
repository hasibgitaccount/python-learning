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


# if we want to change this then we can do that by setting up the basic configuration. and we need to do it right after importing the logging module.
# then we can specify some arguments for the basic configuration.
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

'''logging.debug ('this is a debug message')
logging.info ('this is an info message')
logging.warning ('this is a warning message')
logging.error ('this is an error message')
logging.critical ('this is a critical message')'''
# by default our logger is called the root logger.



# if i want to log in different modules, then it's best practice to not use this root logger, but create your own logger in my module.

# for that we need to go to another file(module) , here we created a helper file(module).

# after finishing the work in helper file(module) we come back to this file(module)
# now here after importing logging and setting the basic config if i import the helper file(module) then it will lock the message from the helper file(module) with the name of this logger.so its good practice to create your own logger in your files(modules) with this get logger function and then give it name with double underscore here as a name.
import helperlog

# if i create this log on here, then it will create a hierarchy of loggers. is starts at the root logger and all this new logger gets added to this hierarchy and they propagate its messages up to the base logger.

# now if i dont want to have this propagation, i can say logger.propogate equals false in helperlog.py file(module). by default its true. and now this will not propogate to the base logger. 

# import helperlog
# now if we run the module and import the helperlog file(module) then nothing gets logged because it doesn't propogate to our base logger.

# LOCK HANDLERS

# handlers objects are responsible for dispatching the appropriate lock message to the handlers specific destination. i can use different handlers to send log messages to this standard output stream to files via HTTP or via email.

# how to set different log handlers.
logger1 = logging.getLogger(__name__)

# create handler
# i want to have a handler that locks to this stream, a stream handler. this equals logging.streaming handler. 
stream_h = logging.StreamHandler()

# #then a file handler that locks to the file. the file handler equals logging.file handler and then it needs a name.
file_h = logging.FileHandler('file.log')

# and then typically for each handler you want to set the level and the format.
stream_h.setLevel(logging.WARNING)

# and for the file handler, the file handler should only log method messages.  
file_h.setLevel(logging.ERROR)

# now lets specify some format.
fomatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

#   PAUSED THE VIDEO AT 2 HOURS 28 MINUTES 45 SECONDS.
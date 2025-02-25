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


'''
if i create
'''
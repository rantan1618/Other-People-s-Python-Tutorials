# Logging
# Purpose: Record progress and problems...
# Levels: Debug, Info, Warning, Error, Critcal

import logging

print(dir(logging))
'''
['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler',
 'Filter', 'Filterer', 'Formatter', 'Handler', 'INFO', 'LogRecord', 'Logger',
  'LoggerAdapter', 'Manager', 'NOTSET', 'NullHandler', 'PercentStyle', 'PlaceHolder',
   'RootLogger', 'StrFormatStyle', 'StreamHandler', 'StringTemplateStyle', 'Template',
    'WARN', 'WARNING', '_STYLES', '_StderrHandler', '__all__', '__author__',
     '__builtins__', '__cached__', '__date__', '__doc__', '__file__', '__loader__',
      '__name__', '__package__', '__path__', '__spec__', '__status__', '__version__',
       '_acquireLock', '_addHandlerRef', '_checkLevel', '_defaultFormatter', '_defaultLastResort',
        '_handlerList', '_handlers', '_levelToName', '_lock', '_logRecordFactory',
         '_loggerClass', '_nameToLevel', '_register_at_fork_reinit_lock', '_releaseLock',
          '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime', '_str_formatter',
           '_warnings_showwarning', 
'addLevelName', 'atexit', 'basicConfig', 'captureWarnings', 'collections', 'critical',
 'currentframe', 'debug', 'disable', 'error', 'exception', 'fatal', 
'getLevelName', 'getLogRecordFactory', 'getLogger', 'getLoggerClass', 'info', 'io',
 'lastResort', 'log', 'logMultiprocessing', 'logProcesses', 'logThreads', 'makeLogRecord',
  'os', 'raiseExceptions', 're', 'root', 'setLogRecordFactory', 'setLoggerClass', 'shutdown',
   'sys', 'threading', 'time', 'traceback', 'warn', 'warning', 'warnings', 'weakref']
'''

# Create and configure logger
LOG_FORMAT = "%(Levelname)s" %(asctime)s - %(message)s"
logging.basicConfig(filename = "Other Peoples Tutorials\Socratica\log_file.log"
                                        level = logging.DEBUG,
                                        format = LOG_FORMAT,
                                        filemode = 'w')
logger = logging.getLogger()

# Test Messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

# Test the logger
logger.info("Our first message.")

print(logger.level)

# Logger Warning Levels
# NOTSET 0
# DEBUG 10
# INFO 20
# WARNING 30
# ERROR 40
# CRITICAL 50

def quadratic_forumla(a, b, c):
    ''' Return the solution to the equation ax^2 + bx + c = 0.'''
    logger.info("quadratic_formula({0}, {1}, {2}".format(a, b, c))

    # Complete the 
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the roots
    logger.debug("# Compute the two roots.")
    roots1 = (-b + math.sqrt(disc)) / (2*a)
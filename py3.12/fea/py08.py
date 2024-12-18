import logging
def log_access(level = logging.DEBUG):
    def decorator(func):
        logger = logging.getLogger(func.__module__)
        log_level = level
        def wrapper(*args, **kwargs):
            logger.log(log_level, 'call %s():' % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_access(logging.INFO)
def homepage():
    print('homepage')

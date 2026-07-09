def welcome_decorator(function):
    def wrapper():
        print("Welcome to python class")
        function()
    return wrapper
@welcome_decorator
def topic_name():
    print("Today topic is decorator")
topic_name()
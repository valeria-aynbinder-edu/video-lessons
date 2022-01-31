def greeting_decorator(other_func):

    def greeting_func():
        print(f"\n---------------------------------------\n"
              f"Hello!\nWelcome to function {other_func.__name__}!\n"
              f"---------------------------------------\n")
        # Note we call the function we received as parameter
        # inside our inner function
        other_func()
        print(f"\n---------------------------------------\n"
              f"Good-bye!\nThanks for using function {other_func.__name__}!"
              f"\n---------------------------------------\n")

    return greeting_func

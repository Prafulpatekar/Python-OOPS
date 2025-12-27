def login_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise Exception("User not authenticated")
        return func(user, *args, **kwargs)

    return wrapper


def func_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result

    return wrapper


@func_logger
@login_required
def get_user_info(user):
    return user.get("info")

lst = [1, 2, 3, 4, 5]
# lst.remove()



dct = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "gaming", "coding"],
}



if __name__ == "__main__":
    # Example user data
    # users = [
    #     {"is_authenticated": True, "info": "User information goes here"},
    #     {"is_authenticated": False, "info": "User information goes here"},
    # ]

    # # Call the decorated function with the user data
    # for user_data in users:
    #     try:
    #         print(get_user_info(user_data))  # Should work
    #     except Exception as e:
    #         print(e)
    print(dct.fromkeys(lst,0))  # Creates a new dictionary with keys from lst and values set to 0
    print(dct.get("name"))  # Returns the value associated with the key "name"
    print(dct.items())  # Returns a view object that displays a list of a dictionary's key-value tuple pairs
    print(dct.values())  # Returns a view object that displays a list of all the keys in the dictionary
    st = {1, 2, 3, 4, 5}

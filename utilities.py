import os

def print_formatter(msg: str, formatter: str = '-') -> None:
    formatter_multiplier = len(msg)
    duplicated_formatter = formatter * formatter_multiplier

    print(duplicated_formatter)
    print(msg)
    print(duplicated_formatter)


def welcome_msg() -> None:
    user_name: str = os.getlogin()
    msg: str = f'Welcome {user_name}'
    print_formatter(msg)

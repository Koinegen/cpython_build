import random


async def super_secret_function() -> float:
    return random.random()


def error_function():
    raise Exception('This is test')

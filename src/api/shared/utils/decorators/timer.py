import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(
            f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute"
        )
        return result

    return wrapper


def async_timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(
            f"Async function '{func.__name__}' took {execution_time:.4f} seconds to execute"
        )
        return result

    return wrapper

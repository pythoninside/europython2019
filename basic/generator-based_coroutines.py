# Generator-based coroutines are a bit more complex
from typing import Generator


#                           Generator[YieldType, SendType, ReturnType]
def echo_n_times(n: int) -> Generator[str, str, int]:
    value = 'Please type something'
    orig_n = n
    while n >= 0:
        value = yield value
        n -= 1
    return orig_n

# Coroutines can be type-annotated like regular functions.
# Pure generators return an iterator.
from asyncio import AbstractEventLoop
from socket import socket
from typing import Optional, Iterator


def my_range(n: int) -> Iterator[int]:
    # while i:=0 < n:  <- assignment expressions not supported :-(
    i = 0
    while i < n:
        yield i
        i += 1
    return 'foo'  # <- this is embed in the StopIteration exception


async def connection_handler(client: socket, loop: AbstractEventLoop) -> None:
    while True:
        data: Optional[bytes] = await loop.sock_recv(client, 10000)
        if not data:
            break
        await loop.sock_sendall(client, data)
    print('Connection closed')
    client.close()

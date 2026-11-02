#!/usr/bin/env python3

"""Module number 4"""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

async def handle_connection(websocket):
    """Sends a message and waits for the response"""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send(f'ERR:EMPTY')
            else:
                await websocket.send(f'OK:{message}')
    except ConnectionClosed:
        pass


async def main():
    server = await serve(handle_connection(), '127.0.0.1', 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())

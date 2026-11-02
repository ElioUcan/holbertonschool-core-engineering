#!/usr/bin/env python3

"""Module number 4"""

import asyncio
from websockets.asyncio.client import connect
from websockets.exceptions import ConnectionClosed

async def connect_and_send(uri: str, text: str) -> str:
    """Sends a message and waits for the response"""
    try:
        async with connect(uri) as websocket:
            if len(text.strip()) == 0:
                await websocket.send(f'ERR:EMPTY')
            else:
                await websocket.send(f'OK:{text}')
            message = await websocket.recv()
            print(f'{message}')
    except ConnectionClosed:
        print(ConnectionClosed)


if __name__ == "__main__":
    asyncio.run(connect_and_send("ws://127.0.0.1:8765", 'Hello WebSocket'))

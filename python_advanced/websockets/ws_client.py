#!/usr/bin/env python3

"""Module number 4"""

import asyncio
from websockets.asyncio.client import connect


async def connecr_and_send(uri: str, text: str) -> str:
    """Sends a message and waits for the response"""
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send('Hello WebSocket')
        message = await websocket.recv()
        print(message)


if __name__ == "__main__":
    asyncio.run(connecr_and_send())

#!/usr/bin/env python3

"""Module number 5"""

import asyncio
import json
from websockets.asyncio.client import serve
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def handle_client(websocket):
    """Unicast connection"""
    connected_clients.add(websockets)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    server = await serve(handle_client, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())

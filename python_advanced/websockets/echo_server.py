#!/usr/bin/env python3

"""Echo server with asyncio"""

from websockets.asyncio.server import serve
import asyncio


async def connnection_handler(websocket):
    """Takes a web socket and responds hello"""
    async for message in websocket:
        await websocket.send(message)


async def main():
    server = await serve(connnection_handler, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())

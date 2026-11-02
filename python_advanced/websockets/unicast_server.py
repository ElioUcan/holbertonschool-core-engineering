#!/usr/bin/env python3

"""Module number 5"""

import asyncio
import json
from websockets.asyncio.client import serve

connected_clients = {}


async def handle_client(websocket):
    """Unicast connection"""
    idx = None
    try:
        message1 = await websocket.recv()
        data = json.loads(message1)

        if data.get("action") == "register" and data.get("idx"):
            idx = data["idx"]
            connected_clients[idx] = websocket
            await websocket.send("User registered")
        else:
            await websocket.close()
            return
        async for message in websocket:
            data = json.loads(message)
            target = data.get("target")
            payload = data.get("message")

            if target in connected_clients:
                target_ws = connected_clients[target]
                await target_ws.send(f"U:{message}")
            else:
                pass
    except Exception as e:
        pass

    finally:
        if idx in connected_clients:
            del connected_clients[idx]


async def main():
    async with websocket.serve(handle_client, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())

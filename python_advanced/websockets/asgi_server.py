#!/usr/bin/env python3

import asyncio
from starlette.websockets import WebSocket, WebSocketDisconnect
from starlette.routing import Route, WebSocketRoute
from starlette.applications import Starlette
from starlette.responses import HTMLResponse


async def hpage_endpoint(request):
    """
    HTTP endpoint displays html
    """
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def ws_endpoint(websocket: WebSocket):
    """
    Websocket endpoint echoes text
    """
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data)
    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        Route("/", hpage_endpoint),
        WebSocketRoute("/ws", ws_endpoint)
    ]
)

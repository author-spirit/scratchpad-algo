import socketio

sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio, static_files={
    '/': './public/'
})

@sio.event
async def connect(sid, environ):
    print("Connected to ", sid)
    await sio.emit("server_message", "Guys!! New one joined.. "+ sid, skip_sid=sid)

@sio.event
async def disconnect(sid):
    print("Disconnected ", sid)


@sio.event
async def message(sid, data):
    print("Data from client", data)

    # Send the server message to only to -> sid
    await sio.emit("server_message", {"text": "Hey Client, I am server"}, to=sid)


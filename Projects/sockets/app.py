import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})

@sio.event
def connect(sid, environ):
    print("Connected to ", sid)

@sio.event
def disconnect(sid):
    print("Disconnected ", sid)

@sio.event
def message(sid, data):
    print("Data from client", data)

    # Send the server message to only to -> sid
    sio.emit("server_message", {"text": "Hey Client, I am server"}, to=sid)

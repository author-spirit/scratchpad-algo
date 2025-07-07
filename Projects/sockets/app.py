import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})

@sio.event
def connect(sid, environ):
    print("Connected to ", sid)
    pass

@sio.event
def disconnect(sid):
    print("Disconnected ", sid)



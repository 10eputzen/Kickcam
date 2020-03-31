import tornado.ioloop
import tornado.web
from tornado import websocket
from myconfig import *

GLOBALS={
    'sockets': []
}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class ClientSocket(websocket.WebSocketHandler):
    def open(self):
        GLOBALS['sockets'].append(self)
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message("You said: " + message)

    def on_close(self):
        print("WebSocket closed")
        GLOBALS['sockets'].remove(self)

    def check_origin(self, origin):
        return True

class Announcer(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = self.get_argument('data')
        for socket in GLOBALS['sockets']:
            socket.write_message(data)
        self.write('Posted')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", ClientSocket),
    (r"/push", Announcer),
    #http://localhost:8888/push?data=XXX
])

if __name__ == "__main__":
    application.listen(websocketPort)
    tornado.ioloop.IOLoop.instance().start()
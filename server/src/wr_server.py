import tornado.ioloop
import tornado.web
import handler
import model
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

def make_app():
    return tornado.web.Application([
        (r"/predict",handler.WinRatePredictHandler),
        ])


if __name__ == "__main__":
    app = make_app()
    app.listen(12345)
    tornado.ioloop.IOLoop.current().start()

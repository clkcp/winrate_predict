import tornado.ioloop
import tornado.web
import tornado.websocket
import model
import json
class WinRatePredictHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("Websocket opened")

    def on_message(self, message):
        m = model.PredictModel()
        win_rate = m.predict(message)
        print message
        heros = json.loads(message)
        self.write_message(str(win_rate))
        self.close()

    def on_close(self):
        print("Websocket closed")

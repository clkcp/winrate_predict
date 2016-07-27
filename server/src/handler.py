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
        self.ret_message = {"state":1}
        self.error_message = {"state":0}

    def send_error_message(self):
        self.write_message(json.dumps(self.error_message))

    def send_message(self, ret):
        self.ret_message.update(ret)
        self.write_message(json.dumps(self.ret_message))
        print "Send", self.ret_message
    
    def verify(self, heros):
        if not ("A" in heros.keys() and "B" in heros.keys()):
            return False
        if not (len(heros["A"]) == 5 and len(heros['B']) == 5):
            return False
        return True

    def on_message(self, message):
        m = model.PredictModel()
        win_rate = m.predict(message)
        heros = json.loads(message)
        print heros
        if not self.verify(heros):
            self.send_error_message()
        ret = {"win_rate":win_rate}
        self.send_message(ret)
        self.close()

    def on_close(self):
        print("Websocket closed")

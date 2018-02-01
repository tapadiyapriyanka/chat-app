from channels.routing import route
from websocket_app.consumers import ws_connect, ws_disconnect

# def message_handler(message):
#     print(message['text'])

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]

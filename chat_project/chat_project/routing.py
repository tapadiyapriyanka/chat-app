from channels.routing import route
from chat_app.consumers import ws_connect, ws_disconnect, ws_receive #ws_message


channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.receive', ws_receive),
    route('websocket.disconnect', ws_disconnect),
    # route("websocket.receive", ws_message),
]

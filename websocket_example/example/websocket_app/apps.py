from django.apps import AppConfig


class WebsocketAppConfig(AppConfig):
    name = 'websocket_app'

    def ready(self):
        import websocket_app.signals

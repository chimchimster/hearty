from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print(self.scope['user'])

    async def disconnect(self, code):
        pass

    async def websocket_receive(self, message):
        event = message['text']
        await self.send(json.dumps({'text': event}))

    async def websocket_send(self, message):
        await self.send(json.dumps({'text': message}))

    async def receive(self, text_data=None, bytes_data=None):
        pass

    async def send(self, text_data=None, bytes_data=None, close=False):
        pass
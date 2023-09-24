import json
import websockets


class ApiTester:
    def __init__(self, server_address, port):
        self.uri = f'ws://{server_address}:{port}'

    async def send_request(self, request):
        async with websockets.connect(self.uri) as ws:
            await ws.send(json.dumps(request))
            response = await ws.recv()
            return json.loads(response)

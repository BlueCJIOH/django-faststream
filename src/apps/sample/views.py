from rest_framework.views import APIView
from rest_framework.response import Response
import httpx

from apps.faststream_app.stream import broker


class PublishView(APIView):
    async def post(self, request):
        message = request.data.get("message", "Hello from Django")
        await broker.publish(message, topic="test-topic")

        httpx_client: httpx.AsyncClient = request.state["httpx_client"]
        await httpx_client.head("https://www.example.com/")

        return Response({"status": "sent", "message": message})

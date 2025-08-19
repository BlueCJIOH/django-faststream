from asgiref.sync import async_to_sync
from rest_framework.views import APIView
from rest_framework.response import Response
import httpx

from apps.faststream_app.stream import broker


class PublishView(APIView):
    def post(self, request):
        message = request.data.get("message", "Hello from Django")
        async_to_sync(broker.publish)(message, topic="test-topic")

        with httpx.Client() as httpx_client:
            httpx_client.head("https://www.example.com/")

        return Response({"status": "sent", "message": message})

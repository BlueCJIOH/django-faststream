from faststream import FastStream
from faststream.kafka import KafkaBroker

broker = KafkaBroker('kafka:9092')
faststream_app = FastStream(broker)

@broker.subscriber('test-topic')
async def handle(message: str) -> None:
    print(f'Received: {message}')

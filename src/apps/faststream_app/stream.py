import os
from faststream import FastStream
from faststream.kafka import KafkaBroker


KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

broker = KafkaBroker(KAFKA_BOOTSTRAP)
faststream_app = FastStream(broker)

@broker.subscriber('test-topic')
async def handle(message: str) -> None:
    print(f'Received: {message}')

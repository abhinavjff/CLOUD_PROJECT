from kafka import KafkaConsumer
import json
import psycopg2
import sys

# Kafka Consumer setup
consumer = KafkaConsumer(
    "api-requests",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="log-consumer-group"
)

# PostgreSQL connection setup
try:
    conn = psycopg2.connect(
        dbname="kafka_logs",
        user="kafka_user",
        password="kafka_pass",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
except Exception as e:
    print("❌ Could not connect to PostgreSQL:", e)
    sys.exit(1)

# Consuming and storing logs
print("🟢 Listening for logs from 'api-requests' topic...")
for message in consumer:
    try:
        log = message.value
        user_id = log.get("user_id")
        event = log.get("event")
        endpoint = log.get("endpoint")
        response_time = log.get("response_time_ms")

        cursor.execute(
            """
            INSERT INTO logs (user_id, event, endpoint, response_time_ms)
            VALUES (%s, %s, %s, %s)
            """,
            (user_id, event, endpoint, response_time)
        )
        conn.commit()
        print(f"✅ Stored log: {log}")
    except Exception as e:
        print("❌ Error storing log:", e)

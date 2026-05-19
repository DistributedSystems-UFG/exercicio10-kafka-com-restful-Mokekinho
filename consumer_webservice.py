from kafka import KafkaConsumer
from const import *
import sys

import threading


from flask import Flask, jsonify, request

ultima_msg = "Nenhuma mensagem recebida ainda"

def kafka_worker():
    global ultima_msg

    consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT], auto_offset_reset='earliest')


    topic = "temperaturaServer"
    

    consumer.subscribe([topic])
    for msg in consumer:
        ultima_msg = msg.value.decode('utf-8')
        print(f"Kafka recebeu: {ultima_msg}")




server = Flask(__name__)

@server.route('/temperatura', methods=['GET'])
def getTemperatura():
    return jsonify(ultima_msg), 200


if __name__ == '__main__':
    t = threading.Thread(target=kafka_worker, daemon=True)
    t.start()
    try:
        server.run(host = REST_IP,port=REST_PORT, debug=True)
    except KeyboardInterrupt:
        print("\nInterrupção detectada! Finalizando o producer...")
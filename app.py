import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_produtividade():
    while True:
        produtividade = {
            "maquina": {
                "nome": "Máquina de produção 1",
                "id": 1234,
                "produtividade": {
                    "data": "2023-07-12",
                    "tempo_operacional": random.randint(5000, 10000),
                    "quantidade_produzida": random.randint(500, 1500),
                    "taxa_defeito": random.uniform(0.01, 0.10)
                }
            }
        }
        return jsonify(produtividade)
        time.sleep(1)

if __name__ == '__main__':
    app.run()
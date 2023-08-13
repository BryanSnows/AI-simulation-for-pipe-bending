import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

production_order = [
    {
        "quantidade_planejada": "500900",
        "op_number": 123456789,
        "produtividade": {
            "data": "2023-07-12",
            "quantidade_esperada": 9000,
        }
    },
    {
        "quantidade_planejada": "500900",
        "op_number": 987654321,
        "produtividade": {
            "data": "2023-07-12",
            "quantidade_esperada": 8000,
        }
    },
    {
        "quantidade_planejada": "500900",
        "op_number": 192837465,
        "produtividade": {
            "data": "2023-07-12",
            "quantidade_esperada": 6000,
        }
    }
]

@app.route('/<int:op_number>')
def get_produtividade(op_number):
    for op in production_order:
        if op['op_number'] == op_number:
            return jsonify(op)
    return jsonify({"error": "Op não encontrada"}), 404

if __name__ == '__main__':
    app.run()
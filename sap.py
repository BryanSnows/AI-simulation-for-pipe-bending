import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

production_order = [
    {
        "op_number": "123456789",
        "production_goal_expected": "500",
        "tubo": {
            "descricao_tubo": "2023-07-12",
            "pipe_model_code": "ARC321423341234",
        }
    },
    {
        "op_number": "987654321",
        "production_goal_expected": "500",
        "tubo": {
            "descricao_tubo": "2023-07-12",
            "pipe_model_code": "ARC321423341234",
        }
    },
    {
        "op_number": "192837465",
        "production_goal_expected": "500",
        "tubo": {
            "descricao_tubo": "2023-07-12",
            "pipe_model_code": "ARC321423341234",
        }
    }
]

@app.route('/<string:op_number>')
def get_produtividade(op_number):
    for op in production_order:
        if op['op_number'] == op_number:
            return jsonify(op)
    return jsonify({"error": "Op não encontrada"}), 404

if __name__ == '__main__':
    app.run()
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
            "cod_tubo": 12,
        }
    },
    {
        "op_number": "987654321",
        "production_goal_expected": "600",
        "tubo": {
            "descricao_tubo": "2023-07-13",
            "cod_tubo": 13,
        }
    },
    {
        "op_number": "192837465",
        "production_goal_expected": "700",
        "tubo": {
            "descricao_tubo": "2023-07-14",
            "cod_tubo": 14,
        }
    },
    {
        "op_number": "112837465",
        "production_goal_expected": "800",
        "tubo": {
            "descricao_tubo": "2023-07-15",
            "cod_tubo": 15,
        }
    },
    {
        "op_number": "112837464",
        "production_goal_expected": "900",
        "tubo": {
            "descricao_tubo": "2023-07-16",
            "cod_tubo": 16,
        }
    },
    {
        "op_number": "999888777",
        "production_goal_expected": "10000",
        "tubo": {
            "descricao_tubo": "2023-08-24",
            "cod_tubo": 100,
        }
    },
    {
        "op_number": "125456789",
        "production_goal_expected": "500",
        "tubo": {
            "descricao_tubo": "2023-07-12",
            "cod_tubo": 12,
        }
    },
    {
        "op_number": "987654621",
        "production_goal_expected": "600",
        "tubo": {
            "descricao_tubo": "2023-07-13",
            "cod_tubo": 13,
        }
    },
    {
        "op_number": "192737465",
        "production_goal_expected": "700",
        "tubo": {
            "descricao_tubo": "2023-07-14",
            "cod_tubo": 14,
        }
    },
    {
        "op_number": "112839465",
        "production_goal_expected": "800",
        "tubo": {
            "descricao_tubo": "2023-07-15",
            "cod_tubo": 15,
        }
    },
    {
        "op_number": "112837434",
        "production_goal_expected": "900",
        "tubo": {
            "descricao_tubo": "2023-07-16",
            "cod_tubo": 16,
        }
    },
    {
        "op_number": "999888745",
        "production_goal_expected": "10000",
        "tubo": {
            "descricao_tubo": "2023-08-24",
            "cod_tubo": 100,
        }
    }
];

@app.route('/<string:op_number>')
def get_produtividade(op_number):
    for op in production_order:
        if op['op_number'] == op_number:
            return jsonify(op)
    return jsonify({"error": "Op não encontrada"}), 404

if __name__ == '__main__':
    app.run()
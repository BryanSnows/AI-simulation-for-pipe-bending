import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

production_order = [
    {
        "op_number": "123456789",
        "production_goal_expected": "500",
        "tubo": {
            "descricao_tubo": "TESTE KEYID",
            "cod_tubo": "ARC123456789983",
        }
    },
    {
        "op_number": "987654321",
        "production_goal_expected": "600",
        "tubo": {
            "descricao_tubo": "MODELO B",
            "cod_tubo": "ARC123456987456",
        }
    },
    {
        "op_number": "192837465",
        "production_goal_expected": "700",
        "tubo": {
            "descricao_tubo": "MODELO A UPDATE",
            "cod_tubo": "ARC987456321451",
        }
    },
    {
        "op_number": "112837465",
        "production_goal_expected": "800",
        "tubo": {
            "descricao_tubo": "TESTE FILE",
            "cod_tubo": "ARC756845698745",
        }
    },
    {
        "op_number": "112837464",
        "production_goal_expected": "900",
        "tubo": {
            "descricao_tubo": "TESTE FRONT PAULA",
            "cod_tubo": "ARC123456789000",
        }
    },
    {
        "op_number": "999888777",
        "production_goal_expected": "10000",
        "tubo": {
            "descricao_tubo": "TUBO A",
            "cod_tubo": "ARC927826672873",
        }
    },
    {
        "op_number": "125456789",
        "production_goal_expected": "500",
        "tubo": {
            "descricao_tubo": "TUBO UM",
            "cod_tubo": "ARC321423341234",
        }
    },
    {
        "op_number": "987654621",
        "production_goal_expected": "600",
        "tubo": {
            "descricao_tubo": "TESTE QUE DEU ERRADO",
            "cod_tubo": "ARC213423413411",
        }
    },
    {
        "op_number": "192737465",
        "production_goal_expected": "700",
        "tubo": {
            "descricao_tubo": "TUBOTESTE ERIKA",
            "cod_tubo": "ARC987654300000",
        }
    },
    {
        "op_number": "112839465",
        "production_goal_expected": "800",
        "tubo": {
            "descricao_tubo": "TUBO TESTEDOIS",
            "cod_tubo": "ARC292893737399",
        }
    },
    {
        "op_number": "112837434",
        "production_goal_expected": "900",
        "tubo": {
            "descricao_tubo": "TESTE SEM",
            "cod_tubo": "ARC564879556146",
        }
    },
    {
        "op_number": "999888745",
        "production_goal_expected": "10000",
        "tubo": {
            "descricao_tubo": "SKCWVLMLM",
            "cod_tubo": "ARC564879562136",
        }
    },
    {
        "op_number": "11111111",
        "production_goal_expected": "10000",
        "tubo": {
            "descricao_tubo": "SKCWVLMLM",
            "cod_tubo": "ARC5264879561112136",
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
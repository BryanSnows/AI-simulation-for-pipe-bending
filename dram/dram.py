import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        "enrollment": "123456789",
        "user_name": "ricardo silva",
        "password":"dram@1234",
    },
    {
        "enrollment": "987654321",
        "user_name": "bryan neves pinto",
        "password":"dram@1234",
    },
    {
        "enrollment": "192837465",
        "user_name": "kalebao dias",
        "password":"dram@1234",
    },
    {
        "enrollment": "112837465",
        "user_name": "ingra dantona",
        "password":"dram@1234",
    },
    {
        "enrollment": "112837464",
        "user_name": "paula murta",
        "password":"dram@1234",
    },
    {
        "enrollment": "999888777",
        "user_name": "leozinho pereira",
        "password":"dram@1234",
    },
    {
        "enrollment": "125456789",
        "user_name": "ricardo senna",
        "password":"dram@1234",
    },
    {
        "enrollment": "987654621",
        "user_name": "joao maia",
        "password":"dram@1234",
    },
    {
        "enrollment": "192737465",
        "user_name": "julio cesar",
        "password":"dram@1234",
    },
    {
        "enrollment": "112839465",
        "user_name": "ricardo bastos",
        "password":"dram@1234",
    },
    {
        "enrollment": "112837434",
        "user_name": "felipe feitosa",
        "password":"dram@1234",
    },
    {
        "enrollment": "999888745",
        "user_name": "joaquim pereria",
        "password":"dram@1234",
    },
    {
        "enrollment": "11111111",
        "user_name": "manoel da silva",
        "password":"dram@1234",
    }
];

@app.route('/<string:enrollment>')
def get_produtividade(enrollment):
    for user in users:
        if user['enrollment'] == enrollment:
            return jsonify(user)
    return jsonify({"error": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run()
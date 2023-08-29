import json
import redis
import time

REDIS_HOST = "172.100.11.127"
REDIS_PORT = 6379
REDIS_PASSWORD = "qweQWE123"

REDIS_KEY = "5_teste"

def update_and_save_to_redis(updated_data):

    redis_conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

    updated_data_str = json.dumps(updated_data)

    redis_conn.hset(REDIS_KEY, "data", updated_data_str)

    print("Dados salvos no Redis.")

data = {
    "process_id": 40,
    "process_status": True,
    "machine_model_id": 5,
    "daily_production_id": 232,
    "machineModel": {
        "machine_model_id": 5,
        "machine_model_name": "CNC 05",
        "machine_model_ip": "000.215.245.45",
        "machine_model_status": True
    },
    "dailyProduction": {
        "daily_production_id": 232,
        "production_goal_id": 58,
        "daily_production_date": "2023-08-30T04:00:00.000Z",
        "daily_production_goal": 250,
        "daily_production_produced": 0,
        "daily_production_situation": 1,
        "productionGoal": {
            "production_goal_id": 58,
            "production_goal_order": "123456789",
            "production_goal_expected": 500,
            "production_goal_produced": 0,
            "production_goal_situation": 1,
            "production_goal_start_date": "2023-08-29T16:55:35.000Z",
            "pipe_model_id": 8,
            "production_goal_finish_date": "2023-08-30T16:55:35.000Z",
            "production_goal_day": True,
            "pipeModel": {
                "pipe_model_id": 8,
                "pipe_model_name": "TESTE KEYID",
                "pipe_model_code": "ARC123456789983",
                "pipe_model_path": "elgin-cnc/1419991689690463990.jpg",
                "pipe_model_status": True,
                "pipe_model_created_at": "2023-07-18",
                "pipe_model_updated_at": "2023-07-21"
            }
        }
    }
}


while True:
    
    data["dailyProduction"]["daily_production_produced"] += 5
    data["dailyProduction"]["productionGoal"]["production_goal_produced"] += 5

    
    update_and_save_to_redis(data)

    print("Valores atualizados e salvos no Redis.")

    time.sleep(5)
from fastapi import FastAPI
from app.utils import json_to_dict_list
import os
from typing import Optional

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))
# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)
# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'students.json')
#path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'students.json') # сокращенная запись


app = FastAPI()

@app.get("/students")
def get_all_students():
    return json_to_dict_list(path_to_json)
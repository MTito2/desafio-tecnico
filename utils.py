import json
from config import FILES_PATH
from datetime import datetime

def read_json(name_path, name_file: str):
    name_json_file = name_path / name_file

    with open(name_json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
        
def export_json(content, name_path, name_file="content.json") -> None:
    name_json_file = name_path / name_file

    with open(name_json_file, "w", encoding="utf-8") as file:
        json.dump(content, file, indent=4, ensure_ascii=False)

def save_log(log_message, log_type):
    logs_path = FILES_PATH / "logs.txt"
    current_date = datetime.now()
    current_date = current_date.strftime("[%d-%m-%Y %H:%M:%S]")

    if log_type == "info":
        log_message = f"{current_date} [INFO] {log_message}\n"
    
    elif log_type == "error":
        log_message = f"{current_date} [ERROR] {log_message}\n"
        

    with open(logs_path, "a", encoding="utf-8") as file:
        file.write(log_message)

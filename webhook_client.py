from config import FILES_PATH
from utils import save_log, export_json
from datetime import datetime
import requests

def send_webhook():

    try:
        file_name = "Teste RPA - Mateus da Cunha Tito.xlsx"
        file_path = FILES_PATH / file_name

        url = "https://n8n.dev.onfly.com.br/webhook/b5264095-007e-4c33-a27f-edee2bb6570b"

        files = {
            "file": open(file_path, "rb")
        }

        response = requests.post(
            url,
            files=files,
            auth=("teste.rpa", "Teste@Onfly123")
        )

        evidence = [
            {
                "file": file_name,
                "webhook": url,
                "submission_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "status": response.status_code
            }
        ]

        save_log("Webhook enviado com sucesso", "info")
        export_json(evidence, FILES_PATH, "webhook_evidence.json")
    
    except Exception as error:
        save_log(error, "error")

    

    

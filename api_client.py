import requests
from utils import save_log

def request_country_info(country):

        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")

        if response.status_code == 200:
            save_log("API Request Country acessada com sucesso", "info")
            response = response.json()

            return {
                "capital": response[0]["capital"],
                "languages": response[0]["languages"],
                "currencies": response[0]["currencies"],
            }

  
        save_log(f"API Request Country [Error {response.status_code}]", "error")
        print("Erro encontrado, verifique o arquivo 'logs.txt' para mais detalhes")
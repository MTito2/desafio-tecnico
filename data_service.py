from api_client import request_country_info
from scraping import init_scraping
from utils import save_log

def compile_country_data():

    try:
        scraping_content = init_scraping()
        content = []

        for item in scraping_content:
            country_info = request_country_info(item["country"])

            population = item["population"].replace(",", "")

            languages = country_info["languages"]
            languages_concatenated = ""

            for languages_abbreviation, language in languages.items():
                languages_concatenated += f"{language}, "

            currencies = country_info["currencies"]
            currencies_concatenated = ""

            for currency_abbreviation, currency_info in currencies.items():
                for infos, value in currency_info.items():
                    if infos == "name":
                        currencies_concatenated += f"{value}, "

            content.append(
                {
                    "country": item["country"],
                    "population": population,
                    "median_age": item["median_age"],
                    "capital": country_info["capital"][0],
                    "languages": languages_concatenated[:-2],
                    "currencies": currencies_concatenated[:-2],
                }
            )
        
        save_log("Compilação realizada com sucesso", "info")
        return content
    
    except Exception as error:
        save_log(error, "error")
        print("Erro encontrado, verifique o arquivo 'logs.txt' para mais detalhes")


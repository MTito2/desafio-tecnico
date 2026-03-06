import os
from utils import save_log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def init_scraping():
    try:
        options = Options()
        options.add_argument("--headless=new") 

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.worldometers.info/world-population/population-by-country/")

        table_content = driver.find_element(by=By.XPATH, value="//div//tbody")
        rows = table_content.find_elements(by=By.TAG_NAME, value="tr")
        
        rows_number = len(rows)
        row_counter = 0

        content = []
        for row in rows:
            row_counter += 1
            progress = round(row_counter / rows_number * 100)

            os.system("cls")
            print(f"Progresso do Scraping [{progress}%]")

            cells = row.find_elements(by=By.TAG_NAME, value="td")

            median_age = cells[9].text

            if median_age != "–":
                country = cells[1].text.replace("&", "and")

                items = {
                "id": cells[0].text,
                "country": country,
                "population": cells[2].text,
                "yearly_change": cells[3].text,
                "net_change": cells[4].text,
                "density": cells[5].text,
                "land_area": cells[6].text,
                "migrants": cells[7].text,
                "fert_late": cells[8].text,
                "median_age": median_age,
                "urban_pop": cells[10].text,
                "world_share":  cells[11].text, 
                }

                content.append(items)

        driver.quit()

        save_log("Scraping realizado com sucesso", "info")
        return sorted(content, key=lambda item: item["median_age"], reverse=True)[:10]
    
    except Exception as error:
        save_log(error, "error")
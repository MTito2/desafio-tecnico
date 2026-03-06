from data_service import compile_country_data
from report_generator import generate_xlsx
from webhook_client import send_webhook

content = compile_country_data()
generate_xlsx(content)
send_webhook()



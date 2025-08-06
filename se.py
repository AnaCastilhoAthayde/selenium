from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
#Opções para abrir o navegador visível (pode remover headless=True se quiser ver o navegador)
options = Options()

#Opções para abrir o navegador visível (pode remover headless=True se quiser ver o navegador)

navegador = webdriver.Chrome(options=options)

# Acessa o site desejado
navegador.get("https://quotes.toscrape.com/")

frases = navegador.find_elements(By.CLASS_NAME, "text")
autores = navegador.find_elements(By.CLASS_NAME, "author")

for i in range(len(frases)):
    print(frases[i].text)
    print(f"- {autores[i].text}")
    print()

time.sleep(15)

navegador.quit()

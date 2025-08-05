from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Opções para abrir o navegador visível (pode remover headless=True se quiser ver o navegador)
options = Options()
options.headless = False  # Coloque True para rodar "escondido"

# Abre o navegador automaticamente com driver interno
navegador = webdriver.Chrome(options=options)

# Acessa o site desejado
navegador.get("https://www.google.com")

import time
time.sleep(20)
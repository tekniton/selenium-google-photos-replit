import os
os.system("pip install selenium")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)
driver.get("https://photos.app.goo.gl/pd59edTYcT3NJpxT9")

# Scroll hasta el fondo
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Obtener URLs de imágenes
images = driver.find_elements("tag name", "img")
urls = [img.get_attribute("src") for img in images if img.get_attribute("src")]

# Guardar en un archivo
with open("urls.txt", "w") as f:
    for url in urls:
        f.write(url + "\n")

print(f"{len(urls)} imágenes guardadas en urls.txt")
driver.quit()

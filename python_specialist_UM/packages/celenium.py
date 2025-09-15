# we can now trying the celenium in mac
#this one is working_but anothers have proböem _ i mean with the selenium
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_linkedin(email, password):
    # Pfad zum Chrome-Browser
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    # Chrome-Service erstellen
    service = Service(chrome_path)
    # Chrome-Optionen festlegen
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # Chrome-Webdriver initialisieren
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.linkedin.com/login")

    # Login-Daten eingeben und einloggen
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn__primary--large"))).click()
        print("Erfolgreich bei LinkedIn eingeloggt.")
    except Exception as e:
        print("Fehler beim Einloggen bei LinkedIn:", e)
        driver.quit()

    return driver

def open_linkedin_and_search_jobs(csv_file, email, password):
    # Einloggen bei LinkedIn
    driver = login_to_linkedin(email, password)

    # Weiter mit dem Job-Suchprozess
    if driver:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                linkedin_url = row['Linkedin Adresse']
                if linkedin_url:
                    if not linkedin_url.startswith('http://') and not linkedin_url.startswith('https://'):
                        linkedin_url = 'https://' + linkedin_url

                    # LinkedIn-Seite öffnen
                    driver.get(linkedin_url)

                    # Auf "Aktuelle Jobangebote" klicken
                    try:
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Aktuelle Jobangebote'))).click()
                    except Exception as e:
                        print("Fehler beim Klicken auf 'Aktuelle Jobangebote':", e)
                        continue

                    # Nach Jobangeboten mit dem Titel "GIS" suchen
                    job_titles = driver.find_elements(By.XPATH, "//span[contains(text(), 'GIS')]")

                    # Wenn Jobangebote gefunden wurden, die in die CSV-Datei geschrieben werden sollen
                    if job_titles:
                        for title in job_titles:
                            job_title = title.text
                            print("GIS Job gefunden:", job_title)
                            # Jobtitel in CSV-Datei schreiben
                            try:
                                with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow([job_title])
                            except Exception as e:
                                print("Fehler beim Schreiben in die CSV-Datei:", e)

        # Chrome-Webdriver schließen
        driver.quit()

# Email und Passwort für LinkedIn einstellen
linkedin_email = "amhb1985@gmail.com"
linkedin_password = "your_password"

# CSV-Datei und LinkedIn-E-Mail und -Passwort angeben
open_linkedin_and_search_jobs('CoList.csv', linkedin_email, linkedin_password)

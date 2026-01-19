# this is the first test without the selenium
import csv
import webbrowser

def open_linkedin(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            linkedin_url = row['Linkedin Adresse']
            if linkedin_url:
                if not linkedin_url.startswith('http://') and not linkedin_url.startswith('https://'):
                    linkedin_url = 'https://' + linkedin_url
                webbrowser.get('chrome').open(linkedin_url)

open_linkedin('CoList.csv')


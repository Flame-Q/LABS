import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import sys
import re
import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="soupsieve")

input_file = 'countries.txt'
output_file = 'countries_data.csv'
cache_dir = 'cache'

if len(sys.argv) > 1:
    input_file = sys.argv[1]
if len(sys.argv) > 2:
    output_file = sys.argv[2]

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

def get_page(country):
    """Получаем страницу из кэша или загружаем"""
    cache_file = os.path.join(cache_dir, f"{country.replace(' ', '_')}.html")
    
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        with open(cache_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        return response.text
    except Exception as e:
        print(f"Ошибка при загрузке страницы {country}: {e}")
        return None

def parse_country_data(html, country):
    """Парсим данные о стране"""
    if not html:
        return "Not found", "Not found", "Not found"
    
    soup = BeautifulSoup(html, 'html.parser')
    
    capital = "Not found"
    area = "Not found"
    population = "Not found"
    
    try:
        capital_selectors = [
            'th:-soup-contains("Capital")',
            'th:-soup-contains("Capital and largest city")',
            'th:-soup-contains("Admin center")'
        ]
        
        for selector in capital_selectors:
            capital_row = soup.select_one(selector)
            if capital_row:
                capital_link = capital_row.find_next('td').find('a')
                if capital_link:
                    capital = capital_link.get_text(strip=True)
                else:
                    capital = capital_row.find_next('td').get_text(strip=True).split('[')[0].split('\n')[0]
                break
        
        area_selectors = [
            'th.infobox-label:-soup-contains("Area")',
            'th:-soup-contains("• Total")',
            'th:-soup-contains("Total")'
        ]
        
        for selector in area_selectors:
            area_row = soup.select_one(selector)
            if area_row:
                area_td = area_row.find_next('td')
                if area_td:
                    area_text = area_td.get_text(strip=True)
                    
                    area_matches = re.findall(r'\d{1,3}(?:,\d{3})+', area_text)
                    if area_matches:
                        area = area_matches[0].replace(',', '')
                    else:
                        large_numbers = re.findall(r'\d{6,}', area_text.replace(',', ''))
                        if large_numbers:
                            area = large_numbers[0]
                break
        
        population_selectors = [
            'th.infobox-label:-soup-contains("Population")',
            'th:-soup-contains("Population")'
        ]
        
        for selector in population_selectors:
            population_row = soup.select_one(selector)
            if population_row:
                population_td = population_row.find_next('td')
                if population_td:
                    population_text = population_td.get_text(strip=True)
                    
                    population_matches = re.findall(r'\d{1,3}(?:,\d{3})+', population_text)
                    if population_matches:
                        population = max(population_matches, key=lambda x: len(x)).replace(',', '')
                    else:
                        large_numbers = re.findall(r'\d{6,}', population_text.replace(',', ''))
                        if large_numbers:
                            population = max(large_numbers, key=lambda x: len(x))
                break
                
    except Exception as e:
        print(f"Ошибка при парсинге {country}: {e}")
    
    return capital, area, population

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        countries = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"Файл {input_file} не найден")
    sys.exit(1)

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['country', 'city', 'area', 'population'])
    
    for country in countries:
        print(f"Обрабатываем: {country}")
        
        try:
            html = get_page(country)
            
            capital, area, population = parse_country_data(html, country)
            
            writer.writerow([country, capital, area, population])
            
            print(f"  Столица: {capital}, Площадь: {area}, Население: {population}")
            
        except Exception as e:
            print(f"Ошибка при обработке {country}: {e}")
            writer.writerow([country, "Error", "Error", "Error"])
        
        time.sleep(1)

print(f"Готово! Результат сохранен в {output_file}")
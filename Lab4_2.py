import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

# Настройки
base_url = "https://worldathletics.org"
disciplines = {
    '60m': '60/metres/men',
    '100m': '100/metres/men', 
    '200m': '200/metres/men',
    '400m': '400/metres/men',
    '60m-women': '60/metres/women',
    '100m-women': '100/metres/women',
    '200m-women': '200/metres/women',
    '400m-women': '400/metres/women'
}

years = range(2001, 2025)
results = []

# Функция для получения данных
def get_data(year, discipline):
    url = f"{base_url}/records/toplists/{discipline}/outdoor/{year}/senior"
    print(f"Обрабатываем: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем таблицу с результатами
        table = soup.find('table', class_='records-table')
        if not table:
            print(f"Таблица не найдена для {year} {discipline}")
            return None
            
        # Берем первую строку (топ-1 результат)
        row = table.find('tbody').find('tr')
        if not row:
            print(f"Нет данных для {year} {discipline}")
            return None
            
        # Извлекаем данные
        cells = row.find_all('td')
        
        name = cells[1].find('a').text.strip()
        country = cells[2].find('span').text.strip()
        time = cells[3].text.strip()
        date = cells[4].text.strip()
        
        return {
            'year': year,
            'discipline': discipline.split('-')[0],
            'gender': 'women' if 'women' in discipline else 'men',
            'name': name,
            'country': country,
            'time': time,
            'date': date
        }
        
    except Exception as e:
        print(f"Ошибка при обработке {year} {discipline}: {e}")
        return None

# Собираем данные
for discipline in disciplines:
    for year in years:
        data = get_data(year, disciplines[discipline])
        if data:
            results.append(data)
        sleep(1)  # Чтобы не нагружать сервер

# Сохраняем в CSV
with open('top_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['year', 'discipline', 'gender', 'name', 'country', 'time', 'date'])
    writer.writeheader()
    writer.writerows(results)

print("Готово! Данные сохранены в top_results.csv")
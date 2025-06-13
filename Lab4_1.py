# Импортируем нужные библиотеки
import requests
import json
import os

# Получаем данные о странах Азии
print("Начинаем загрузку данных...")
countries_data = requests.get("https://restcountries.com/v3.1/region/asia").json()

# Список для хранения подходящих стран
good_countries = []

# Перебираем все страны
for country in countries_data:
    # Проверяем население
    people = country.get('population', 0)
    if people > 30000000:  # 30 миллионов
        
        # Получаем столицу (иногда её нет)
        cap = 'Нет данных'
        if 'capital' in country and len(country['capital']) > 0:
            cap = country['capital'][0]
        
        # Получаем площадь
        square = country.get('area', 0)
        
        # Считаем плотность
        if square > 0:
            density = people / square
        else:
            density = 0
        
        # Добавляем данные в список
        good_countries.append({
            'name': country['name']['common'],
            'capital': cap,
            'area': square,
            'population': people,
            'density': density,
            'flag': country['flags']['png']
        })

# Сохраняем в файл
print("Сохраняем данные в файл...")
with open('asia_countries.json', 'w') as f:
    json.dump(good_countries, f, indent=4)

# Сортируем по плотности
print("Сортируем страны...")
good_countries.sort(key=lambda x: x['density'], reverse=True)

# Выводим топ-5
print("\nТоп 5 самых плотно населенных стран:")
for i in range(5):
    c = good_countries[i]
    print(f"{i+1}. {c['name']} ({c['density']:.1f} чел/км²)")

# Скачиваем флаги
print("\nСкачиваем флаги...")
if not os.path.exists('flags'):
    os.mkdir('flags')

for i in range(5):
    country = good_countries[i]
    name = country['name']
    url = country['flag']
    
    # Чистим имя для файла
    filename = name.replace(' ', '_').replace(',', '') + '.png'
    
    # Качаем картинку
    img = requests.get(url).content
    
    # Сохраняем
    with open(f'flags/{filename}', 'wb') as f:
        f.write(img)
        print(f"Сохранен флаг {name}")

print("\nГотово!")
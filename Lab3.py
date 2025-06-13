import pickle
import random
import string

# 1. Создание словаря пользователей и их паролей для 6 сайтов
users = {
    "Иванов": {
        "Facebook": "Password123",
        "Google": "qwerty",
        "Twitter": "123456",
        "Instagram": "InstaPass",
        "LinkedIn": "LinkPass",
        "VK": "VKontakte"
    },
    "Петров": {
        "Facebook": "petrovPass",
        "Google": "googlePass",
        "Twitter": "twPass",
        "Instagram": "instaPetrov",
        "LinkedIn": "linkedPetrov",
        "VK": "vkPetrov"
    },
    "Сидоров": {
        "Facebook": "SidorovPass",
        "Google": "googleSidorov",
        "Twitter": "twSidorov",
        "Instagram": "instaSidorov",
        "LinkedIn": "linkedSidorov",
        "VK": "vkontakteSidorov"
    },
    "Кузнецов": {
        "Facebook": "KuzPass",
        "Google": "googleKuz",
        "Twitter": "twKuz",
        "Instagram": "instaKuz",
        "LinkedIn": "linkedKuz",
        "VK": "vkKuz"
    },
    "Смирнов": {
        "Facebook": "SmirnovPass",
        "Google": "googleSmirnov",
        "Twitter": "twSmirnov",
        "Instagram": "instaSmirnov",
        "LinkedIn": "linkedSmirnov",
        "VK": "vkSmirnov"
    },
    "Васильев": {
        "Facebook": "VasilievPass",
        "Google": "googleVasiliev",
        "Twitter": "twVasiliev",
        "Instagram": "instaVasiliev",
        "LinkedIn": "linkedVasiliev",
        "VK": "vkVasiliev"
    },
    "Николаев": {
        "Facebook": "NikolaevPass",
        "Google": "googleNikolaev",
        "Twitter": "twNikolaev",
        "Instagram": "instaNikolaev",
        "LinkedIn": "linkedNikolaev",
        "VK": "vkNikolaev"
    }
}

# 2. Вывод списка всех пользователей и средней длины их паролей
print("Список пользователей и средняя длина их паролей:")
for user, passwords in users.items():
    avg_length = sum(len(password) for password in passwords.values()) / len(passwords)
    print(f"{user}: {avg_length:.2f}")

# 3. Определение сайта с минимальной длиной пароля для каждого пользователя
print("\nСайт с минимальной длиной пароля для каждого пользователя:")
for user, passwords in users.items():
    min_site = min(passwords.keys(), key=lambda site: len(passwords[site]))
    print(f"{user}: {min_site} (длина пароля: {len(passwords[min_site])})")

# 4. Замена повторяющихся паролей на новые
def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

password_counts = {}
for passwords in users.values():
    for password in passwords.values():
        password_counts[password] = password_counts.get(password, 0) + 1

for user, passwords in users.items():
    for site, password in passwords.items():
        if password_counts[password] > 1:
            new_password = generate_password()
            while new_password in password_counts:
                new_password = generate_password()
            passwords[site] = new_password
            password_counts[new_password] = 1

# 5. Выделение пользователей, у которых пароль для Facebook начинается с заглавной буквы
print("\nПользователи, у которых пароль для Facebook начинается с заглавной буквы:")
for user, passwords in users.items():
    if passwords["Facebook"][0].isupper():
        print(f"{user}: {passwords['Facebook']}")

# 6. Сохранение словаря в бинарный файл data.pickle
with open('data.pickle', 'wb') as f:
    pickle.dump(users, f)

# Чтение из бинарного файла
with open('data.pickle', 'rb') as f:
    loaded_users = pickle.load(f)

print("\nДанные успешно сохранены и загружены из файла data.pickle")
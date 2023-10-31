users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
total = len(users)
users_unique = set(users)
total_users_unique = len(users_unique)
visit = {
    "Общее количество": total,
    "Уникальные посещения": total_users_unique
}
print(visit)
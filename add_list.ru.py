username = input("введите имя пользователя: ")
print(" имя пользователя:",username)
title=[]
for i in range(3) :
    title.append(input( f"введите заголовок заметки {i+1}: "))
print("заголовок заметки: ", title)
content = input("введите описание заметки: ")
print("описание заметки:", content)
status = input("введите статус заметки: ")
print("статус заметки:", status)
created_date = input("введите дату создания заметки (пример: 10.11.2024): ")
print("дата создания заметки:",created_date[:5])
issue_date = input("введите дату истечения заметки (пример: 10.11.2024): ")
print("дата истечения заметки", issue_date[:5])

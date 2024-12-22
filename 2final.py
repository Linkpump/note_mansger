note = {}
username = input("введите имя пользователя: ")
#print(" имя пользователя:",username)
title=[]
for i in range(3) :
    title.append(input( f"введите заголовок заметки {i+1}: "))
content = input("введите описание заметки: ")
#print("описание заметки:", content)
status = input("введите статус заметки: ")
#print("статус заметки:", status)
created_date = input("Дата создания заметки (пример: 10.11.2024): ")
#print("дата создания заметки:", created_date[:5])
issue_date = input("дата истечения заметки (пример: 10.11.2024): ")
#print("дата истечения заметки", issue_date[:5])
note["имя пользователя"] = username
note["заголовок заметки"] = title
note["описание заметки"] = content
note["описание заметки"] = status
note["дата создания заметки"] = created_date[:5]
note["дата истечения заметки"] = issue_date[:5]
for key, value in note.items():
 print(f'\n{key}: {value}')
print(note) # можно вывести и первым способом ( выше ) и вторым ( с помощью этой строчки ), но думаю, что способ выше лучше смотрится

user_name = input ("Ведите имя пользователя: ")
title = [input("Ведите первый заголовок : "), input("Ведите второй заголовок : "), input("Ведите третий заголовок : ")]
content = input ("Введите описание заметки : ")
status = input ("Введите статус заметки : ")
create_date = input ("Дата создания заметки в формате день-месяц-год : ")
issue_date = input ("Дата истечения заметки в формате день-месяц-год : ")
note = [user_name, title, content, status, create_date, issue_date]
print(*note, sep="\n")
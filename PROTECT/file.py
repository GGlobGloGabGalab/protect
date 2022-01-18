import os

print("Текущая деректория:", os.getcwd())

os.mkdir("Protect directory")
os.chdir("Protect directory")

print("Текущая директория изменилась на Protect directory:", os.getcwd())

text_file = open("pass.txt", "w")
text_file.write ("hello")

opp = input('Пароль:')
if 'pass.txt' == opp:
    print('есть контакт!')
else:
    print('нет контакта(((')
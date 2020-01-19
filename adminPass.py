from os import path, getcwd

def checkData(word, flag = False):
    #flag нужен для того, что конвертировать автоматом
    #в int (если false) или в string (если true)
    word = word.lstrip(' ')
    word = word.rstrip('\n')
    if flag:
        return int(word)
    else:
        return word


#Работа с файлом
firstStart = True
startProgram = True
#Admin Data
#Получаем данные с файла txt
#Если его нет, то создаём и записываем туда всё
if not path.exists(getcwd() + 'passAdmin.txt'):
    fileAdmin = open('passAdmin.txt', 'w')
    fileAdmin.write('adminName = MyAdmin29\n')
    fileAdmin.write('adminPassword = test22\n')
    fileAdmin.write('adminSecretKey = 37\n')
    fileAdmin.close()

fileAdmin = open('passAdmin.txt', 'r')
allData = fileAdmin.readlines()
adminName = checkData(allData[0].split('=')[1])
adminPassword = checkData(allData[1].split('=')[1])
adminSecretKey = checkData(allData[2].split('=')[1], True)
fileAdmin.close()


def RecoverPersonalDates(name, password, secretKey):
    stateProgram = True
    global adminName
    global adminPassword
    global adminSecretKey
    print("\nВосстановить данные? \nЕсли вы ввели 2 поля правильно, то вы будете допущены к изменению данных")
    writeData = input("Введите \"Да\": ")
    if writeData == "Да" or  writeData == "да": 
        if (name == adminName and password == adminPassword) or (name == adminName and secretKey == adminSecretKey) or (password == adminPassword and secretKey == adminSecretKey): 
            print("Вы допущены к изменению данных администратора!")
            adminName = input("Введите новый логин: ")
            adminPassword = input("Введите новый пароль: ")
            adminSecretKey = int(input("Введите новый секретный ключ: "))
        else:
            print("Отклонено в восстановлении. \nПричина: должно быть как минимум 2 поля правильно заполенено!")
            stateProgram = False
    else:
        print("Отклонено в восстановлении.")
        stateProgram = False
    return stateProgram 


#Run Programm
print("Программа запущена.")
while startProgram:
    print() #Не спрашивай, чтобы красиво было, сцук
    name = input("Введите логин: ")
    password = input("Введите пароль: ")
    secretKey = int(input("Введите кодовую цифру: "))
    print() #По той же причине
    if name == adminName and password == adminPassword and secretKey == adminSecretKey:
        if firstStart:
            print("Рад приветствовать вас впервые, администратор!")
        else:
            print("Администратор, рад вас снова видеть!")
    else:
        print("Проблема... Неверные данные.")
        if RecoverPersonalDates(name, password, secretKey): 
            print("Данные изменены! Попробуйте их снова!")
            fileAdmin = open('passAdmin.txt', 'w')
            fileAdmin.write('adminName = ' + adminName + "\n")
            fileAdmin.write('adminPassword = ' + adminPassword + "\n")
            fileAdmin.write('adminSecretKey = ' + str(adminSecretKey) + "\n")
            fileAdmin.close()
        #else: 
            #startProgram = False
    firstStart = False
print("Программа завершена.")

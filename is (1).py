import sqlite3
def Connect():
    return sqlite3.connect('futbick.db')


class User():
    bilet = ""
    def userpanel():
        ticket = input("на какое число вы хотите приобрести билет?\n1. 21.04.1998\n2. 22.04.1998\n3. 21.05.1945\n")
        match ticket:
            case "1":
                print("вы приобрели билет на матч Барселона-ЦСКА")
                User.bilet = "1"
            case "2":
                print("вы приобрели билет на матч Бавария-Мюнхен")
                User.bilet = "2"
            case "3":
                print("вы приобрели билет на матч Сборная Зимбабве-Роналдо")
                User.bilet = "3"
class Registation():
    username = ""
    password = ""
    def registration():
        while True:
            print("как вы хотите войти?\n1. Как покупатель\n2. Как админ")
            a = input()
            match a:
                case "1":
                    Registation.username = input("введите имя: ")
                    Registation.password = input("введите пароль:")
                    User.userpanel()
                    Database.CreateTable()
                    Database.CreateClient(Registation.username, User.bilet)
                case "2":
                    Admin.CheckAdminPassword()


class Admin():
    def CheckAdminPassword():
        password = "Сарварбек"
        a = input("введите пароль: ")
        if a == password:
            Admin.ControlPanel()
        else:
            print("неверный пароль!")
            Admin.CheckAdminPassword()

    def ControlPanel():
        while True:
            chose = input("МЕНЮ:\n1. Показать всех покупателей\n2. Удалить покупателя\n3. Выйти\n")
            match chose:
                case "1":
                    Database.ShowAllClients()
                case "2":
                    name = input("введите имя клиента ")
                    Database.KickClientByName(name)
                    print("клиент удален")
                case "3":
                    break
        return 0

class Database():
    def CreateTable():
        conn = Connect()
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS Clients(
            Id INTEGER PRIMARY KEY,
            ClientName TEXT NOT NULL,
            Bilet TEXT NOT NULL
            );
        ''')
        conn.commit()
        conn.close()

    def CreateClient(name, ticket):
        conn = Connect()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO Clients (ClientName, Bilet) VALUES(?,?)', (name, ticket))
        conn.commit()
        conn.close()

    def ShowAllClients():
        conn = Connect()
        cur = conn.cursor()

        cur.execute('SELECT * FROM Clients')
        clients = cur.fetchall()

        for client in clients:
            print(client)

            conn.close()

    def KickClientByName(name):
        conn = Connect()
        cur = conn.cursor()

        cur.execute('DELETE FROM Clients WHERE ClientName = ?', (name))
        conn.commit()
        conn.close()

Registation.registration()
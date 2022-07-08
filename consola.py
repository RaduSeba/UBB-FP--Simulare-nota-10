from repository.evenimentrep import EvenimentRepoFile
import datetime
from service.evenimentservice import EvenimentService

class Consola:
    def __init__(self,service):
        self.__srv=service

    def __print_menu(self): 
        print("Optiunile sunt:add,exit")  

    def __show_zi(self,lista):
        print("Evenimentele din ziua curenta sunt:")
        if(len(lista)==0):
            print("Nu Exista evenimente astazi"  )
        else:
            for eveniment in lista:
                print("Data :",eveniment.getdata(),"Ora:",eveniment.getora(),"Descirere:",eveniment.getdescriere())          

    def __add_eveniment(self):
        try:
            date_tranzactie = input('Adugati data evenimetului (YYYY-MM-DD format) :')
            year, month, day = map(int, date_tranzactie.split('-'))
            data = datetime.date(year, month, day)
            timp_eveniment=input("Adaugati timpul desfasurarii evenimetului:")
            hour,minutes=map(int,timp_eveniment.split(":"))
            timp=datetime.time(hour,minutes)
            descriere=input("Descriere:")
            added_eveniment=self.__srv.adauga(data,timp,descriere)
            print("Evenimentul:",added_eveniment,"a fost adaugat cu succes")
        except ValueError:
            print("Data/Ora trebuie sa fie in formatul indicat")

    def __get(self):
        l=self.__srv.all(datetime.date.today())
        return l

    def __sortare(self):
        text=input("textul:")
        fisier=input("numele fisierului:")
        self.__srv.fisier(text,fisier)    

    def __data(self):
        date_tranzactie = input('Adugati data evenimetului (YYYY-MM-DD format) :')
        year, month, day = map(int, date_tranzactie.split('-'))
        data = datetime.date(year, month, day)
        l=self.__srv.all(data)
        self.__show_zi(l)

    def show_ui(self):
        self.__show_zi(self.__get())
        while True:
            self.__print_menu()
            cmd=input("Comanda este:")
            cmd=cmd.lower().strip()
            if cmd=="add":
                self.__add_eveniment()
            elif cmd=="exit":
                return
            elif cmd=="eveniment_data":
                self.__data()    
            elif cmd=="sortare":
                self.__sortare()    
            else:
                print("Comanda invalida ") 
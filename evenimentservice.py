from entities import eveniment
from entities.eveniment import Eveniment
from repository.evenimentrep import EvenimentRepoFile 

class EvenimentService:
    def __init__(self,repo):
        self.__repo=repo

    def adauga(self,data,ora,descriere):
        eveniment=Eveniment(data,ora,descriere)
        self.__repo.store(eveniment)

    def all(self,data):
        return self.__repo.get_all(data)        

    def fisier(self,text,fisier):
        self.__repo.sortare(text,fisier)    
class Eveniment:
    def __init__(self,data,ora,descriere):
        self.__data=data
        self.__ora=ora
        self.__descriere=descriere

    def getora(self):
        return self.__ora

    def getdata(self):
        return self.__data

    def getdescriere(self):
        return self.__descriere

    def __str__(self):
        return "Data :"+str(self.__data)+"Ora:"+str(self.__ora)+"Descriere: "+str(self.__descriere) 

    def __eq__(self, object) :
        if self.__data==object.getdata():
            return True
        return False    

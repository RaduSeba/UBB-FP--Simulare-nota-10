import datetime
from entities.eveniment import Eveniment 

class EvenimentRepoFile:
    def __init__(self,filename):
        self.__fielname=filename

    def __load_from_file(self):
        with open(self.__fielname,"r") as f:
            evenimente=[]
            lines=f.readlines()
            for line in lines:
                eveniment_data,eveniment_ora,eveniment_descriere=[token.strip() for token in line.split(" ")] 
                year, month, day = map(int, eveniment_data.split('-'))
                data = datetime.date(year, month, day)
                hour,minutes,seconds=map(int,eveniment_ora.split(":"))
                timp=datetime.time(hour,minutes,seconds)
                eve=Eveniment(data,timp,eveniment_descriere)  
                evenimente.append(eve)
        f.close()
        return evenimente

    def __save_to_file(self,evenimente):
        with open(self.__fielname,"w") as f:
            for eveniment in evenimente:
                eveniment_string=str(eveniment.getdata())+" "+str(eveniment.getora())+" "+str(eveniment.getdescriere())+"\n" 
                f.write(eveniment_string)    

    def store(self,eveniment):
        eveniment_list=self.__load_from_file()
        eveniment_list.append(eveniment)
        self.__save_to_file(eveniment_list)

    def get_all(self,data1):
       l=self.__load_from_file()    
       filtered_list = [eveniment for eveniment in l if eveniment.getdata()==data1 ]
       """
       for eveniment in l:
            year, month, day = map(int, eveniment.getdata().split('-'))
            data2 = datetime.date(year, month, day)
            if data2==data1:
                filtered_list.append(eveniment)
       """         
       return filtered_list 

    def __save_to_file_nou(self,evenimente,fisier):
        with open("data/"+fisier+".txt","w") as f:
            for eveniment in evenimente:
                eveniment_string=str(eveniment.getdata())+" "+str(eveniment.getora())+" "+str(eveniment.getdescriere())+"\n" 
                f.write(eveniment_string) 

    def sortare(self,sir,fisier):
        l=self.__load_from_file()    
        filtered_list = [eveniment for eveniment in l if sir in eveniment.getdescriere()]
        filtered_list.sort(key=lambda x: x.getdata(),reverse=False)
        self.__save_to_file_nou(filtered_list,fisier)



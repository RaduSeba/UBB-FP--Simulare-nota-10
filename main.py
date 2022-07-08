from repository.evenimentrep import EvenimentRepoFile
from service.evenimentservice import EvenimentService
from ui.consola import Consola

repo=EvenimentRepoFile("data/evenimente.txt")
service=EvenimentService(repo)

ui=Consola(service)
ui.show_ui()
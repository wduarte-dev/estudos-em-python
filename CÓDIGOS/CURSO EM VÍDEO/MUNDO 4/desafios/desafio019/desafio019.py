from time import sleep
class Livro:
    def __init__(self, title:str, pages:int):
        self.title = title
        self.pages = pages
        self.actual_page = 1
        print(f'Você abriu o livro "{self.title}"! Este livro possui {self.pages} páginas e você está na página {self.actual_page}.')
    def first_page(self):
        if self.actual_page == 1:
            print('Você já está na 1° página!')
            return True
        return False
    def last_page(self):
        if self.actual_page == self.pages:
            print(f'Parabéns! O livro "{self.title}" chegou ao fim.')
            return True
        return False

    def forward(self, x):
        if self.last_page():
            return
        aux_var = 0
        for next_page in range(x):
            if self.actual_page >= self.pages:
                break
            self.actual_page += 1
            aux_var += 1
            sleep(0.5)
            print(f'Pág {self.actual_page} >', end=' ', flush=True)
        sleep(0.5)
        print(f'Você avançou {aux_var} páginas e agora está na página {self.actual_page}.')
    
    def backward(self, x):
        if self.first_page():
            return None
        aux_var = 0
        for back_page in range(x):
            if self.actual_page == 1:
                break
            self.actual_page -= 1
            aux_var += 1
            sleep(0.5)
            print(f'Pág {self.actual_page} >', end=' ', flush=True)
        sleep(0.5)
        print(f'Você recuou {aux_var} páginas e agora está na página {self.actual_page}.')


l1 = Livro('Guia básico de Python vol.1', 10)
l1.forward(2)
l1.forward(4)
l1.forward(3)
l1.forward(1)
l1.forward(10) # o código impede o avanço de mais páginas do que o total
l1.backward(5)
l1.backward(4)
l1.backward(1) # o código impede recuar páginas negativas
l1.backward(10)
l1.forward(10)
        
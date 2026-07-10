from rich.panel import Panel
from rich import print
class Churrasco:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount
    def info(self):
        total_kg = 400 * self.amount / 1000
        total_price = total_kg * 82.4
        per_person = total_price / self.amount
        msg1 = 'Cada participante comerá 400g e o preço da carne é R$82.40/kg;\n'
        total_kg_info = f'É necessário comprar {total_kg}kg de carne;\n'
        total_price_info = f'O custo total será de R${total_price:,.2f};\n'
        per_person_info = f'Cada pessoa pagará R${per_person:,.2f}.'
        painel = Panel.fit(title=f'{self.title} com {self.amount} pessoas',
        renderable=msg1 + total_kg_info + total_price_info + per_person_info)
        print(painel)

c1 = Churrasco('Churras', 100)
c1.info()


from dataclasses import dataclass, field
@dataclass
class Gamer:
    name: str
    nickname: str
    fav_games: list[str] = field(default_factory=list, repr=False) #cria uma lista individual e vazia para cada objeto

    def add_fav_game(self, game_name : str) -> None:
        self.fav_games.append(game_name)
    def info(self) -> None:
        print(f'DADOS DO JOGADOR:\nNome: {self.name}\nNick: @{self.nickname}\n\nJOGOS FAVORITOS:')
        for game in sorted(self.fav_games):
            print(game)

if __name__ == '__main__':
    g1 = Gamer('Wellington', 'daylouz')
    g1.add_fav_game('The Witcher 3')
    g1.add_fav_game('Hollow Knight')
    g1.add_fav_game('Celeste')
    g1.info()

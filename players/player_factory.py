from players.types.iplayer import IPlayer


class PlayerFactory:
    def __init__(self, players: list[IPlayer]) -> None:
        self.players = self.__map_to_players(players)
        pass

    def render(self) -> None:
        for player in self.players.values():
            player.render()

    def get_player(self, id: str) -> IPlayer:
        return self.players[id]

    def __map_to_players(self, players: list[IPlayer]) -> dict[str, IPlayer]:
        new_players = dict()
        for player in players:
            print(player.id)
            new_players[player.id] = player

        return new_players


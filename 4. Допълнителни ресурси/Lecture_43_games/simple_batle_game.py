import random


class Player:
    def __init__(self, army, name="Player", hit_points=50):
        self.hit_points = hit_points
        self.name = name
        self.army = army

    def hits(self):
        return random.randint(1, 10)


def fight(player1, player2):
    rounds = 0
    while True:
        if player1.hit_points <= 0:
            return player2
        if player2.hit_points <= 0:
            return player1

        if rounds % 2 == 0:
            player2.hit_points -= player1.hits()
        else:
            player1.hit_points -= player2.hits()
        rounds += 1


army1 = [Player("Army1") for _ in range(5)]
army2 = [Player("Army2") for _ in range(5)]

army1_fight_wins = 0
army2_fight_wins = 0
for i in range(len(army1)):
    if fight(army1[1], army2[2]).army == "Army1":
        army1_fight_wins += 1
    else:
        army2_fight_wins += 1

if army1_fight_wins > army2_fight_wins:
    print("Army 1 wins")
else:
    print("Army 2 wins")





from random import uniform
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
    @staticmethod
    def hit():
        if (x := uniform(0,1)) < 0.8:
            return True
        else:
            return False
        
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def start_game(self):
        while ((self.p1.points != 11) and (self.p2.points != 11)):
            if self.p1.hit():
                self.p1.points += 1
            else:
                self.p2.points += 1

            if self.p2.hit():
                self.p2.points += 1
            else:
                self.p1.points += 1

        if self.p1.points > self.p2.points:
            return self.p1.name
        else:
            return self.p2.name

p1, p2 = Player('Ping'), Player('Pong')
game = Game(p1, p2)
print(game.start_game())

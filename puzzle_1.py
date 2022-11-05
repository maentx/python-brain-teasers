#!/usr/bin/python

class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1

p1 = Player('Parzival')
print(Player.count)
print(p1.count)

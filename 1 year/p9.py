from random import randint
class Warrior:
	def __init__(self, name):
		self.name = name
		self.hp = 100
	def died(self):
		if self.hp <= 0:
			return True

	def fight(obj):
		obj.hp -= randint(1,100)
		print(obj.name, obj.hp)

a = Warrior('Рикардо')
b = Warrior('Кикики')
while (a.hp > 0) and (b.hp > 0):
	Warrior.fight(a)
	Warrior.fight(b)

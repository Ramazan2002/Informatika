from random import randint, choice

class Raspberry:
	states = ['Отсутствует', 'Цветение', 'Зелёная', 'Красная']

	def __init__(self, index):
		self.i = 0
		self._index = index
		self._state = Raspberry.states[0]

	def grow(self):
		self.i += 1
		self._state = Raspberry.states[self.i]

	def is_ripe(self):
		if self._state == Raspberry.states[3]:
			return True
		else:
			return False

class RuspberryBush:
	def __init__(self, quantity):
		self.raspberries = [Raspberry(i) for i in range(quantity)]

	def grow_all(self):
		for berry in self.raspberries:
			berry.grow()

	def all_are_ripe(self):
		for berry in self.raspberries:
			if not berry.is_ripe():
				return False
			else:
				return True

	def give_away_all(self):
		self.raspberries = []

class Human:
	def __init__(self, name):
		self.name = name
		self._plant = RuspberryBush(randint(0, 50))

	def work(self):
		self._plant.grow_all()

	def harvest(self):
		if self._plant.all_are_ripe():
			self._plant.give_away_all()
			print('Собрано')
		else:
			print('Ещё рано!')

	@staticmethod
	def knowledge_base():
		print('Сажать малину надо весной')


# Human.knowledge_base()
# a = Human('Gregor')
# a.work()
# a.harvest()
# a.work()
# a.work()
# a.harvest()

class Warrior:
	
	def __init__(self, damage, name = 'No name', max_hp = 100, hp = 100, race = 'Не указано',
				gender = 'Не указано', chance = 0, buff_scale = 1, class_name = None):
		self.name = name
		self.damage = damage
		self.max_hp = max_hp
		self.hp = max_hp
		self.race = race
		self.gender = gender
		self.buff_scale = buff_scale
		self.chance = chance
		self.class_name = class_name

	def is_attacked(self,obj):
		if self.chance > randint(0,100):
			pass
		else:
			self.hp -= obj.damage
			if self.hp < 0:
				self.hp = 0

	def attack(self, obj):
		a = obj.hp
		obj.is_attacked(obj)
		b = obj.hp
		if a != b:
			print(f'{self.race} {self.class_name} {self.name} произвёл атаку на {obj.race}'
				  f' {obj.class_name} {obj.name} силой {self.damage}')
		else:
			print(f'{self.race} {self.class_name} {self.name} промахнулся по {obj.race} '
				  f'{obj.class_name} {obj.name}')

	def bio(self):
		print(self.race, self.gender, self.name, self.hp)


class Human(Warrior):
	def __init__(self, chance, damage, max_hp, class_name, name = 'No name'):
		self.name = name
		self.class_name = class_name
		self.race = 'Человек'
		self.buff_scale = 1.1
		self.chance = chance * self.buff_scale
		super().__init__(damage, race = self.race, buff_scale = self.buff_scale, chance = self.chance,
						 max_hp = self.max_hp, class_name= self.class_name, name = self.name)

class Light(Human):
	def __init__(self, name):
		self.name = name
		self.chance = 30
		self.damage = randint(30, 50)
		self.max_hp = 200
		self.class_name = __class__.__name__
		super().__init__(chance = self.chance, max_hp = self.max_hp, name = self.name,
						 damage = self.damage, class_name = self.class_name)

class Heavy(Human):
	def __init__(self, name):
		self.name = name
		self.chance = 0
		self.damage = randint(50, 70)
		self.max_hp = 500
		self.class_name = __class__.__name__
		super().__init__(chance = self.chance, max_hp = self.max_hp, name = self.name,
						 damage = self.damage, class_name = self.class_name)

class Druid(Human):
	def __init__(self, name):
		self.name = name
		self.chance = 70
		self.damage = randint(0,100)
		self.max_hp = 100
		self.class_name = __class__.__name__
		super().__init__(chance = self.chance, max_hp = self.max_hp, name = self.name,
						 damage = self.damage, class_name = self.class_name)

	def attack(self, obj):
		if isinstance(obj, Shaman) and isinstance(obj, Druid):
			pass
		else:
			if self.damage >= 30:
				if isinstance(obj, Human) and not(isinstance(obj, Druid)):
					obj.hp = obj.max_hp
					print(f'{self.race} {self.class_name} {self.name} вылечил '
						  f'{obj.race} {obj.class_name} {obj.name}')
			else:
				if isinstance(obj, Orc):
					obj.hp = 10
					print(f'{self.race} {self.class_name} {self.name} заразил '
						  f'{obj.race} {obj.class_name} {obj.name}')

class Orc(Warrior):
	def __init__(self, chance, damage, max_hp, class_name, name):
		self.class_name = class_name
		self.name = name
		self.chance = chance
		self.race = 'Орк'
		self.buff_scale = 1.1
		self.damage = damage * self.buff_scale
		super().__init__(self.damage, race = self.race, buff_scale = self.buff_scale, name = self.name,
						chance = self.chance, max_hp = self.max_hp, class_name = self.class_name)


class Berserker(Orc):
	def __init__(self, name):
		self.name = name
		self.max_hp = 600
		self.damage = randint(60, 90)
		self.chance = 10
		self.class_name = __class__.__name__
		super().__init__(chance = self.chance, damage = self.damage, name = self.name,
						 max_hp = self.max_hp, class_name = self.class_name)

class Shaman(Orc):
	def __init__(self, name):
		self.name = name
		self.max_hp = 120
		self.chance = 70
		self.damage = randint(0,100)
		self.class_name = __class__.__name__
		super().__init__(chance = self.chance, max_hp = self.max_hp, name = self.name,
						 damage = self.damage, class_name = self.class_name)
	
	def attack(self, obj):
		if isinstance(obj, Shaman) and isinstance(obj, Druid):
			pass
		else:
			if self.damage < 50:
				if isinstance(obj, Orc) and not(isinstance(obj,Shaman)):
					obj.hp = obj.max_hp
					print(f'{self.race} {self.class_name} {self.name} вылечил '
						  f'{obj.race} {obj.class_name} {obj.name}')
			else:
				if isinstance(obj, Human):
					obj.hp = 10
					print(f'{self.race} {self.class_name} {self.name} заразил '
						  f'{obj.race} {obj.class_name} {obj.name}')

def game():
	human_classes = [Light, Heavy, Druid]
	orc_classes = [Berserker, Shaman]
	human_army = [choice(human_classes)(name = str(i)) for i in range(5)]
	orc_army = [choice(orc_classes)(name = str(i)) for i in range(5)]
	x = [human_army, orc_army]
	while (len(human_army) > 0 or len(orc_army) == 0) and (len(human_army) == 0 or len(orc_army) > 0):
		a, b = choice(orc_army), choice(human_army)
		if isinstance(a, Shaman):
			a.attack(choice(choice(x)))
		else:
			a.attack(b)
		for unit in human_army:
			if unit.hp == 0:
				print(unit.race, unit.class_name, unit.name, 'убит в бою')
				human_army = list(filter(lambda x: x.hp != 0, human_army))
				if human_army:
					a = choice(human_army)
				else:
					break
		if b.hp != 0:
			if isinstance(b, Druid):
				b.attack(choice(choice(x)))
			else:
				b.attack(a)
		for unit in orc_army:
			if unit.hp == 0:
				print(unit.race, unit.class_name, unit.name, 'убит в бою')
				orc_army = list(filter(lambda x: x.hp != 0, orc_army))
				if orc_army:
					b = choice(orc_army)
				else:
					break
	if human_army:
		print('Победила команда Human')
	else:
		print('Победила команда Orc')

game()

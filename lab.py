import random


class Chok
	def __init__(self, cost, name)
		self.cost = cost
		self.name = name








	def printinfo(self)
		print(Цена ,self.cost,  , Шоколадка , self.name)

class Iterator
	def iterateChok(self, count)
		list = [Сникерс, Марс, Твикс, Натс]
		for i in list

			chok = Chok(random.randint(40, 70), i)
			chok.printinfo()

def main()
	iterator = Iterator()
	iterator.iterateChok(10)

if __name__ == __main__
	main()
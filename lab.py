import random


class Chok
	def __init__(self, cost, name)
		self.cost = cost
		self.name = name








	def printinfo(self)
		print(���� ,self.cost,  , ��������� , self.name)

class Iterator
	def iterateChok(self, count)
		list = [�������, ����, �����, ����]
		for i in list

			chok = Chok(random.randint(40, 70), i)
			chok.printinfo()

def main()
	iterator = Iterator()
	iterator.iterateChok(10)

if __name__ == __main__
	main()
#Established Class of Game Tiles

resource_dict = {'W':'Wood ','B':'Brick','O':'Ore  ','WH':'Wheat','S':'Sheep','R':'Road ','SE':'Sment','C':'City ','D':'D.Crd'}

class Tile():

	def __init__(self, resource, dice_number, id_number):
		
		self.id_number = id_number
		self.resource = resource
		self.dice_number = dice_number
		self.robber = False
		self.settlements = [0,0,0,0,0,0,0] #[Total, Pos 1, Pos 2, Pos ...]
		self.cities = [0,0,0,0,0,0,0] #[Total, Pos 1, Pos 2, Pos ...]

		
	def __str__(self):

		robber_str = ''
		if self.robber == True:
			robber_str = '(ROBBER)'
		else:
			robber_str = ''

		return f'({self.id_number:>2d}) {resource_dict[self.resource.upper()]}: {self.dice_number:>2d}, Stl:{self.settlements[0]}, Cti:{self.cities[0]} {robber_str}'
	
	def build_settlement(self, pos = 1):
		
		self.settlements[pos] = 1
		self.settlements[0] = self.settlements[0] + 1

	def build_city(self, pos = 1):

		self.cities[pos] = 1
		self.cities[0] = self.cities[0] + 1

	def place_robber(self):

		self.robber = True

	def remove_robber(self):

		self.robber = False

	def calc_resource_prod(dice_roll):
		
		if self.robber == False and self.dice_number == dice_roll:
			return self.settlements[0] + self.cities[0]

		else:
			pass


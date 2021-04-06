#class stores information wrt to items constructed

from catan_tile import resource_dict
from colorama import Fore, Back, Style

import colorama
colorama.init()


class Demand():

	def __init__(self):


		self.roads = ['R']
		self.settlements = ['SE']
		self.cities = ['C']
		self.dev_cards = ['D']

		self.wood = ['W']
		self.brick = ['B']
		self.ore = ['O']
		self.sheep = ['S']
		self.wheat = ['WH']

		self.items_ma = [self.roads,self.settlements,self.cities,self.dev_cards]
		self.items_mi = [self.wood,self.brick,self.ore,self.sheep,self.wheat]

		self.items = self.items_ma + self.items_mi

	def build_buy(self,item):

		if item == 'R':

			self.roads.append(1)
			self.settlements.append(0)
			self.cities.append(0)
			self.dev_cards.append(0)

			self.wood.append(1)
			self.brick.append(1)
			self.ore.append(0)
			self.sheep.append(0)
			self.wheat.append(0)

		if item == 'SE':

			self.roads.append(0)
			self.settlements.append(1)
			self.cities.append(0)
			self.dev_cards.append(0)

			self.wood.append(1)
			self.brick.append(1)
			self.ore.append(0)
			self.sheep.append(1)
			self.wheat.append(1)

		if item == 'C':

			self.roads.append(0)
			self.settlements.append(0)
			self.cities.append(1)
			self.dev_cards.append(0)

			self.wood.append(0)
			self.brick.append(0)
			self.ore.append(3)
			self.sheep.append(0)
			self.wheat.append(2)

		if item == 'D':

			self.roads.append(0)
			self.settlements.append(0)
			self.cities.append(0)
			self.dev_cards.append(1)

			self.wood.append(0)
			self.brick.append(0)
			self.ore.append(1)
			self.sheep.append(1)
			self.wheat.append(1)

	def trend_calc(self,scope = 10):

		#reports absolute and relative demand of the most recent items built/purchased

		abs_total_help = []
		abs_summary = []

		for ele in self.items_ma:

			if len(ele) < scope + 1:
				strt = 1

			else:
				strt = len(ele) - scope

			abs_total_help.append(sum(ele[strt:]))

		abs_total = sum(abs_total_help)

		rel_summary_help = []

		if abs_total != 0:

			for ele in abs_total_help:
				
				rel_summary_help.append(ele / abs_total)

			summary = []

			ct = 0

			for ele in self.items_ma:

				summary.append((ele[0],abs_total_help[ct],rel_summary_help[ct]))

				ct += 1


			print(Fore.YELLOW + f'Resource Demand ({scope} Most Recent Builds)' + Fore.RESET)
			print(Fore.YELLOW + 'Resource: Absolute - Proportion' + Fore.RESET)

			for resource, absolute, relative in summary:

				relative = '{:.0%}'.format(relative)

				print(f'{resource_dict[resource]}: {absolute} - {relative}')

			print('-------------')

		abs_total_help = []
		abs_summary = []

		for ele in self.items_mi:

			if len(ele) < scope + 1:
				strt = 1

			else:
				strt = len(ele) - scope

			abs_total_help.append(sum(ele[strt:]))

		abs_total = sum(abs_total_help)

		rel_summary_help = []

		if abs_total != 0:

			for ele in abs_total_help:
				
				rel_summary_help.append(ele / abs_total)

			summary = []

			ct = 0

			for ele in self.items_mi:

				summary.append((ele[0],abs_total_help[ct],rel_summary_help[ct]))

				ct += 1

			for resource, absolute, relative in summary:

				relative = '{:.0%}'.format(relative)

				print(f'{resource_dict[resource]}: {absolute} - {relative}')
			print('\n')














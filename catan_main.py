#Settlers of Catan Game Assistant

#Import libraries, classes

from catan_demand import Demand
from catan_tile import Tile
from catan_tile import resource_dict
from colorama import Fore, Back, Style

import colorama
colorama.init()

#Create helper functions

def roll_probability():

	results = []
	prob_dict = {}

	for die1 in range(1,7):

		for die2 in range(1,7):

			results.append(die1 + die2)

	for die in range(2,13):

		prob = results.count(die) / len(results)

		prob_dict[die] = prob

	return prob_dict

def inpt_check(inpt,*args):

	inpt_check = 0

	while inpt_check == 0:

		try: 
			inpt = int(inpt)

		except ValueError:
			inpt = inpt.upper()

		except:
			print(Fore.RED + f'Sorry, please enter {args} only:' + Fore.RESET)
			inpt = input()				
		
		try:
			inpt = inpt.upper()

		except AttributeError:
			inpt = int(inpt)

		except: 
			print(Fore.RED + f'Sorry, please enter {args} only:' + Fore.RESET)
			inpt = input()


		if inpt in args:
			inpt_check = 1
			return inpt
		else:
			print(Fore.RED + f'Sorry, please enter {args} only:' + Fore.RESET)
			inpt = input()


def add_city(tile_list):

	print(Fore.YELLOW + 'Tile Assignments:' + Fore.RESET)
	for ele in tile_list:
		print(ele)

	print('\n')

	trigger = 0	

	while trigger == 0:

		print(Fore.RED + 'Provide Tile Number to add a City (1-18):' + Fore.RESET)
		tile_number = input()
		tile_number = inpt_check(tile_number,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)

		print(Fore.RED + 'Provide Location of City (Position # 1-6):' + Fore.RESET)
		city_index = input()
		city_index = inpt_check(city_index,1,2,3,4,5,6)

		#modify tile object
		tile_list[tile_number - 1].build_city(city_index)

		print(Fore.RED + 'Is this Settlement touching another Tile? (Y/N)' + Fore.RESET)
		add_another = input()
		add_another = inpt_check(add_another,'Y','N')

		if add_another == 'N':
			trigger = 1

def add_settlement(tile_list):

	print(Fore.YELLOW + 'Tile Assignments:' + Fore.RESET)
	for ele in tile_list:
		print(ele)

	print('\n')

	trigger = 0	

	while trigger == 0:

		print(Fore.RED + 'Provide Tile Number to add a Settlement (1-18):' + Fore.RESET)
		tile_number = input()
		tile_number = inpt_check(tile_number,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)

		print(Fore.RED + 'Provide Location of Settlement (Position # 1-6):' + Fore.RESET)
		settlement_index = input()
		settlement_index = inpt_check(settlement_index,1,2,3,4,5,6)

		#modify tile object
		tile_list[tile_number - 1].build_settlement(settlement_index)

		print(Fore.RED + 'Is this Settlement touching another Tile? (Y/N)' + Fore.RESET)
		add_another = input()
		add_another = inpt_check(add_another,'Y','N')

		if add_another == 'N':
			trigger = 1

def move_robber(tile_list):

	print(Fore.YELLOW + 'Tile Assignments:' + Fore.RESET)
	for ele in tile_list:
		print(ele)

	print('\n')

	print(Fore.RED + 'Where is the Robber? (Enter Tile Number 1-19):' + Fore.RESET)
	robber_to = input()
	robber_to = inpt_check(robber_to,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)

	for ele in tile_list:
		
		ele.remove_robber()

	tile_list[robber_to - 1].place_robber()


def exp_gen(roll_prob, tile_list):

	resource_list = []
	wood_prob = []
	brick_prob = []
	ore_prob = []
	wheat_prob = []
	sheep_prob = []

	#extract resources and numbers
	for ele in tile_list:
		resource_list.append((ele.resource.upper(), ele.dice_number, ele.settlements, ele.cities, ele.robber))

	for ele in resource_list:
		resource, num, settlements, cities, robber = ele

		if robber == False:

			if resource == 'W':
				wood_prob.append(roll_prob[num] * (settlements[0] + cities[0] * 2))

			if resource == 'B':
				brick_prob.append(roll_prob[num] * (settlements[0] + cities[0] * 2))

			if resource == 'O':
				ore_prob.append(roll_prob[num] * (settlements[0] + cities[0] * 2))

			if resource == 'WH':
				wheat_prob.append(roll_prob[num] * (settlements[0] + cities[0] * 2))

			if resource == 'S':
				sheep_prob.append(roll_prob[num] * (settlements[0] + cities[0] * 2))

	wood_prob_sum = sum(wood_prob)
	brick_prob_sum = sum(brick_prob)
	ore_prob_sum = sum(ore_prob)
	wheat_prob_sum = sum(wheat_prob)
	sheep_prob_sum = sum(sheep_prob)

	total_gen = wood_prob_sum + brick_prob_sum + wheat_prob_sum + sheep_prob_sum + ore_prob_sum

	if total_gen == 0:

		resource_list = []

		for ele in tile_list:
			resource_list.append((ele.resource.upper(), ele.dice_number))

		for ele in resource_list:
			resource, num = ele

			if resource == 'W':
				wood_prob.append(roll_prob[num])

			if resource == 'B':
				brick_prob.append(roll_prob[num])

			if resource == 'O':
				ore_prob.append(roll_prob[num])

			if resource == 'WH':
				wheat_prob.append(roll_prob[num])

			if resource == 'S':
				sheep_prob.append(roll_prob[num])

	wood_prob_sum = sum(wood_prob)
	brick_prob_sum = sum(brick_prob)
	ore_prob_sum = sum(ore_prob)
	wheat_prob_sum = sum(wheat_prob)
	sheep_prob_sum = sum(sheep_prob)

	total_gen = wood_prob_sum + brick_prob_sum + wheat_prob_sum + sheep_prob_sum + ore_prob_sum

	wood_gen_share = sum(wood_prob)/total_gen
	brick_gen_share = sum(brick_prob)/total_gen
	ore_gen_share = sum(ore_prob)/total_gen
	wheat_gen_share = sum(wheat_prob)/total_gen
	sheep_gen_share = sum(sheep_prob)/total_gen

	return {'W':'{:.0%}'.format(wood_gen_share),'B':'{:.0%}'.format(brick_gen_share),'O':'{:.0%}'.format(ore_gen_share),'WH':'{:.0%}'.format(wheat_gen_share),'S':'{:.0%}'.format(sheep_gen_share)}

def roll_tracker(pre_rolls, roll):

	pre_rolls[roll - 2] = pre_rolls[roll - 2] + 1
	return pre_rolls

def roll_prob_calc(pre_rolls):

	roll_prob = []

	for ele in pre_rolls:
		prob = ele / sum(pre_rolls)
		roll_prob.append(prob)

	return roll_prob

def resource_input():

	resources_abr = ['W','B','O','WH','S']
	 		
	print(Fore.RED + "Resource: \n 'W' for Wood, 'B' for Brick, 'O' for Ore, 'Wh' for Wheat, 'S' for Sheep:" + Fore.RESET)
	resource = input()
		
	check = 0

	while check == 0:

		if resource.upper() in resources_abr:
			check = 1
		
		else: 
			print(Fore.RED + "Sorry, please enter 'W' for Wood, 'B' for Brick, 'O' for Ore, 'Wh' for Wheat, 'S' for Sheep only:" + Fore.RESET)
			resource = input()

	return resource.upper()

def dice_number_input():

	dice_numbers = [2,3,4,5,6,7,8,9,10,11,12]
	
	print(Fore.RED + 'Dice Number: \n (Integer, 2-12)' + Fore.RESET) 		
	dice_number = input()
	dice_number = inpt_check(dice_number,2,3,4,5,6,7,8,9,10,11,12)
	return dice_number


#Create Game Tiles
tile_check = 0

while tile_check == 0:

	'''
	tiles = [Tile('o',10,1),Tile('s',2,2),Tile('w',9,3),Tile('wh',12,4),Tile('b',6,5),Tile('s',4,6),Tile('b',10,7),
	Tile('wh',9,8),Tile('w',11,9),Tile('w',3,10),Tile('o',8,11),Tile('w',8,12),Tile('o',3,13),Tile('wh',4,14),
	Tile('s',5,15),Tile('b',5,16),Tile('wh',6,17),Tile('s',11,18)]
	'''

	tiles = []

	for num in range(1,19):
		resource = resource_input()
		dice_number = dice_number_input()
		id_number = num
		tiles.append(Tile(resource, dice_number, num))

	print(Fore.YELLOW + 'Tile Assignments:' + Fore.RESET)
	for ele in tiles:
		print(ele)

	print('\n')

	print(Fore.RED + 'Are the Tiles assigned correctly? (Y/N):' + Fore.RESET)
	correct = input().upper()

	inp_check = 0

	while inp_check == 0:

		if correct in ['Y','N']:
			inp_check = 1

		else:
			print(Fore.RED + 'Sorry, please enter either "Y" or "N":' + Fore.RESET)
			correct = input().upper()

	if correct == 'Y':
		tile_check = 1

	print('\n')

#define helper variables

setup_complete = 0
prev_rolls = [0,0,0,0,0,0,0,0,0,0,0]	
demand = Demand()

#Ongoing input
game_on = 0

while game_on == 0:

	#calculate resource scarcity
	share = exp_gen(roll_probability(),tiles)

	#sort share dictionary
	share_val_sorted = sorted(share.values())
	share_sorted = {}

	for val in share_val_sorted:
		for key in share.keys():
			if share[key] == val:
				share_sorted[key] = val

	#print sorted share dictionary
	print(Fore.YELLOW + 'Percent of Initial Expected Resource Generation:' + Fore.RESET)

	ct = 1

	for key, value in share_sorted.items():
		most_scarce = '(Most Scarce)'
		least_scarce = ''
		
		if ct > 1:
			most_scarce = ''

		if ct == 5:
			least_scarce = '(Least Scarce)'

		print(f'{resource_dict[key]}: {value} {most_scarce}{least_scarce}')

		ct += 1

	print('\n')

	#material demand tracking and printout
	
	if setup_complete == 1:
		scope = 10
		demand.trend_calc(scope)
	
	#roll history tracking and comparison
	roll_comp = []
	
	if sum(prev_rolls) != 0:
		roll_his_percent = roll_prob_calc(prev_rolls)
		roll_prob = roll_probability()

		ct = 0

		while ct < len(prev_rolls):

			roll_comp.append((ct+2,roll_his_percent[ct],roll_prob[ct + 2]))

			ct += 1

		print(Fore.YELLOW + 'Num: Probability | Actual' + Fore.RESET)

	for ele in roll_comp:
		num, his, prob = ele

		print(f'{num:2d}: {prob:>3.0%} | {his:>3.0%}')

	if setup_complete == 0:

		print(Fore.RED + 'What you you like to do?: Add Settlement "Se", Complete Set-Up("SU"), End Game "E")' + Fore.RESET)
		act = input()
		act = inpt_check(act,'SE',"SU",'E')
		print('\n')

		if act == 'SU':

			setup_complete = 1

	if setup_complete == 1:

		print(Fore.RED + 'What would you like to do?: (Enter Roll (#2-12), Add Road "R", Add Settlement "Se", Add City "C", Buy Dev Card "D", Move Robber "MR", End Game "E")' + Fore.RESET)
		act = input()
		act = inpt_check(act,'R','SE','C','MR','E','D',2,3,4,5,6,7,8,9,10,11,12)
		print('\n')

	if act == 'C':

		add_city(tiles)

		if setup_complete == 1:
			demand.build_buy(act)

	if act == 'SE':

		add_settlement(tiles)

		if setup_complete == 1:
			demand.build_buy(act)

	if act == 'MR':

		move_robber(tiles)

	if act == 'E':

		game_on = 1

	if act == 'D' and setup_complete == 1:

		demand.build_buy(act)

	if act == 'R' and setup_complete == 1:

		demand.build_buy(act)

	if act in range(2,13):

		prev_rolls = roll_tracker(prev_rolls, act)

	print(Fore.YELLOW + 'Tile Assignments:' + Fore.RESET)
	for ele in tiles:
		print(ele)

	print('\n')


#cd OneDrive\\Documents\\Python\\Catan Game Assistant

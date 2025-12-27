#Inheritance
class SportsPlayer:

	def __init__(self,name,sport, height, weight,dob,country):
		self.name=name
		self.sport=sport
		self.height=height
		self.weight=weight
		self.__dob=dob
		self.__country=country
		
	def change_name(self,new_name):
		self.name=new_name
		
	def change_sport(self,new_sport):
		self.sport=new_sport
		
	def change_height(self,new_height):
		self.height=new_height
		
	def change_weight(self,new_weight):
		self.weight=new_weight
		
	def get_all_details(self):
		return[
		self.name,
		self.sport,
		self.height,
		self.weight,
		self.__dob,
		self.__country
		]
		
	def print_details(self):
            print("Name: ", self.name)
            print("Sport: ",self.sport)
            print("Height: ",self.height)
            print("Weight: ",self.weight)
            print("DOB :",self.__dob)
            print("Country: ",self.__country)

class FootballPlayer(SportsPlayer):
	def __init__(
	self,
	name,
	sport,
	height,
	weight,
	dob,
	country,
	position,
	jersey_no,
	club,
	goals,
	assists
	):
		SportsPlayer.__init__(self,name,sport,height,weight,dob,country)
		self.position=position
		self.jersey_no=jersey_no
		self.club=club
		self.goals=goals
		self.assists=assists
		
	def set_position(self,position):
		self.position=position
		
	def set_jersey_no(self,jersey_no):
		self.jersey_no=jersey_no
	
	def set_club(self,club):
		self.club=club
		
	def set_goals(self,goals):
		self.goals=goals
		
	def set_assists(self,assists):
		self.assists=assists
		
	def print_details(self):
		print(f" The players name is {self.name} plays the sport of {self.sport} with jersey number {self.jersey_no} and belong to club {self.club}.")
	
footy = FootballPlayer("Christiano ",
    "Football",
    "187",
    "85",
    "05/02/1985",
    "portugal",
    "ST",
    "7",
    "Man United",
    "820",
    "273")
footy.change_name("Christiano Ronaldo")
footy.print_details()
	
		
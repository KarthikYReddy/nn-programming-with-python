class Player:
    def __init__(self,name,sport):
    	self.name=name
    	self.sport=sport
    	
    def _run(self):
    	return "Running"
    	
    def walking(self):
    	return "walking"
    	
class Coach:
	def __init__(self,name,player):
		self.name=name
		self.player=player
		
	def command_player(self):
		return self.player._run()
		
	def walk(self):
		return self.player.walking()
		
player = Player("Micheal Jordan","Basketball")
coach = Coach("Phil",player)
print(coach.walk())

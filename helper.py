import pygame, os
pygame.font.init()
screen_width = 1400
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

font = pygame.font.SysFont('georgia', 20)
displayStartText = font.render("START SCREEN", False, (0, 0, 0))
displaySettingText = font.render("SETTINGS", False, (0, 0, 0))
displayScoreText = font.render("HIGH SCORE: ", False, (0, 0, 0))

# Animations Class -- Finished logic
# 	Takes care of all animations; characters and backgrounds
class Animations(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, directory):
		super().__init__()
		self.attack_animation = False
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.sprites = []
		list = os.listdir(directory)
		list.sort()

		for item in list[1:]:
			if directory == "Animations/Background" or directory == "Animations/Background2" or directory == "Animations/Background3":
				self.sprites.append(pygame.transform.scale(pygame.image.load(directory + '/' + item).convert(), (1400,900)))
			else:
				self.sprites.append(pygame.image.load(directory + '/' + item).convert())

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x, pos_y]

	def idle(self):
		self.attack_animation = True

	def update(self, speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

	def isOver(self, pos):
		if pos[0] > self.pos_x and pos[0] < self.pos_x + self.width:
			if pos[1] > self.pos_y and pos[1] < self.pos_y + self.height:
				return True
		return False

# Text Button Class -- Finished Logic
# 	Placeholder for image based buttons
class Button:
	def __init__(self, color, x, y, width, height, text=''):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.surf = pygame.Surface((width, height))
		self.surf.fill(color)
		self.rect = (x, y)

	def draw(self, win, outline=None):
		# Call this method to draw the button on the screen
		if outline:
			pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
			pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

		if self.text != '':
			text = font.render(self.text, 1, (0, 0, 0))
			win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

	def isOver(self, pos):
		# Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False


# Image Button Class -- WIP
# True button class
class ImgButton():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect

class Player():
	def __init__(self, player):
		self.lives = 3
		self.character = "placeholder"
		self.player = player
		self.game_sprites = pygame.sprite.Group()
	def setCharacter(self, character, player):
		self.character = character
		if player == 1:
			if character == "Animations/SilverSitAnimation":
				self.player1Animation = Animations(100, 300, character)
			else:
				self.player1Animation = Animations(50, 350, character)
			self.game_sprites.add(self.player1Animation)
		if player == 2:
			if character == "Animations/SilverSitAnimation":
				self.player2Animation = Animations(850, -100, character)
			else:
				self.player2Animation = Animations(800, -60, character)
			self.game_sprites.add(self.player2Animation) 

heart = pygame.transform.scale(pygame.image.load("Images/heart.png"), (100,100))
platform = pygame.transform.scale(pygame.image.load("Images/platform.png"), (800,800))
sound = pygame.transform.scale(pygame.image.load("Images/sound.png"), (100,100))
mute = pygame.transform.scale(pygame.image.load("Images/mute.png"), (100,100))
startText = Button((255, 255, 255), screen_width/2, screen_height/2, 100, 25, "Start")
settingText = Button((255, 255, 255), screen_width/2, screen_height/2 + 50, 100, 25, "Settings")
returnText = Button((255, 255, 0), 1200, 100, 100, 25, "Return")
volumeText = Button((255, 255, 0), 650, 500, 100, 25, "Volume")
quitText = Button((255, 255, 255), screen_width/2, screen_height/2 + 100, 100, 25, "Quit")
endlessText = Button((255, 255, 255), screen_width/2, screen_height/2, 150, 25, "Endless Mode")
versusText = Button((255, 255, 255), screen_width/2, screen_height/2 + 50, 150, 25, "Versus Mode")

from sys import exit as sys_exit

import pygame, pygame.freetype

class Game:
	def __init__(self):
		# Initializing backend variables & modules
		pygame.init()
		self.display = pygame.display.set_mode((600, 600))
		pygame.display.set_caption('TronPy')
		self.font = pygame.freetype.SysFont('Arial', 30)
		self.clock = pygame.time.Clock()
		self.dt = 0
		self.counter = 0
		self.can_move_player_one = False
		self.can_move_player_two = False
		self.game_state = 0

		# Initializing frontend variables
		self.player_one = []
		self.player_one_vel_X = 0
		self.player_one_vel_y = 0
		self.player_two = []
		self.player_two_vel_x = 0
		self.player_two_vel_y = 0

	def update(self):
		self.handle_events()

		self.counter += self.dt
		if self.counter >= 1:
			self.counter = 0
			self.can_move_player_one = True
			self.can_move_player_two = True

			if self.game_state == 0:
				if self.player_one_vel_x != 0 or self.player_one_vel_y != 0:
					self.move_player_one()
				if self.player_two_vel_x != 0 or self.player_two_vel_y != 0:
					self.move_player_two()
				self.handle_collisions()

	def render(self):
		self.display.fill((0, 0, 0))

		if self.game_state == 0:
			for piece in self.player_one:
				pygame.draw.rect(self.display, (255, 0, 0), (piece[0], piece[1], 20, 20))
			for piece in self.player_two:
				pygame.draw.rect(self.display, (0, 255, 0), (piece[0], piece[1], 20, 20))

		pygame.display.flip()

	def run(self):
		self.new_game()
		while True:
			self.update()
			self.render()
			self.dt = self.clock.tick(60) / 1000

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys_exit()
			elif event.type == pygame.KEYDOWN:
				if self.game_state == 0:
					if event.key == pygame.key.key_code('w') and self.can_move_player_one:
						if self.player_one_vel_y == 0:
							self.player_one_vel_y = -1
							self.player_one_vel_x = 0
					if event.key == pygame.key.key_code('s') and self.can_move_player_one:
						if self.player_one_vel_y == 0:
							self.player_one_vel_y = 1
							self.player_one_vel_x = 0
					if event.key == pygame.key.key_code('a') and self.can_move_player_one:
						if self.player_one_vel_x == 0:
							self.player_one_vel_x = -1
							self.player_one_vel_y = 0
					if event.key == pygame.key.key_code('d') and self.can_move_player_one:
						if self.player_one_vel_x == 0:
							self.player_one_vel_x = 1
							self.player_one_vel_y = 0

					if event.key == pygame.key.key_code('up') and self.can_move_player_two:
						if self.player_two_vel_y == 0:
							self.player_two_vel_y = -1
							self.player_two_vel_x = 0
					if event.key == pygame.key.key_code('down') and self.can_move_player_two:
						if self.player_two_vel_y == 0:
							self.player_two_vel_y = 1
							self.player_two_vel_x = 0
					if event.key == pygame.key.key_code('left') and self.can_move_player_two:
						if self.player_two_vel_x == 0:
							self.player_two_vel_x = -1
							self.player_two_vel_y = 0
					if event.key == pygame.key.key_code('right') and self.can_move_player_two:
						if self.player_two_vel_x == 0:
							self.player_two_vel_x = 1
							self.player_two_vel_y = 0

	def handle_collisions(self):
		# Check collisions against player one body
		for i in range(len(self.player_one), 1):
			if self.player_one[0][0] == self.player_one[i - 1][0] and self.player_one[0][1] == self.player_one[i - 1][1]:
				self.game_state = 2
			elif self.player_two[0][0] == self.player_one[i][0] and self.player_two[0][1] == self.player_one[i][1]:
				self.game_state = 1

		# Check collision against player two body
		for i in range(len(self.player_two), 1):
			if self.player_two[0][0] == self.player_two[i - 1][0] and self.player_two[0][1] == self.player_twp[i - 1][1]:
				self.game_state = 1
			elif self.player_one[0][0] == self.player_two[i][0] and self.player_one[0][1] == self.player_two[i][1]:
				self.game_state = 2

		# Check player one collision against wall
		if self.player_one[0][0] < 0 or self.player_one[0][0] == 600 or self.player_one[0][1] < 0 or self.player_one[0][1] == 600:
			self.game_state = 2

		# Check player two collision against wall
		if self.player_two[0][0] < 0 or self.player_two[0][0] == 600 or self.player_two[0][1] < 0 or self.player_two[0][1] == 600:
			self.game_state = 1

	def move_player_one(self):
		self.player_one.append([self.player_one[0][0], self.player_one[0][1]])
		self.player_one[0][0] += self.player_one_vel_x * 20
		self.player_one[0][1] += self.player_one_vel_y * 20

	def move_player_two(self):
		self.player_two.append([self.player_two[0][0], self.player_two[0][1]])
		self.player_two[0][0] += self.player_two_vel_x * 20
		self.player_two[0][1] += self.player_two_vel_y * 20

	def new_game(self):
		self.player_one = [[15 * 20, 10 * 20]]
		self.player_one_vel_x = 0
		self.player_one_vel_y = 0
		self.player_two = [[15 * 20, 20 * 20]]
		self.player_two_vel_x = 0
		self.player_two_vel_y = 0

if __name__ == '__main__':
	game = Game()
	game.run()
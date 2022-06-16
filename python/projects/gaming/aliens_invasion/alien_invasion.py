# alien_invasion.py
# Updated: cramos 12/jun/2022

# Based on PythonCrashCourse book (page 229)

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Main class to handle all game assets and functionallity"""

	def __init__(self):
		"""Initialize the game and create the resources"""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

		# Set the background color
		self.bg_color = (230, 230, 230)
 
	def run_game(self):
		"""Start the main loop for the game"""

		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_events(self):
		""" Respond to keypress and mouse events """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

			#print(f"Something happens")

	def _check_keydown_events(self, event):
		""" Responds to keypress """
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True
		if event.key == pygame.K_LEFT:
			# Move the ship to the left
			self.ship.moving_left = True
		if event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		""" Responds to key releases """
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _update_screen(self):
		""" Update images on the screen and flip to new screen """
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		# Make the most recently drawn screen visible
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game

	ai = AlienInvasion()
	ai.run_game()

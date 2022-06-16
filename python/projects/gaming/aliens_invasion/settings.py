# settings.py
# Updated: cramos 12/jun/2022
# This is part of the AliensInvasion project
# Based on PythonCrashCourse book (page 229)

class Settings:
	""" A class to store all settings of the Aliens Invasion """
	def __init__(self):
		""" Initialize the game's settings """
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5
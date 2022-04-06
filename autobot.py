"""Documentação para Automação do SIGEF"""

from pyautogui import PAUSE, press, write, locateCenterOnScreen, click
from time import sleep
from data import SPOTIFY
 
class CenterImageNotFoundError(Exception):
	"""docstring for CenterImageNotFoundError"""
	def __init__(self, message = 'Coordenadas centrais x e y da imagem não foram encontradas'):	
		self.message = message
		super().__init__(self.message)

class AutoBot(object):
	"""docstring for AutoBot"""
	def __init__(self, browser: str, data: dict):
		super(AutoBot, self).__init__()
		self.PAUSE = 2
		self.browser = browser
		self.data = data

	def __choose_browser_and_login__(self):

		browsers = {
			'chrome': 'google chrome',
			'firefox': 'firefox',
			'edge': 'microsoft edge',
			'explorer': 'internet explorer'
		}

		press('win')

		write(browsers.get(self.browser))

		press('enter')

		sleep(2)

		write(self.data.get('site'))

		press('enter')

	def __select_image_click__(self, function: str):

		sleep(5)

		try:

			x, y = locateCenterOnScreen(self.data.get(function))

			click(x = x, y = y)

		except:

			raise CenterImageNotFoundError()

	def __write__(self, text: str):

		sleep(2)

		write(text)

if __name__ == '__main__':

	autobot = AutoBot(browser = 'chrome', data = SPOTIFY)

	autobot.__choose_browser_and_login__()

	autobot.__select_image_click__(function = 'search')

	autobot.__write__('marília mendonça bin')

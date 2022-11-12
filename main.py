import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.Label import Label

class PongGame(Widget):
	pass

class PongApp(App):
	def build(self):
		return PongGame()

if __name__ == '__main__':
	PongApp().run()

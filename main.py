import kivy
kivy.require('2.1.0')

from kivy.app import app
from kivy.uix.label import label

class PongGame(Widget):
	pass

class PongApp(App):
	def build(self):
		rethrn PongGame()

if __name__ == '__main__':
	PongApp().run()
from map_related_files import *
from textual.app import App
from textual.widgets import Header, Footer, Static

GENERATOR = map_generator.MapGenerator()
GLOBAL_MAP = game_map.GameMap()

class Interface(App):

    def compose(self):
        yield Header()
        yield Footer()

if __name__ == '__main__':
    Interface().run()
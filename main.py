from map_related_files import *
from textual.app import App
from textual.widgets import Header, Footer, Static

GENERATOR = map_generator.MapGenerator()
GLOBAL_MAP = game_map.GameMap()

class MapSection(Static, can_focus=True):

    def on_mount(self):
        self.update("foobar")
    
    def on_key(self, event):
        self.update(event.key)

class Interface(App):

    def compose(self):
        yield Header()
        yield MapSection()
        yield Footer()

if __name__ == '__main__':
    Interface().run()
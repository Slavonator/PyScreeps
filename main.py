from map_related_files import *
from textual.app import App
from textual.widgets import Header, Footer, Static

GENERATOR = map_generator.MapGenerator()
GLOBAL_MAP = game_map.GameMap()

class TestLocalMapWidget(Static):

    def on_mount(self):
        self.generate_map()

    def on_click(self):
        self.generate_map()

    def generate_map(self):
        self.update(GENERATOR.generate_map())


class Interface(App):

    def compose(self):
        yield Header()
        yield TestLocalMapWidget()
        yield Footer()


if __name__ == '__main__':
    Interface().run()
from map_related_files import *
from textual.app import App
from textual.widgets import Header, Footer, Static

GENERATOR = map_generator.MapGenerator()
GLOBAL_MAP = game_map.GameMap()

class MapWidget(Static, can_focus=True):

    def on_mount(self):
        self.current_section = (0, 0)
        self.display_current_section()
    
    def on_key(self, event):
        try:
            if event.key == 'up':
                self.move_current_section('n')
            if event.key == 'down':
                self.move_current_section('s')
            if event.key == 'left':
                self.move_current_section('e')
            if event.key == 'right':
                self.move_current_section('w')
        except IndexError:
            self.update(f'{GLOBAL_MAP.max_y, GLOBAL_MAP.min_y}')

    def move_current_section(self, direction):
        x, y = self.current_section
        for symbol in direction:
            if symbol == 'n':
                y += 1
            if symbol == 's':
                y -= 1
            if symbol == 'e':
                x += 1
            if symbol == 'w':
                x -= 1
        self.current_section = (x, y)
        self.display_current_section()


    def display_current_section(self):
        sector = GLOBAL_MAP.get_sector(*self.current_section)
        if sector is None:
            sector = game_map.Sector(GENERATOR.generate_map(), self.current_section)
            GLOBAL_MAP.add_sector(sector)
        self.update(str(sector))


class Interface(App):

    def compose(self):
        yield Header()
        yield MapWidget()
        yield Footer()

if __name__ == '__main__':
    Interface().run()
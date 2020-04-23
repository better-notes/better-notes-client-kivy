import requests
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

import app.commons
import app.settings


class NoteApp(App):  # type: ignore
    def build(self) -> Carousel:
        scroll_view = ScrollView(do_scroll_y=True)
        grid_layout = GridLayout(cols=1, size_hint_y=10)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        note_bytes = requests.get(app.settings.DATA_URL)
        note_list = app.commons.msgpack.loads(note_bytes.content)

        for note in note_list:
            tags_grid = GridLayout(rows=len(note["tags"]))
            for tag in note["tags"]:
                label = TextInput(text=tag["name"])
                tags_grid.add_widget(label)

            label = TextInput(text=note["text"])

            grid = GridLayout(cols=2)
            grid.add_widget(label)
            grid.add_widget(tags_grid)
            grid_layout.add_widget(grid)

        scroll_view.add_widget(grid_layout)
        return scroll_view

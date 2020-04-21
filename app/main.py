import requests
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from app import commons, settings


class NoteApp(App):  # type: ignore
    def build(self) -> Carousel:
        carousel = Carousel(direction="top")

        note_bytes = requests.get(settings.DATA_URL)
        note_list = commons.msgpack.loads(note_bytes.content)

        for note in note_list:

            tags_grid = GridLayout(rows=len(note["tags"]))
            for tag in note["tags"]:
                label = Label(text=tag["name"], markup=True)
                tags_grid.add_widget(label)

            label = Label(text=note["text"], markup=True)

            grid = GridLayout(cols=2)
            grid.add_widget(label)
            grid.add_widget(tags_grid)

            carousel.add_widget(grid)

        return carousel


NoteApp().run()

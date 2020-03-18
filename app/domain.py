import dataclasses
from cmd import Cmd

import entity
import repositores


class CLI(Cmd):
    _text_media_repo: repositores.TextMediaRepository = (
        repositores.TextMediaRepository()
    )

    def _stdout(self, message: str):
        self.stdout.write(f'{message}\n')

    def do_exit(self, input_: str) -> bool:
        return True

    do_q = do_exit

    def default(self, inp):
        self._stdout('Unknown command.\n')

    def do_add(self, input_: str) -> None:
        text_media = self._text_media_repo.add(
            entity.TextMedia.Input(value=input_)
        )
        self._stdout(f'Added text media: {text_media}')

    def do_list(self, input_: str) -> None:
        self._stdout(self._text_media_repo.as_dict())

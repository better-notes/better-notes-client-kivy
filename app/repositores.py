import dataclasses
import json
import json.decoder
from typing import Any, Dict

import entity

Json = Dict[str, Any]


class DictTextMediaRepository:
    _file_path: str = '.storage.json'

    def _get_store(self) -> Json:
        try:
            with open(self._file_path, 'r') as file:
                return json.loads(file.read())
        except FileNotFoundError:
            self._dump_store({})
            return {}

    def _dump_store(self, store: Json):
        with open(self._file_path, 'w') as file:
            file.write(json.dumps(store))

    def as_dict(self):
        return self._get_store()

    def add(self, text_media_input: entity.TextMedia.Input) -> entity.TextMedia:
        store = self._get_store()

        text_media = entity.TextMedia(
            id_=len(store), **dataclasses.asdict(text_media_input)
        )
        assert text_media.id_ not in store.keys()
        store[text_media.id_] = dataclasses.asdict(text_media)

        self._dump_store(store)
        return text_media

    def get_by_id(self, id_: int) -> entity.TextMedia:
        store = self._get_store()
        return entity.TextMedia(**store[id_])


TextMediaRepository = DictTextMediaRepository

import dataclasses


@dataclasses.dataclass
class TextMedia:

    @dataclasses.dataclass
    class Input:
        value: str

    id_: int
    value: str

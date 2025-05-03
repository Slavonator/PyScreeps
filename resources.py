class Resource:
    def __init__(
            self,
            name: str,
            extractable_by: list | None=None,
            rarity: float=0
    ):
        self.name = name
        self.extractable_by = extractable_by if extractable_by is not None else []
        self.rarity = rarity


class Iron(Resource):

    def __init__(self):
        super().__init__("железо", ["all"], 0.5)

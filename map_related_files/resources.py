from datetime import timedelta

class Resource:
    def __init__(
            self,
            name: str,
            extractable_by: list | None=None,
            rarity: float=1,
            timeout: timedelta=timedelta(seconds=10)
        ):
        
        self.name = name
        self.extractable_by = extractable_by if extractable_by is not None else []
        self.rarity = rarity
        self.timeout = timeout

    def get_timeout(self):
        return self.timeout


class Iron(Resource):

    def __init__(self):
        super().__init__(
            "железо",
            ["all"],
            0.5,
            timeout=timedelta(seconds=30)
        )

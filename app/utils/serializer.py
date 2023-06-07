def serialize(item: dict) -> dict:
    return {
        **{i: str(item[i]) for i in item if i == "_id"},
        **{i: item[i] for i in item if i != "_id"},
    }

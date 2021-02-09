import aiosqlite

db = None

async def conn(config, models):
    global db
    db = await aiosqlite.connect(config["database_path"])
    for model in models:
        query = """
        CREATE TABLE IF NOT EXISTS {} ({});
        """
        values = []
        for column, data in model.__schema__.items():
            types = {
                str: "TEXT",
                int: "INTEGER",
                float: "REAL",
                bool: "INTEGER"
            }
            if data["type"] not in types.keys():
                raise TypeError("Data type of {} is not valid.".format(data["type"].__class__.__name__))
            current_value = f"{column} {types[data['types']]}"
            if data["nullable"] is False:
                current_value += " NOT NULL"
            if data["default"] is not ...:
                current_value += "DEFAULT '{}'".format(data["default"])
            if data["queryextra"]:
                current_value += data["queryextra"]
            values.append(current_value+",")


class ModelBase:
    instance = None

    __tablename__ = ...
    __schema__ = ...

    @classmethod
    async def get(cls, key):
        raise NotImplementedError

    async def edit(self, *, instance = None, new_values: dict):
        raise NotImplementedError

    async def delete(self, *, instance = None):
        raise NotImplementedError

    @classmethod
    async def create(cls, key, values, tablename: str):
        raise NotImplementedError


class StoreItem:

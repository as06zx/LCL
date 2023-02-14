class Summoner:
    def __init__(self, connection):
        self.connection = connection

    async def GetSummoners(self, name):
        param = {
            "name": name
        }
        summoners = await self.connection.request("get", "/lol-summoner/v1/summoners", params=param)
        return summoners

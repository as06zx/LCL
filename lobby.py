class Lobby:
    def __init__(self, connection):
        self.connection = connection

    async def GetMembers(self):
        members = await( await self.connection.request("get", "/lol-lobby/v2/lobby/members")).json()
        return members

    async def CreateLobby(self, name="", map=11, team_size=5, password=None):
        lobby_body = {
            "customGameLobby": {
                "configuration": {
                    "gameMode": "CLASSIC",
                    "gameMutator": "",
                    "gameServerRegion": "",
                    "mapId": map,
                    "mutators": {
                        "id": 1
                    },
                    "spectatorPolicy": "AllAllowed",
                    "teamSize": team_size,
                },
                "lobbyName": name,
                "lobbyPassword": password,
            },
            "isCustom": True,
            "queueId": -1
        }
        
        await self.connection.request("post", "/lol-lobby/v2/lobby", data=lobby_body)

class Profissional:
    def __init__(self, dt_req: str, cli_id: str, coords: str):
        ano, mes, dia = dt_req[:4], dt_req[4:6], dt_req[6:]
        self.dt_req = f'{dia}/{mes}/{ano}'
        self.cli_id = cli_id
        self.coords = coords

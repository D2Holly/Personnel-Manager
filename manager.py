class ShipBrigade:
    def __init__(self, ship_name):
        self.ship_name = ship_name
        self.crew = []

    def __repr__(self):
        return self.ship_name

print(ShipBrigade("Bob"))

from enum import Enum


class SweetPotatoState(Enum):
    UNBAKED = 1
    HALF_BAKED = 2
    BAKED = 3
    BURNT = 4


class SweetPotato:
    def __init__(self) -> None:
        self.bake_time = 0
        self.state = SweetPotatoState.UNBAKED
        self.flavours = []

    def bake(self, time):
        assert time >= 0
        self.bake_time += time
        t = self.bake_time
        if 0 <= t <= 5:
            self.state = SweetPotatoState.UNBAKED
        elif 5 < t <= 10:
            self.state = SweetPotatoState.HALF_BAKED
        elif 10 < t <= 15:
            self.state = SweetPotatoState.BAKED
        else:
            self.state = SweetPotatoState.BURNT

    def add_flavour(self, flavour):
        self.flavours.append(flavour)

    def __str__(self) -> str:
        m = {
            SweetPotatoState.UNBAKED: "生的",
            SweetPotatoState.HALF_BAKED: "半生不熟",
            SweetPotatoState.BAKED: "熟了",
            SweetPotatoState.BURNT: "糊了",
        }
        state = m[self.state]
        return "烤地瓜{}\n加了调料: {}".format(state, " ".join(self.flavours))


if __name__ == "__main__":
    potato = SweetPotato()
    potato.bake(7)
    potato.add_flavour("糖")
    print(str(potato))
    potato.bake(5)
    potato.add_flavour("盐")
    print(str(potato))

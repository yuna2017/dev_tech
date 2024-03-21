class SweetPotato():
    def __init__(self):
        self.time = 0
        self.state = 'Raw'
        self.condiments = []

    def cook(self, t):
        self.time += t

        if 0 <= self.time < 3:
            self.state = 'Raw -^-'
        elif 3 <= self.time < 5:
            self.state = 'Half-baked 0.0'
        elif 5 <= self.time < 8:
            self.state = 'Well-baked OwO'
        elif 8 <= self.time:
            self.state = 'Overcooked!! QAQ'

    def add_condiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'The time of cooking is {self.time} minutes,its state is {self.state}, the condiments added are {self.condiments}'


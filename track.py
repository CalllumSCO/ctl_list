class Track:
    def __init__(self, name, retro, rating, timesplayed, playedbase):
        self.name = name
        self.retro = retro
        self.rating = rating
        self.timesplayed = timesplayed
        self.playedbase = playedbase
    
    def __str__(self):
        return f'{self.name}, Retro: {self.retro}, Rating: {self.rating}, Times Played: {self.timesplayed}, PlayedBase = {self.playedbase}'
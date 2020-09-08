class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def output(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {self.museum}.')


my_input = Painting(input(), input(), input())
my_input.output()

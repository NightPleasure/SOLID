from abc import ABC, abstractmethod

class Event(ABC):
    @abstractmethod
    def get_details(self):
        pass


class Movie(Event):
    def __init__(self, title, genre, director, release_date):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_date = release_date

    def get_details(self):
        return f"{self.title} ({self.release_date}) - {self.genre}, directed by {self.director}"


class Concert(Event):
    def __init__(self, artist, date, venue, tickets_available):
        self.artist = artist
        self.date = date
        self.venue = venue
        self.tickets_available = tickets_available

    def get_details(self):
        return f"{self.artist} - {self.date}, {self.venue}, {self.tickets_available} tickets available"


events = [Movie("The Shawshank Redemption", "Drama", "Frank Darabont", 1994),
          Concert("The Rolling Stones", "12/10/2023", "Madison Square Garden", 5000)]

for event in events:
    print(event.get_details())

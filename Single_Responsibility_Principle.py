class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

    def create_event(self):
        print(f"Evenimentul '{self.name}' a fost creat cu succes la data de {self.date} în locația {self.location}.")

class Activity:
    def __init__(self, name, duration, location):
        self.name = name
        self.duration = duration
        self.location = location

    def create_activity(self):
        print(f"Activitatea '{self.name}' a fost creată cu succes, va dura {self.duration} minute și se va desfășura în locația {self.location}.")

class EventManager:
    def __init__(self):
        self.events = []
        self.activities = []

    def add_event(self, event):
        self.events.append(event)
        print(f"Evenimentul '{event.name}' a fost adăugat în lista de evenimente.")

    def add_activity(self, activity):
        self.activities.append(activity)
        print(f"Activitatea '{activity.name}' a fost adăugată în lista de activități.")

    def list_events(self):
        for event in self.events:
            print(f"Evenimentul '{event.name}' va avea loc la data de {event.date} în locația {event.location}.")

    def list_activities(self):
        for activity in self.activities:
            print(f"Activitatea '{activity.name}' va dura {activity.duration} minute și se va desfășura în locația {activity.location}.")


event = Event('Conferința de marketing', '2023-05-20', 'Sala de conferințe')
event.create_event()

activity = Activity('Workshop de social media', 60, 'Sala 1')
activity.create_activity()

manager = EventManager()
manager.add_event(event)
manager.add_activity(activity)

manager.list_events()
manager.list_activities()

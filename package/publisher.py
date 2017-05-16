from . import event

class Publisher(object):
    
    events = event.Event()
    
    def trigger(self, event_name, data):
        self.events(event_name, data)
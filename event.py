class Event(object):

    def __init__(self):
        self.handlers = []
    
    def add(self, handler):
        self.handlers.append(handler)
        return self
    
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    
    def fire(self, event_name, data, earg=None):
        for handler in self.handlers:
            handler(event_name, data, earg)
    
    __iadd__ = add
    __isub__ = remove
    __call__ = fire

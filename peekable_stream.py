
class PeekableStream:

    def __init__(self, iterator):
        self.iter = iterator 
        self.next = None
        self._fill()

    def _fill(self):
        try:
            self.next = next(self.iter)
        except StopIteration:
            self.next = None
            
    def peek(self):
        return self.next 

    def move_next(self):
        if self.next != None:
            self._fill() 

    def peek_and_move(self):
        val = self.peek()
        self.move_next()
        return val

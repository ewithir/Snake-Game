from tkinter import *

# Константы
WIDTH = 800
HEIGHT = 600
SEGMENT_SIZE = 20
IN_GAME = True

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x,
                                          y,
                                          x + SEGMENT_SIZE,
                                           y + SEGMENT_SIZE,
                                          fill="white")



class Snake(object):
    def __init__(self, segments):
        self.segments = segments

        self.mapping = {
            "Down" : (0,1),
            "Up" : (0, -1),
            "Right": (1,0),
            "Left": (-1,0)
        }


        self.vector = self.mapping['Right']

    def move(self):
        for i in range(len(self.segments) -1):
            segments = self.segments[i].instance

            x1, y1, x2, y2 = c.coords(self.segments[i + 1].instance)
            c.coords(segments, x1, y1, x2, y2)
            x1, y1, x2, y2 = c.coords(self.segments[-2].instance)

            c.coords(self.segments[-1].instance,
                     x1+ self.vector[0] * SEGMENT_SIZE,
                     y1+ self.vector[1] * SEGMENT_SIZE,
                     x1+ self.vector[0] * SEGMENT_SIZE,
                     y1+ self.vector[1] * SEGMENT_SIZE,)
def change_direction(self, event):
    if event.keysym in self.mapping:
        self.vector = self.mapping[event.keysym]
def add_segment(self):
    last_segment = c.coords(self.segments[0].instance)
    x = last_segment[2] - SEGMENT_SIZE
    y = last_segment[3] - SEGMENT_SIZE
    self.segments.insert(0, Segment(x, y))

root = Tk()

c = Canvas(root, width=WIDTH, height = HEIGHT, bg="#00a67c")
c.grid()

segments = [
    Segment(SEGMENT_SIZE, SEGMENT_SIZE),
    Segment(SEGMENT_SIZE*2, SEGMENT_SIZE),
    Segment(SEGMENT_SIZE*3, SEGMENT_SIZE),
]

s = Snake(segments)

c.focus_set()
root.mainloop()
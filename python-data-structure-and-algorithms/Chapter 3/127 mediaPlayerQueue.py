# -----------------------------------
# copy from --124 nodeQueue.py--
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def enqueue(self, data):
        node = Node(data)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        data = None
        if self.head:
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.count -= 1
        return data


# -----------------------------------

from random import randint


class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10)


import time

class MediaQueue(Queue):
    def __init__(self):
        super(MediaQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        while self.count > 0:
            track = self.dequeue()
            print(f'Now play {track.title}')
            time.sleep(track.length)

track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")
media_player = MediaQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()
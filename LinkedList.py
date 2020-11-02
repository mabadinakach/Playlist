class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def append(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

        if self.head is None:
            self.head = new_node
    
    def print_songs(self):
        current = self.head
        while current is not None:
            print(current.data["title"])
            current = current.next

    def print_whole(self):
        current = self.head
        while current is not None:
            print(f"{current.data['title']} - {current.data['artist']} - {current.data['genre']}")
            current = current.next
    
    def update(self, data, change):
        change = Node(change)
        data = Node(data)
        current = self.head
        while current is not None:
            if current.data["title"] == data.data:
                current.data = change.data
                break
            current = current.next

    def find(self, song):
        song = Node(song)
        current = self.head
        found = False
        while current != None:
            if current.data["title"] == song.data:
                print(f"Song {song.data} found")
                found = True
                break
            current = current.next
        if found is False:
            print(f"Song {song.data} not found")
        return found

    def delete_head(self):
        self.head = self.head.next

    def delete_tail(self):
        current = self.head
        previous = current
        while current.next != None:
            previous = current
            current = current.next
            self.tail = previous
        previous.next = None
        return current

    def delete(self, data):
        data = Node(data)
        current = self.head
        while current.next is not None:
            if current.next.data["title"] == data.data:
                current.next = current.next.next 
                break
            current = current.next
                
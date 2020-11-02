class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.previous = None
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def append(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
            new_node.previous = self.tail 
        self.tail = new_node

        if self.head is None:
            new_node.previous = None
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
        print()
    
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
                print(f"Song {song.data} found\n")
                found = True
                break
            current = current.next
        if found is False:
            print(f"Song {song.data} not found\n")
        return found

    def delete_head(self):
        self.head = self.head.next

    def delete_tail(self):
        # current_node = self.head
        # while current_node.next != self.tail:
        #     current_node = current_node.next
        # current_node.next = None
        
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

    #TODO: Hacer funcionar esto!!
    def reverse(self):
        current = self.tail
        temp = self.head
        self.head = current
        while current is not None:
            #current.previous = current.next
            current.next = current.previous
            current.previous = current

            current = current.next
        self.tail = temp
        #print(temp.data)
        if temp.next != None:
            temp.next.next = self.tail
        temp.next = None
        
                
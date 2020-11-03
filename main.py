#from LinkedList import LinkedList, Node
from DoublyLinkedList import DoublyLinkedList, Node

pl = DoublyLinkedList()

pl.append({
    "title":"In the Court of the Crimson King",
    "artist":"King Crimson",
    "genre":"Progressive Rock",
})

pl.append({
    "title":"On the Sea",
    "artist":"Beach House",
    "genre":"Space Rock",
})

pl.append({
    "title":"Any Colour You Like",
    "artist":"Pink Floyd",
    "genre":"Psychedelic Rock",
})

pl.append({
    "title":"Notion",
    "artist":"Tash Sultana",
    "genre":"Alternative Rock",
})

pl.append({ # TAIL
    "title":"How to Fly",
    "artist":"Sticky Fingers",
    "genre":"Alternative Rock",
})

pl.prepend({ # HEAD
    "title":"Jigsaw Falling Into Pieces",
    "artist":"Radiohead",
    "genre":"Experimental Rock",
})


pl.delete_head()
pl.delete_tail()
pl.find("How to Fly")
pl.delete("Notion")

pl.print_whole()
print("REVERSE:")
pl.reverse()
pl.print_whole()
pl.print_songs()
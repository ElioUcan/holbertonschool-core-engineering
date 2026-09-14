#!/usr/bin/env python3

class VerboseList(list):

    """A list that does not stop talking"""

    def append(self, item):
        super().append(item)
        print(f"Added {item} to list")

    def extend(self, x):
        super().extend(x)
        print(f"Extended the list with {x} items")
    def remove(self, item):
        super().remove(item)
        print(f"Removed {item} fron the list")

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {item} from the list")
        return super().pop(index)

verboselist = VerboseList()

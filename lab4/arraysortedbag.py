"""
Author: Tolu Bakare
File: arraysortedbag.py
"""

from arrays import Array

class ArraySortedBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArraySortedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
            if self.count(item) != other.count(item):
                return False
        return True

    def __contains__(self, other):
        """Binary searches for item in array. Returns True
        if other in self, False otherwise"""
        left = 0
        right = self._size
        while left <= right:
            midpoint = (left + right) // 2
            if other == self._items[midpoint]:
                return True
            elif other < self._items[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return False


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if self._size == len(self._items):
            self.resize(2)

        correct = 0
        while correct < self._size and self._items[correct] < item:
            correct += 1
                    
        for j in range(self._size, correct, -1):
            self._items[j] = self._items[j - 1]
            
        self._items[correct] = item
        self._size += 1
      

    def resize(self, sizeFactor):
        tempArray = Array(round(len(self._items) * sizeFactor))
        for i in range(self._size):
            tempArray[i] = self._items[i]        
        self._items = tempArray

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary
        sizeArray = self._size
        sizeBag = len(self._items)
        div = sizeArray/sizeBag
        booli = (len(self._items) * 0.5) >= 10
        if div <= 0.25 and booli:
            self.resize(0.5)

    def count(self, item):
        if not item in self:
            raise KeyError(str(item) + " not in bag")

        number = 0
        for oop in self:
            if oop == item:
                number += 1

        return number
        

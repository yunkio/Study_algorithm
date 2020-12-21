'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
'''
from typing import *


# 내 코드 - 6232ms (2%..)
class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.map = [ListNode(-1)] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        head = self.map[key % self.size]
        current = head.next
        while current:
            if current.key == key:
                break
            current = current.next
        else:
            current = ListNode(key)
            current.next = head.next
            head.next = current
        current.val = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        current = self.map[key % self.size].next
        while current:
            if current.key == key:
                break
            current = current.next
        else:
            return -1
        return current.val

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        current = self.map[key % self.size]
        while current and current.next:
            if current.next.key == key:
                break
            current = current.next
        else:
            return None
        current.next = current.next.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

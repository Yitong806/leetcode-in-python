from typing import Optional


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.current_capacity = 0
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.mapping.keys():
            return -1
        target_node = self.mapping[key]
        self.remove_a_node(target_node)

        self.add_node_in_tail(key, target_node.value)
        return target_node.value


    def put(self, key: int, value: int) -> None:
        if key in self.mapping.keys():
            target_node = self.mapping[key]
            self.remove_a_node(target_node)
            self.add_node_in_tail(key, value)
        else:
            # new key

            # full, drop the head one
            if self.current_capacity == self.capacity:
                self.drop_node_in_head()

            self.add_node_in_tail(key, value)


    def remove_a_node(self, current_node):

        prev = current_node.prev
        next = current_node.next
        if prev is not None:
            prev.next = next
        if next is not None:
            next.prev = prev
        if current_node is self.head:
            self.head = self.head.next
        if current_node is self.tail:
            self.tail = self.tail.prev
        current_node.prev = None
        current_node.next = None
        self.mapping.pop(current_node.key)
        self.current_capacity -= 1

    def add_node_in_tail(self, key, value):
        # assert that (key, value) does not appear in the mapping keys
        new_node = Node(key, value)
        if self.current_capacity == 0:
            self.head = self.tail = new_node
        else:
            current_tail = self.tail
            current_tail.next = new_node
            new_node.prev = current_tail
            self.tail = new_node
        self.current_capacity += 1
        self.mapping[key] = new_node

    def drop_node_in_head(self):
        if self.current_capacity == 0:
            return
        self.mapping.pop(self.head.key)
        if self.current_capacity == 1:
            self.head = self.tail = None
        else:
            current_head = self.head
            new_head = current_head.next
            self.head = new_head
            current_head.next = None
            new_head.prev = None
        self.current_capacity -= 1





if __name__ == '__main__':
    # ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    l = LRUCache(2)
    l.put(1, 1)
    l.put(2, 2)
    print(l.get(1))
    l.put(3, 3)
    print(l.get(2))
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
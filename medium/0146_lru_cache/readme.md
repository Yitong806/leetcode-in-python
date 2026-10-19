# 0146 LRU Cache

## Problem
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:
- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key` to the cache. If the number of keys exceeds the `capacity`, evict the least recently used key.

All operations must run in **O(1)** average time complexity.

1. `1 <= capacity <= 3000`
2. `0 <= key <= 10^4`
3. `0 <= value <= 10^5`
4. At most `2 * 10^5` calls will be made to `get` and `put`.

## Approach

### Hash Map + Doubly Linked List

The core idea is to combine two data structures so that both **lookup** and **reordering** are O(1):

- **Hash map** (`mapping`): maps `key` to its corresponding linked list node, enabling O(1) lookup.
- **Doubly linked list**: maintains items in order of usage. The head side represents most recently used; the tail side represents least recently used.

#### Why doubly linked list?
Unlike a singly linked list, a doubly linked list allows O(1) removal of any node (given a direct reference) because each node knows both its `prev` and `next` pointers. This is essential for moving a node to the "most recently used" position without traversal.

#### Operations

**`get(key)`**:
1. If `key` not in `mapping`, return `-1`.
2. Otherwise, retrieve the node from `mapping`.
3. Remove the node from its current position in the list.
4. Re-insert it at the tail (most recently used side).
5. Return the node's value.

**`put(key, value)`**:
- **Key exists**: remove the old node, then insert a new node with the updated value at the tail.
- **Key does not exist**:
  1. If the cache is at capacity, evict the head node (least recently used) — remove it from both the list and `mapping`.
  2. Create a new node and insert it at the tail.
  3. Add the mapping `key → node`.

#### Helper Methods

| Method | Responsibility |
|--------|---------------|
| `remove_a_node(node)` | Unlink `node` from the list, update `head`/`tail` if needed, remove from `mapping`, decrement `current_capacity` |
| `add_node_in_tail(key, value)` | Create a new node and append it to the tail; update `head`/`tail` for the first element; add to `mapping` |
| `drop_node_in_head()` | Remove the head node from the list and `mapping` (used when evicting) |

#### Edge Cases Handled
- Empty cache (`current_capacity == 0`): `head` and `tail` both point to `None`.
- Single-element cache (`current_capacity == 1`): removing the only node resets both `head` and `tail` to `None`.
- Removing the head or tail node: `head`/`tail` pointers are updated accordingly.

## Complexity
- **Time**: O(1) average for both `get` and `put`. Hash map operations are O(1); linked list insertion and removal at known positions are O(1).
- **Space**: O(capacity) — at most `capacity` nodes are stored in the hash map and linked list.
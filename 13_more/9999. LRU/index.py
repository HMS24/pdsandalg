"""Least Recently Used Cache

- [x] implement LRU Cache
- [ ] wrapper class

"""


class ListNode:
    
    def __init__(self, key=0, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.total_items_in_cache = 0
        self.hash_table = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # 從 hash table get，沒有就 return None
        try:
            node = self.hash_table[key]
        except:
            return None

        # move that item to front
        self._move_to_head(node)
        
        return node.val

    def put(self, key, value):
        # 存在
            # update value
            # move to head
        if key in self.hash_table:
            node = self.hash_table[key]
            node.val = value

            self._move_to_head(node)
            
            return
        
        # 不存在
            # create node
            # inert to head and self.total_items_in_cache+=1
            # is over capacity
                # yes
                    # remove entry and self.total_items_in_cache-=1
        node = ListNode(key, value)
        self._add_to_front(node)
        self.hash_table[key] = node
        self.total_items_in_cache += 1

        if self._is_over_max_capacity():
            self._remove_tail()

    @staticmethod
    def _remove_from_list(node):
        saved_prev = node.prev
        saved_next = node.next

        saved_prev.next = saved_next
        saved_next.prev = saved_prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node):
        self._remove_from_list(node)
        self._add_to_front(node)

    def _is_over_max_capacity(self):
        return self.total_items_in_cache > self.max_capacity

    def _remove_tail(self):
        tail_node = self.tail.prev
        self._remove_from_list(tail_node)
        del self.hash_table[tail_node.key]

        self.total_items_in_cache -= 1

cache = LRUCache(5)
cache.put(1, "Hello")
cache.put(2, "Hello again")
cache.put(3, "Hello again again")
cache.put(4, "Hello again again again")

print(cache.get(5))
print(cache.tail.prev)
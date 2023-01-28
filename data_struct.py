from collections import deque
import pprint


string_hello = "Hello \n \t world!!!"
integer_num = 7896
float_num = 2349.234
is_somebool = False

manyline_string = """
sdfgsdfgsdf 
sdfge
sdfghfsrt
erws """
# or
# manyline_string = ("wertewrt"
# "sdrf"
# "sdfgh")
print(manyline_string)

byte_num = 0b1000101
print(byte_num)

byte_string = hex(byte_num)
print(byte_string)

char_from_chcode = chr(byte_num)
print(char_from_chcode)

# e - умножить на 10 в степени n
# -e - умножить на 10 в степени -n
exsp_num = 6.02214076e23
print(exsp_num)

people = ["Tom", "Sam", None, True, 1]
print(people)

people.append("Alice")
people.insert(1, "Bill")
people.extend(["Mike", "Sam"])
index_of_tom = people.index("Tom")
removed_item = people.pop(index_of_tom)
last_item = people.pop()
people.remove("Alice")
print(people)

const_people = tuple(people)

people.clear()
print(people)

print(const_people)

# ranger numbers
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")

user_dict = {
    "tom@gmail.com": "Tom",
    "id": 0,
    "specialization": "coder",
    "people": False,
    "hobby": "drawing"}
print(user_dict)
for param in user_dict:
    print(f"Parameter: {param}; Value: {user_dict[param]}")
print(user_dict.get("hobby", "unknown"))
print(user_dict.pop("hobby", "unknown") + ' delete')  # delete hobby and print hobby
print(user_dict.get("hobby", "unknown"))
words = [word for word in user_dict]
user_dict.clear()
print(words)
# sets
users = {"Tom", "Bob", "Alice", "Tom"}
users2 = {"Sam", "Kate", "Bob"}
print(users)  # without tom number 2
users3 = users.union(users2)
print(users3)
print(users & users2)
print(users ^ users2)

const_users = frozenset({"Tom", "Bob", "Alice"})

# очередь
# Initializing a queue
queue = deque()
# Adding elements to a queue
queue.append('r')
queue.append('e')
queue.append('i')
print(queue)
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print("\nQueue after removing elements")
print(queue)\



# связный список
class NodeList:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None


list1 = SLinkedList()
list1.headval = NodeList("Mon")
e2 = NodeList("Tue")
e3 = NodeList("Wed")
# Link first Node to second node
list1.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3


# бинарное дерево

class NodeTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data) -> None:  # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = NodeTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = NodeTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self) -> None:  # Print the tree
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


# Use the insert method to add nodes
tree = NodeTree(12)
tree.insert(6)
tree.insert(14)
tree.insert(3)
tree.PrintTree()


# граф
# Create the dictionary with graph elements
graph = {'a': ['b', 'c'],
         'b': ['a', 'd'],
         'c': ['a', 'd'],
         'd': ['e'],
         'e': ['d']}
print(graph)


# хеш-таблицы
class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        for key, value in elements:  # calculates the hash of each key
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size  # positions the element in the bucket using hash
            self.buckets[index].append((key, value))  # adds a tuple in the bucket

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return (value)

        return None

    def __str__(self):
        return pprint.pformat(self.buckets)  # pformat returns a printable representation of the object


capitals = [
    ('France', 'Paris'),
    ('United States', 'Washington D.C.'),
    ('Italy', 'Rome'),
    ('Canada', 'Ottawa')
]
hashtable = Hashtable(capitals)
print(hashtable)
print(f"The capital of Italy is {hashtable.get_value('Italy')}")

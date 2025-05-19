class request:
    def __init__(self, id=0, name="", priority=0):
        self.id = id
        self.name = name
        self.priority = priority


class bst_node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.base = None

    def insert(self, id, name):
        def insert_node(node, id, name):
            if node is None:
                return bst_node(id, name)
            if id < node.id:
                node.left = insert_node(node.left, id, name)
            elif id > node.id:
                node.right = insert_node(node.right, id, name)
            return node

        self.base = insert_node(self.base, id, name)

    def search(self, id):
        def search_node(node, id):
            if node is None or node.id == id:
                return node
            if id < node.id:
                return search_node(node.left, id)
            else:
                return search_node(node.right, id)

        return search_node(self.base, id) is not None

    def remove(self, id):
        def find_min(node):
            while node and node.left:
                node = node.left
            return node

        def remove_node(node, id):
            if node is None:
                return node
            if id < node.id:
                node.left = remove_node(node.left, id)
            elif id > node.id:
                node.right = remove_node(node.right, id)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                x = find_min(node.right)
                node.id = x.id
                node.name = x.name
                node.right = remove_node(node.right, x.id)
            return node

        self.base = remove_node(self.base, id)

    def print_preorder(self):
        def preorder(node):
            if node is None:
                return
            print("ID:", node.id, ", Name:", node.name)
            preorder(node.left)
            preorder(node.right)

        print("\nBST (Pre-Order):")
        preorder(self.base)

    def is_empty(self):
        return self.base is None

    def size(self):
        def count(node):
            if node is None:
                return 0
            return 1 + count(node.left) + count(node.right)

        return count(self.base)


class max_heap:
    def __init__(self):
        self._heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heap_up(self, i):
        while i > 0 and self._heap[self.parent(i)].priority < self._heap[i].priority:
            self._heap[i], self._heap[self.parent(i)] = self._heap[self.parent(i)], self._heap[i]
            i = self.parent(i)

    def heap_down(self, i):
        big = i
        l = self.left(i)
        r = self.right(i)

        if l < len(self._heap) and self._heap[l].priority > self._heap[big].priority:
            big = l
        if r < len(self._heap) and self._heap[r].priority > self._heap[big].priority:
            big = r
        if big != i:
            self._heap[i], self._heap[big] = self._heap[big], self._heap[i]
            self.heap_down(big)

    def insert(self, id, priority):
        newrequest = request(id, "", priority)
        self._heap.append(newrequest)
        self.heap_up(len(self._heap) - 1)

    def max(self):
        if not self._heap:
            return request()
        max_item = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self.heap_down(0)
        return max_item

    def print_heap(self):
        print("\nHeap (Level Order):")
        for item in self._heap:
            print("ID:", item.id, ", Priority:", item.priority)

    def change_priority(self, id, new_priority):
        for i in range(len(self._heap)):
            if self._heap[i].id == id:
                if new_priority > self._heap[i].priority:
                    self._heap[i].priority = new_priority
                    self.heap_up(i)
                    print("Priority increased.")
                return
        print("Request not found in heap.")

    def remove(self, id):
        for i in range(len(self._heap)):
            if self._heap[i].id == id:
                self._heap[i] = self._heap[-1]
                self._heap.pop()
                self.heap_down(i)
                return True
        return False

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)


class manager:
    def __init__(self):
        self.bst = bst()
        self.heap = max_heap()

    def insert(self, id, name, priority):
        self.bst.insert(id, name)
        self.heap.insert(id, priority)

    def delete(self, id):
        if self.bst.search(id):
            self.bst.remove(id)
            self.heap.remove(id)
            print("Request deleted.")
        else:
            print("Request not found.")

    def search(self, id):
        if self.bst.search(id):
            print("Request found in BST.")
        else:
            print("Request not found.")

    def process_highest_priority(self):
        if self.heap.is_empty():
            print("No request to process.")
            return
        top = self.heap.max()
        self.bst.remove(top.id)
        print("Processed request with ID:", top.id, "and priority:", top.priority)

    def change_priority(self, id, new_priority):
        self.heap.change_priority(id, new_priority)

    def print_bst(self):
        self.bst.print_preorder()

    def print_heap(self):
        self.heap.print_heap()

    def size_info(self):
        print("BST size:", self.bst.size(), ", Heap size:", self.heap.size())

    def empty_info(self):
        print("BST is", "empty" if self.bst.is_empty() else "not empty",
              ", Heap is", "empty" if self.heap.is_empty() else "not empty")

manager = manager()

while True:
    print("\n------ Request Management System ------")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Highest priority")
    print("5. Increase priority")
    print("6. Print BST")
    print("7. Print Heap")
    print("8. Size info")
    print("9. Empty check")
    print("0. Exit")

    choice = input("Choice: ")

    if choice == "0":
        break

    if choice in ["1", "2", "3", "5"]:
        try:
            id = int(input("Enter ID: "))
        except ValueError:
            print("Invalid ID.")
            continue

    if choice == "1":
        name = input("Enter Name: ")
        try:
            priority = int(input("Enter Priority: "))
        except ValueError:
            print("Invalid Priority.")
            continue
        manager.insert(id, name, priority)

    elif choice == "2":
        manager.delete(id)

    elif choice == "3":
        manager.search(id)

    elif choice == "4":
        manager.process_highest_priority()

    elif choice == "5":
        try:
            new_priority = int(input("Enter new priority: "))
        except ValueError:
            print("Invalid priority.")
            continue
        manager.change_priority(id, new_priority)

    elif choice == "6":
        manager.print_bst()

    elif choice == "7":
        manager.print_heap()

    elif choice == "8":
        manager.size_info()

    elif choice == "9":
        manager.empty_info()

    else:
        print("Invalid choice.")

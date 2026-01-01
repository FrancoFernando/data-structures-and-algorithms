class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None
    
    def is_leaf(self):
        return self.left is None and self.right is None
    
    def is_root(self):
        return self.parent is None
    
    def is_left_child(self):
        return self.parent is not None and self.parent.left == self
    
    def is_right_child(self):
        return self.parent is not None and self.parent.right == self


class Treap:
    def __init__(self):
        self.root = None
    
    def _set_left(self, parent, child):
        """Helper to set left child and update parent reference."""
        parent.left = child
        if child is not None:
            child.parent = parent
    
    def _set_right(self, parent, child):
        """Helper to set right child and update parent reference."""
        parent.right = child
        if child is not None:
            child.parent = parent
    
    def _right_rotate(self, x):
        """
        Performs a right rotation on node x.
        
            y                x
           / \              / \
          x   T3    -->   T1   y
         / \                  / \
        T1  T2              T2  T3
        
        Returns the new root of the subtree (x).
        """
        if x is None or x.parent is None:
            raise ValueError("Cannot rotate root or None node")
        
        y = x.parent
        if y.left != x:
            raise ValueError("Node must be left child for right rotation")
        
        p = y.parent
        
        # Update grandparent's reference
        if p is not None:
            if p.left == y:
                self._set_left(p, x)
            else:
                self._set_right(p, x)
        else:
            self.root = x
            x.parent = None
        
        # Perform rotation
        self._set_left(y, x.right)
        self._set_right(x, y)
        
        return x
    
    def _left_rotate(self, x):
        """
        Performs a left rotation on node x.
        
          y                  x
         / \                / \
        T1  x      -->     y   T3
           / \            / \
          T2  T3        T1  T2
        
        Returns the new root of the subtree (x).
        """
        if x is None or x.parent is None:
            raise ValueError("Cannot rotate root or None node")
        
        y = x.parent
        if y.right != x:
            raise ValueError("Node must be right child for left rotation")
        
        p = y.parent
        
        # Update grandparent's reference
        if p is not None:
            if p.left == y:
                self._set_left(p, x)
            else:
                self._set_right(p, x)
        else:
            self.root = x
            x.parent = None
        
        # Perform rotation
        self._set_right(y, x.left)
        self._set_left(x, y)
        
        return x
    
    def search(self, key):
        """Search for a key in the treap."""
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None
    
    def _search_with_priority(self, key, priority):
        """Search for a node with both matching key and priority."""
        node = self.root
        while node is not None:
            if key == node.key and priority == node.priority:
                return node
            elif key <= node.key:
                node = node.left
            else:
                node = node.right
        return None
    
    def insert(self, key, priority):
        """Insert a new key-priority pair into the treap."""
        new_node = Node(key, priority)
        
        # Step 1: Find the correct position and insert as a leaf (BST insertion)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        parent = None
        
        while current is not None:
            parent = current
            if key <= current.key:
                current = current.left
            else:
                current = current.right
        
        # Attach the new node to its parent
        if key <= parent.key:
            self._set_left(parent, new_node)
        else:
            self._set_right(parent, new_node)
        
        # Step 2: Bubble up to restore heap property
        self._bubble_up(new_node)
    
    def _bubble_up(self, node):
        """Bubble up a node until heap property is restored."""
        while node.parent is not None and node.priority < node.parent.priority:
            if node.is_left_child():
                self._right_rotate(node)
            else:
                self._left_rotate(node)
        
        # Update root if node bubbled all the way up
        if node.parent is None:
            self.root = node
    
    def delete(self, key, priority):
        """Remove an entry with the given key and priority from the treap."""
        # Step 1: Find the node to delete
        node = self._search_with_priority(key, priority)
        if node is None:
            return False
        
        # Step 2: Push down to leaf
        self._push_down_to_leaf(node)
        
        # Step 3: Disconnect the leaf
        if node.parent is not None:
            if node.is_left_child():
                self._set_left(node.parent, None)
            else:
                self._set_right(node.parent, None)
        else:
            self.root = None
        
        return True
    
    def _push_down_to_leaf(self, node):
        """Push a node down until it becomes a leaf."""
        while not node.is_leaf():
            # Choose which child to rotate up
            if node.right is None:
                # Only left child exists
                self._right_rotate(node.left)
            elif node.left is None:
                # Only right child exists
                self._left_rotate(node.right)
            else:
                # Both children exist, choose the one with higher priority
                if node.left.priority < node.right.priority:
                    self._right_rotate(node.left)
                else:
                    self._left_rotate(node.right)
    
    def peek(self):
        """Return the highest priority entry without removing it."""
        if self.root is None:
            return None
        return (self.root.key, self.root.priority)
    
    def min_key(self):
        """Return the minimum key in the treap."""
        if self.root is None:
            return None
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key
    
    def max_key(self):
        """Return the maximum key in the treap."""
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key
    
    def is_empty(self):
        """Check if the treap is empty."""
        return self.root is None
    
    def _inorder_traversal(self, node, result):
        """Helper method for inorder traversal."""
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.priority))
            self._inorder_traversal(node.right, result)
    
    def inorder(self):
        """Return all entries in sorted order by key."""
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _check_bst_invariant(self, node, min_key=None, max_key=None):
        """Check if BST invariant is satisfied."""
        if node is None:
            return True
        
        if min_key is not None and node.key < min_key:
            return False
        if max_key is not None and node.key > max_key:
            return False
        
        return (self._check_bst_invariant(node.left, min_key, node.key) and
                self._check_bst_invariant(node.right, node.key, max_key))
    
    def _check_heap_invariant(self, node):
        """Check if heap invariant is satisfied."""
        if node is None:
            return True
        
        if node.left is not None and node.left.priority < node.priority:
            return False
        if node.right is not None and node.right.priority < node.priority:
            return False
        
        return (self._check_heap_invariant(node.left) and
                self._check_heap_invariant(node.right))
    
    def verify_invariants(self):
        """Verify both BST and heap invariants."""
        return (self._check_bst_invariant(self.root) and
                self._check_heap_invariant(self.root))


# Test the implementation
if __name__ == "__main__":
    print("Testing Treap Implementation\n")
    
    # Create a treap and insert some tasks
    treap = Treap()
    
    tasks = [
        ("bug-1247", 77),
        ("feature-auth", 10),
        ("refactor-db", 55),
        ("docs-api", 95),
        ("test-ui", 32),
        ("clean-backlog", 76),
        ("erp", 89),
        ("schedule-call", 56)
    ]
    
    print("Inserting tasks:")
    for key, priority in tasks:
        print(f"  {key}: {priority}")
        treap.insert(key, priority)
    
    print("\nVerifying invariants:", treap.verify_invariants())
    
    print("\nTasks in sorted order (by key):")
    for key, priority in treap.inorder():
        print(f"  {key}: {priority}")
    
    print("\nHighest priority task:", treap.peek())
    print("Min key:", treap.min_key())
    print("Max key:", treap.max_key())
    
    print("\nSearching for 'test-ui':", treap.search("test-ui") is not None)
    print("Searching for 'nonexistent':", treap.search("nonexistent") is not None)
    
    print("\nDeleting 'refactor-db' (priority 55)...")
    treap.delete("refactor-db", 55)
    print("Verifying invariants:", treap.verify_invariants())
    
    print("\nTasks after deletion:")
    for key, priority in treap.inorder():
        print(f"  {key}: {priority}")
    
    print("\nNew highest priority task:", treap.peek())

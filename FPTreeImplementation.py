class TreeNode:
    def __init__(self, name, count, parent):
        self.name = name
        self.count = count
        self.parent = parent
        self.children = {}
        self.link = None

    def increment(self, count):
        self.count += count

class FPTree:
    def __init__(self, transactions, min_sup):
        self.root = TreeNode('root', 1, None)
        self.header = {}
        self.min_sup = min_sup
        self.build_tree(transactions)

    def build_tree(self, transactions):
        # First pass: count item frequency and filter based on min_sup
        item_count = {}
        for transaction in transactions:
            for item in transaction:
                item_count[item] = item_count.get(item, 0) + 1

        # Remove items not meeting min_sup
        item_count = {item: count for item, count in item_count.items() if count >= self.min_sup}

        # Create header table for linking similar items
        for item in item_count:
            self.header[item] = None

        # Second pass: build the tree
        for transaction in transactions:
            # Filter and sort items by frequency
            sorted_items = sorted([item for item in transaction if item in item_count], key=lambda x: (-item_count[x], x))
            self._insert_tree(sorted_items, self.root)

    def _insert_tree(self, items, node):
        if items:
            first_item = items[0]
            next_node = node.children.get(first_item)
            if not next_node:
                next_node = TreeNode(first_item, 0, node)
                node.children[first_item] = next_node
                # Link it to header table
                if self.header[first_item] is None:
                    self.header[first_item] = next_node
                else:
                    current = self.header[first_item]
                    while current.link:
                        current = current.link
                    current.link = next_node
            next_node.increment(1)
            self._insert_tree(items[1:], next_node)

    def mine_tree(self):
        def mine_node(path, node):
            """ Recursively mine the tree """
            if node.name is not None:
                new_pattern = path + [node.name]
                yield (new_pattern, node.count)
            for child in node.children.values():
                yield from mine_node(new_pattern, child)

        # Start mining from the root node
        itemsets = []
        for itemset, count in mine_node([], self.root):
            itemsets.append((itemset, count))
        return itemsets

# Example usage:
transactions = [['bread', 'milk'], ['bread', 'diaper', 'beer', 'eggs'], ['milk', 'diaper', 'bread', 'beer'], ['milk', 'diaper', 'bread']]
fp_tree = FPTree(transactions, min_sup=2)
frequent_itemsets = fp_tree.mine_tree()
print(frequent_itemsets)

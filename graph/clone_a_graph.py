"""Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:



Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]"""

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        OldtoNew = {}

        def dfs(node):
            if node in OldtoNew:
                return OldtoNew[node]
            copy = Node(node.val)
            OldtoNew[node]=copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)


# Set up neighbors (undirected graph)
node1.neighbors = [node2]
node2.neighbors = [node1, node3]
node3.neighbors = [node2]

def print_graph(node):
    from collections import deque
    visited = set()
    queue = deque([node])
    result = []
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        result.append((current.val, [n.val for n in current.neighbors]))
        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
    return result

# Clone the graph
solution = Solution()
cloned_graph = solution.cloneGraph(node1)

# Print both original and cloned graphs
print("Original Graph:", print_graph(node1))
print("Cloned Graph:", print_graph(cloned_graph))
'''
Problem Statement: Given A Graph, Build A New One With Reversed Edges

Given a strongly connected directed graph containing n nodes, you have to build a new graph containing n nodes where edges are reversed than the original graph.

This is also called Transposing the graph.

Input Format:
-------------
There is only one argument pointing to a random node of the graph.

Output Format:
--------------
Return any node in the new graph.

As input is a strongly connected graph, you will be able to visit all the nodes, given any random node.

Also when we reverse all the edges of strongly connected graph it will remain strongly connected graph, hence returning any one node is sufficient. 

Constraints:
------------
- 1 <= n <= 315
- Given graph is strongly connected.
- Given graph does not contain multi edges (there will not be more than one edge connecting same pair of vertices in the same direction) and self loops. 
- Each node contains distinct values. 
- 1 <= value stored in node <= n
- You are not allowed to modify the given graph. Return completely new graph. 

> Sample Test Case:

Sample Input:
-------------
Any node of the graph where:
For n = 3
nodes = [1 2 3]
edges = [(1 -> 2), (2 -> 3), (3 -> 1)]

you could be given any node (1, 2 or 3) as input.

Sample Output:
--------------
Any node of the new graph where:
For n = 3
nodes = [1 2 3]
edges = [(2 -> 1), (3 -> 2), (1 -> 3)]

you could return any node as output.

'''

class Node:
    def __init__(self):
        self.val = 0
        self.neighbours = []

def build_other_graph(node):
    # creating empty dictionary
    transpose_graph = {}
    # dfs function to traverse graph with argument given node nad transpose_graph as input
    dfs(node, transpose_graph)
    return transpose_graph[1]
    
def dfs(node, transpose_graph):
    # creating the temperory node with Node class attribute
    temp_node = Node()
    # adding the given node value to temperory node value
    temp_node.val = node.val
    # storing the temp_node into a key(node.val) of the new transpose_graph
    # so transpose_graph[node.val] is node in new graph
    transpose_graph[node.val] = temp_node
    #print(transpose_graph[node.val].val,temp_node.val)
    
    # we loop for the neighbours of given node
    for neighbour in node.neighbours:
        # if the neighbours value(node, according to defination above) not present in graph 
        if neighbour.val not in transpose_graph:
            # then we call DFS)
            dfs(neighbour, transpose_graph)
        # Now we add neighbours(transpose_graph[node.val]) to node (transpose_graph[neighbour.val])
        transpose_graph[neighbour.val].neighbours.append(transpose_graph[node.val])


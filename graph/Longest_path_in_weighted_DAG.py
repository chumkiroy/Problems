'''
Problem Statement: Longest path in a weighted Directed-acyclic-graph

Given a weighted DAG (directed acyclic graph), where weight of an edge denotes the length of that edge.

Nodes in the graph are numbered from 1 to dag_nodes, where dag_nodes denotes the total number of nodes in the graph.

Also, you are given a node from_node and a node to_node. You have to find longest path from from_node to to_node in the given graph. 

Input Format:
-------------
There are six arguments.

First one is an integer dag_nodes, second one is an array dag_from, third one is an array dag_to and forth one is an array dag_weight. These four arguments cumulatively describes the weighted DAG. dag_nodes describes the total number of nodes in the given graph and there is an edge from dag_from[i] node to dag_to[i] node with length dag_weight[i].

Fifth argument is from_node and sixth argument is to_node.  

Output Format:
--------------
Return an array describing longest path from from_node to to_node.
There can be multiple longest paths, so you are free to return any of them. 

Constraints:
------------
- Given graph is a valid weighted DAG.
- Given graph does not contain multi edges (there will not be more than one edge connecting same pair of vertices). 
- to_node is reachable from from_node.
- 1 <= dag_nodes <= 450
- 1 <= dag_from[i], dag_to[i], from_node, to_node <= dag_nodes
- 1 <= dag_weight[i] <= 2 * 10^9
- Total number of edges in graph <= (dag_nodes * (dag_nodes - 1)) / 2

Sample Test Case:
-----------------
Sample Input:

dag_nodes = 4
dag_from = [1 1 1 3]
dag_to = [2 3 4 4]
dag_weight = [2 2 4 3]
from_node = 1
to_node = 4

Sample Output: [1 3 4]

Explanation:
------------
Total there are two paths from node 1 to node 4.
1) 1 -> 4 with length 4.
2) 1 -> 3 -> 4 with length 2 + 3 = 5.

So, Longest path from node 1 to node 4 is [1 3 4] with length 5.

Notes:
Time: 30 min
When from_node = to_node, path contains only one node, so output should be [from_node] containing only one node. 

It can be helpful to first store edges node wise and then use it.

Something like this:

vector<vector<pair<int, int>>> node_wise_edges(dag_nodes + 1, vector<pair<int, int>>(0));

for (int i = 0; i < dag_edges; i++)
{
    node_wise_edges[dag_from[i]].push_back({dag_to[i], dag_weight[i]});
}
Now we have all the outgoing edges from node i in vector node_wise_edges[i]. And it will be easier to use. 
'''

#	For the weighted graph:
#	1. The number of nodes is <name>_nodes.
#	2. The number of edges is <name>_edges.
#	3. An edge exists between <name>_from[i] to <name>_to[i] and the weight of the edge is <name>_weight[i].
#
def construct_adj_list(dag_from, dag_to, dag_weight):
    adj_list = {}
    #adj_list = {vertex:[(neighbour, weight)]}
    for i in range(len(dag_weight)):
        vertex = dag_from[i]
        neighbour = dag_to[i]
        weight = dag_weight[i]
        if vertex not in adj_list:
            adj_list[vertex] = [(neighbour, weight)]
        else:
            adj_list[vertex].append((neighbour, weight))
        if neighbour not in adj_list:
            adj_list[neighbour] = []
    return adj_list

def dfs(vertex, to_node, adj_list, cache):
    if vertex in cache:
        return cache[vertex]
    if vertex == to_node:
        cache[to_node] = (0, [to_node])
        return cache[to_node]
    maxVal = -1
    maxPath = []
    for pair in adj_list[vertex]:
        neighbour = pair[0]
        weight = pair[1]
        n_val, n_path = dfs(neighbour, to_node, adj_list, cache)
        if n_val == -1:
            continue
        if (n_val + weight) >= maxVal:
            maxVal = n_val + weight
            maxPath = [vertex] + n_path
    cache[vertex] = (maxVal, maxPath)
    return cache[vertex]

def find_longest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node):
    if from_node == to_node:
        return [to_node]
    adj_list = construct_adj_list(dag_from, dag_to, dag_weight)
    cache = {}
    return dfs(from_node, to_node, adj_list, cache)[1]

dag_nodes = 4
dag_from = [1, 1, 1, 3]
dag_to = [2, 3, 4, 4]
dag_weight = [2, 2, 4, 3]
from_node = 1
to_node = 4

print find_longest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node)

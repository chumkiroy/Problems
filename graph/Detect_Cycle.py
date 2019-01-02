'''
Problem Statement: Detect Cycle in a Directed Graph

You are given Directed Graph G. You need to find out whether at least one cycle exist in the graph or not.

Input Format:
-------------
Three arguments for function, N, M and 2D Array of size M*2 where N denotes number of vertices and M denotes number of directed edges and 2D array of size M*2 represent M directed edges.

For array of size M*2, each row will represent directed edge, where value in column 1 and column 2 will be index (0-based) of starting vertex and ending vertex respectively of that directed edge.

Output Format:
--------------
Return boolean true if at least one cycle exist in graph else boolean false.

Constraints:
------------
- 2 <= N <= 100000
- 1 <= M <= 100000
- Indexing of vertices starting from 0.
- No multiple edges i.e. if an edge is present which is directed from vertex u to vertex v, then no other edge will present which is directed from vertex u to vertex v.
- Graph can have multiple components.

Sample Test Case:
------------------
Sample Input: N = 5, M = 7, edges = [[0,1],[0,3],[1,3],[1,2],[2,3],[4,0],[2,4]]
Sample Output: true

Explanation:
------------
Graph formed from 5 vertices and given 7 directed edges have 1 cycle (0 --> 1 --> 2 --> 4 --> 0) So, Output will be true.

'''

def isCycle(graph):
    visited = set()
    path = [object()]
    path_set = set(path)
    stack = [iter(graph)]
    while stack:
        for v in stack[-1]:
            if v in path_set:
                return True
            elif v not in visited:
                visited.add(v)
                path.append(v)
                path_set.add(v)
                stack.append(iter(graph.get(v, ())))
                break
        else:
            path_set.remove(path.pop())
            stack.pop()
    return False

def hasCycle(N, M, edges):
    g = {}
    for i in range(N):
        g[i] = []
        
    for i in range(M):
        src = edges[i][0]
        dst = edges[i][1]
        if src == dst:
            return True
        g[src].append(dst)
        temp = g[dst]
        if src in temp:
            return True

    if isCycle(g) == True:
        return True
    return False

N = 5
M = 7
edges = [[0,1],[0,3],[1,3],[1,2],[2,3],[4,0],[2,4]]
print hasCycle(N, M, edges)

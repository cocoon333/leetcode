"""
5702. Find Center of Star Graph

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
"""

class Solution:
    def findCenter(self, edges):
        s = set() 
        for edge in edges:
            for node in edge:
                len_s = len(s)
                s.add(node)
                if len(s) == len_s:
                    return node

if __name__ == "__main__":
    s = Solution()
    assert(s.findCenter([[1,2],[2,3],[4,2]]) == 2)
    assert(s.findCenter([[1,2],[5,1],[1,3],[1,4]]) == 1)
    assert(s.findCenter([[5,2],[1,5],[5,3]]) == 5)

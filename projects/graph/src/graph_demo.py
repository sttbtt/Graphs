#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph

    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_edge('0', '1')
    # graph.add_edge('0', '3')

    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_directed_edge('5', '3')
    graph.add_directed_edge('6', '3')
    graph.add_directed_edge('7', '1')
    graph.add_directed_edge('4', '7')
    graph.add_directed_edge('1', '2')
    graph.add_directed_edge('7', '6')
    graph.add_directed_edge('2', '4')
    graph.add_directed_edge('3', '5')
    graph.add_directed_edge('2', '3')
    graph.add_directed_edge('4', '6')
 
    # graph.add_directed_edge('1', '2')
    # graph.add_directed_edge('1', '3')
    # graph.add_directed_edge('2', '4')
    # graph.add_directed_edge('2', '5')
    # graph.add_directed_edge('3', '5')
    # graph.add_directed_edge('4', '6')
    # graph.add_directed_edge('5', '6')
    # graph.add_directed_edge('6', '7')
    
    print(f'Graph Vertices: {graph.vertices}')
    print('Breadth-First Traversal:')
    graph.bft('1')
    print('Depth-First Traversal:')
    graph.dft('1')
    print('Depth-First Recursion First:')
    print(graph.dft_r_brady('1'))
    print('Depth-First Recursion Second:')
    print(graph.dft_r_brady('2'))
    print('Breadth-First Path:')
    print(graph.bfs_brady('1', '6'))
    print('Depth-First Path:')
    print(graph.dfs_brady('1', '6'))

if __name__ == '__main__':
    # TODO - parse argv
    main()

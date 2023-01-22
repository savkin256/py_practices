import copy


def depth_first_search(graph, start, visited):
    visited_int = copy.deepcopy(visited)
    visited_int.append(start)
    for v in graph[start]:
        if v not in visited_int:
            visited_int = depth_first_search(graph, v, visited_int)
    return visited_int


def breadth_first_search(graph, start, visited):
    queue = [start]
    visited_int = copy.deepcopy(visited)
    visited_int.append(start)
    while len(queue) > 0:
        for v in graph[queue[0]]:
            if v not in visited_int:
                queue.append(v)
                visited_int.append(v)
        queue.pop(0)
    return visited_int


def main():
    initial_position = '0'
    already_visited = []
    tree = {
        '0': set(['1', '2']),
        '1': set(['0', '3', '4']),
        '2': set(['0', '4', '5', '8']),
        '3': set(['1', '7']),
        '4': set(['1', '2']),
        '5': set(['2', '6', '7']),
        '6': set(['5']),
        '7': set(['3', '5']),
        '8': set(['2'])
    }

    print("GRAPH = ", tree)
    print("VISITED by DFS = ", depth_first_search(tree, initial_position, already_visited))
    print("VISITED by BFS = ", breadth_first_search(tree, initial_position, already_visited))


if __name__ == '__main__':
    main()

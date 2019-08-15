import sys


def earliest_ancestor(ancestors, starting_node):
    # take an array of ancestors,
    # ancestor is a tuple with (x, y) x pointing to y

    # step 1: build the graph
    # our graph is going to be represented by an adjacency list
    graph = {}

    def connect_node(graph, ancestors):
        parent, child = ancestors
        if not graph.get(child, None):
            graph[child] = [parent]
        else:
            graph[child].append(parent)

    for pair in ancestors:
        connect_node(graph, pair)

    # step 2: search the graph starting at the given node

    def dft(graph, start):
        stack = []
        visited = set()
        stack.append([start])
        longest = []

        while len(stack) > 0:
            path = stack.pop()
            current = path[-1]

            if current not in visited:
                if len(path) >= len(longest):
                    longest = path

                for parent in graph.get(current, []):
                    stack.append(path + [parent])

        return longest[-1] if len(longest) > 1 else -1

    return dft(graph, starting_node)


if __name__ == "__main__":

    start = 1

    if len(sys.argv) > 1:
        start = int(sys.argv[1])

    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, start))

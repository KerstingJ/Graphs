
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def island_counter(islands):
    graph = {}

    for col in range(len(islands)):
        for row in range(len(islands[col])):
            if not islands[col][row] == 0:
                con = []
                if col > 0:
                    if islands[col-1][row] != 0:
                        con.append((col-1, row))
                if col < len(islands) - 1:
                    if islands[col+1][row] != 0:
                        con.append((col+1, row))
                if row > 0:
                    if islands[col][row - 1] != 0:
                        con.append((col, row - 1))
                if row < len(islands[col]) - 1:
                    if islands[col][row + 1] != 0:
                        con.append((col, row + 1))

                graph[(col, row)] = con

    visited = set()
    count = 0

    for col in range(len(islands)):
        for row in range(len(islands[col])):
            # tuple(col, row)
            if graph.get((col, row), None) and tuple([col, row]) not in visited:
                print((col, row))
                count += 1

                q = []
                q.append((col, row))

                while len(q) > 0:
                    vertex = q.pop(0)

                    if vertex not in visited:
                        visited.add(vertex)

                        for neighbor in graph[vertex]:
                            if neighbor not in visited:
                                q.append(neighbor)

    return count


print(island_counter(islands))

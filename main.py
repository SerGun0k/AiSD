from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    distances = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                distances[neighbor] = distances[node] + 1
                visited.add(neighbor)  # Помечаем вершину как посещенную только здесь

    return distances


def read_graph_from_file(file_name):
    graph = defaultdict(list)
    with open(file_name, 'r') as file:
        for i, line in enumerate(file):
            if i == 0:
                continue  # Пропускаем первую строку
            neighbors = list(map(int, line.strip().split()))
            graph[i] = neighbors
    return graph

def write_distances_to_file(distances, file_name):
    with open(file_name, 'w') as file:
        for node, distance in distances.items():
            file.write(f"Shortest distance to node {node}: {distance}\n")

if __name__ == "__main__":
    file_name = "input_graph.txt"  # Имя файла с данными
    start_node = 1  # Заданная вершина

    graph = read_graph_from_file(file_name)
    distances = bfs(graph, start_node)
    write_distances_to_file(distances, "output_distances.txt")  # Имя файла для записи результатов

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
                visited.add(neighbor)

    return distances

def read_graph_from_file(file_name):
    graph = defaultdict(list)
    try:
        with open(file_name, 'r') as file:
            for i, line in enumerate(file):
                if i == 0:
                    continue  # Пропускаем первую строку
                neighbors = list(map(int, line.strip().split()))
                graph[i] = neighbors
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
    return graph

def find_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = bfs(graph, node)
            visited.update(component.keys())
            components.append(list(component.keys()))

    return components

def write_distances_to_file(distances, file_name):
    with open(file_name, 'w') as file:
        for node, distance in distances.items():
            file.write(f"Кратчайшее расстояние до вершины {node}: {distance}\n")

if __name__ == "__main__":
    file_name = "input_graph.txt"  # Имя файла с данными

    graph = read_graph_from_file(file_name)
    if graph:
        connected_components = find_connected_components(graph)

        print("Количество компонент связности:", len(connected_components))
        print("Состав компонент связности:")
        for i, component in enumerate(connected_components, 1):
            print(f"Компонента {i}: {component}")

        start_node = 1  # Заданная вершина
        distances = bfs(graph, start_node)
        if distances:
            write_distances_to_file(distances, "output_distances.txt")  # Имя файла для записи результатов
            print("Результаты записаны в файл output_distances.txt")
        else:
            print(f"Из вершины {start_node} недостижимы другие вершины в графе.")

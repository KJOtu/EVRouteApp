import csv
import heapq


def load_graph_from_csv(file_path):
    graph = {}
    charging_stations = ['H', 'K', 'Q', 'T']
    
    with open(file_path, mode='r') as infile:
        reader = csv.reader(infile)
        next(reader)  
        for rows in reader:
            source, target, distance = rows
            distance = int(distance)
            if source not in graph:
                graph[source] = {}
            if target not in graph:
                graph[target] = {}
            graph[source][target] = distance
            graph[target][source] = distance  
    
    return graph, charging_stations


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


def recommend_station(shortest_paths, charging_stations):
    recommended_station = min(charging_stations, key=lambda station: shortest_paths[station])
    return recommended_station, shortest_paths[recommended_station]


def main():
    file_path = 'C:/Users/yourpath/graph_data.csv' 
    graph, charging_stations = load_graph_from_csv(file_path)
    start_node = 'A'
    
    shortest_paths = dijkstra(graph, start_node)
    
    recommended_station, distance = recommend_station(shortest_paths, charging_stations)
    
    print(f"The most efficient route is to the charging station at {recommended_station}, distance: {distance}")

if __name__ == "__main__":
    main()

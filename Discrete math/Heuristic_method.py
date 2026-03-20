import random

def read_graph(filename):
    vertices = []
    edges = []

    with open(filename, 'r') as f:
        mode = None

        for line in f:
            line = line.strip()
            if not line:
                continue

            if line == "V":
                mode = "vertices"
                continue
            if line == "E":
                mode = "edges"
                continue

            if mode == "vertices":
                vertices.append(line.replace("(", "").replace(")", ""))
            elif mode == "edges":
                parts = line.split("-")
                u = parts[0].replace("(", "").replace(")", "")
                v = parts[1].replace("(", "").replace(")", "")
                w = int(parts[2])
                edges.append((u, v, w))

    return vertices, edges

def cut_value(partition, edges):
    cut = 0
    for u, v, w in edges:
        if partition[u] != partition[v]:
            cut += w
    return cut

def max_cut(vertices, edges, max_iterations=1000):
   
    partition = {v: random.randint(0, 1) for v in vertices}
    best_cut = cut_value(partition, edges)

    for _ in range(max_iterations):
        improved = False
        for v in vertices:
            partition[v] ^= 1  
            new_cut = cut_value(partition, edges)
            if new_cut > best_cut:
                best_cut = new_cut
                improved = True
            else:
                partition[v] ^= 1  
        if not improved:
            break

    groupA = {v for v in vertices if partition[v] == 1}
    groupB = set(vertices) - groupA
    return best_cut, (groupA, groupB)

def main():
    filename = "graph.txt"
    vertices, edges = read_graph(filename)

    best_cut, best_partition = max_cut(vertices, edges)

    print("Maximum Cut Value:", best_cut)
    print("Group A:", best_partition[0])
    print("Group B:", best_partition[1])

if __name__ == "__main__":
    main()
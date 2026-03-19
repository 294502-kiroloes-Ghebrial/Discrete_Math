def read_graph(file_name):
    vertices = []
    edges = []
    mode = None

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line == "V":
                mode = "verts"
                continue
            if line == "E":
                mode = "edges"
                continue

            if mode == "verts":
                vertices.append(line.replace("(", "").replace(")", ""))
            elif mode == "edges":
                u, v, w = line.replace("(", "").replace(")", "").split("-")
                edges.append((u, v, int(w)))

    return vertices, edges


def cut_value(A, B, edges):
    total = 0
    for u, v, w in edges:
        if (u in A and v in B) or (u in B and v in A):
            total += w
    return total


def max_cut(vertices, edges):
    n = len(vertices)
    best_val = 0
    best_partition = None

    for mask in range(1 << n):
        A = {vertices[i] for i in range(n) if mask & (1 << i)}
        B = set(vertices) - A
        val = cut_value(A, B, edges)
        if val > best_val:
            best_val = val
            best_partition = (A, B)

    return best_val, best_partition


def main():
    vertices, edges = read_graph("graph.txt")
    best_val, partition = max_cut(vertices, edges)
    print("Max-Cut Value:", best_val)
    print("Partition A:", partition[0])
    print("Partition B:", partition[1])


if __name__ == "__main__":
    main()
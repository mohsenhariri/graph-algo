import subprocess
import random
from datetime import datetime


def graph(vertices: int):
    graph = []
    for i in range(vertices):
        rnd_lst = random.sample(range(0, 30), vertices - 1)
        rnd_lst.insert(i, 0)
        graph.append(rnd_lst)
    return graph


def export_DOT(graph) -> None:
    vertices = len(graph)
    gv_str = "digraph {\n"
    for i in range(vertices):
        for j in range(vertices):
            if i != j:
                gv_str = gv_str + f'V{i} -> V{j} [label="{graph[i][j]}",weight="{graph[i][j]}"];\n'

    gv_str += "}"

    with open("graph.gv", "w") as f:
        f.write(gv_str)


def export_DOT_stream_digraph(graph) -> None:
    vertices = len(graph)
    with open("graph.gv", "w") as f:
        f.write("digraph {\n")
        for i in range(vertices):
            for j in range(vertices):
                value = graph[i][j]
                if i != j and value != 0:
                    f.write(f'V{i} -> V{j} [label="{value}",weight="{value}"];\n')
        f.write("}")


colors = ["orange", "pink", "yellow", "brown", "violet", "brown"]
# colors = {"orange","pink","yellow","brown","violet","red"}


def export_DOT_stream(graph) -> None:
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    penwidth = 3.0
    vertices = len(graph)
    with open(f"graph-{current_time}.gv", "w") as f:
        f.write("graph {\n")
        for i in range(vertices):
            for j in range(vertices):
                color = random.choice(colors)
                value = graph[i][j]
                if i != j and value != 0:
                    f.write(f'V{i} -- V{j} [label="{value}",weight="{value}", color="{color}",penwidth={penwidth}];\n')
        f.write("}")
    result = subprocess.run(["dot", "-Tsvg", "graph.gv"], capture_output=True)
    with open(f"graph-{current_time}.svg", "wb") as f:
        f.write(result.stdout)

    # print(result.stdout)


g = graph(5)
# export_DOT(graph)
export_DOT_stream(g)
print(g)

#  matrix to adjacency list
# for i in range(len(graph)):
#     for j in range(len(graph)):

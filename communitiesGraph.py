import csv
import networkx as nx
import matplotlib.pyplot as plt

# Opening the txt file which contains communities
# Choose your file by renaming it in 'open()"
with open("commu2015.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lst = []
    for row in csv_reader:
        lst.append(row)
    print(lst)


# Let's construct the community graph
G = nx.Graph()
lst.remove(lst[0])

for i in range(len(lst)):
    if len(lst[i]) == 1:  # Only one person a community : it is removed from the graph
        # G.add_nodes_from(lst[i])
        lst[:] = [lst[i] for lst[i] in lst]
    else:  # community is more than 1 person :
        cont = len(lst[i])
        for j in range(cont):
            for k in range(cont-1, j, -1):
                # print(lst[i][j])
                G.add_node(lst[i][j])
                # print("{" + str(lst[i][j]) + ";" + str(lst[i][k]) + "}")
                G.add_edge(lst[i][j], lst[i][k])
        # print(j)
        # print(cont)


# Write the graph in GML format for use in Gephi
# Rename as you wish
nx.write_gml(G, "Communities2015.GML")


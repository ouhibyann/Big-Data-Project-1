import networkx as nx
import csv

G = nx.read_gml("Graph_of_Names.GML")

# Using Girvan_newman algorithm to find communities
communities = nx.algorithms.community.centrality.girvan_newman(G)
file = 'commu.txt'
commu = open(file, 'w+')
with open(file, 'w') as fp:
    csv.register_dialect("custom", delimiter=";")
    writer = csv.writer(fp, dialect="custom")
    for tup in communities:
        writer.writerow(tup)


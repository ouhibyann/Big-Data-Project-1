import networkx as nx
import csv

print("Enter the name file with .GML extension")
file_Name = str(input()) # file_Name of the graph on which we'll apply the algo
G = nx.read_gml(file_Name)

# Using Girvan_newman algorithm to find communities
communities = nx.algorithms.community.centrality.girvan_newman(G)
file = 'commu.txt'
commu = open(file, 'w+')
with open(file, 'w') as fp:
    csv.register_dialect("custom", delimiter=";")
    writer = csv.writer(fp, dialect="custom")
    for tup in communities:
        writer.writerow(tup)
    # need correction because the for never stop

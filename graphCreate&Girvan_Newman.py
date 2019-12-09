import csv
import re
import itertools
import networkx as nx
import matplotlib.pyplot as plt


# Used to read the CSV file
with open('savedrecs_2015_Names.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    file1 = open("Nodes_clean.txt", "w+")
    for row in csv_reader:
        # print(row)
        for i in row:
            if i != '' and i != '\t':
                file1.write(i)
        file1.write('\n')
        line_count += 1
    print("Number of articles : " + str(line_count))
    file1.close()

    # This part extracts all the first name letters
    file2 = open("Nodes_clean.txt", 'r')
    lst_Full_Name = []
    for row in file2:
        match3 = re.findall("[a-zA-Z-_]+, [a-zA-Z] |[a-zA-Z-_]+, [a-zA-Z]", row)
        lst_Full_Name.append(match3)
    print(lst_Full_Name)
    file2.close()

    # List containing full names without ','
    lst_Name_corrected = []
    for i in range(len(lst_Full_Name)):
        lst_Name_corrected.append([])
        for j in range(len(lst_Full_Name[i])):
            corrected = lst_Full_Name[i][j].replace(',', '')
            # print(lst_Name[i])
            lst_Name_corrected[i].append(corrected)
        # print(lst_Name_corrected)
    lst_Full_Name = lst_Name_corrected
    # Proper full name list with contributions kept
    # Calculation number of nodes
    nb_nodes = 0
    for i in range(len(lst_Full_Name)):
        nb_nodes = nb_nodes + len(lst_Full_Name[i])
    print("Number of nodes : " + str(nb_nodes))

# Let's construct the graph
G = nx.Graph()

for i in range(len(lst_Full_Name)):
    # Only one person wrote the article :
    if len(lst_Full_Name[i]) == 1:
        G.add_nodes_from(lst_Full_Name[i])
    # Article is written by more than 1 person :
    else:
        G.add_nodes_from(lst_Full_Name[i])
        cont = len(lst_Full_Name[i])
        for j in range(cont):
            for k in range(cont-1, j, -1):
                print("{" + str(lst_Full_Name[i][j]) + ";" + str(lst_Full_Name[i][k]) + "}")
                G.add_edge(lst_Full_Name[i][j], lst_Full_Name[i][k])
        print(j)
        print(cont)


# Write G in GML format for use in Gephi
nx.write_gml(G, "Graph_of_Names.GML")

# Using Girvan_newman algorithm to find communities
'''communities = nx.algorithms.community.centrality.girvan_newman(G)
for communities in itertools.islice(communities, 5):
    print(communities)'''


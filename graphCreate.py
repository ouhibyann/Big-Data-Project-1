import csv
import re
from itertools import chain
import networkx as nx
import matplotlib.pyplot as plt


# Used to read the CSV file
with open('savedrecs-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    file1 = open("Nodes_clean.txt", "w+")
    for row in csv_reader:
        #print(row)
        for i in row:
            if i != '' and i != '\t':
                file1.write(i)
        file1.write('\n')
        line_count += 1
    print("Number of articles : " + str(line_count))
    file1.close()

    #This part extracts all the first name letters
    file2 = open("Nodes_clean.txt", 'r')
    lst_Full_Name = []
    for row in file2:
        match3 = re.findall("[a-zA-Z-_]+, [a-zA-Z] |[a-zA-Z-_]+, [a-zA-Z]", row)
        lst_Full_Name.append(match3)
    #print(lst_Full_Name)
    '''making full Name a multiple list to 1D list
    #Can be deleted if one wants to keep contributions
    #lst_Full_Name = list(chain.from_iterable(lst_Full_Name))
    #print(lst_Full_Name)'''
    file2.close()

    #List containing full names without ','
    lst_Name_corrected = []
    for i in range(len(lst_Full_Name)):
        lst_Name_corrected.append([])
        for j in range(len(lst_Full_Name[i])):
            corrected = lst_Full_Name[i][j].replace(',', '')
            #print(lst_Name[i])
            lst_Name_corrected[i].append(corrected)
        #print(lst_Name_corrected)
    lst_Full_Name = lst_Name_corrected
    #Proper full name list with contributions kept
    #Calculation number of nodes
    nb_nodes = 0
    for i in range(len(lst_Full_Name)):
        nb_nodes = nb_nodes + len(lst_Full_Name[i])
    print("Number of nodes : " + str(nb_nodes))

#Let's construct the graph
G = nx.Graph()

'''for i in range(len(lst_Full_Name)): #Considering each authors from an article as a node + all edges between them
    for j in range(len(lst_Full_Name[i])):
        G.add_node(lst_Full_Name[i][j])
    print(nx.info(G))

nx.draw(G)
plt.draw()
plt.show()'''


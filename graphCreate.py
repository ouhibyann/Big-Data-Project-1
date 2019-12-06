import csv
import re
import igraph

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
    print("Number of nodes is : " + str(line_count))
    file1.close()

    #This part extracts all the first name letters
    #In order to latter obtain a single list with the author name associated with first name
    file2 = open("Nodes_clean.txt", 'r')
    lst_First_Name = []
    count = 0
    for row in file2:
        #lst_First_Name.append([])
        match = re.findall(" [a-zA-Z] | [a-zA-Z]", row)
        lst_First_Name.append(match)
        count += 1
    print(lst_First_Name)


import csv
import re
import igraph

# Used to read the CSV file
with open('savedrecs-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    lst_Full_Name = []
    file1 = open("Nodes_clean.txt", "w+")
    for row in csv_reader:
        lst_Full_Name.append([])
        print(row)
        for i in row:
            if i != '' and i != '\t':
                file1.write(i)
                # The type of Name + first name is as followed :
                full_Name = re.match("[a-zA-Z0-9_], [a-zA-Z0-9_]", i)
                lst_Full_Name[line_count].append(full_Name)
        file1.write('\n')
        line_count += 1
    print("Number of nodes is : " + str(line_count))

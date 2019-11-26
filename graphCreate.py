import csv

# Used to read the CSV file
with open('savedrecs-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    file1 = open("Nodes_clean.txt", "w+")
    for row in csv_reader:
        print(row)
        for i in row:
            if i != '' and i != '\t':
                file1.write(i)
        file1.write('\n')

        line_count += 1

    print("Number of nodes is : " + str(line_count))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
rowCount = 3
columnCount = 4
maxLens = []
# for i in range(rowCount):
#    maxLens.append(max([len(string) for string in tableData[i]]))
maxLens = map(lambda table_data_string: max([len(string) for string in table_data_string]),
              [tableData[i] for i in range(rowCount)])

for i in range(columnCount):
    for j in range(rowCount):
        print tableData[j][i].rjust(maxLens[j]) + '  ',
    print

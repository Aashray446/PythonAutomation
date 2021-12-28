def printTable(table):
    width = [0] * len(table)
    count = 0
    for lst in table:
        max_len = 0
        for i in range(0, len(lst)):
            if(len(lst[i]) > max_len):
                max_len = len(lst[i])
        width[count] = max_len
        count += 1
        
    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(width[item]), end=' ')
        print()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

printTable(table_data)

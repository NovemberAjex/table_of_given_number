table_input = int(input("Please enter the no:  "))
table_upper_range = int(input("Please write the upper range:  "))
table_lower_range = int(input("Please write the lower range:  "))
for table in range(table_lower_range,table_upper_range+1):
    y = table_input*table
    print(y)
import marina.marinalib as m

# column
column = m.init()

# string constants for testing
test: str = "first"
test1: str = "first1"
test2: str = "first2"
all_tests = [test, test1, test2]

# just inserts the entire `all_tests` list
for i in range(len(all_tests)):
    m.Insert(column, all_tests[i])
    
# exports to csv and prints
m.ExportCSV("../marina", column)
m.Print(column)
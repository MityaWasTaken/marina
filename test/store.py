import sys

# sys import because file is in paralell directory
sys.path.append("../marina")
import ll as l

column = l.LinkedList()

# inserts data into the database
column.Insert("hello")

# searches for the data just added
searchData = column.Search("hello")
if searchData == True:
    print("exists")
else:
    print("does not exist")
    

# prints the data to prove that the search was correct
column.Print()
## marina
### a low latency in-memory database
-------------------------------------------
```
import marina.marinalib as m

# instantiate the column
column = m.init()

# string constants for testing
test: str = "first"

m.Insert(column, test)
m.Print(column)

# export as a csv
m.ExportCSV("../path", column)
```

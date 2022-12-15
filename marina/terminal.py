# for working with marina through the terminal

import sql.parse as p
import ll as l


linkedlist = l.LinkedList()

while True:
    data = str(input("QueryMarina -> "))
    
    parsed = p.Parser(data)

    if parsed == "P":
        linkedlist.Print()
    
    elif parsed != "P" and str(parsed).islower():
        linkedlist.Remove(str(parsed).lower())
        
        
    elif parsed != "P" and str(parsed).isupper() == True:
        linkedlist.Insert(str(parsed).lower())
    
    elif parsed != "P" and parsed.istitle() == True:
        searchData = linkedlist.Search(str(parsed).lower())

        print(searchData)
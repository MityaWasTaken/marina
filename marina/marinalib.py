# marinalib; library for using marina to work in python files

import marina.ll as l
import os
import random

def randomCode():
    l = []

    for i in range(5):
        number = random.randint(1, 9)
        l.append(str(number))
    return "".join(l)

def init():
    linkedlist = l.LinkedList()
    return linkedlist

def Print(linkedlist):
    linkedlist.Print()
    
def Insert(linkedlist, data):
    linkedlist.Insert(data)

def Remove(linkedlist, data):
    linkedlist.Remove(data)
    
def Search(linkedlist, data):
    search = linkedlist.Search(data)
    return search

def ExportCSV(directory, linkedlist):
    llobj = l.LinkedList()
    rc = randomCode()
    os.system("cd ~; cd {}; touch {}.csv".format(directory, rc))
    
    with open("{}/{}.csv".format(directory, rc), "a") as f:
        f.write("{}\n".format(linkedlist.convertArray()))
from __future__ import print_function
import sys
import csv
import uuid

#references
#uuid -> http://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/
#

class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse):
        print("This is {0}.".format(self.name))
        self.deposit(warehouse)
        print("Thank you, come again!")

    def deposit(self, warehouse):

        f = open('./tasks.txt', 'r')
        try:
            reader = csv.reader(f)
            my_list = list(reader)
            for row in my_list:

                print("   ")
                if(row[0] == 'd'):
                    print("Stored books:", warehouse.list_contents())

                elif(row[0] == 'a'):
                    row.append("not loan")

                    print("Adding book info..")
                    row.insert(1,uuid.uuid1().time)
                    AddingB=warehouse.store(row)
                    print("Book ID:" , AddingB[1])
                    #print(x)
                elif(row[0] == 'sy'):
                    print("Books with the specified age:")
                    for name in warehouse.list_contents():
                        if(name[5] > row[1] and name[5] < row[2]):
                            print (name)

                elif(row[0] == 'si'):
                  print("Display books with specified ISBN:")
                  for name in warehouse.list_contents():
                      if(name[3] == row[1]):
                          print(name)

                elif(row[0] == 'ol'):
                  for name in warehouse.list_contents():
                     if(name[3] == row[1]):
                         name[6] = 'on loan'
                         print("Unavailable:",name)

                elif(row[0] == 'nol'):
                  for name in warehouse.list_contents():
                     if(name[3] == row[1]):
                         name[6] = 'not on loan'
                         print("Available:",name)

        finally:
            f.close()
            # if item:
            #     warehouse.store(self.name, item)

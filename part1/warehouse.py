#Pyro daemon server, listens for remote method calls, dispatch them to the appropriate object
# and return results to the caller

from __future__ import print_function
import Pyro4

@Pyro4.expose
class Warehouse(object):
    def __init__(self):
        self.contents =  []

    def list_contents(self):
        return self.contents
        

    def store(self, name):
        self.contents.append(name)
        #print(name)
        return name


def main():
    warehouse = Warehouse()
    Pyro4.Daemon.serveSimple(
        {
            warehouse: "example.warehouse"
        },
        ns=True)


if __name__ == "__main__":
    main()

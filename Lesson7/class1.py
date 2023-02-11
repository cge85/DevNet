class Router:
    #Router Class
    def __init__(self, model, swversion, ip_addr):
        #initialize values
        self.model = model
        self.swversion = swversion
        self.ip_addr =ip_addr

    def getdesc(self):
        #return a formated description of the router
        desc = f"Router Model             :{self.model}\n"\
               f"Software Version         :{self.swversion}\n"\
               f"Router Management Address:{self.ip_addr}"
        return desc

#This is how you create a class switch with inheretance of the router class in order to re-use the same attributes.
class Switch(Router):
    def getdesc(self):
        #return a formated description of the router
        desc = f"Switch Model             :{self.model}\n"\
               f"Software Version         :{self.swversion}\n"\
               f"Switch Management Address:{self.ip_addr}"
        return desc

#Here is where the route and switch objects are created
rtr1 = Router("iosV", "15.6.7", "10.100.100.1")
rtr2 = Router("isr4221", "16.9.5", "10.10.100.5")
sw1 = Switch("Cat9300", "15.10.0","192.168.10.10")

#print out the router and switch objects with descriptions
print("Rtr1\n", rtr1.getdesc(), sep="")
print("Rtr2\n", rtr2.getdesc(), sep="")
print("Sw1\n", sw1.getdesc(), sep="")
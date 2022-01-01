#Plane class
class Plane:
   
    #Initializer 
    def __init__(self,model,manufacturer,fuel):
        self.model = model
        self.manufacturer = manufacturer
        self.fuel = fuel
    
    #Str method
    def __str__(self):
        return '{}, {} :: {} / 100'.format(self.model,self.manufacturer,self.fuel)
   
    #Representation
    def __repr__(self):
        return '{}, {} :: {} / 100'.format(self.model,self.manufacturer,self.fuel)
    #Equals operator   
    def __eq__(self,other):
        if self.model == other.model:
            if self.manufacturer == other.manufacturer:
                return True
        return False
   
    #Checks if fuel is empty
    def is_empty(self):
            if self.fuel == 0:
                return True
            return False
    
    #Refuels the planes by a certain amount
    def refuel(self,amount):
        '''Will only refuel if amount is > 0 and will not make
        fuel go over capacity'''
        if amount + self.fuel > 100:
            raise PlaneError('unable to refuel by {}'.format(amount))
        elif amount < 0:
            raise PlaneError('unable to refuel by {}'.format(amount))
        else:
            self.fuel += amount

class Hangar:
    
    #Initializer
    def __init__(self,name):
        self.name = name
        self.planes = []
    
    #Str method
    def __str__(self):
        str = ''
        for i in self.planes:
            str += '\t' + i.__str__() + '\n'
        return '{}:\n{}'.format(self.name,str)
    
    #Equal method
    def __eq__(self,other):
        #Checks if list lengths are the same
        if len(self.planes) != len(other.planes):
            return False
        else:
            #Only returns true if planes are in exact order
            for i in range(len(self.planes)):
                if self.planes[i] != other.planes[i]:
                    return False
        return True
    
    #Add plane method
    def add_plane(self,plane):
    #Declars that no errors have been made
        Error = False
        #If plane is duplicate raises error
        for i in self.planes:
            if plane == i  and plane.fuel == i.fuel:
                raise PlaneError('duplicate plane \'{}:{}\''.format(i.model,
i.manufacturer))
                Error = True
        #Appends plane if no error made
        if Error == False:
            self.planes.append(plane)
    
    #Searches planes based on their model
    def plane_by_model(self,model):
    #Checks each plane in the list
        for i in self.planes:
        #If the model matches the requested the plane is returned
            if i.model == model:
                return i
        #If no plane is found an exception is raised
        raise PlaneError('no plane found with model \'{}\''.format(model))
    
    #Creates a new list of all planes by a company
    def planes_by_manufacturer(self,company):
        #Stores planes
        holder = []
        #Searches each item in the planes 
        for i in self.planes:
        #If the plane manufacturer matches the company it is added to the list
            if i.manufacturer == company:
                holder.append(i)
        #If the list is empty after the loop an exception is raised
        if holder == []:
            raise PlaneError('no planes built by \'{}\''.format(company))
        else:
            return holder
    
    #Checks amount of planes that are out of fuel        
    def total_empty(self):
    #Declares a count to keep track of empty planes
        count = 0
        #Runs is empty method for each plane in list
        for i in self.planes:
        #Increments count if planes are emptu
            if i.is_empty() == True:
                count +=1
        return count
    
    #Refuels all elligible planes
    def refuel_all(self, amount):
    	#Attempts to refuel all planes in list using refuel method
        for i in self.planes:
            try:
                i.refuel(amount)
            except:
                pass
    
    
class PlaneError(Exception):
    
    #Initializer
    def __init__(self,msg): 
        self.msg = msg
    
    #String method
    def __str__(self):
        return self.msg

class Timetable:
                  
   
    
    def __init__(self, name, hour, minutes):
     
         
        self.name = name 
        self.hour = hour
        self.minutes = minutes
    

First = Timetable("Piątnica", 23, 59)
Second = Timetable("Czajnikowo", 12, 20)
Thrid = Timetable("Kamczatka", 10, 15)

print('Rozkład jazdy:')
print ("autobus do:",Thrid.name,"o godzine:", Thrid.hour,":", Thrid.minutes)


class buss:
       
    
    def __init__(self, buss, number):
        self.buss = buss
        self.number = number
        
Bus = buss("Dzienny", 11)
Bus = buss("Nocny", 12)  

print("Bus:")
print(Bus.buss, Bus.number)     


class Passanger:
       
    
    def __init__(self, ok, discount):
        self.ok = ok
        self.discount = discount
   
    
Senior = Passanger("Senior", '70%')
Student = Passanger("Student", '53%')
Disabled = Passanger("Niepełnosprawny", '90%')
Regular = Passanger("Regular", '100%')

print("Ulgi:")
print (Senior.ok, Senior.discount)

class Ticket:
       
    
    def __init__(self, tk, price):
        self.tk = tk
        self.price = price
        
Price1 = ('7$')
Price2 = ('5,3$')
Price3 = ('9$')  
Price4 = ('10$')    
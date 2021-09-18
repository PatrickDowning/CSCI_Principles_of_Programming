from datetime import datetime
#This class is used to define contact name and telephone number
class Contact():
    #these are the attributes of the class
    def __init__(self,contactName,teleNum):
        self.contactName= contactName
        self.teleNum= teleNum
    #these are the two getters for the class
    def get_name(self):
        return self.contactName
    def get_phone(self):
        return self.teleNum   
    #This is the toString for the contact class
    def toString(self):
        return 'Person name is: '+str(self.contactName)+'. Person number is: '+ str(self.teleNum)+"." 

#this is the Event abstract class 
class Event:
    #attribute of Contact class
    def __init__(self,x,date):
        self.x =x
        self.date = date
    #This is the toString for the contact class
    def toString(self):
        return str(self.x.toString()) + 'this is the date: '+ str(self.date)
        
#This is the appointment class, it allows you to set a type for appointments
class Appointment(Event):
    #these are the attributes of the class
    def __init__(self, x, date, typ):
        super().__init__(x,date)
        self.typ=typ
    #type getter for appointment
    def get_type(self):
        return(self.typ)
    #This is the toString for the appointment class
    def toString(self):
        return 'The type of appointment is'+ str(self.typ) +str(self.x.toString()) + 'this is the date: '+ str(self.date)


#This class adds list of attendes to an Event
class Meeting(Event):
    # List to keep track of attendes,decided to put list here rather than _init_
    meeting_list =[]
    #these are the attributes of the class
    def __init__(self,x,date):
        super().__init__(x,date)
    #method that adds attende
    def addAttende(self,attende):
        self.meeting_list.append(attende)
    #getter for attendes
    def get_attende(self):
        return self.meeting_list
    #This is the toString for the meeting class
    def toString(self):
        return str(self.x.toString()) + 'this is the date: '+ str(self.date)

#This class allows you to keep track of your appointment
class appointmentBook:
    def __init__(self,ist):
        self.ist = ist
    #add event while making sure no time conflicts
    #Tiime/dates string must be in the order of (month date @ timepm/am)
    def add_event(self,event):
            for x in self.ist:
                if x.date == event.date:
                    return
            self.ist.append(event)

    #This was an extra method i used to test case some aome arguments
    def call_list(self, lis_t):
        for x in lis_t:
            a= x
            print(a.toString())
    #This class seperates date from time and then 
    def get_event_for_date(self,time):
        empt= []
        for x in self.ist:
            b = x.date.split(" @")
            empt.append(b)
        for x in empt:
            if time in x:
                return x



#tests for methods
def main():
   #setting up contacts
   a0= Contact('pat',1603458660)
   a1=Contact('James',2323232323)
   a2=Contact('Jamie',1441441444)
   
   #Setting up events, events date string have to be in the format of(month date @ timepm/am) since i used the split method to seperate
   c0= Event(a0,'Octobet 12 @5pm')
   c1= Event(a1,'Octobet 18 @5pm')
   c2= Event(a2,'Septembert 18 @6pm')
   #Have to initil a list for appointmentBook
   h=[]
   j=[]
   k=[]
   L=[]
   b0= appointmentBook(h)
   b1=appointmentBook(j)
   b2=appointmentBook(k) 
   b3=appointmentBook(L) 
   #check to see if two same dates work
   b0.add_event(c1)
   b0.add_event(c1)
   b0.add_event(c0)
   b0.call_list(b0.ist)
   print('Test 1')
   #check to see if different dates work
   b1.add_event(c1)
   b1.call_list(b1.ist)
   print('Test 2')
   b2.add_event(c2)
   b2.add_event(c1)
   b2.call_list(b2.ist)
   print('Test 3')
    #checks parameters for get_event_for_date
   print(b3.get_event_for_date('7pm'))
   print(b0.get_event_for_date("5pm"))
   print(b2.get_event_for_date("6pm"))
if __name__ == "__main__":
    main()
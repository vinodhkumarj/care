
# coding: utf-8

# # create class 

# In[ ]:


class caretaker:

    
        def __init__(self,name,age,salary,job,review,rating,noofAdults,no_ofCaretakers):
            
            self.name=name
            self.age=age 
            self.salary=salary 
            self.job=job 
            self.review=review 
            self.rating=rating 
            self.Adults=noofAdults
            self.Ncaretakers=no_ofCaretakers

        def showName(self):
            print("Name: ",self.name)
        def showAge(self): 
            print("Age: ",self.age)

        def showSalary(self):
            print("salary: ",self.salary)
        def showJob(self):
            print("job: ",self.job)

        def showReview(self):
            print("reviews: ",self.review)

        def showRating(self):
            print("rating: ",self.rating)
        def showAdults(self):
            print( "No. of Adults:	",self.Adults) 
        def showNcaretakers(self):
            print("No. of caretakers working:",self.Ncaretakers) 
obj1=caretaker('Raju','30','5000','caretaker','good caretaker','4','2','20')
obj1.showName()
obj1.showAge()
obj1.showSalary() 
obj1.showJob() 
obj1.showReview()
obj1.showRating() 
obj1.showAdults() 
obj1.showNcaretakers()


# # create class

# In[ ]:


class elder:
    def __init__(self,name,salary,review,rating):
        self.name=name
        self.salary=salary
        self.review=review
        self.rating=rating
        
    def showName(self):
        print( "Name: ",self.name)
    
    def showSalary(self):
        print("salary:",self.salary)
        
    def showReview(self):
        print("review:",self.review)
        
    def showRating(self):
        print("rating:",self.rating)
obj=elder('Ramaiah','55','Raju','Healthy','5') 
obj.showName()
obj.showAge()
obj.showCaretakerName()
obj.showReview()
obj.showRating()


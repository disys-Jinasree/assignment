class res:
    def __init__(self):
        print("welcome to swiggy")
     
hotel=[{"honame":"1.A2B"," dish":"briyani","  price":200},
        {"honame":"2.akshayam"," dish":"shake","  price":190},             
        {"honame":"3.buhari"," dish":"aloogobi","  price":100},            
        {"honame":"4.sangeet"," dish":"pannergobi","  price":170},
        {"honame":"5.hampa"," dish":"aloomatar","  price":180},
        {"honame":"6.nasi"," dish":"aloomethi","  price":150},
        {"honame":"7.bay6"," dish":"alootikki","  price":120},
        {"honame":"8.dank"," dish":"hotdogs","  price":720},
        {"honame":"9.libraryblu"," dish":"wintersquash","  price":920},
        {"honame":"10.vasanthabhavan"," dish":"frenchfries","  price":220},
        {"honame":"11.hotelInn"," dish":"macroni","  price":220},
        {"honame":"12.chemistry"," dish":"pasta","  price":220},
        {"honame":"13.bobnmarley"," dish":"pizza","  price":120},
        {"honame":"14.seashells"," dish":"sizzler","  price":120},
        {"honame":"15.hawaiifood"," dish":"fishfo","  price":120},
        {"honame":"16.palmshore"," dish":"manchurian","  price":120},
        {"honame":"17.copperkitchen"," dish":"cheesepizza","  price":120},
        {"honame":"18.redbox"," dish":"fries","  price":120},
        {"honame":"19.nakshatra"," dish":"sambaridly","  price":120},
        {"honame":"20.coffeday"," dish":"cappucino","  price":120},
        {"honame":"21.mcdonalds"," dish":"milkshake","  price":120},
        {"honame":"22.hotelstar"," dish":"dosa","  price":120}]





for i in hotel:
    for j,k in i.items():
        print(f"{j}={k}")

class swiggy:

    def __init__(self,num):
        self.num=num
        
    
       
    def hotell(self):
        for i in hotel:
            if i["honame"]==self.num:
                print(i)
                for j in i:
                    print(j)
                    
    def dishname(self):
        self.dishname=input("enter the dish")
        for i in hotel:
            if i["dish"]==self.dishname:
                print(i)

    def payment(self):
        self.pay=int(input("enter pay"))
        for i in hotel:
            if i["price"]==self.pay:
                print("your payment is successful")
            else:
                raise ValueError("your payment is failed")
            






food=input("enter a hotel: ") 
ob=swiggy(food)
ob.hotell()
ob.dishname()
ob.payment()











            
'''    
        for i in range (0,hotel):
         
            if(hotel[i].honame==self.input):
             
                for j in range (0, hotel[i].dishes.length):
                 
                    print (hotel[i].dishes[j].dishname,hotel[i].dishes[j].price)
                 
    def __init__(self,dish,price):
        self.dishh = dish
        self.cost = price
        
        
    def order_summary(self):
        print("details",self.dishh,self.cost)


class payment(swiggy):
    def __init__(self):
        self.bill_amount = 1500

    def delv(self):
        self.location = input("Enter address: ")


    def address(self):
        if self.location == str:
            print("valid address")
        else:
            raise TypeError("address entered is not that type")


    def show_summary(self):
        print("delivary : ",self.location)
        print("Total ",self.bill_amount)
        ob1.display()



obj=swiggy("www","fff")
obj.show()
obj=()
obj.order_summary
pay=payment()
pay.delv
pay.address
'''
                
       

                 
                 
           
            

                                        

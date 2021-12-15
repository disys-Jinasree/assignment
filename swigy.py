class res:
    def __init__(self):
        print("welcome to swiggy")
     
hotel=[{"honame":"A2B","dish":"briyani","price":200},
        {"honame":"akshayam","dish":"shake","price":190},             
        {"honame":"buhari","dish":"aloogobi","price":100},            
        {"honame":"sangeet","dish":"pannergobi","price":170},
        {"honame":"hampa","dish":"aloomatar","price":180},
        {"honame":"nasi","dish":"aloomethi","price":150},
        {"honame":"bay6","dish":"alootikki","price":120},
        {"honame":"dank","dish":"hotdogs","price":720},
        {"honame":"libraryblu","dish":"wintersquash","price":920},'''{"dishname":"pannergravy","price":20}]},'''
        {"honame":"vasanthabhavan","dish":"frenchfries","price":220},'''{"dishname":"upma","price":20}]},'''
        {"honame":"hotelInn","dish":"macroni","price":220},'''{"dishname":"veggemix","price":20}]},'''
        {"honame":"chemistry","dish":"pasta","price":220},'''{"dishname":"pineapple juice","price":20}]},'''
        {"honame":"bobnmarley","dish":"pizza","price":120},'''{"dishname":"squash","price":20}]},'''
        {"honame":"seashells","dish":"sizzler","price":120},'''{"dishname":"caramelpudding","price":20}]},'''
        {"honame":"hawaiifood","dish":"fishfo","price":120},'''{"dishname":"falafel","price":20}]},'''
        {"honame":"palmshore","dish":"manchurian","price":120},'''{"dishname":"whiterice","price":20}]}''',
        {"honame":"copperkitchen","dish":"cheesepizza","price":120},'''{"dishname":"burger","price":20}]},'''
        {"honame":"redbox","dish":"fries","noodles":120},'''{"dishname":"schezwannoodles","price":20}]},'''
        {"honame":"nakshatra","dish":"sambaridly","price":120},'''{"dishname":"idly podi","price":20}]},'''
        {"honame":"coffeday","dish":"cappucino","price":120},'''{"dishname":"burger","price":20}]},'''
        {"honame":"mcdonalds","dish":"milkshake","price":120},'''{"dishname":"nachos","price":20}]},'''
        {"honame":"hotelstar","dish":"dosa","price":120}]'''{"dishname":"biriyani","price":20}]}]'''





for i in hotel:
    for j,k in i.items():
        print(f"{j}={k}")

class swiggy:

    def __init__(self,num):
        self.num=num
        
    
       
    def search(self):
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
            






num1=input("enter a hotel") 
ob=swiggy(num1)
ob.search()
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
                
       

                 
                 
           
            

                                        

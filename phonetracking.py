apps={"sunday":{"Linkedin":"1/2 hr","whatsapp":"2 hrs","facebook":"1 hr","instagram":"3 hrs","youtube":"2 hrs"},
          "monday":{"Linkedin":"2 hsr","whatsapp":"2 hrs","facebook":"1 hr","instagram":"3 hrs","youtube":"4 hrs"},
          "tuesday":{"Linkedin":"1 hr","whatsapp":"3 hrs","facebook":"2 hr","instagram":"5 hrs","youtube":"2 hrs"},
          "wednesday":{"Linkedin":"1 hr","whatsapp":"2 hrs","facebook":"1 hr","instagram":"3 hrs","youtube":"2 hrs"},
          "thursday":{"Linkedin":"2 hrs","whatsapp":"3 hrs","facebook":"1 hr","instagram":"3 hrs","youtube":"2 hrs"},
          "friday":{"Linkedin":"3 hr","whatsapp":"2 hrs","facebook":"1 hr","instagram":"3 hrs","youtube":"2 hrs"}}
class phonetracking:


    def __init__(self,day):
         self.day=day

    def search(self):
        for i in apps:
            for j,k in apps.items():
                if isinstance(j,str):
                    if(k>="2 hrs"):
                        print("this app exceeds given screen time ",k)
                    else:
                        print("no apps")
                else :
                    print("app not defined")
    def display():
        for j in apps:
            print("the list of apps in phone are :",j)

    def select():
        print(""" 1.to view apps of a day"
                  2.show apps """)
    choice=int(input("Please Enter Your Choice:"))
    if(choice==1):
        day=input("Enter The day:")
        week=phonetracking(day)
        week.search()
    else:
        display()
    select()
            

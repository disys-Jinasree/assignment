class phonecontacts:
    c_name = []
    phnumber = []
    count = 2

    def number():
         if (len(contact_number)==10):
                if type(.contact_number) == str:                                                                            #TYPE VALIDATION
                    print("Phone number verified")
                else:
                    raise TypeError("Phone number should contain only integers ")
         else:
                raise ValueError("phone number should not be grater than or lesser than 10")

         for i in range(count):
            cname = input("Name of the person: ")

            contact_number = input("contact Number: ") 

            c_name.append(cname)
            phnumber.append(contact_number)

         print("---------------")
    number()

    

    def search():
        contact = input("\nEnter contact detail : ")

        print("Search result:")

        if contact in c_name:
            index = c_name.index(contact)
            contact_number = phnumber[index]
            print("Name: {}, Phone Number: {}".format(contact, contact_number))

        else:
            print("Name Not Found")
    search()

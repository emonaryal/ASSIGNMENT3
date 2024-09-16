def staff_info(): 
    #This function is used for introduction
    global Date
    global Staff_ID
    global Staff_Name
    global Requisition_ID
    Date= input("Enter the Date ")
    #This function is used to enter the date
    Staff_ID= input("Enter the staff id ")
    #This function is used to enter the staff id
    Staff_Name= input("Enter the staff name ")
    #This function is used to enter the staff name
    Requisition_ID= 10000++1
    #This function is used to get the Requisition ID
    print ("Date:", Date)
    #This function is used to print the Date
    print ("Staff ID:", Staff_ID)
    #This function is used to print the Staff Id
    print ("Staff Name:", Staff_Name)
    #This function is used to print the Staff Name
    print ("Requistion ID:", Requisition_ID)
    #This function is used to print the Requisition ID
    return {
        #We will return the all inputs
        Date, Staff_ID, Staff_Name, Requisition_ID
    }
    #We close the return
staff_info()
#Close the program



def requisitions_total(staff_info):
    #This function is used to introduce the function
    global Requisition_item_total
    Coffee= input("Enter the price of coffee $")
    #We input the price of coffee
    Paper= input("Enter the price of paper $")
    #Now enter the price of paper
    Pen= input("Enter the price of Pen $")
    #Enter the price of pen
    Requisition_item_total= int(Coffee)+ int(Paper)+ int(Pen)
    #Now we add the total amount using integers
    print ("The total value of Requisition item is $", Requisition_item_total)
    #print the total value of Requisition item
    return{
        #Return the value to requisition_item_total
        Requisition_item_total
    }
    #Now we close the returned value
requisitions_total(staff_info)
#Close the program




def requisition_approval(requisitions_total):
    #This function is used to introduce the function
    global approval_reference_number
    #This function is used to call the approval_reference_number in every function
    if Requisition_item_total < 500:
        #This function is using the if loop
        print("Status:Approved")
        #Now print the status if it is correct
    else:
        #Now use else function
        print("pending")
        #Print if this syntax is correct
    approval_reference_number= str(Staff_ID) + str(Requisition_ID)[2:]
    #In this line we add the Staff_Id and Requisition_ID using str to find the approval_reference_number
    print("Approval Reference Number: ", approval_reference_number)
    #print the result
requisition_approval(requisitions_total)
#close the function


def display_requisitons():
    print("Date: ", Date)
    print ("Requistion ID:", Requisition_ID)
    print("Staff ID: ", Staff_ID)
    print ("Staff Name:", Staff_Name)
    print ("Total: $", Requisition_item_total)
    if Requisition_item_total < 500:
        print("Status:Approved")
    else:
        print("pending")
    print("Approval Reference Number: ", approval_reference_number)
display_requisitons()
    
    
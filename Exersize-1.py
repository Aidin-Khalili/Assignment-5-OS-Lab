from os import system

def add(list):
    global total
    global basket
    global basket_id
    while(True):
        x , y = input("Please enter id & quantity of your product : ").split()
        x_value = abs(int(x))
        y_value = abs(int(y))
        index = x_value - 1
        available_product = list[index][2]
        availabe_cnt = int(available_product)
        if availabe_cnt < y_value:
            print("There aren\'t enough of this product avaialbe in our store. Please try again & consider that in our store there are : ", availabe_cnt)
        else:
           customer_list_availabe = []
           total += int(list[index][1]) * y_value
           customer_list_availabe.append(list[index][0])
           customer_list_availabe.append(y)
           updating_add(list, y_value, index)
           basket.append(customer_list_availabe)
           basket_id.append(index)
           break
def updating_add(list,count,index):
    product_update = int(list[index][2])-count
    list[index][2]=str(product_update)
def remove(list,user_basket,basket_id):
    if user_basket == []:
        print("Now your basket is empty. we have a lot of things ... try some ;)")
    else:
        user_choice = abs(int(input("please enter id of the product that you want to remove it from your basket : ")))
        index1 = user_choice - 1
        user_basket_quantity = int(user_basket[index1][1])
        user_basket.pop(index1)
        update_remove(list, user_basket_quantity, basket_id, index1)
        basket_id.pop(index1)
def update_remove(list, user_basket_quantity, basket_id, index):
    global total
    index_list = basket_id[index]
    result = int(list[index_list][2]) + user_basket_quantity
    list[index_list][2] = str(result)
    total = total - (int(list[index_list][1])*user_basket_quantity)
def showlist(list):
    print("[ ID ] [ Name ] [ cost ] [ Quatity ] ")
    i = 1
    for item in list:
        print(i,end=' ')
        for j in item:
            print(j,end=' ')
        i += 1
        print("")
def currentList_totalcost(basket , total_cost):
    str_basket= ""
    print("[ ID ] [ Name ] [ Quatity ] ")
    i = 1
    for item in basket:
         print(i," ", end = "")
         str_basket = ' '.join(item)
         print(str_basket)
         i += 1
    print("So your total cost(sunnation cost of your basket) is : ", total_cost)
def edit_file(list):
    pass = input("Please enter the password").lower()
    store_product_file = open("Aidin_os_text.txt",'a')
    if pass == "aidin_admin":
        while(True):
            manager_choice = abs(int(input(" Please choose one thing : \n 1. To remove something \n 2. To add something \n 3. To edit something\n")))
            if manager_choice == 1:
                remove_item = abs(int(input("Please enter item from the list that you want to remove it : ")))
                list.pop(remove_item - 1)
                break
            elif manager_choice == 2 :
                new_product = []
                x,y,z = input("Please enter the name, cost & quantity").split(" ")
                new_product.append(x)
                new_product.append(y)
                new_product.append(z)
                list.append(new_product)
                str_holder1 = ''.join(new_product)
                store_product_file.write(str_holder1)
                break
            elif manager_choice == 3:
                edit_input = int(input("Please enter ID from the list that you want to edit it : "))
                index = edit_input-1
                x,y,z = input("Please enter the name, cost & quantity").split(" ")
                list[index][0]=x
                list[index][1]=y
                list[index][2]=z
                break
            else:
                print("Your input isn\'t correct. Please try again")
    else:
        print("Incorrect pasword !")
    store_product_file.close()
def show_menu():
    System("clean")
    print("""Please choose one option to continue :
        1. Show List of products
        2. Add item to your basket
        3. Show your current basket & total cost
        4. Remove item from basket 
        5. Edit product from database (the manager can it needs pasword)
        6. Search by the name 
        7. Exit""")
    print("Enter your choice : ", end = '')
def search_as_name(list, name):
    for item in list:
      if name in item:
          return list.index(item)
      else:
          print("This product doesn\'t exist now !")
basket = []
basket_id =[]
total = 0
def shop():
    global basket
    store_product_file = open('myText','r')
    my_list = []
    my_list = store_product_file.read().split("\n")
    my_list2 = [item.split(' ') for item in my_list]
    while(True):
        show_menu()
        user_choice = int(input())
        if user_choice == 1:
            showlist(my_list2)
            print("It has done.")
        elif user_choice == 2:
            add(my_list2)
            print("It has done.")
        elif user_choice == 3:
            currentList_totalcost(basket, total)
            print("It has done.")
        elif user_choice == 4:
            remove(my_list2,basket, basket_id)
            print("It has done.")
        elif user_choice == 5:
            edit_file(my_list2)
            print("It has done.")
        elif user_choice == 6:
            name = input("please enter name of your product : ").lower()
            name_id = search_as_name(my_list2,name)
            print("The product id is", name_id + 1)
            print("It has done.")
        elif user_choice == 7:
            print("Thank for buying from our shop. Have good time ;) ")
            break
        else:
            print("please try again & choose num of one service")
    store_product_file.close()
    
if __name__ == '__main__':
    shop()
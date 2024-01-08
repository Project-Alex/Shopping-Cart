import os

product_dict        =   {"1"   :   "Squeaky Toy",
                         "2"   :   "Tennis Ball",
                         "3"   :   "Bird Seed",
                         "4"   :   "Hamster Cage",
                         "5"   :   "Cat Litter",
                        }

price_dict           =  {"1"   :   2,
                         "2"   :   4,
                         "3"   :   4,
                         "4"   :   3,
                         "5"   :   2,
                        }

cart_quantity_dict   =  {"1"   :   0,
                         "2"   :   0,
                         "3"   :   0,
                         "4"   :   0,
                         "5"   :   0,
                        }

display_line = "#" + "="*90 + "#"
counter = 0

close_cart = False
while not close_cart:
    print(counter)
    print(display_line)
    print("Welcome to Pets, Pets, Pets, and also more Pets Ltd.!")
    print(display_line)

    # Cart item display
    print("Your cart contains: ")
    for item in product_dict:
        if cart_quantity_dict[item] > 0:
            print(product_dict[item] + "\tx " + str(cart_quantity_dict[item]) + "\t£" + 
                  str(price_dict[item] * cart_quantity_dict[item]), sep='',end='\n')
    print(display_line)

    # Cart price display
    total_cart_cost = 0     # Reset total for fresh calculation
    for x in price_dict:
        total_cart_cost += price_dict.get(x) * cart_quantity_dict.get(x)
    print(f"Your current total is:\t£{total_cart_cost}\n" + display_line)


    print("1. Add an item to your basket")
    print("2. Remove an item from your basket")
    print("3. Checkout\n" + display_line)

    menu_select = input("Please select an option (1 - 3): ")

    # Option 1 - Add item
    os.system('cls')
    print(display_line)
    if menu_select == "1":
        for i, item in enumerate(product_dict,1):
            print(i, '. ' + product_dict[item] + "\t\t £" + str(price_dict[item]), sep='',end='\n'
                  + display_line + "\n")
        
        add_item_validation = False
        while not add_item_validation:
            try:
                add_item = str(input("\nPlease select an option from 1 to " + str(len(product_dict)) + ": "))
                cart_quantity_dict[add_item] += 1
                counter += 1
                add_item_validation = True
                os.system('cls')
            except IndexError:
                print("Invalid input, please try again.")
            except ValueError:
                print("Invalid input, please try again.")

    elif menu_select == "2":
        # print(display_line)
        for i, item in enumerate(product_dict, 1):
            if cart_quantity_dict[item] > 0:
                print(i, '. ' + product_dict[item] + "\t\t x " + str(cart_quantity_dict[item]), sep='',end='\n'
                      + display_line + "\n")
        
        remove_item_validation = False
        while not remove_item_validation:
            try:
                remove_item = str(input("Please enter the corresponding number to remove an item (-1 to go back): "))
                if remove_item == -1:
                    break
                elif remove_item > counter:
                    raise Exception
                cart_quantity_dict[remove_item] -= 1
                counter -= 1
                remove_item_validation = True
                os.system('cls')
            except Exception:
                print("Invalid input, please try again.")            
    
    elif menu_select == "3":
        print(display_line + 
              f"\nYour total to pay is:\t £{round(total_cart_cost)}\n"
              f"{display_line}\n"
              f"1. Checkout and close.\n"
              f"2. Main menu\n"
              f"{display_line}")
        main_menu = int(input("Please select either 1 or 2: "))
        if main_menu == 1:
            close_cart = True
            print(display_line +
                "\nThank you for visiting Pets, Pets, Pets, and also more Pets Ltd.!"
                "\nPlease come again soon!\n" +
                display_line)
        else:
            pass
    else:
        os.system('cls')
        print("Invalid input, please try again.")


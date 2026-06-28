from ecommercesystem import Ecommercesystem
ecs = Ecommercesystem()

while True:

    print("==========E-COMMERCE SYSTEM===========")
    print("1. add product")
    print("2. display products")
    print("3. search product")
    print("4. add to cart")
    print("5. view cart")
    print("6. exit")

    choice = input("enter your choice:")

    if choice == "1":
        ecs.add_product()

    elif choice == "2":
        ecs.display_products()

    elif choice == "3":
        ecs.search_product()

    elif choice == "4":
        ecs.add_to_cart()

    elif choice == "5":
        ecs.view_cart()

    elif choice == "6":
        print("Thank you")    
        break

    else:
        print("invalid choice, please try again.")               

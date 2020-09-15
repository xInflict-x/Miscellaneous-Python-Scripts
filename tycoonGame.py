import time


class businesses():
    lemonade_stand = 1
    newspaper_delivery = 0
    car_wash = 0
    pizza_delivery = 0
    donut_shop = 0
    shrimp_boat = 0
    hockey_team = 0
    movie_studio = 0
    bank = 0
    oil_company = 0


class player():
    money = 1
    prestige_level = 0
    prestige_multiplier = 0.65 * prestige_level + 1
    total_businesses = businesses.lemonade_stand + businesses.newspaper_delivery + businesses.car_wash + businesses.pizza_delivery + businesses.donut_shop + businesses.shrimp_boat + businesses.hockey_team + businesses.movie_studio + businesses.bank + businesses.oil_company


class lemonade_stand():
    money_output = round((5 * 1.1 ** businesses.lemonade_stand) / 10 * player.prestige_multiplier)
    upgrade_cost = round(13.0 * money_output + 10)


class newspaper_delivery():
    money_output = round((6 * 1.2 ** businesses.newspaper_delivery) / 10 * player.prestige_multiplier)
    upgrade_cost = round(13.5 * money_output + 20)


class car_wash():
    money_output = round((7 * 1.3 ** businesses.car_wash) / 10 * player.prestige_multiplier)
    upgrade_cost = round(14.0 * money_output + 30)


class pizza_delivery():
    money_output = round((8 * 1.4 ** businesses.pizza_delivery) / 10 * player.prestige_multiplier)
    upgrade_cost = round(14.5 * money_output + 40)


class donut_shop():
    money_output = round((9 * 1.5 ** businesses.donut_shop) / 10 * player.prestige_multiplier)
    upgrade_cost = round(15.0 * money_output + 50)


class shrimp_boat():
    money_output = round((10 * 1.6 ** businesses.shrimp_boat) / 10 * player.prestige_multiplier)
    upgrade_cost = round(15.5 * money_output + 60)


class hockey_team():
    money_output = round((11 * 1.7 ** businesses.hockey_team) / 10 * player.prestige_multiplier)
    upgrade_cost = round(16.0 * money_output + 70)


class movie_studio():
    money_output = round((12 * 1.8 ** businesses.movie_studio) / 10 * player.prestige_multiplier)
    upgrade_cost = round(16.5 * money_output + 80)


class bank():
    money_output = round((13 * 1.9 ** businesses.bank) / 10 * player.prestige_multiplier)
    upgrade_cost = round(17.0 * money_output + 90)


class oil_company():
    money_output = round((14 * 2.0 ** businesses.oil_company) / 10 * player.prestige_multiplier)
    upgrade_cost = round(17.5 * money_output + 100)

def update():
    player.prestige_multiplier = 0.65 * player.prestige_level + 1
    player.total_businesses = businesses.lemonade_stand + businesses.newspaper_delivery + businesses.car_wash + businesses.pizza_delivery + businesses.donut_shop + businesses.shrimp_boat + businesses.hockey_team + businesses.movie_studio + businesses.bank + businesses.oil_company
    lemonade_stand.money_output = round((5 * 1.1 ** businesses.lemonade_stand) / 10 * player.prestige_multiplier)
    lemonade_stand.upgrade_cost = round(13.0 * lemonade_stand.money_output + 10)

    newspaper_delivery.money_output = round((6 * 1.2 ** businesses.newspaper_delivery) / 10 * player.prestige_multiplier)
    newspaper_delivery.upgrade_cost = round(13.5 * newspaper_delivery.money_output + 20)

    car_wash.money_output = round((7 * 1.3 ** businesses.car_wash) / 10 * player.prestige_multiplier)
    car_wash.upgrade_cost = round(14.0 * car_wash.money_output + 30)

    pizza_delivery.money_output = round((8 * 1.4 ** businesses.pizza_delivery) / 10 * player.prestige_multiplier)
    pizza_delivery.upgrade_cost = round(14.5 * pizza_delivery.money_output + 40)

    donut_shop.money_output = round((9 * 1.5 ** businesses.donut_shop) / 10 * player.prestige_multiplier)
    donut_shop.upgrade_cost = round(15.0 * donut_shop.money_output + 50)

    shrimp_boat.money_output = round((10 * 1.6 ** businesses.shrimp_boat) / 10 * player.prestige_multiplier)
    shrimp_boat.upgrade_cost = round(15.5 * shrimp_boat.money_output + 60)

    hockey_team.money_output = round((11 * 1.7 ** businesses.hockey_team) / 10 * player.prestige_multiplier)
    hockey_team.upgrade_cost = round(16.0 * hockey_team.money_output + 70)

    movie_studio.money_output = round((12 * 1.8 ** businesses.movie_studio) / 10 * player.prestige_multiplier)
    movie_studio.upgrade_cost = round(16.5 * movie_studio.money_output + 80)

    bank.money_output = round((13 * 1.9 ** businesses.bank) / 10 * player.prestige_multiplier)
    bank.upgrade_cost = round(17.0 * bank.money_output + 90)

    oil_company.money_output = round((14 * 2.0 ** businesses.oil_company) / 10 * player.prestige_multiplier)
    oil_company.upgrade_cost = round(17.5 * oil_company.money_output + 100)

    if businesses.car_wash  < 1:
        car_wash.money_output = 0
    if businesses.pizza_delivery  < 1:
        pizza_delivery.money_output = 0
    if businesses.donut_shop  < 1:
        donut_shop.money_output = 0
    if businesses.shrimp_boat  < 1:
        shrimp_boat.money_output = 0    
    if businesses.hockey_team  < 1:
        hockey_team.money_output = 0 
    if businesses.movie_studio  < 1:
        movie_studio.money_output = 0 
    if businesses.bank  < 1:
        bank.money_output = 0 
    if businesses.oil_company < 1:
        oil_company.money_output = 0 


def total_output():
    if businesses.lemonade_stand > 0:
        player.money += lemonade_stand.money_output
    if businesses.newspaper_delivery > 0:
        player.money += newspaper_delivery.money_output
    if businesses.car_wash > 0:
        player.money += car_wash.money_output
    if businesses.pizza_delivery > 0:
        player.money += pizza_delivery.money_output
    if businesses.donut_shop > 0:
        player.money += donut_shop.money_output
    if businesses.shrimp_boat > 0:
        player.money += shrimp_boat.money_output
    if businesses.hockey_team > 0:
        player.money += hockey_team.money_output
    if businesses.movie_studio > 0:
        player.money += movie_studio.money_output
    if businesses.bank > 0:
        player.money += bank.money_output
    if businesses.oil_company > 0:
        player.money += oil_company.money_output
    print("Money: " + str(player.money))
    time.sleep(5/10)


def prestige():
    if player.money >= 1000000 * 1.1 ** player.prestige_level:
        confirm = input("1)Yes\n2)No\nAre you sure you want to prestige for: " + str(1000000 * 1.1 ** player.prestige_level) + "\n> ")
        if confirm == "1":
            player.money = 0
            businesses.lemonade_stand = 1
            businesses.newspaper_delivery = 0
            businesses.car_wash = 0
            businesses.pizza_delivery = 0
            businesses.donut_shop = 0
            businesses.shrimp_boat = 0
            businesses.hockey_team = 0
            businesses.movie_studio = 0
            businesses.bank = 0
            businesses.oil_company = 0
            player.prestige_level += 1
            menu()
        if confirm == "2":
            menu()
    else:
        print("You do not have " + str(1000000 * 1.1 ** player.prestige_level))
        menu()

def stats():
    print("[-------------------------------------------]")
    print("PLAYER: ")
    print("[Money]: " + str(round(abs(player.money))))
    print("[Prestige]: " + str(player.prestige_level))
    print("[Businesses]: " + str(player.total_businesses))
    print("[-------------------------------------------]")
    print("BUSINESSES: ")
    print("[Lemonade Stand]: " + str(businesses.lemonade_stand) + " \n[Income]: " + str(lemonade_stand.money_output))
    print("[Newspaper Delivery]: " + str(businesses.newspaper_delivery) + " \n[Income]: " + str(newspaper_delivery.money_output))
    print("[Car Wash]: " + str(businesses.car_wash) + " \n[Income]: " + str(car_wash.money_output))
    print("[Pizza Delivery]: " + str(businesses.pizza_delivery) + " \n[Income]: " + str(pizza_delivery.money_output))
    print("[Donut Shop]: " + str(businesses.donut_shop) + " \n[Income]: " + str(donut_shop.money_output))
    print("[Shrimp Boat]: " + str(businesses.shrimp_boat) + " \n[Income]: " + str(shrimp_boat.money_output))
    print("[Hockey Team]: " + str(businesses.hockey_team) + " \n[Income]: " + str(hockey_team.money_output))
    print("[Movie Studio]: " + str(businesses.movie_studio) + " \n[Income]: " + str(movie_studio.money_output))
    print("[Bank]: " + str(businesses.bank) + " \n[Income]: " + str(bank.money_output))
    print("[Oil Company]: " + str(businesses.oil_company) + " \n[Income]: " + str(oil_company.money_output))
    print("[-------------------------------------------]")
    menu()

def shop():
    update()
    print("1)Lemonade Stand: " + str(businesses.lemonade_stand) + " | Price: " + str(lemonade_stand.upgrade_cost))
    print("2)Newspaper Delivery: " + str(businesses.newspaper_delivery) + " | Price: " + str(newspaper_delivery.upgrade_cost))
    print("3)Car Wash: " + str(businesses.car_wash) + " | Price: " + str(car_wash.upgrade_cost))
    print("4)Pizza Delivery: " + str(businesses.pizza_delivery) + " | Price: " + str(pizza_delivery.upgrade_cost))
    print("5)Donut Shop: " + str(businesses.donut_shop) + " | Price: " + str(donut_shop.upgrade_cost))
    print("6)Shrimp Boat: " + str(businesses.shrimp_boat) + " | Price: " + str(shrimp_boat.upgrade_cost))
    print("7)Hockey Team: " + str(businesses.hockey_team) + " | Price: " + str(hockey_team.upgrade_cost))
    print("8)Movie Studio: " + str(businesses.movie_studio) + " | Price: " + str(movie_studio.upgrade_cost))
    print("9)Bank: " + str(businesses.bank) + " | Price: " + str(bank.upgrade_cost))
    print("10)Oil Company: " + str(businesses.oil_company) + " | Price: " + str(oil_company.upgrade_cost))
    shop_choice = input("What do you want to buy?\n> ")
    if shop_choice == "1":
        if player.money >= lemonade_stand.upgrade_cost:
            player.money -= lemonade_stand.upgrade_cost
            businesses.lemonade_stand += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "2":
        if player.money >= newspaper_delivery.upgrade_cost:
            player.money -= newspaper_delivery.upgrade_cost
            businesses.newspaper_delivery += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "3":
        if player.money >= car_wash.upgrade_cost:
            player.money -= car_wash.upgrade_cost
            businesses.car_wash += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "4":
        if player.money >= pizza_delivery.upgrade_cost:
            player.money -= pizza_delivery.upgrade_cost
            businesses.pizza_delivery += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "5":
        if player.money >= donut_shop.upgrade_cost:
            player.money -= donut_shop.upgrade_cost
            businesses.donut_shop += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "6":
        if player.money >= shrimp_boat.upgrade_cost:
            player.money -= shrimp_boat.upgrade_cost
            businesses.shrimp_boat += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "7":
        if player.money >= hockey_team.upgrade_cost:
            player.money -= hockey_team.upgrade_cost
            businesses.hockey_team += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "8":
        if player.money >= movie_studio.upgrade_cost:
            player.money -= movie_studio.upgrade_cost
            businesses.movie_studio += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "9":
        if player.money >= bank.upgrade_cost:
            player.money -= bank.upgrade_cost
            businesses.bank += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()
    if shop_choice == "10":
        if player.money >= oil_company.upgrade_cost:
            player.money -= oil_company.upgrade_cost
            businesses.oil_company += 1
            print("Success!")
            menu()
        else:
            print("You do not have enough money!")
            menu()


def menu():
    update()
    print("1)Generate Money")
    print("2)Shop")
    print("3)Prestige")
    print("4)Stats")
    print("5)Exit")
    menu_choice = input("What do you want to do?\n> ")
    if menu_choice == "1":
        gen_choice = int(input("How many times?\n> "))
        for x in range (0, gen_choice):
            total_output()
        menu()
    if menu_choice == "2":
        shop()
    if menu_choice == "3":
        prestige()
    if menu_choice == "4":
        stats()
    if menu_choice == "5":
        exit()
menu()
input()

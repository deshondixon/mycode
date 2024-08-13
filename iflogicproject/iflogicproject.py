#!/usr/bin/env python3

def carFinder():
    print("Welcome to Car Finder, where we help you find which vehicle fits you best!")

    count = 0 
    
    while True:
        print("\n1. What is the most important thing about a car?")
        choice = input("a) Speed  b) Comfort  c) Efficiency: ").lower()
        if choice == "a":
            count += 3
            break
        elif choice == "b":
            count += 2
            break
        elif choice == "c":
            count += 1
            break
        else:
            print("Invalid input. Please choose a, b, or c.")

    while True:
        print("\n2. How often do you drive?")
        choice = input("a) Daily  b) A few times a week  c) Rarely: ").lower()
        if choice == "a":
            count += 3
            break
        elif choice == "b":
            count += 2
            break
        elif choice == "c":
            count += 1
            break
        else:
            print("Invalid input. Please choose a, b, or c.")

    while True:
        print("\n3. Whats is your preferred car size? ")
        choice = input("a) Large  b) Medium  c) Small: ").lower()
        if choice == "a":
            count += 3
            break
        elif choice == "b":
            count += 2
            break
        elif choice == "c":
            count += 1
            break
        else:
            print("Invalid input. Please choose a, b, or c.")

    while True:
        print("\n4. What's your budget range?")
        choice = input("a) High  b) Medium  c) Low: ").lower()
        if choice == "a":
            count += 3
            break
        elif choice == "b":
            count += 2
            break
        elif choice == "c":
            count += 1
            break
        else:
            print("Invalid input. Please choose a, b, or c.")


    while True:
        print("\n5. Do you prefer gas or electric")
        choice = input("a) Gas  b) Electric  c) No preference: ").lower()
        if choice == "a" or "c":
            if count >= 13:
                print("\nYou are a person of class! Only the finer things in life will fit you, buy a luxury sports car like a Porsche 911 or an Audi R8.")
            elif count >= 10: 
                print("\nYou like to go fast at an affordable price! Buy a mid-range sports car like a Ford Mustang or a Mazda MX-5 Miata.")
            elif count >= 7:
                print("\nYou have a preference for realiabilty and affordablitly. Buy a sedan like a Honda Accord or a Toyota Camry.")
            else: 
                print("\nYou have a preference for realiabilty and affordablitly. Buy a sedan like a Honda Accord or a Toyota Camry.")
            break
        elif choice == "b":
            if count >= 13:
                print("\nYou are a person of class! Only the finer things in life will fit you, buy a luxury sports car like a Tesla Model S or an Porsche Taycan.")
            elif count >= 10:
                print("\nYou like to go fast at an affordable price! Buy a mid-range sports car like a Tesla Model 3 or a Ford Mustang Mach-E")
            elif count >= 7:
                print("\nYou have a preference for realiabilty and affordablitly. Buy a sedan like a Hyundai Ioniq or a Nissan Leaf.")
            else:
                print("\nYou have a preference for realiabilty and affordablitly. Buy a sedan like a Hyundai Ioniq or a Nissan Leaf.")
            break
        else:
            print("Invalid input. Please choose a, b, or c.")


carFinder()



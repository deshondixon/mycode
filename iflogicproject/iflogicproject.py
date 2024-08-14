#!/usr/bin/env python3

def carFinder():
    print("""

__        __   _                            _                              
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___                        
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \                       
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |                      
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/                       
                                                                           
    ____             _____ _           _                                   
   / ___|__ _ _ __  |  ___(_)_ __   __| | ___ _ __                         
  | |   / _` | '__| | |_  | | '_ \ / _` |/ _ \ '__|                        
  | |__| (_| | |    |  _| | | | | | (_| |  __/ |                           
   \____\__,_|_|    |_|   |_|_| |_|\__,_|\___|_| 


""")
    print("We will help you find which vehicle fits you best!")

    count = 0 
    
    while True:
        print("\n1. What is the most important thing about a car?")
        print("a) Speed  b) Comfort  c) Efficiency: ")
        choice = input("> ").lower()
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
        print("a) Daily  b) A few times a week  c) Rarely: ")
        choice = input("> ").lower()
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
        print("a) Large  b) Medium  c) Small: ")
        choice = input("> ").lower()
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
        print("a) High  b) Medium  c) Low: ")
        choice = input("> ").lower()
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
        print("a) Gas  b) Electric  c) No preference: ")
        choice = input("> ").lower()
        if choice == "a" or choice == "c":
            if count >= 11:
                print("\nYou are a person of class! Only the finer things in life will fit you, buy a luxury sports car like a Porsche 911 or an Audi R8.")
            elif count >= 9: 
                print("\nYou like to go fast at an affordable price! Buy a mid-range sports car like a Ford Mustang or a Mazda MX-5 Miata.")
            elif count >= 7:
                print("\nYou have a preference for realiabilty and affordablitly. Buy a sedan like a Honda Accord or a Toyota Camry.")
            else: 
                print("\nYou prefer efficiency and practicality. Consider a compact car like a Honda Civic or a Toyota Corolla.")
            break
        elif choice == "b":
            if count >= 11:
                print("\nYou are a person of class! Only the finer things in life will fit you, buy a luxury sports car like a Tesla Model S or an Porsche Taycan.")
            elif count >= 9:     
                print("\nYou like to go fast at an affordable price! Buy a mid-range sports car like a Tesla Model 3 or a Ford Mustang Mach-E")
            elif count >= 7:
                print("\nYou have a preference for realiabilty and affordablitly. Buy a sedan like a Hyundai Ioniq or a Nissan Leaf.")
            else:
                print("\nYou prefer efficiency and practicality. Consider a compact electric car like a Chevrolet Bolt EV or a Nissan Leaf.")
            break
        else:
            print("Invalid input. Please choose a, b, or c.")

    print("""

                                                                      ++ +++  ++
                                                                      +++++++++++++
                                         +++++                     +++++++++++++++
                                ++++++++++++++++++++          +++++++++++ +    ++++++
                              ++++  +++++++++++++++     +++++     +++ ++ + + ++  +++
                           ++++ ++++++++++++++++++++++++         +++++++++++ +++  +++++
                          ++++++++ +++++ ++++++++++++      +++++++++++  +   + ++++++
                         +++++                +++++    +++++++++++++++  +++++++++++++
                         +++++  +++     +++   ++++   +++         ++++++++++++++++++
                         ++ ++ +              ++++ ++++++++++++++++++++++++++++ ++++
                  ++++++  ++++  +++++ +++++   + ++++++++++++++++++++++++++++++++   +
                +++    +  ++++ +  + + +   ++  ++++++++++++++++++++++++++++++++++   ++
                +     ++++++++ +   ++ +++ ++  ++    +++++               +++++++++  ++
               ++     ++ +++    +++     +++    ++  ++                      +++ ++   ++
                +     +++++        ++++         ++++                        ++++++  ++
                ++    ++   ++           ++++  +++++                          +++++   +
                 +     +   ++  ++++  ++++     ++ +                            ++++   ++
              +++++    ++   +    ++++++++ +   ++++++++++++                    ++++   ++
        ++++++++++      +++++           +++ ++++       ++                      ++++  ++
      ++        +++++    +  +++           ++ +   ++++  +                        +++  ++
     ++     ++++    +    +  ++  +++    +++  + +++ ++  ++                     ++++++  ++
      +         ++ +    + + +++     ++++   +  ++ ++   ++                   ++++  ++  ++
      +  ++++   +++ +  ++ + + ++   ++ +++++   +  +++++++                  +++++  ++  ++
     ++      ++++  ++   + +++   +++++++  +    + +                        +++++ ++++   +
      +  +       ++++   + ++       ++++       +++ + + +++++++++++++++++++++++++++++   ++++++
     ++    ++++++  ++   + ++      +++++       + + + + +                           +        ++++++++
      ++  +     ++++   +++++     +++++++      +++ + +  ++++++++++++++++++++++++++++++++++++       +++
       ++ +++++++ +  ++++ +      +++++++     ++  +++++++                         ++       ++++++++  ++++
       ++       ++++++++  +++++++++++++++++++++                                  ++                 +   ++
         ++++++++ ++  ++  +++++++++++++++++++++                                 ++                  +    ++
                  + +++     ++++++++++++++++  +                               ++   ++++++           +++  ++
                  +           +++++++++++++   +                             ++  ++++++++++++          +++++
          +++    ++++ ++     +++++++++++++++  ++++++++                         ++++++++++++++       ++   +
         ++ ++++++    ++    +++++++ +++++++++++++++++++++++++++++++++++++++++++++++++ +++++++      ++ ++++
        +++    +++  ++    ++++++++ +++++++++++++               +++++     ++++++++++     +++++++++ ++     +
        +      + +++++++++  ++++++++++++++++++++                         ++++++++++++++++++++   +++++++++
         ++++ ++            ++++++++++++++++++++                         ++++++++++     +++++
             +               +++++++++++++  +++                           +++++++++++++++++++
                +++++++  +++ +++++++++++++ +++                              ++++++++++++++++
              +++++++++++++++++++++++++++ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         +++     ++++++++ +          ++                ++++      +++++++++++++++++++++++++
                  +++++++++++++++++++++++++


        """)

if __name__ == "__main__":
    carFinder()

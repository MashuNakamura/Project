from week_2_stack import Stack

if __name__ == "__main__":
    # User input size dataset
    size = int(input("Input size dataset : "))
    s = Stack(size)
    
    # Loop Main
    while True:
        print("\n======= MENU =======")
        print("1. Add Data")
        print("2. Pop Data")
        print("3. Peek Data")
        print("4. Clear Data")
        print("0. Keluar")
        print("======================")
        print(f"[INFO] Dataset : {s.dataset}")
        
        # User select menu by input
        menu = int(input("Input Menu : "))
        
        if menu == 0:
            print("[INFO] Thank you for visiting")
            break
        
        elif menu == 1:
            data = input('Input data : ')
            s.push(data)
            
        elif menu == 2:
            s.pop()
            
        elif menu == 3:
            s.peek()
            
        elif menu == 4:
            s.clear()
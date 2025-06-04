from robot import Robot

if __name__ == "__main__":
    robot1 = Robot("Acumalaka", 2, None)
    robot2 = Robot("Bombardino", 5, None)
    robot3 = Robot("Cerberus", 4, None)
    robot4 = Robot("Dominator", 6, None)
    robot5 = Robot("Electra", 3, None)
    robot6 = Robot("Fission", 7, None)
    robot7 = Robot("Gigantor", 8, None)

    # Print langsung masing-masing robot
    print(f"{robot1.name}, {robot1.size}")
    print(f"{robot2.name}, {robot2.size}")
    print(f"{robot3.name}, {robot3.size}")
    print(f"{robot4.name}, {robot4.size}")
    print(f"{robot5.name}, {robot5.size}")
    print(f"{robot6.name}, {robot6.size}")
    print(f"{robot7.name}, {robot7.size}")
    
    # Sambungkan teman
    robot1.friend = robot3
    robot3.friend = robot5
    robot5.friend = robot2
    robot2.friend = robot7
    robot7.friend = robot4
    robot4.friend = robot6
    robot6.friend = None  # terakhir

    # Loop melalui teman-teman
    ptr = robot1
    while ptr != None:
        print(f"{ptr.name}, {ptr.size}")
        ptr = ptr.friend
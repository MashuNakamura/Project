from robot import Robot

if __name__ == "__main__":
    list_robot = []
    for i in range(0, 7):
        rob = Robot("Robot", 1 + (i / 10), None)
        if i > 0 and i < 5:
            list_robot[-1].friend = rob
        list_robot.append(rob)
    
    ptr = list_robot[0]
    while ptr is not None:
        print(f"{ptr.name}, {ptr.size}")
        ptr = ptr.friend
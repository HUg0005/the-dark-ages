import socket
import json
import time
import threading
from termcolor import colored


def recvData(required_data):
    data, addr = s.recvfrom(1024)
    if str(required_data) == (data.decode().split())[0]:
        return (data.decode().split())[1]


def getClient(client_type):
    request_message = "request clients"
    s.sendto(request_message.encode(), server)
    clients_list = json.loads(recvData("client_list"))
    return tuple(clients_list[str(client_type) + str(player_num)])


def getStats(stats):
    stats_message = "getstats" + " " + stats
    s.sendto(stats_message.encode(), getClient("stats"))
    data, addr = s.recvfrom(1024)
    return int(data.decode())


def checkCoords(coords):
    check_message = "checkcoords" + " " + coords
    s.sendto(check_message.encode(), getClient("map"))
    data, addr = s.recvfrom(1024)
    return data.decode()


def checkExists(unit):
    check_message = "checkexist" + " " + unit
    s.sendto(check_message.encode(), getClient("map"))
    data, addr = s.recvfrom(1024)
    return data.decode()


def getPos(unit_name):
    pos_message = "getpos" + " " + unit_name
    s.sendto(pos_message.encode(), getClient("map"))
    recived, addr = s.recvfrom(1024)
    data = recived.decode()
    return data


def buildRequest(coords, building):
    buildings_list = ["wall", "archery", "stable", "barracks", "workshop"]
    if building not in buildings_list:
        print("Invalid building")
        return
    if building != "wall" and checkExists(building) == "yes":
        print(building + " has already been built!")
        return
    if checkCoords(coords) == "empty":
        request_message = str("set" + " " + coords + " " + building)
        s.sendto(request_message.encode(), getClient("map"))
        if building == "wall":
            unitDataList(building, "#", 500, 0, 0, "wall_" + player_num,
                         "None", "None")
        elif building == "barracks":
            unitDataList(building, "B", 1000, 0, 0,
                         "barracks_" + player_num, "None", "None")
        elif building == "archery":
            unitDataList(building, "A", 1000, 0, 0,
                         "archer_" + player_num, "None", "None")
        elif building == "stable":
            unitDataList(building, "S", 2000, 0, 0,
                         "stable_" + player_num, "None", "None")
        elif building == "workshop":
            unitDataList(building, "W", 2500, 0, 0,
                         "workshop_" + player_num, "None", "None")
        print("Built" + " " + building + " at " + coords)
    else:
        print("Building blocked by", checkCoords(coords) + "!")


def getNextTo(unit_name, direction):
    current_pos = getPos(unit_name).split(",")
    current_pos_up = current_pos[0] + "," + str((int(current_pos[1]) - 1))
    current_pos_down = current_pos[0] + "," + str((int(current_pos[1]) + 1))
    current_pos_left = str((int(current_pos[0]) - 1)) + "," + current_pos[1]
    current_pos_right = str((int(current_pos[0]) + 1)) + "," + current_pos[1]
    if direction == "up":
        return checkCoords(current_pos_up)
    elif direction == "down":
        return checkCoords(current_pos_down)
    elif direction == "left":
        return checkCoords(current_pos_left)
    elif direction == "right":
        return checkCoords(current_pos_right)


def sendStats(food, stone, wood):
    stats = "stats" + " " + str(food) + " " + str(stone) + " " + str(wood)
    s.sendto(stats.encode(), getClient("stats"))


def setCoords(coords, unit_name):
    spawn_message = "set" + " " + coords + " " + unit_name
    s.sendto(spawn_message.encode(), getClient("map"))


def getEnemyNumber():
    if player_num == "1":
        return "2"
    elif player_num == "2":
        return "1"


def unitDataList(unit_name, unit_symbol, unit_health, movement_speed,
                 food_consumption, unit_type, unit_status, damage):
    if unit_name not in unit_data.keys():
        unit_data[unit_name] = [unit_symbol, unit_health, movement_speed,
                                food_consumption, unit_type, unit_status,
                                damage]
    else:
        if unit_symbol is not None:
            unit_data[unit_name][0] = unit_symbol
        elif unit_health is not None:
            unit_data[unit_name][1] = unit_health
        elif movement_speed is not None:
            unit_data[unit_name][2] = movement_speed
        elif food_consumption is not None:
            unit_data[unit_name][3] = food_consumption
        elif unit_type is not None:
            unit_data[unit_name][4] = unit_type
        elif unit_status is not None:
            unit_data[unit_name][5] = unit_status
        elif damage is not None:
            unit_data[unit_name][6] = damage

    s.sendto("unitdata".encode(), getClient("map"))
    s.sendto(json.dumps(unit_data).encode(), getClient("map"))


def removeUnit(unit_name):
    unit_data.pop(unit_name)
    kill_message = "set" + " " + getPos(unit_name) + " " + "empty"
    s.sendto(kill_message.encode(), getClient("map"))


def moveUnit(unit_name, direction, distance_input):
    distance = int(distance_input)
    if direction == "up":
        while distance != 0:
            current_pos = getPos(unit_name)
            current_pos_list = current_pos.split(",")

            current_pos_up = current_pos_list[0] + \
                "," + str((int(current_pos_list[1]) - 1))
            if getNextTo(unit_name, "up"):
                setCoords(current_pos_up, unit_name)
                setCoords(current_pos, "empty")
                distance -= 1
            else:
                blocked_by = checkCoords(current_pos_up)
                print(unit_name.replace("_", "").replace(
                    player_num, "") + " is blocked by " + blocked_by)
                break

    if direction == "down":
        while distance != 0:
            current_pos = getPos(unit_name)
            current_pos_list = current_pos.split(",")

            current_pos_down = current_pos_list[0] + \
                "," + str((int(current_pos_list[1]) + 1))
            if getNextTo(unit_name, "down") == "empty":
                setCoords(current_pos_down, unit_name)
                setCoords(current_pos, "empty")
                distance -= 1
            else:
                blocked_by = checkCoords(current_pos_down)
                print(unit_name.replace("_", "").replace(
                    player_num, "") + " is blocked by " + blocked_by)
                break

    if direction == "left":
        while distance != 0:
            current_pos = getPos(unit_name)
            current_pos_list = current_pos.split(",")

            current_pos_left = str(
                (int(current_pos_list[0]) - 1)) + "," + current_pos_list[1]
            if getNextTo(unit_name, "left") == "empty":
                setCoords(current_pos_left, unit_name)
                setCoords(current_pos, "empty")
                distance -= 1
            else:
                blocked_by = checkCoords(current_pos_left)
                print(unit_name.replace("_", "").replace(
                    player_num, "") + " is blocked by " + blocked_by)
                break

    if direction == "right":
        while distance != 0:
            current_pos = getPos(unit_name)
            current_pos_list = current_pos.split(",")

            current_pos_right = str(
                (int(current_pos_list[0]) - 1)) + "," + current_pos_list[1]
            if getNextTo(unit_name, "right") == "empty":
                setCoords(current_pos_right, unit_name)
                setCoords(current_pos, "empty")
                distance -= 1
            else:
                blocked_by = checkCoords(current_pos_right)
                print(unit_name.replace("_", "").replace(
                    player_num, "") + " is blocked by " + blocked_by)
                break
    time.sleep(unit_data[unit_name][2])


def createVillager(villager_type):
    if villager_num < 6:
        if villager_type == "farmer":
            villager_name = villager_type + \
                str(farmer_num) + "_" + str(player_num)
        elif villager_type == "lumberjack":
            villager_name = villager_type + \
                str(lumberjack_num) + "_" + str(player_num)
        else:
            villager_name = villager_type + \
                str(miner_num) + "_" + str(player_num)

        if getNextTo("town_center", "down") == "empty":
            town_center_pos = getPos("town_center").split(",")
            town_center_spawn = town_center_pos[0] + \
                "," + str(int(town_center_pos[1]) + 1)
            setCoords(town_center_spawn, villager_name)
            if villager_type == "farmer":
                symbol = colored("0", "yellow")
            elif villager_type == "lumberjack":
                symbol = colored("0", "green")
            else:
                symbol = "0"
            unitDataList(villager_name, symbol, 100,
                         1, -1, villager_type, "idle", 1)
            sendStats(-100, 0, 0)
        else:
            print("Town Center spawn site blocked!")
    else:
        print("Villager limit reached!")


def createMilitia():
    militia_name = "militia" + str(militia_num) + "_" + str(player_num)
    if checkExists("barracks") == "yes":
        if getNextTo("barracks", "down") == "empty":
            barracks_pos = getPos("barracks").split(",")
            barracks_spawn = barracks_pos[0] + \
                "," + str(int(barracks_pos[1]) + 1)
            setCoords(barracks_spawn, militia_name)
            unitDataList(militia_name, "!", 150, 1, -1,
                         "militia_" + player_num, "idle", 50)
        else:
            print("Barracks spawn site blocked!")
    else:
        print("You must build a barracks to create a militia!")


def createArcher():
    archer_name = "archer" + str(militia_num) + "_" + str(player_num)
    if checkExists("archery") == "yes":
        if getNextTo("archery", "down") == "empty":
            archery_pos = getPos("archery").split(",")
            archery_spawn = archery_pos[0] + "," + str(int(archery_pos[1]) + 1)
            setCoords(archery_spawn, archer_name)
            unitDataList(archer_name, ")", 125, 1, -1,
                         "archer_" + player_num, "idle", 25)
        else:
            print("Archery spawn site blocked!")
    else:
        print("You must build a archery to create a archer!")


def createKnight():
    knight_name = "knight" + str(knight_num) + "_" + str(player_num)
    if checkExists("stable") == "yes":
        if getNextTo("stable", "down") == "empty":
            stable_pos = getPos("stable").split(",")
            stable_spawn = stable_pos[0] + "," + str(int(stable_pos[1]) + 1)
            setCoords(stable_spawn, knight_name)
            unitDataList(knight_name, "^", 200, 2, -2,
                         "knight_" + player_num, "idle", 100)
        else:
            print("Stable spawn site blocked!")
    else:
        print("You must build a stable to create a knight!")


def createRam():
    ram_name = "ram" + str(ram_num) + "_" + str(player_num)
    if checkExists("workshop") == "yes":
        if getNextTo("workshop", "down") == "empty":
            workshop_pos = getPos("workshop").split(",")
            workshop_spawn = workshop_pos[0] + \
                "," + str(int(workshop_pos[1]) + 1)
            setCoords(workshop_spawn, ram_name)
            unitDataList(ram_name, "=", 100, 1, 0,
                         "ram_" + player_num, "idle", 200)
        else:
            print("Workshop spawn site blocked!")
    else:
        print("You must build a workshop to create a ram!")

# Threads


def consumeFood(run_time):
    if run_time % 10 == 0:
        for unit in unit_data:
            if getStats("food") > 0:
                sendStats(unit_data[unit][3], 0, 0)
            elif unit_data[unit][3] != 0:
                removeUnit(unit)
                print(unit, "was killed by starvation")


def farmer(run_time):
    farmer_amount = 0
    if run_time % 10 == 0:
        for unit_name in unit_data:
            if unit_data[unit_name][3] == "farmer_" + player_num:
                if getNextTo(unit_name, "up") == "farm":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "farming", None)
                    farmer_amount += 1
                if getNextTo(unit_name, "down") == "farm":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "farming", None)
                    farmer_amount += 1
                if getNextTo(unit_name, "left") == "farm":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "farming", None)
                    farmer_amount += 1
                if getNextTo(unit_name, "right") == "farm":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "farming", None)
                    farmer_amount += 1
                else:
                    unitDataList(unit_name, None, None, None,
                                 None, None, "idle", None)
                    farmer_amount -= 1
        food = 1 * farmer_amount
        sendStats(food, 0, 0)


def lumberjack(run_time):
    lumberjack_amount = 0
    if run_time % 10 == 0:
        for unit_name in unit_data:
            if unit_data[unit_name][3] == "lumberjack_" + player_num:
                if getNextTo(unit_name, "up") == "tree":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "chopping", None)
                    lumberjack_amount += 1
                if getNextTo(unit_name, "down") == "tree":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "chopping", None)
                    lumberjack_amount += 1
                if getNextTo(unit_name, "left") == "tree":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "chopping", None)
                    lumberjack_amount += 1
                if getNextTo(unit_name, "right") == "tree":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "chopping", None)
                    lumberjack_amount += 1
                else:
                    unitDataList(unit_name, None, None, None,
                                 None, None, "idle", None)
                    lumberjack_amount -= 1
        wood = 1 * lumberjack_amount
        sendStats(0, wood, 0)


def miner(run_time):
    miner_amount = 0
    if run_time % 10 == 0:
        for unit_name in unit_data:
            if unit_data[unit_name][3] == "miner_" + player_num:
                if getNextTo(unit_name, "up") == "stone":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "mining", None)
                    miner_amount += 1
                if getNextTo(unit_name, "down") == "stone":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "mining", None)
                    miner_amount += 1
                if getNextTo(unit_name, "left") == "stone":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "mining", None)
                    miner_amount += 1
                if getNextTo(unit_name, "right") == "stone":
                    unitDataList(unit_name, None, None, None,
                                 None, None, "mining", None)
                    miner_amount += 1
                else:
                    unitDataList(unit_name, None, None, None,
                                 None, None, "idle", None)
                    miner_amount -= 1
        stone = 1 * miner_amount
        sendStats(0, 0, stone)


def militia():
    for unit_name in unit_data:
        if unit_data[unit_name][4] == "militia_" + player_num:
            if getNextTo(unit_name, "up").endswith(enemy_num):
                unitDataList(unit_name, None, None, None,
                             None, None, "fighting", None)
                unit_data[getNextTo(unit_name, "up")][1] -= 50
            elif getNextTo(unit_name, "down").endswith(enemy_num):
                unitDataList(unit_name, None, None, None,
                             None, None, "fighting", None)
                unit_data[getNextTo(unit_name, "down")][1] -= 50
            elif getNextTo(unit_name, "left").endswith(enemy_num):
                unitDataList(unit_name, None, None, None,
                             None, None, "fighting", None)
                unit_data[getNextTo(unit_name, "left")][1] -= 50
            elif getNextTo(unit_name, "right").endswith(enemy_num):
                unitDataList(unit_name, None, None, None,
                             None, None, "fighting", None)
                unit_data[getNextTo(unit_name, "right")][1] -= 50
            else:
                unitDataList(unit_name, None, None, None,
                             None, None, "idle", None)


def threads():
    run_time = 0
    while True:
        consumeFood(run_time)
        farmer(run_time)
        miner(run_time)
        lumberjack(run_time)
        militia()

        run_time += 1
        time.sleep(1)

# Main script


# Get info
host = input("Server IP: ")
port = int(input("Server Port: "))
player_num = input("Player Number: ")
enemy_num = getEnemyNumber()
server = (host, port)

# Default variables
farmer_num = 0
lumberjack_num = 0
miner_num = 0
militia_num = 0
archer_num = 0
knight_num = 0
ram_num = 0
villager_num = 0

unit_data = {"town_center": ["X", 1000, 0, 0,
                             "town_center_" + player_num, "None", "None"]}

# Connect to Server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("localhost", 0))
    clientid = "console" + player_num
    s.sendto(clientid.encode(), server)
except:
    print("Cannot find server!")

print("Waiting for game to start...")
start, addr = s.recvfrom(1024)
if start.decode() == "start":
    # Start threads
    threading._start_new_thread(threads, ())

    while True:
        usr_command = input("-> ").split()

        if usr_command[0] == "b":
            buildRequest(usr_command[1], usr_command[2])

        elif usr_command[0] == "c":
            if usr_command[1] == "farmer":
                createVillager("farmer")
                farmer_num += 1
                villager_num += 1
            elif usr_command[1] == "lumberjack":
                createVillager("lumberjack")
                lumberjack_num += 1
                villager_num += 1
            elif usr_command[1] == "miner":
                createVillager("miner")
                miner_num += 1
                villager_num += 1
            elif usr_command[1] == "militia":
                createMilitia()
                militia_num += 1
            elif usr_command[1] == "archer":
                createArcher()
                archer_num += 1
            elif usr_command[1] == "knight":
                createKnight()
                knight_num += 1
            elif usr_command[1] == "ram":
                createRam()
                ram_num += 1
            else:
                print("Unknown unit type,", usr_command[1] + "!")

        elif usr_command[0] == "m":
            threading._start_new_thread(
                moveUnit, (usr_command[1] + "_" + player_num, usr_command[2],
                           usr_command[3]))

        elif usr_command[0] == "map":
            if usr_command[1] == "stop":
                s.sendto("stop".encode(), getClient("map"))
            elif usr_command[1] == "start":
                s.sendto("start".encode(), getClient("map"))
            elif usr_command[1] == "1":
                s.sendto("map 1".encode(), getClient("map"))
            elif usr_command[1] == "2":
                s.sendto("map 2".encode(), getClient("map"))
            else:
                print(usr_command[1], "is not a valid map command!")

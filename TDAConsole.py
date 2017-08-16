import socket
import json
import time
import threading
from termcolor import colored


def get_client(client_type):
    request_message = "request clients"
    s.sendto(request_message.encode(), server)
    data, addr = s.recvfrom(1024)
    clients_list = json.loads(data.decode())
    return tuple(clients_list[str(client_type) + str(player_num)])


def get_stats(stats):
    stats_message = "getstats" + " " + stats
    s.sendto(stats_message.encode(), get_client("stats"))
    data, addr = s.recvfrom(1024)
    return int(data.decode())


def check_coords(coords):
    check_message = "checkcoords" + " " + coords
    s.sendto(check_message.encode(), get_client("map"))
    data, addr = s.recvfrom(1024)
    return data.decode()


def check_exists(unit):
    check_message = "checkexist" + " " + unit
    s.sendto(check_message.encode(), get_client("map"))
    data, addr = s.recvfrom(1024)
    return data.decode()


def get_pos(unit_name):
    pos_message = "getpos" + " " + unit_name
    s.sendto(pos_message.encode(), get_client("map"))
    recived, addr = s.recvfrom(1024)
    data = recived.decode()
    return data


def build_request(coords, building):
    buildings_list = ["wall", "archery", "stable", "barracks", "workshop"]
    if building not in buildings_list:
        print("Invalid building")
        return
    if building != "wall" and check_exists(building) == "yes":
        print(building + " has already been built!")
        return
    if check_coords(coords) == "empty":
        request_message = str("set" + " " + coords + " " + building)
        s.sendto(request_message.encode(), get_client("map"))
        if building == "wall":
            unit_data_list(building, "#", 500, 0, 0, "wall_" +
                           player_num, "None", "None")
        elif building == "barracks":
            unit_data_list(building, "B", 1000, 0, 0,
                           "barracks_" + player_num, "None", "None")
        elif building == "archery":
            unit_data_list(building, "A", 1000, 0, 0,
                           "archer_" + player_num, "None", "None")
        elif building == "stable":
            unit_data_list(building, "S", 2000, 0, 0,
                           "stable_" + player_num, "None", "None")
        elif building == "workshop":
            unit_data_list(building, "W", 2500, 0, 0,
                           "workshop_" + player_num, "None", "None")
        print("Built" + " " + building + " at " + coords)
    else:
        print("Building blocked by", check_coords(coords) + "!")


def get_next_to(unit_name, direction):
    current_pos = get_pos(unit_name).split(",")
    current_pos_up = current_pos[0] + "," + str((int(current_pos[1]) - 1))
    current_pos_down = current_pos[0] + "," + str((int(current_pos[1]) + 1))
    current_pos_left = str((int(current_pos[0]) - 1)) + "," + current_pos[1]
    current_pos_right = str((int(current_pos[0]) + 1)) + "," + current_pos[1]
    if direction == "up":
        return check_coords(current_pos_up)
    elif direction == "down":
        return check_coords(current_pos_down)
    elif direction == "left":
        return check_coords(current_pos_left)
    elif direction == "right":
        return check_coords(current_pos_right)


def send_stats(food, stone, wood):
    stats = "stats" + " " + str(food) + " " + str(stone) + " " + str(wood)
    s.sendto(stats.encode(), get_client("stats"))


def set_coords(coords, unit_name):
    spawn_message = "set" + " " + coords + " " + unit_name
    s.sendto(spawn_message.encode(), get_client("map"))


def get_enemy_number():
    if player_num == "1":
        return "2"
    elif player_num == "2":
        return "1"


def unit_data_list(unit_name, unit_symbol, unit_health, movement_speed, food_consumption, unit_type, unit_status, damage):
    if unit_name not in unit_data.keys():
        unit_data[unit_name] = [unit_symbol, unit_health, movement_speed,
                                food_consumption, unit_type, unit_status, damage]
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

    s.sendto("unitdata".encode(), get_client("map"))
    s.sendto(json.dumps(unit_data).encode(), get_client("map"))


def remove_unit(unit_name):
    unit_data.pop(unit_name)
    kill_message = "set" + " " + get_pos(unit_name) + " " + "empty"
    s.sendto(kill_message.encode(), get_client("map"))


def move_unit(unit_name, direction, distance_input):
    distance = int(distance_input)
    if direction == "up":
        while distance != 0:
            current_pos = get_pos(unit_name)
            current_pos_list = current_pos.split(",")

            current_pos_up = current_pos_list[0] + \
                "," + str((int(current_pos_list[1]) - 1))
            if get_next_to(unit_name, "up"):
                set_coords(current_pos_up, unit_name)
                set_coords(current_pos, "empty")
                distance -= 1
            else:
                blocked_by = check_coords(current_pos_up)
                print(unit_name.replace("_", "").replace(
                    player_num, "") + " is blocked by " + blocked_by)
                break

    if direction == "down":
        while distance != 0:
            current_pos = get_pos(unit_name)
            current_pos_list = current_pos.split(",")

            current_pos_down = current_pos_list[0] + \
                "," + str((int(current_pos_list[1]) + 1))
            if get_next_to(unit_name, "down") == "empty":
                set_coords(current_pos_down, unit_name)
                set_coords(current_pos, "empty")
                distance -= 1
            else:
                blocked_by = check_coords(current_pos_down)
                print(unit_name.replace("_", "").replace(
                    player_num, "") + " is blocked by " + blocked_by)
                break

    if direction == "left":
        while distance != 0:
            current_pos = get_pos(unit_name)
            current_pos_list = current_pos.split(",")

            current_pos_left = str(
                (int(current_pos_list[0]) - 1)) + "," + current_pos_list[1]
            if get_next_to(unit_name, "left") == "empty":
                set_coords(current_pos_left, unit_name)
                set_coords(current_pos, "empty")
                distance -= 1
            else:
                blocked_by = check_coords(current_pos_left)
                print(unit_name.replace("_", "").replace(
                    player_num, "") + " is blocked by " + blocked_by)
                break

    if direction == "right":
        while distance != 0:
            current_pos = get_pos(unit_name)
            current_pos_list = current_pos.split(",")

            current_pos_right = str(
                (int(current_pos_list[0]) - 1)) + "," + current_pos_list[1]
            if get_next_to(unit_name, "right") == "empty":
                set_coords(current_pos_right, unit_name)
                set_coords(current_pos, "empty")
                distance -= 1
            else:
                blocked_by = check_coords(current_pos_right)
                print(unit_name.replace("_", "").replace(
                    player_num, "") + " is blocked by " + blocked_by)
                break
    time.sleep(unit_data[unit_name][2])


def create_villager(villager_type):
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

        if get_next_to("town_center", "down") == "empty":
            town_center_pos = get_pos("town_center").split(",")
            town_center_spawn = town_center_pos[0] + \
                "," + str(int(town_center_pos[1]) + 1)
            set_coords(town_center_spawn, villager_name)
            if villager_type == "farmer":
                symbol = colored("0", "yellow")
            elif villager_type == "lumberjack":
                symbol = colored("0", "green")
            else:
                symbol = "0"
            unit_data_list(villager_name, symbol, 100,
                           1, -1, villager_type, "idle", 1)
            send_stats(-100, 0, 0)
        else:
            print("Town Center spawn site blocked!")
    else:
        print("Villager limit reached!")


def create_militia():
    militia_name = "militia" + str(militia_num) + "_" + str(player_num)
    if check_exists("barracks") == "yes":
        if get_next_to("barracks", "down") == "empty":
            barracks_pos = get_pos("barracks").split(",")
            barracks_spawn = barracks_pos[0] + \
                "," + str(int(barracks_pos[1]) + 1)
            set_coords(barracks_spawn, militia_name)
            unit_data_list(militia_name, "!", 150, 1, -1,
                           "militia_" + player_num, "idle", 50)
        else:
            print("Barracks spawn site blocked!")
    else:
        print("You must build a barracks to create a militia!")


def create_archer():
    archer_name = "archer" + str(militia_num) + "_" + str(player_num)
    if check_exists("archery") == "yes":
        if get_next_to("archery", "down") == "empty":
            archery_pos = get_pos("archery").split(",")
            archery_spawn = archery_pos[0] + "," + str(int(archery_pos[1]) + 1)
            set_coords(archery_spawn, archer_name)
            unit_data_list(archer_name, ")", 125, 1, -1,
                           "archer_" + player_num, "idle", 25)
        else:
            print("Archery spawn site blocked!")
    else:
        print("You must build a archery to create a archer!")


def create_knight():
    knight_name = "knight" + str(knight_num) + "_" + str(player_num)
    if check_exists("stable") == "yes":
        if get_next_to("stable", "down") == "empty":
            stable_pos = get_pos("stable").split(",")
            stable_spawn = stable_pos[0] + "," + str(int(stable_pos[1]) + 1)
            set_coords(stable_spawn, knight_name)
            unit_data_list(knight_name, "^", 200, 2, -2,
                           "knight_" + player_num, "idle", 100)
        else:
            print("Stable spawn site blocked!")
    else:
        print("You must build a stable to create a knight!")


def create_ram():
    ram_name = "ram" + str(ram_num) + "_" + str(player_num)
    if check_exists("workshop") == "yes":
        if get_next_to("workshop", "down") == "empty":
            workshop_pos = get_pos("workshop").split(",")
            workshop_spawn = workshop_pos[0] + \
                "," + str(int(workshop_pos[1]) + 1)
            set_coords(workshop_spawn, ram_name)
            unit_data_list(ram_name, "=", 100, 1, 0,
                           "ram_" + player_num, "idle", 200)
        else:
            print("Workshop spawn site blocked!")
    else:
        print("You must build a workshop to create a ram!")

# Threads


def consume_food(run_time):
    if run_time % 10 == 0:
        for unit in unit_data:
            if get_stats("food") > 0:
                send_stats(unit_data[unit][3], 0, 0)
            elif unit_data[unit][3] != 0:
                remove_unit(unit)
                print(unit, "was killed by starvation")


def farmer(run_time):
    farmer_amount = 0
    if run_time % 10 == 0:
        for unit_name in unit_data:
            if unit_data[unit_name][3] == "farmer_" + player_num:
                if get_next_to(unit_name, "up") == "farm":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "farming", None)
                    farmer_amount += 1
                if get_next_to(unit_name, "down") == "farm":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "farming", None)
                    farmer_amount += 1
                if get_next_to(unit_name, "left") == "farm":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "farming", None)
                    farmer_amount += 1
                if get_next_to(unit_name, "right") == "farm":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "farming", None)
                    farmer_amount += 1
                else:
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "idle", None)
                    farmer_amount -= 1
        food = 1 * farmer_amount
        send_stats(food, 0, 0)


def lumberjack(run_time):
    lumberjack_amount = 0
    if run_time % 10 == 0:
        for unit_name in unit_data:
            if unit_data[unit_name][3] == "lumberjack_" + player_num:
                if get_next_to(unit_name, "up") == "tree":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "chopping", None)
                    lumberjack_amount += 1
                if get_next_to(unit_name, "down") == "tree":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "chopping", None)
                    lumberjack_amount += 1
                if get_next_to(unit_name, "left") == "tree":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "chopping", None)
                    lumberjack_amount += 1
                if get_next_to(unit_name, "right") == "tree":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "chopping", None)
                    lumberjack_amount += 1
                else:
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "idle", None)
                    lumberjack_amount -= 1
        wood = 1 * lumberjack_amount
        send_stats(0, wood, 0)


def miner(run_time):
    miner_amount = 0
    if run_time % 10 == 0:
        for unit_name in unit_data:
            if unit_data[unit_name][3] == "miner_" + player_num:
                if get_next_to(unit_name, "up") == "stone":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "mining", None)
                    miner_amount += 1
                if get_next_to(unit_name, "down") == "stone":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "mining", None)
                    miner_amount += 1
                if get_next_to(unit_name, "left") == "stone":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "mining", None)
                    miner_amount += 1
                if get_next_to(unit_name, "right") == "stone":
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "mining", None)
                    miner_amount += 1
                else:
                    unit_data_list(unit_name, None, None, None,
                                   None, None, "idle", None)
                    miner_amount -= 1
        stone = 1 * miner_amount
        send_stats(0, 0, stone)


def militia():
    for unit_name in unit_data:
        if unit_data[unit_name][4] == "militia_" + player_num:
            if get_next_to(unit_name, "up").endswith(enemy_num):
                unit_data_list(unit_name, None, None, None,
                               None, None, "fighting", None)
                unit_data[get_next_to(unit_name, "up")][1] -= 50
            elif get_next_to(unit_name, "down").endswith(enemy_num):
                unit_data_list(unit_name, None, None, None,
                               None, None, "fighting", None)
                unit_data[get_next_to(unit_name, "down")][1] -= 50
            elif get_next_to(unit_name, "left").endswith(enemy_num):
                unit_data_list(unit_name, None, None, None,
                               None, None, "fighting", None)
                unit_data[get_next_to(unit_name, "left")][1] -= 50
            elif get_next_to(unit_name, "right").endswith(enemy_num):
                unit_data_list(unit_name, None, None, None,
                               None, None, "fighting", None)
                unit_data[get_next_to(unit_name, "right")][1] -= 50
            else:
                unit_data_list(unit_name, None, None, None,
                               None, None, "idle", None)


def threads():
    run_time = 0
    while True:
        consume_food(run_time)
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
enemy_num = get_enemy_number()
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
            build_request(usr_command[1], usr_command[2])

        elif usr_command[0] == "c":
            if usr_command[1] == "farmer":
                create_villager("farmer")
                farmer_num += 1
                villager_num += 1
            elif usr_command[1] == "lumberjack":
                create_villager("lumberjack")
                lumberjack_num += 1
                villager_num += 1
            elif usr_command[1] == "miner":
                create_villager("miner")
                miner_num += 1
                villager_num += 1
            elif usr_command[1] == "militia":
                create_militia()
                militia_num += 1
            elif usr_command[1] == "archer":
                create_archer()
                archer_num += 1
            elif usr_command[1] == "knight":
                create_knight()
                knight_num += 1
            elif usr_command[1] == "ram":
                create_ram()
                ram_num += 1
            else:
                print("Unknown unit type,", usr_command[1] + "!")

        elif usr_command[0] == "m":
            threading._start_new_thread(
                move_unit, (usr_command[1] + "_" + player_num, usr_command[2], usr_command[3]))

        elif usr_command[0] == "map":
            if usr_command[1] == "stop":
                s.sendto("stop".encode(), get_client("map"))
            elif usr_command[1] == "start":
                s.sendto("start".encode(), get_client("map"))
            elif usr_command[1] == "1":
                s.sendto("map 1".encode(), get_client("map"))
            elif usr_command[1] == "2":
                s.sendto("map 2".encode(), get_client("map"))
            else:
                print(usr_command[1], "is not a valid map command!")

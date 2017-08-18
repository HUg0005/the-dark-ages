import socket
import json
import threading


def startGame():
    for client in client_list.keys():
        s.sendto("start".encode(), client_list[client])


def cli():
    while True:
        # if "map1" in client_list.keys() and "console1" in client_list.keys() \
                # and "stats1" in client_list.keys() and "map2" in \
                # client_list.keys() and "console2" in client_list.keys() and \
                # "stats2" in client_list.keys():
            print("All clients are connected. Type start to start game.")
            usr_input = input("->")
            if usr_input == "start":
                startGame()
                break


host = "127.0.0.1"
try:
    port = int(input("Server port: "))
except:
    print("Invalid port!")
stop = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind((host, port))
    print("Server Started")
    print("Waiting for clients...")
except:
    print("Unable to create server!")
client_list = {}

threading._start_new_thread(cli, ())

while True:
    rawdata, addr = s.recvfrom(1024)
    data = rawdata.decode()
    if data == "getClient":
        clients = "getClientData" + " " + json.dumps(client_list)
        s.sendto(clients.encode(), addr)

    elif data == "map1":
        # print("Map1 connected.")
        client_list["map1"] = addr

    elif data == "console1":
        # print("Console1 connected.")
        client_list["console1"] = addr

    elif data == "stats1":
        # print("Stats1 connected.")
        client_list["stats1"] = addr

    elif data == "map2":
        print("Map2 connected.")
        client_list["map2"] = addr

    elif data == "console2":
        print("Console2 connected.")
        client_list["console2"] = addr

    elif data == "stats2":
        print("Stats2 connected.")
        client_list["stats2"] = addr

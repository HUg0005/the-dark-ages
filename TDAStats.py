import socket


def printStats():
    print("Food: " + str(resources_list["food"]) +
          "  Stone: " + str(resources_list["stone"]) + "  Wood: " + str(
          resources_list["wood"]))


host = input("Server IP: ")
port = int(input("Server Port: "))
player_num = input("Player Number: ")
server = (host, port)

# Connect to Server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("localhost", 0))
    clientid = "stats" + player_num
    s.sendto(clientid.encode(), server)
except:
    print("Cannot find server!")

resources_list = {"food": 150, "wood": 150, "stone": 150}
unit_health_list = {}

print("Waiting for game to start...")
start, addr = s.recvfrom(1024)
if start.decode() == "start":
    while True:
        receved, addr = s.recvfrom(1024)
        data = receved.decode().split()
        if data[0] == "stats":
            resources_list["food"] += int(data[1])
            resources_list["stone"] += int(data[2])
            resources_list["wood"] += int(data[3])
            printStats()

        elif data[0] == "getStats":
            if data[1] == "food":
                s.sendto(str("getStatsData" + " " +
                             resources_list["food"]).encode(), addr)
            elif data[1] == "stone":
                s.sendto(str("getStatsData" + " " +
                             resources_list["stone"]).encode(), addr)
            elif data[1] == "wood":
                s.sendto(str("getStatsData" + " " +
                             resources_list["wood"]).encode(), addr)

import socket


# Print food, wood and stone stats
def printStats():
    print("Food: " + str(resources_list["food"]) +
          "  Stone: " + str(resources_list["stone"]) + "  Wood: " + str(
          resources_list["wood"]))


#  Get server IP address and port
server = (input("Server IP: "), int(input("Server Port: ")))

# Get player number
player_num = input("Player Number: ")

# Connect to Server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("localhost", 0))
    clientid = "stats" + player_num
    s.sendto(clientid.encode(), server)
except:
    print("Cannot find server!")

# Create list containing resources
resources_list = {"food": 150, "wood": 150, "stone": 150}

# Create list containing unit and building health
unit_health_list = {}

# Wait for "start" from server
print("Waiting for game to start...")
start, addr = s.recvfrom(1024)
if start.decode() == "start":
    # Collect data from other clients
    while True:
        receved, addr = s.recvfrom(1024)
        data = receved.decode().split()
        # Get resources from other client and add them to resources_list
        if data[0] == "stats":
            resources_list["food"] += int(data[1])
            resources_list["stone"] += int(data[2])
            resources_list["wood"] += int(data[3])
            printStats()

        # Return resources to client
        elif data[0] == "getStats":
            if data[1] == "food":
                s.sendto(("getStatsData" + " " +
                         str(resources_list["food"])).encode(), addr)
            elif data[1] == "stone":
                s.sendto(("getStatsData" + " " +
                         str(resources_list["stone"])).encode(), addr)
            elif data[1] == "wood":
                s.sendto(("getStatsData" + " " +
                         str(resources_list["wood"])).encode(), addr)

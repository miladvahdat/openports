import socket
# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

valid_characters = "[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.]"

while True:
    target = input("What website to scan?: ")
    if all(char in valid_characters for char in target):
        break
        print("It is valid")
    else:
        print("That's invalid url, please try again.")


def pscan(port):
    try:
        # now connect to the web server on port
        con = serversocket.connect((target, port))
        return True
    except:
        return False


for x in [22, 23,  80, 443]:
    if pscan(x):
        print('Port', x, 'is open')
    else:
        print('Port', x, 'is closed')
try:
    print("IP address of " + target + " is " + socket.gethostbyname(target))
except socket.error as error:
    print("ERROR : {} ".format(error))
if __name__ == "__pscan__":
    pscan()
print("Done")

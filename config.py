import configparser
import sys

from src import printcolors as pc

try:
    config = configparser.ConfigParser(interpolation=None)
    config.read("config/credentials.ini")
except FileNotFoundError:
    pc.printout('Error: file "config/credentials.ini" not found!\n', pc.RED)
    sys.exit(0)
except Exception as e:
    pc.printout("Error: {}\n".format(e), pc.RED)
    sys.exit(0)

def getUsername():
    try:

        username = config["Credentials"]["username"]

        if username == '':
            pc.printout('Username is blank. Please enter your username: ', pc.YELLOW)
            username = input().strip()
            while username == '':
                pc.printout('Username cannot be blank. Please enter your username: ', pc.YELLOW)
                username = input().strip()
            config["Credentials"]["username"] = username
            with open("config/credentials.ini", "w") as configfile:
                config.write(configfile)
        return username
    except KeyError:
        pc.printout('Error: missing "username" field in "config/credentials.ini"\n', pc.RED)
        sys.exit(0)

def getPassword():
    try:

        password = config["Credentials"]["password"]

        if password == '':
            pc.printout('Password is blank. Please enter your password: ', pc.YELLOW)
            password = input().strip()
            while password == '':
                pc.printout('Password cannot be blank. Please enter your password: ', pc.YELLOW)
                password = input().strip()
            config["Credentials"]["password"] = password
            with open("config/credentials.ini", "w") as configfile:
                config.write(configfile)
        return password
    except KeyError:
        pc.printout('Error: missing "password" field in "config/credentials.ini"\n', pc.RED)
        sys.exit(0)

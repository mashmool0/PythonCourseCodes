import socket
import threading

# ذخیره کاربران در فایل txt
USER_DATABASE = "users.txt"


def handle_client(client_socket):
    while True:
        try:
            # دریافت داده‌ها از کلاینت
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            command, payload = data.split("|", 1)

            if command == "REGISTER":
                username, password = payload.split(",")
                if is_user_exists(username):
                    client_socket.send(
                        "REGISTER_FAIL|User already exists".encode('utf-8'))
                else:
                    add_user(username, password)
                    client_socket.send(
                        "REGISTER_SUCCESS|User registered successfully".encode('utf-8'))

            elif command == "LOGIN":
                username, password = payload.split(",")
                if authenticate_user(username, password):
                    client_socket.send("LOGIN_SUCCESS|Welcome".encode('utf-8'))
                else:
                    client_socket.send(
                        "LOGIN_FAIL|Invalid username or password".encode('utf-8'))

        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()


def is_user_exists(username):
    try:
        with open(USER_DATABASE, "r") as file:
            users = file.readlines()
        for user in users:
            if user.split(",")[0] == username:
                return True
    except FileNotFoundError:
        return False
    return False


def add_user(username, password):
    with open(USER_DATABASE, "a") as file:
        file.write(f"{username},{password}\n")


def authenticate_user(username, password):
    try:
        with open(USER_DATABASE, "r") as file:
            users = file.readlines()
        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                return True
    except FileNotFoundError:
        return False
    return False


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8080))
    server.listen(5)
    print("Server started on port 8080")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()

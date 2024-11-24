import socket
import threading
import tkinter as tk
from tkinter import messagebox

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))


def send_request(request):
    client.send(request.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    return response


def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields are required")
        return

    response = send_request(f"REGISTER|{username},{password}")
    status, message = response.split("|", 1)

    if status == "REGISTER_SUCCESS":
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Error", message)


def login_user():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields are required")
        return

    response = send_request(f"LOGIN|{username},{password}")
    status, message = response.split("|", 1)

    if status == "LOGIN_SUCCESS":
        messagebox.showinfo("Success", message)
        root.destroy()  # بعد از ورود موفقیت‌آمیز، پنجره بسته می‌شود
    else:
        messagebox.showerror("Error", message)


# ساخت رابط گرافیکی
root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_register = tk.Button(root, text="Register", command=register_user)
btn_register.pack()

btn_login = tk.Button(root, text="Login", command=login_user)
btn_login.pack()

root.mainloop()

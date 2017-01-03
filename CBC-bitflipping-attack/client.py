import socket

from networking import *
from utils import *


def get_cookie(socket, user_data):
    sendline(socket, user_data)
    recvuntil(socket, "cookie: ")
    return unhex(recvline(socket))


def send_cookie(socket, cookie):
    cookie = enhex(cookie)
    sendline(socket, cookie)


s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1234))

payload = 'asdf'
cookie = get_cookie(s, payload)

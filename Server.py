import socket
import util
import lang_en
import threading


def register(conn):
    code = conn.recv(1024).decode(config_object.encoding)
    message = f"code {code} entered"
    username = conn.recv(1024).decode(config_object.encoding)
    password = conn.recv(1024).decode(config_object.encoding)
    if code == 'login':
        with open('login.txt', 'r') as file:
            f = file.readlines()
            for line in f:
                if line.startswith('username: {} , password: {}'.format(username, password)) is True:
                    g = 'login was successful!'
                    conn.send(g.encode(config_object.encoding))
                    break
            if line.startswith('username: {} , password: {}'.format(username, password)) is False:
                m = 'wrong info'
                conn.send(m.encode(config_object.encoding))
                while True:
                    un = conn.recv(1024).decode(config_object.encoding)
                    p = conn.recv(1024).decode(config_object.encoding)
                    for lin in f:
                        if lin.startswith('username: {} , password: {}'.format(un, p)) is True:
                            c = 'login was successful!'
                            conn.send(c.encode(config_object.encoding))
                            break
    else:
        with open('login.txt', 'r') as file:
            f = file.readlines()
            while True:
                if 'username: {} , password: {}\n'.format(username, password) in f:
                    m = 'info already exists.change your username or password please.'
                    conn.send(m.encode(config_object.encoding))
                    username = conn.recv(1024).decode(config_object.encoding)
                    password = conn.recv(1024).decode(config_object.encoding)
                else:
                    with open('login.txt', 'a') as fil:
                        fil.write('username: {} , password: {}\n'.format(username, password))
                        c = 'sign up was successful!'
                        conn.send(c.encode(config_object.encoding))
                        break


def broadcast(msg):
    for each in li_st:
        each.send(msg.encode('ascii'))


def handle(conn):
    while True:
        msg = conn.recv(1024).decode("ascii")
        broadcast(msg)


def chat():
    while True:
        conn, addr = server.accept()
        li_st.append(conn)
        register(conn)
        t = threading.Thread(target=handle, args=(conn,))
        t.start()


if __name__ == '__main__':
    config_data = util.read_config_data()
    config_object = util.Config(config_data)
    # defining variables
    names = list()
    li_st = list()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((config_object.host, config_object.port))
    server.listen()
    a = threading.Thread(target=chat())
    a.start()

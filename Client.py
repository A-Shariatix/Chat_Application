import socket
from util import Config, read_config_data
import threading
  def login():
username = input('Enter your username : ')
password = input('Enter your password : ')
client.send(username.encode(config_object.encoding))
client.send(password.encode(config_object.encoding))
  def chat():
while True:
m = '{}: {}'.format(name, input())
client.send(m.encode(config_object.encoding))
  def receive():
while True:
m = client.recv(1024).decode(config_object.encoding)
print(m)
  if __name__ == '__main__':
config_data = read_config_data()
config_object = Config(config_data)
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((config_object.host, config_object.port))
  name = input('Enter your name skinny bitch : ')
client.send(name.encode(config_object.encoding))
message = client.recv(1024).decode('ascii')
print(message)
t = threading.Thread(target=chat)
t.start()
t_1 = threading.Thread(target=receive)
t_1.start()

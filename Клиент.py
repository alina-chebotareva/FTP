import socket
HOST = 'localhost'
PORT = 6876
commands = {'pwd': 'show the name of a working directory',
            'lst': 'show the content of a working directory',
            'cat <filename>': 'receive a content of a file',
            'crt <dirname>': 'create a new directory',
            'crf <filename> [text to write]': 'create a new file',
            'rem <dirname>': 'delete a directory',
            'ref <filename>': 'delete a file',
            'ren <filename> [newfilename]': 'rename a file',
            'cup': 'move to upper directory',
            'chd <dirname>': 'move to <dirname>',
            'get <filename>': 'recieve a file',
            'STOP': 'disconnect server'
            }
while True:
    print("Список команд:")
    delimiter = '\n'
    request = input('>')
    if request == 'STOP':
        break
    else:
        sock = socket.socket()
        sock.connect((HOST, PORT))
        sock.send(request.encode())
        response = sock.recv(1024).decode()
        print(response)
    if request[:3] == 'get':
        f = open('test.txt', 'w')
        f.write(response)
        f.close()
    sock.close()
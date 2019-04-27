import socket
from rsa import get_decrypted_message
from sudoku import solved_sudoku, decrypt_sudoku
from config import *
import json

def start_server():

    mySocket = socket.socket()
    mySocket.bind((HOST, PORT))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print('Connection from: ' + str(addr))
    while True:
        data = conn.recv(20480).decode()
        if not data:
            break

        data = json.loads(data) 
        print('Server: Data sent by client =>' + str(data))
        print('Server: Decrypting message..')
        
        decrypted_message = []
        for element in data:
            decrypted_element = get_decrypted_message(message=str(element))
            print(decrypted_element[1:])
            decrypted_message.append(decrypted_element[1:])
        

        decrypted_message = decrypt_sudoku(solved_sudoku, decrypted_message)
        
        print(f'Server: Message => {decrypted_message}')

        acknoledgement = 'Message successfully received by Server.'
        print(f'Sending: {acknoledgement}')
        conn.send(acknoledgement.encode())

    conn.close()


if __name__ == '__main__':
    start_server()

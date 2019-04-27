import socket
from rsa import get_encrypted_message, get_decrypted_message
from sudoku import encrpyt_sudoku, solved_sudoku
import json
from config import *


def create_client():
    socket_conn = socket.socket()
    socket_conn.connect((HOST, PORT))

    message = input(' -> ')
    sudoku_encrypted = encrpyt_sudoku(solved_sudoku, message)
    encrypted_message = []
    for element in sudoku_encrypted:
        # print('A' + str(element))
        _encrypt = str(get_encrypted_message('A' + str(element)))
        encrypted_message.append(_encrypt)
    encrypted_message_json = json.dumps(encrypted_message)

    while message != 'q':
        socket_conn.send(encrypted_message_json.encode())
        print(f'Client: Sent encrypted message => {encrypted_message_json}')
        data = socket_conn.recv(1024).decode()
        
        print ('Client: ' + data)
        
        message = input(' -> ')
        sudoku_encrypted = encrpyt_sudoku(solved_sudoku, message)
        encrypted_message = []
        for element in sudoku_encrypted:
            encrypted_message.append(str(get_encrypted_message('A' + str(element))))
        encrypted_message_json = json.dumps(encrypted_message)
      
    socket_conn.close()

if __name__ == '__main__':
	create_client()

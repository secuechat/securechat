#!/usr/bin/env python3
import ssl
import socket

#host=input("enter_iP:")
context=ssl.create_default_context()
context.load_verify_locations('/home/kali/Downloads/newcert2.pem')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    with(context.wrap_socket(sock,server_hostname="localhost"))as ssock:
        ssock.connect(("localhost",10000))
        print("________________________________________________________CONNECTED___________________________________________________________________________________")
        while True:
            try:
                send = input("")
                ssock.send(send.encode('ascii'))
                r_text = ssock.recv(1024)
                print("server: ", r_text.decode('ascii'))
            except KeyboardInterrupt:
                print("\n**********************************CONNECTION WAS FORCEFULLY TERMINATED *********************************************************")
                ssock.close()
                quit()

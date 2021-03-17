#!/usr/bin/env python3
import ssl
import socket
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
try:
    context.load_cert_chain('/home/kali/Downloads/newcert2.pem', '/home/kali/Downloads/newkey2.pem')
except :
    pass
localhost="127.0.1.1"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    h_name = socket.gethostname()
    host =localhost
    print(host)
    sock.bind(("localhost", 10000))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print("________________________________________________________CONNECTED___________________________________________________________________________________")
        while True:
            try:
                r_text=conn.recv(1024)
                print("client:",r_text.decode('ascii'))
                send=input("")
                conn.send(send.encode('ascii'))
            except KeyboardInterrupt:
                print("\n**********************************CONNECTION WAS FORCEFULLY TERMINATED *********************************************************")
                ssock.close()
                quit()
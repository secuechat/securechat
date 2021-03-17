import socket
import threading
import os
from tqdm import tqdm

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
h_name=input("ENTER YOUR NAME:")
port=10000
host=input("ENTER THE ADDRESS OF tHE HOST TO GET CONNECTED:")
print("**************connecting****************")
print("________________________________________")
conn.connect((host,port))
conn.send(h_name.encode('ascii'))
server_name=conn.recv(1024).decode('ascii')
print("********************connected**********************")
print("***YOU CAN START TYPING YOUR MESSAGE.FOR FILE SHARING ENTER <FILE_SHARE> TO ENABLE FILESHARE***")
def send():
    while (1):
        message = input()
        if(message=="quit"):
            quit()
        if (message == "FILE_SHARE"):
            conn.send(message.encode('ascii'))
            thread = threading.Thread(target=file_send)
            thread.daemon = True
            thread.start()
        else:
            conn.send(message.encode('ascii'))
            print()

def file_send():
    f_name=input("ENTER THE NAME OF THE FILE")
    conn.send(f_name.encode('ascii'))
    with open(f_name,"rb") as fil:
        content=fil.read()
        conn.sendall(content)



thread=threading.Thread(target=send)
thread.daemon=True
thread.start()



for mess in iter(lambda :conn.recv(4029).decode('ascii'),''):
    if(mess=="FILE_SHARE"):
        recieved_file_name=conn.recv(1024).decode('ascii')
        r_filesize=int(conn.recv(4029).decode('ascii'))
        progress = tqdm(total=r_filesize, desc=f"Receiving {recieved_file_name}", unit="KB")
        with open(recieved_file_name,"wb") as fil:
            r_content=conn.recv(r_filesize)
            fil.write(r_content)
            progress.update(len(r_content))
    else:print("\n"+"    "+server_name+":"+mess)



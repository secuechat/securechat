import socket
import threading
import os
from tqdm import tqdm


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=input("ENTER YOUR NAME:")
port=10000
host="0.0.0.0"
h_name=socket.gethostname()
h_addr=socket.gethostbyname(h_name)
print("The server has got address {}".format(h_addr))
sock.bind((host,port))
sock.listen(1)
conn,addr=sock.accept()
print("**************connecting****************")
client_name=conn.recv(1204).decode()
conn.send(name.encode('ascii'))
print("__________connected to {}_______________".format(client_name))
def send():
    while(1):
        message=input()
        if(message=="quit"):
            quit()
        if(message=="FILE_SHARE"):
            conn.send(message.encode('ascii'))
            #thread = threading.Thread(target=file_send)
            #thread.daemon = True
            #thread.start()
            file_send()
        else:
            conn.send(message.encode('ascii'))
            print()

def file_send():
    f_name=input("***ENTER THE NAME OF THE FILE")
    conn.send(f_name.encode('ascii'))
    filesize = os.path.getsize(f_name)
    conn.send(str(filesize).encode('ascii'))
    progress = tqdm(total=filesize, desc=f"sending {f_name}", unit="KB")
    with open(f_name,"rb") as fil:
        content=fil.read(filesize)
        conn.send(content)
        fil.close()
        progress.update(len(content))



thread=threading.Thread(target=send)
thread.daemon=True
thread.start()

'''def recv():
    print("RECIEVING")
    recieved_file_name=conn.recv(4029).decode('ascii')
    with open(recieved_file_name, "wb") as r_file:
        while True:
            recieved_content = conn.recv(4029)
            if(not recieved_content):
                print("recieved file {} ".format(recieved_file_name))
                break
            r_file.write(recieved_content)'''


for mess in iter(lambda :conn.recv(4029).decode('ascii'),''):
    if (mess == "FILE_SHARE"):
        recieved_file_name=conn.recv(1024).decode('ascii')
        with open(recieved_file_name,"wb") as fil:
            while(1):
                r_content=conn.recv(4029)
                if(not r_content):
                    break
                fil.write(r_content)
    else:print("\n"+"    "+client_name+":"+mess)

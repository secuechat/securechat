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
    progress = tqdm(range(filesize), desc=f"SENDING {f_name}", unit="KB")
    with open(f_name,"rb") as fil:
        while(True):
            content=fil.read(1024)
            if(not content):
                conn.send("completed".encode('ascii'))
                print("\n SENT_SUCCESSFULLY------------------>")
                fil.close()
                break
            else:
                conn.send(content)
            progress.update(len(content))



thread=threading.Thread(target=send)
thread.daemon=True
thread.start()


for mess in iter(lambda :conn.recv(1029).decode('ascii'),''):
    if (mess == "FILE_SHARE"):
        recieved_file_name = conn.recv(1024).decode('ascii')
        r_filesize = int(conn.recv(1024).decode('ascii'))
        with open(recieved_file_name, "wb") as fil:
            progress = tqdm(range(r_filesize), desc=f"Receiving {recieved_file_name}", unit="KB")
            while (True):
                r_content = conn.recv(1024)
                if (r_content.decode('ascii')== "completed"):
                    print(f"\n RECIEVED FILE {recieved_file_name}")
                    fil.close()
                    progress.update(len(r_content))
                    break
                else:
                    fil.write(r_content)
                progress.update(len(r_content))
    else:
        print("\n" + "    " + client_name + ":" + mess)completedhihi
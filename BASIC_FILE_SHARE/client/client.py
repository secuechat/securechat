import socket
import tqdm
import os
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=10000
host=input("ENTER THE IP ADDRESS:")
sock.connect((host,port))
print("-----------------------CONNECTION ESTABLISHED-------------------------------------------------------------------------------->")
f_name=input("ENTER THE NAME OF FILE TO SEND:")
f_size=os.path.getsize(f_name)
sock.send(str(f_size).encode('ascii'))
sock.send(f_name.encode('ascii'))
progress=tqdm.tqdm(range(f_size),desc=f"recieving {f_name}",unit_scale=True,unit_divisor=1027,unit="KB")
with open(f_name,"rb") as file:
    while True:
        content=file.read(1024)
        if(not content):
            sock.send("COMPLETED...".encode('ascii'))
            break
        sock.send(content)
        progress.update(len(content))
print("TRANSFFERED SUCCESSFULLY-------------------------->")

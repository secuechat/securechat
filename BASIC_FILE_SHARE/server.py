import socket
import tqdm
import os


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

h_name=socket.gethostname()
host=socket.gethostbyname(h_name)
port=10000
print("ip address of the SERVER:",host)
sock.bind((host,port))
sock.listen(1)
conn,addr=sock.accept()
f_size=int(conn.recv(1024).decode('ascii'))
f_name=conn.recv(1024).decode('ascii')
f=open(f_name,"wb")
progress=tqdm.tqdm(range(f_size),desc=f"recieving {f_name}",unit_scale=True,unit_divisor=1027,unit="KB")
for mess in iter(lambda :conn.recv(1024),""):
    if(mess.decode('ascii')=="COMPLETED..."):
        f.close()
        conn.close()
        break
    else:
        f.write(mess)
    progress.update(len(mess))
print("RECIEVED-------------------------------------->")

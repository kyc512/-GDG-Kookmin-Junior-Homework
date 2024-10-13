import socket

def create_list():
    return["김예찬", "미래모빌리티학과", "20223428"]

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #소켓생성
    sock.connect(("localhost",9876)) #접속시도(호스트,포트)

    data_list = create_list()  #리스트 생성
    sock.sendall(str(data_list).encode()) #데이터 송신
    
    data = sock.recv(1024).decode() #서버에서 딕셔너리 수신
    received_dict = eval(data)
    print(f"### Recv {received_dict}")
    
    sock.close() #접속 종료
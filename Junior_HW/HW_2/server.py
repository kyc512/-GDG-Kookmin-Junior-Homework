import socket

def  list_to_dict(data_list):
    keys = ["이름", "학과", "학번"]
    return dict(zip(keys, data_list)) #리스트를 딕셔너리로 변환


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 생성
    sock.bind(("localhost",9876)) #바인딩
    sock.listen(1) #접속 대기

    c_sock, addr = sock.accept() #접속 수락

    read_data = c_sock.recv(1024).decode() #데이터 수신
    received_list = eval(read_data) #문자열을 리스트로 변환
    print(f"### Send {received_list}")

    converted_dict = list_to_dict(received_list) #리스트를 딕셔너리로 변환
    
    c_sock.sendall(str(converted_dict).encode()) # 딕셔너리를 문자열로 변환 후 송신
    
    c_sock.close() #클라이언트 소켓 종료 
    sock.close() #서버 소켓 종료
import socket

def get_port_and_host():
    host = input("Введите имя хоста (по умолчанию 'localhost'): ") or 'localhost'
    port = int(input("Введите номер порта (по умолчанию 65432): ") or 65432)
    return host, port

def start_server(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Сервер запущен и слушает порт", port)

        while True:
            conn, addr = s.accept()
            with conn:
                print("Подключение от", addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    message = data.decode()
                    print("Получены данные от клиента:", message)
                    if message.lower() == "exit":
                        print("Клиент запросил разрыв соединения:", addr)
                        break
                    conn.sendall(data)
                    print("Данные отправлены клиенту:", message)
                print("Клиент отключен:", addr)

if __name__ == "__main__":
    host, port = get_port_and_host()
    start_server(host, port)

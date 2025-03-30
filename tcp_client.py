import socket

def start_client(host='localhost', port=11111):
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Успешное соединение с сервером!")

        # Читаем строку с клавиатуры
        message = input("Напишите сообщение для отправки его на сервер: ")
        s.sendall(message.encode())
        print("Данные отправлены серверу: ", message)

        data = s.recv(1024)
        print("Получены данные от сервера: ", data.decode())

if __name__ == "__main__":
    start_client()

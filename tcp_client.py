import socket
import logging

def get_port_and_host():
    host = input("Введите имя хоста (по умолчанию 'localhost'): ") or 'localhost'
    port = int(input("Введите номер порта (по умолчанию 65432): ") or 65432)
    return host, port

def setup_logger():
    logging.basicConfig(filename='server.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s')

def start_server(host='localhost', port=65432):
    setup_logger()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        logging.info(f"Сервер запущен и слушает порт {port}")

        while True:
            conn, addr = s.accept()
            with conn:
                logging.info(f"Подключение от {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    message = data.decode()
                    logging.info(f"Получены данные от клиента: {message}")
                    if message.lower() == "exit":
                        logging.info(f"Клиент запросил разрыв соединения: {addr}")
                        break
                    conn.sendall(data)
                    logging.info(f"Данные отправлены клиенту: {message}")
                logging.info(f"Клиент отключен: {addr}")

if __name__ == "__main__":
    host, port = get_port_and_host()
    start_server(host, port)

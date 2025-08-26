import socket
import threading
import sys

def recibir_mensaje(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                print("\nConexión cerrada por el servidor")
                sock.close()
                sys.exit(0)
            print(f"\nServidor dice: {data}")
        except:
            print("\nError en la conexión con el servidor")
            sock.close()
            sys.exit(1)

def client_main():
    host = input("Ingrese la IP del servidor: ")
    port = 12345
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        
        print("Conectado al servidor")
        print("Escriba 'exit' para salir")
        
        # Hilo para recibir mensajes
        receive_thread = threading.Thread(target=recibir_mensaje, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()
        
        while True:
            msg = input()
            if msg.lower() == 'exit':
                client_socket.send(msg.encode('utf-8'))
                client_socket.close()
                sys.exit(0)
            try:
                client_socket.send(msg.encode('utf-8'))
            except:
                print("Error al enviar mensaje")
                client_socket.close()
                sys.exit(1)
                
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor")
    finally:
        client_socket.close()

if __name__ == "__main__":
    client_main()
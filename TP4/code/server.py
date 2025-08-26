import socket
import threading
import sys

def handle_client(conn, addr):
    print(f"\nCliente {addr} conectado.")
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if not data or data.lower() == 'exit':
                print(f"\nCliente {addr} se ha desconectado.")
                conn.close()
                return
            print(f"\nCliente {addr} dice: {data}")
        except:
            print(f"\nError con cliente {addr}. Desconectando...")
            conn.close()
            return

def server_main():
    host = '0.0.0.0'  # Escucha en todas las interfaces
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"Servidor iniciado en {host}:{port}. Esperando conexiones...")
    print("Escriba 'exit' para cerrar el servidor cuando no haya clientes conectados")
    
    client_connected = False
    current_conn = None
    shutdown_flag = False
    
    # Hilo para manejar entrada del servidor
    def server_input():
        nonlocal client_connected, current_conn, shutdown_flag
        while True:
            msg = input()
            if msg.lower() == 'exit':
                if client_connected:
                    print("No es posible cerrar el proceso servidor si hay un cliente conectado")
                else:
                    print("Cerrando servidor...")
                    shutdown_flag = True
                    if current_conn:
                        current_conn.close()
                    server_socket.close()
                    sys.exit(0)
            elif client_connected and current_conn:
                try:
                    current_conn.sendall(msg.encode('utf-8'))
                except:
                    print("Error al enviar mensaje al cliente")
    
    input_thread = threading.Thread(target=server_input)
    input_thread.daemon = True
    input_thread.start()
    
    try:
        while not shutdown_flag:
            # Aceptar nueva conexión con timeout para verificar shutdown_flag
            server_socket.settimeout(1.0)  # Timeout de 1 segundo
            try:
                conn, addr = server_socket.accept()
            except socket.timeout:
                continue  # Volver a verificar shutdown_flag
            
            client_connected = True
            current_conn = conn
            
            # Hilo para manejar cliente
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.daemon = True
            client_thread.start()
            client_thread.join()  # Esperar a que el cliente se desconecte
            
            client_connected = False
            current_conn = None
            print("Esperando nueva conexión...")
            
    except KeyboardInterrupt:
        print("\nServidor terminado por el usuario")
    except Exception as e:
        print(f"\nError en el servidor: {e}")
    finally:
        server_socket.close()
        sys.exit(0)

if __name__ == "__main__":
    server_main()
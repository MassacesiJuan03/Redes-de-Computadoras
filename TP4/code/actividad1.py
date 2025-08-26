import socket
import threading
import time

def recibir(sock, username):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            mensaje = data.decode('utf-8')
            
            if ':' not in mensaje:
                continue
                
            usuario, contenido = mensaje.split(':', 1)
            
            if contenido == 'exit':
                print(f"\nEl usuario {usuario} ({addr[0]}) ha abandonado la conversación")
                continue
            elif contenido == 'nuevo':
                print(f"\nEl usuario {usuario} se ha unido a la conversación")
                continue
                
            print(f"\n{usuario} ({addr[0]}) dice: {contenido}\n{username}> ", end='')
            
        except Exception as e:
            print(f"\nError al recibir mensaje: {e}")
            break

def enviar(sock, username):
    # Notificar a los demás que un nuevo usuario se ha unido
    sock.sendto(f"{username}:nuevo".encode('utf-8'), ('255.255.255.255', 60000))
    
    while True:
        mensaje = input(f"{username}> ")
        
        if mensaje.lower() == 'exit':
            sock.sendto(f"{username}:exit".encode('utf-8'), ('255.255.255.255', 60000))
            print("Saliendo del chat...")
            time.sleep(1)  # Dar tiempo para que el mensaje se envíe
            break
            
        sock.sendto(f"{username}:{mensaje}".encode('utf-8'), ('255.255.255.255', 60000))

def main():
    username = input("Ingresa tu nombre de usuario: ")
    
    # Configurar el socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(('0.0.0.0', 60000))
    
    # Crear hilos para enviar y recibir
    hilo_recepcion = threading.Thread(target=recibir, args=(sock, username))
    hilo_recepcion.daemon = True
    hilo_recepcion.start()
    
    hilo_envio = threading.Thread(target=enviar, args=(sock, username))
    hilo_envio.start()
    
    hilo_envio.join()  # Esperar a que termine el hilo de envío
    
    # Limpieza
    sock.close()
    print("Chat finalizado correctamente.")

if __name__ == "__main__":
    main()

import socket

class UDPClient:
    MAX_SIZE = 4096
    SERVER_PORT = 9001
    
    def __init__(self, server_address=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = server_address if server_address else "0.0.0.0"
        
        local_port = 9050
        self.sock.bind(('0.0.0.0', local_port))
        
    def send_and_receive(self, msg):
        try:
            message = msg.encode()
            print(f"Sending: {message}")
            
            self.sock.sendto(message, (self.server_address, self.SERVER_PORT))

            print("Waiting to receive response...")
            data, _ = self.sock.recvfrom(self.MAX_SIZE)
            
            print(f"Received {data}")
            
        finally:
            print("Closing socket")
            self.sock.close()
            
if __name__ == "__main__":
    client = UDPClient()
    client.send_and_receive("Hello from client")
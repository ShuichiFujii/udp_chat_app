import socket

class UDPServer:
    MAX_SIZE = 4096
    
    def __init__(self):
        self.IP_address = "0.0.0.0"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_port = 9001
        
        print(f"Starting up on port {self.server_port}")
        
        self.sock.bind((self.IP_address, self.server_port))
        
    def run(self):
        try:
            while True:
                print("\nWaiting to receive message\n")
                
                data, address = self.sock.recvfrom(self.MAX_SIZE)
                
                print(f"Received {len(data)} bytes from {address}")
                print(data)
                
                if data:
                    response = "Hello from server"
                    sent = self.sock.sendto(response.encode(), address)
                    print(f"Sent {sent} bytes back to {address}")
                    
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            
        finally:
            self.sock.close()
                
                
if __name__ == "__main__":
    server = UDPServer()
    server.run()
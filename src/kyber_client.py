import socket
from kyber512_sim import Kyber512Sim  # Yine dosya adını doğru aldık

HOST = '127.0.0.1'
PORT = 65432

kem = Kyber512Sim()

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # 1. Public Key al
        public_key = s.recv(1024)
        print("[<] Public key alındı.")

        # 2. Şifreleme (ciphertext, shared secret üret)
        ciphertext, shared_secret = kem.encrypt(public_key)
        print(f"[✓] Shared secret (client): {shared_secret.hex()}")

        # 3. Ciphertext gönder
        s.sendall(ciphertext)
        print("[>] Ciphertext gönderildi.")

if __name__ == "__main__":
    start_client()

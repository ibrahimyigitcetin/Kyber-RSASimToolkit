import socket
import threading
from kyber512_sim import Kyber512Sim  # Burada dosya adını doğru referans ediyoruz

HOST = '127.0.0.1'
PORT = 65432

kem = Kyber512Sim()
public_key, secret_key = kem.keygen()

def handle_client(conn, addr):
    print(f"[+] {addr} bağlandı.")

    # 1. Public Key gönder
    conn.sendall(public_key)
    print("[>] Public key gönderildi.")

    # 2. Ciphertext al
    ciphertext = conn.recv(1024)
    print("[<] Ciphertext alındı.")

    # 3. Şifre çözme (shared secret üretimi)
    shared_secret = kem.decrypt(ciphertext, secret_key)
    print(f"[✓] Shared secret (server): {shared_secret.hex()}")

    conn.close()
    print(f"[-] {addr} bağlantısı kapatıldı.")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[⚡] Sunucu {HOST}:{PORT} dinleniyor...")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()

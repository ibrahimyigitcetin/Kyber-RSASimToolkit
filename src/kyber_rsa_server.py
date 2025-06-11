import socket
from crypto_module import Kyber512Sim, RSASim

ALGO = "kyber"  # Değiştirilebilir: "rsa" / "kyber"
PORT = 65432

algo = Kyber512Sim() if ALGO == "kyber" else RSASim()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', PORT))
    s.listen()
    print(f"[🔌] Sunucu dinlemede ({ALGO.upper()} modu)...")
    conn, addr = s.accept()
    with conn:
        print(f"[+] Bağlantı: {addr}")
        pk, sk = algo.keygen()
        conn.sendall(pk)
        ct = conn.recv(2048)
        ss = algo.decrypt(ct, sk)
        print(f"[🔐] Shared Secret (Server): {ss.hex()}")

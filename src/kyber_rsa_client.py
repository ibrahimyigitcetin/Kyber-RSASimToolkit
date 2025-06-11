import socket
from crypto_module import Kyber512Sim, RSASim

ALGO = "kyber"  # Değiştirilebilir: "rsa" / "kyber"
PORT = 65432

algo = Kyber512Sim() if ALGO == "kyber" else RSASim()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', PORT))
    pk = s.recv(2048)
    ct, ss = algo.encrypt(pk)
    print(f"[🔐] Shared Secret (Client): {ss.hex()}")
    s.sendall(ct)

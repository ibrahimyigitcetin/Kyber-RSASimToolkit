import os
import psutil
from kyber512_sim import Kyber512Sim

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024  # KB

print("=== Bellek Kullanımı Testi ===")
kem = Kyber512Sim()

mem_before = memory_usage()
pk, sk = kem.keygen()
mem_after_keygen = memory_usage()

ct, ss = kem.encrypt(pk)
mem_after_encrypt = memory_usage()

ss2 = kem.decrypt(ct, sk)
mem_after_decrypt = memory_usage()

print(f"Anahtar üretimi sonrası bellek: {mem_after_keygen:.2f} KB")
print(f"Şifreleme sonrası bellek: {mem_after_encrypt:.2f} KB")
print(f"Şifre çözme sonrası bellek: {mem_after_decrypt:.2f} KB")

from kyber512_sim import Kyber512Sim

print("=== Çıktı Boyutu Testi ===")
kem = Kyber512Sim()

pk, sk = kem.keygen()
ct, ss = kem.encrypt(pk)
ss_dec = kem.decrypt(ct, sk)

print(f"Public Key boyutu: {len(pk)} byte")
print(f"Secret Key boyutu: {len(sk)} byte")
print(f"Ciphertext boyutu: {len(ct)} byte")
print(f"Shared Secret boyutu: {len(ss)} byte")

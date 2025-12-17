#!/usr/bin/env python3

"""The script recovers an unknown 8-byte XOR key using the known PNG header, 
then XORs the entire encrypted file with that key to restore the original image."""


from pathlib import Path

enc_path = Path("encrypted.xpng")   # change name if needed
dec_path = Path("decrypted.png")

# Known PNG header bytes
png_header = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

# Read encrypted file
data = enc_path.read_bytes()

if len(data) < 8:
    raise SystemExit("File is too small to be a PNG.")

# Recover 8-byte XOR key from first 8 bytes
key = bytes([data[i] ^ png_header[i] for i in range(8)])
print("Recovered key bytes:", key)
print("Recovered key (repr):", repr(key))

# Decrypt whole file
dec = bytearray(len(data))
for i, c in enumerate(data):
    dec[i] = c ^ key[i % len(key)]

# Write decrypted PNG
dec_path.write_bytes(dec)
print("Wrote decrypted PNG to:", dec_path)

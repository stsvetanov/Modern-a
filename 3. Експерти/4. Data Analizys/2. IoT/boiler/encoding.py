# bytearray to string python
import bitstring

b = bytearray("test", encoding="utf-8")

print(b)
print(b.decode())


f1 = bitstring.BitArray(float=1.0, length=32)
print(f1.bin)
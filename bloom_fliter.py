import pyhash
bit_vector = [0] * 20
# Non cryptographic hash function(Murmur and FNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# Calcutes the amount of FNV and hash function for pickchu and charmarder
fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikacha") % 20
murmur_char = murmur("Charmander") % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1

bit_vector[fnv_char] = 1
bit_vector[murmur_pika] = 1

fnv_bulb = fnv("Bulbasur") % 20
murmur_bulb  = murmur("Bulbasur") % 20

print(fnv_bulb)
print(murmur_bulb)


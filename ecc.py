import random

# =========================
# PARAMETER KURVA
# y^2 = x^3 + ax + b mod p
# =========================

p = 97
a = 2
b = 3

G = (3, 6)  # Generator point


# =========================
# MODULAR INVERSE
# =========================
def mod_inverse(k, p):
    return pow(k, -1, p)


# =========================
# POINT ADDITION
# =========================
def point_addition(P, Q):

    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if P == Q:
        # Point doubling
        s = ((3 * x1 * x1 + a) * mod_inverse(2 * y1, p)) % p
    else:
        # Point addition
        s = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p

    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p

    return (x3, y3)


# =========================
# SCALAR MULTIPLICATION
# =========================
def scalar_multiplication(k, P):

    result = None
    addend = P

    while k:
        if k & 1:
            result = point_addition(result, addend)

        addend = point_addition(addend, addend)
        k >>= 1

    return result


# =========================
# KEY GENERATION
# =========================
def generate_keys():

    private_key = random.randint(1, p-1)

    public_key = scalar_multiplication(private_key, G)

    return private_key, public_key


# =========================
# ENCRYPTION
# =========================
def encrypt(message_point, public_key):

    k = random.randint(1, p-1)

    C1 = scalar_multiplication(k, G)

    C2 = point_addition(
        message_point,
        scalar_multiplication(k, public_key)
    )

    return C1, C2


# =========================
# DECRYPTION
# =========================
def decrypt(C1, C2, private_key):

    shared = scalar_multiplication(private_key, C1)

    x, y = shared
    inverse_shared = (x, (-y) % p)

    message = point_addition(C2, inverse_shared)

    return message


# =========================
# DEMO PROGRAM
# =========================

print("=== ECC DEMONSTRATION ===\n")

# Key Generation
private_key, public_key = generate_keys()

print("Private Key :", private_key)
print("Public Key  :", public_key)


# Message (representasi sebagai titik)
message = (10, 7)

print("\nOriginal Message Point :", message)

# Encryption
C1, C2 = encrypt(message, public_key)

print("\nCiphertext")
print("C1 :", C1)
print("C2 :", C2)

# Decryption
decrypted = decrypt(C1, C2, private_key)

print("\nDecrypted Message :", decrypted)
# NTRU Lattice-Based Public Key Cryptography System

## Project Overview

This project presents an implementation of an NTRU-inspired public key encryption system using polynomial arithmetic and modular algebra in Python. The system demonstrates the fundamental concepts of lattice-based cryptography, including key generation, encryption, decryption, and message verification.

NTRU is a post-quantum cryptographic algorithm that relies on the hardness of lattice problems, making it a promising alternative to traditional cryptographic systems in the era of quantum computing.

---

## Objectives

- Understand the fundamentals of lattice-based cryptography.
- Implement an NTRU-inspired encryption and decryption workflow.
- Explore polynomial arithmetic in finite fields.
- Demonstrate public key cryptography using polynomial rings.
- Study the importance of parameter selection in NTRU systems.

---

## Features

- Polynomial-based key generation
- Public and private key creation
- Message encryption
- Message decryption
- Center lifting operation
- Modular polynomial reduction
- Decryption verification
- Error handling for non-invertible polynomials

---
## Cryptographic Concepts

- Lattice-Based Cryptography
- NTRU Cryptosystem
- Polynomial Rings
- Modular Arithmetic
- Finite Fields GF(p) and GF(q)
- Public Key Cryptography
- Post-Quantum Cryptography

---

## System Workflow

### Key Generation

1. Select parameters n, p and q.
2. Choose private polynomials f and g.
3. Compute inverses:
   - fp = f⁻¹ mod p
   - fq = f⁻¹ mod q
4. Generate public key:

h = p × fq × g (mod q)

### Encryption

For message polynomial m and random polynomial r:

e = r × h + m (mod q)

### Decryption

Step 1:

a = f × e (mod q)

Step 2:

b = a (mod p)

Step 3:

c = b × fp (mod p)

The decrypted polynomial c should match the original message polynomial m.

---

## Sample Input

```text
Enter n: 5
Enter p: 3
Enter q: 31

Enter f coefficients:
-1 1 1 1 -1

Enter g coefficients:
0 1 1 0 -1

Enter m coefficients:
1 0 1 1 0

Enter r coefficients:
-1 0 1 0 1
```

---

## Sample Output

```text
Public Key h:
17*x + 17

Encrypted Message e:
15*x^4 + 17*x^3 + 18*x^2 + 18*x

Decrypted Message:
x^4 + x^2 + x

Result:
Decryption Successful
```

---

## Test Cases

### Test Case 1

```text
n = 5
p = 3
q = 31

f = -1 1 1 1 -1
g = 0 1 1 0 -1
m = 1 0 1 1 0
r = -1 0 1 0 1
```

Expected Result:

```text
Decryption Successful
```

### Test Case 2

```text
n = 7
p = 3
q = 41

f = 1 0 -1 1 0 1 -1
g = -1 1 0 0 1 -1 1
m = 1 0 2 1 0 1 2
r = 0 1 -1 1 0 -1 1
```

Expected Result:

```text
Decryption Successful
```

### Test Case 3

```text
n = 5
p = 3
q = 37

f = 1 0 1 1 -1
g = 1 -1 0 1 0
m = 2 1 0 1 2
r = 0 1 1 -1 0
```

Expected Result:

```text
Decryption Successful
```

---

## Limitations

- This is a simplified educational implementation of the NTRU cryptosystem.
- Successful decryption depends on suitable parameter selection.
- Secure parameter generation is not automated.
- The implementation has not been tested against practical cryptographic attacks.
- Digital signature functionality is not included.
- The application uses a command-line interface only.
- Performance optimization for large polynomial sizes has not been implemented.

---
## Author

**Siva Surya T**


---

## License

This project is intended for educational and research purposes only.

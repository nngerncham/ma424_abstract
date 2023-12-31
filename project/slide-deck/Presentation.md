---
marp: true
theme: academic
paginate: true
math: katex
style: |
  .meme { 
      margin-top: 0.5cm;
      margin-left: auto;
      margin-right: auto;
      display: block;
  },
  .report {
      max-height: 100%;
      max-width: 100%;
      margin: auto;
      display: block
  }
---

<!-- _class: lead -->

## (Non-Quantum Parts of) Shor's Algorithm

##### By Nawat Ngerncham

---

<!-- _header: RSA Crash Course -->

# RSA (Rivest-Shamir-Adleman)

Suppose that you have some plaintext that is encoded into integer $m$. Given non-negative integers $e, d, N$ such that $0 \leq m < N$, 

- We encrypt the message by 
$$ m \mapsto m^e \pmod N $$

- We decrypt the message by
$$ m^e \mapsto (m^e)^d \pmod N $$

---

<!-- _header: RSA Crash Course -->

# Key Generation in RSA

```python
def generate_rsa_keys():
    p, q = large_prime(size=2)
    N = p * q  # ~2000-4000 bits long, i.e. N in [2^2000, 2^4000]
    e = pick_with_prop(1 < e < phi(N), gcd(e, phi(N)) == 1)
    d = pick_with_prop(de == 1 (mod phi(N)))
    return e, d, N
```

- $e$ and $N$ are public
- $\phi(N)$ can be computed by $\phi(N) = (p-1)(q-1)$
- If you can find $p, q$, then you can compute $d$ very _easily_

---

<!-- _header: Shor's Algorithm -->

# Shor's Algorithm

```python
def shors_algorithm(N):
    guess = randint(2, N)
    p = order(g, N)  # |g| (mod N)

    # f1, f2 can be multiples of the actual factor so take gcd
    f1 = gcd(guess^(p / 2) + 1, N)
    f2 = gcd(guess^(p / 2) - 1, N)

    return f1, f2
```

---

<!-- _header: Why does it work? -->

#### Why do we get the factors from $g \mapsto g^p \pm 1$?

$$
    g^p \equiv 1 \pmod N \iff g^p = m \cdot N + 1
$$

Then, for some integer $m$,

$$
\begin{align*}
    g^p &= mN + 1\\
    g^p - 1 &= mN \\
    (g^{p / 2} + 1)(g^{p / 2} - 1) &= mN
\end{align*}
$$

So, $mn$ has factors as shown above and to get factors of just $n$, we can take the $\gcd$.

---

<!-- _header: What about the quantum part? -->

On a quantum computer, we can compute the order of a number really quickly. Define the following operation.

$$
\begin{align*}
    \text{Input: } \lvert \psi \rangle &= \lvert p_1 \rangle + \lvert p_2 \rangle + \lvert p_3 \rangle + \cdots \\
        &\mapsto \lvert p_1, r_1 \rangle + \lvert p_2, r_2 \rangle + \lvert p_3, r_3 \rangle + \cdots
\end{align*}
$$
where $p_i, r_i$ are such that $g^{p_i} = mN + r_i$. We can set this up such that it returns a single pair $p, r$.

---

<!-- _header: What about the quantum part? -->

On a quantum computer, if there are multiple possible answers, then the return value is actually the superposition. That is, you get
$$ \lvert p_1', r \rangle + \lvert p_2', r \rangle + \lvert p_3', r \rangle + \cdots $$
where each $p_i'$ are $p$ apart.

---

<!-- _header: What should our honest reaction be to this information? -->

- Shor's Algorithm (and other quantum factoring algorithms) require thousands of qubits in order to work properly
- A few notable quantum computers
  - Atom Computing's Unnamed Machine - 1225 qubits (2023)
  - IBM's Osprey - 443 qubits (2022)
  - Google's Sycamore - 53 qubits (~2019)

---

<!-- _header: What should our honest reaction be to this information? -->

- Back in August this year, NIST just approved 3 new quantum-resistant cryptographic algorithms
- These algorithms are lattice-based
  - Given a point $v \in \mathbb{R}^n$ and a set of basis vectors $\mathbb{B} \subseteq \mathbb{R}^n$
  - Lattice is the set of all points that can generated from the vectors in $\mathbb{B}$
  - Find the vector in the lattice generated from $\mathbb{B}$ that is closest to $v$

---

<!-- _class: lead -->

# Thank you!

##### Credit to `kaisugi` on Github for the theme

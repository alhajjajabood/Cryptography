# Cryptography Toolbox

A comprehensive Python-based cryptography toolkit implementing various classical and modern encryption algorithms, cryptanalysis techniques, and key exchange protocols.

**Author:**Abood Al Hajjaj - [@alhajjajabood](https://github.com/alhajjajabood),Mohammad Nakhleh - [@Moevo](https://github.com/Moevo)  
**Date:** December 2025  

## 📋 Overview

This project is a complete cryptography suite that allows users to:
- **Encrypt and decrypt** messages using various ciphers
- **Perform cryptanalysis** through brute force and frequency analysis
- **Generate cryptographic keys** for asymmetric algorithms
- **Simulate attacks** like MITM (Man-in-the-Middle) on key exchange protocols

## 🔐 Supported Algorithms

### Symmetric Key Cryptography
- **Caesar Cipher** - Simple substitution cipher
- **Multiplicative Cipher** - Affine cipher without addition
- **Affine Cipher** - Combination of multiplicative and Caesar ciphers
- **Playfair Cipher** - Digraph substitution cipher
- **Hill Cipher** - Polygraphic substitution using linear algebra
- **DES (Data Encryption Standard)** - Block cipher with Feistel structure
- **AES (Advanced Encryption Standard)** - Modern block cipher

### Asymmetric Key Cryptography
- **RSA** - Public-key cryptosystem
- **Diffie-Hellman Key Exchange (DHKE)** - Secure key exchange protocol
- **ElGamal Encryption** - Public-key cryptosystem based on discrete logarithms

### Cryptanalysis Tools
- **Brute Force Attacks** - Exhaustive key search
- **Frequency Analysis** - Statistical analysis of ciphertext
- **Known Attacks** - BSGS (Baby-Step Giant-Step), Pollard's p-1, etc.

## 🚀 Features

1. **Interactive Menu System** - Easy navigation through different algorithms
2. **Educational Focus** - Shows step-by-step encryption/decryption processes
3. **Attack Simulations** - Demonstrates real cryptographic attacks
4. **File Output** - Saves analysis results to text files
5. **Error Handling** - Validates inputs and prevents common mistakes

## 📁 Project Structure

The main file `cryptography.py` contains:
- **Algorithm implementations** (37 different tasks/functions)
- **Menu system** for user interaction
- **Helper functions** for common operations

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.x
- No external dependencies required (uses only built-in Python libraries)

### Running the Tool
```bash
python cryptography.py
```

### Navigation
1. Run the script to see the main menu
2. Select a cipher category (1-10)
3. Choose specific operation within that category
4. Follow prompts to input text, keys, and parameters
5. View results and choose next action

## 📊 Menu Categories

1. **Caesar Cipher** - Basic shift cipher operations
2. **Multiplicative Cipher** - Multiplication-based encryption
3. **Affine Cipher** - Combined multiplication and addition
4. **Playfair Cipher** - Matrix-based digraph cipher
5. **Hill Cipher** - Linear algebra-based encryption
6. **DES** - Classic 64-bit block cipher
7. **AES** - Modern 128-bit block cipher
8. **RSA** - Public-key encryption and attacks
9. **DHKE** - Key exchange protocol
10. **ElGamal** - Discrete logarithm-based encryption

## ⚠️ Important Notes

### Security Disclaimer
⚠️ **This tool is for EDUCATIONAL PURPOSES ONLY**
- These implementations are simplified for learning
- **DO NOT USE** for securing real-world sensitive data
- Real cryptographic applications require professionally vetted libraries

### Key Limitations
- **DES** uses 64-bit keys (obsolete for real security)
- **AES** implementation is simplified for education
- **RSA** uses small keys suitable for demonstration only

## 📝 Usage Examples

### Encrypting with Caesar Cipher
```
1. Select "Caesar Cipher" from main menu
2. Choose "Encryption"
3. Enter plaintext: "HELLO"
4. Enter key: 3
5. Output: "KHOOR"
```

### Breaking Caesar Cipher with Frequency Analysis
```
1. Select "Caesar Cipher"
2. Choose "Frequency Attack"
3. Enter ciphertext
4. View all possible decryptions ranked by likelihood
```

### RSA Key Generation
```
1. Select "RSA"
2. Choose "Key Generation"
3. Enter prime numbers p and q
4. Get public key (e, n) and private key (d, n)
```

## 🧪 Educational Value

This project is ideal for:
- Computer science students learning cryptography
- Understanding how different encryption algorithms work
- Visualizing cryptographic attacks in action
- Comparing classical vs. modern encryption techniques

## 🔍 Sample Output Files

The tool generates several analysis files:
- `all_candidates.txt` - Hill cipher brute force results
- `playfaier_brutN!_attack.txt` - Playfair exhaustive key search
- `hill_cipher_attack_results_*.txt` - Frequency analysis results
- `playfair_results_*.txt` - Playfair cryptanalysis

## 🤝 Contributing

This is primarily an educational project, but suggestions for:
- Code improvements
- Additional algorithms
- Better documentation
- Bug fixes

are always welcome.

## 📚 Learning Resources

To better understand these algorithms:
- "Cryptography and Network Security" by William Stallings
- "The Code Book" by Simon Singh
- Coursera/edX cryptography courses
- Cryptopals challenges

## 📄 License

### 🆓 Free to Use and Modify
This project is **completely free** to:
- **Use** for educational and personal purposes
- **Modify** and customize for your needs
- **Upgrade** with new features and algorithms
- **Share** with others for learning

You are encouraged to:
- Add new cryptographic algorithms
- Improve existing implementations
- Create better user interfaces
- Fix bugs and optimize performance
- Translate to other programming languages
- Use as a teaching tool in classrooms

**No permission required** - feel free to fork, modify, and enhance this project!

---

**Remember**: Real-world cryptography requires expert implementation, proper key management, and continuous security assessment. This tool demonstrates concepts but doesn't replace professional cryptographic libraries.

Happy learning! 🔐

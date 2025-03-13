# Basic-Ransomware

## Overview
This is a simple Python-based ransomware demonstration created for educational purposes only. It consists of two scripts:
- `rnsm.py`: Encrypts files in the current directory using a symmetric key.
- `decrypt.py`: Decrypts the files encrypted by `rnsm.py` using the stored key.

The ransomware uses the `cryptography` library's Fernet (symmetric encryption) to encrypt and decrypt files. A key is generated during encryption and saved as `theKey.key` for decryption.

**WARNING**: This is a proof-of-concept and should **never** be used maliciously. Unauthorized use of ransomware is illegal and unethical.

## Requirements
- Python 3.x
- `cryptography` library (`pip install cryptography`)

## Files
- `rnsm.py`: The encryption script.
- `decrypt.py`: The decryption script.
- `theKey.key`: The generated encryption key (created by `rnsm.py`).

## How It Works
### Encryption (`rnsm.py`)
1. Scans the current directory for files.
2. Skips `rnsm.py`, `decrypt.py`, and `theKey.key` to avoid encrypting itself or the key.
3. Generates a Fernet key and saves it to `theKey.key`.
4. Encrypts all other files in the directory, overwriting them with encrypted content.

### Decryption (`decrypt.py`)
1. Scans the current directory for files.
2. Skips `rnsm.py`, `decrypt.py`, and `theKey.key`.
3. Reads the key from `theKey.key`.
4. Decrypts all encrypted files, restoring their original content.

## Usage
1. **Install dependencies**:
   ```bash
   pip install cryptography

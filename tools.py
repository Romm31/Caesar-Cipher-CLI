import argparse

def caesar_cipher(text, shift, mode='encode'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encode':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decode':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def bruteforce_caesar(ciphertext):
    print("🔎 Brute-forcing Caesar Cipher:")
    for shift in range(1, 26):
        decoded = caesar_cipher(ciphertext, shift, mode='decode')
        print(f"[Shift {shift:2}] {decoded}")

def main():
    parser = argparse.ArgumentParser(
        description="🔐 Caesar Cipher Tool - Encode, Decode, or Brute-force Caesar Cipher text."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--encode', '-e',
        type=int,
        metavar='SHIFT',
        help='Encrypt text using Caesar Cipher with the given shift. Example: --encode 3 "HELLO"'
    )
    group.add_argument(
        '--decode', '-d',
        type=int,
        metavar='SHIFT',
        help='Decrypt Caesar Cipher text using the given shift. Example: --decode 3 "KHOOR"'
    )
    group.add_argument(
        '--bruteforce', '-bf',
        action='store_true',
        help='Try all 25 possible Caesar Cipher shifts to decrypt the text. Example: --bruteforce "KHOOR"'
    )

    parser.add_argument(
        'text',
        type=str,
        help='The text to process. Use quotes if the text contains spaces or special characters.'
    )

    args = parser.parse_args()

    if args.encode is not None:
        print("🔐 Encoded Text:")
        print(caesar_cipher(args.text, args.encode, mode='encode'))

    elif args.decode is not None:
        print("🔓 Decoded Text:")
        print(caesar_cipher(args.text, args.decode, mode='decode'))

    elif args.bruteforce:
        bruteforce_caesar(args.text)

if __name__ == "__main__":
    main()

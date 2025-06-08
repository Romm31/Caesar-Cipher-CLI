# Caesar Cipher CLI Tool

A simple **Python command-line tool** to encode, decode, or brute-force Caesar Cipher text.  
Perfect for educational purposes or assignments.

**Features**
- Encode text using Caesar Cipher with a specified shift  
- Decode Caesar Cipher text with a known shift  
- Brute-force Caesar Cipher by trying all 25 possible shifts

**Requirements**
- Python 3.x

**Usage**  
Run the script using Python 3:

**Encode**  
Encrypt text using a Caesar shift.  
`python3 tools.py --encode 3 "HELLO WORLD"`

**Decode**  
Decrypt Caesar Cipher text using a known shift.  
`python3 tools.py --decode 3 "KHOOR ZRUOG"`

**Brute-force**  
Try all 25 Caesar shifts to decrypt unknown ciphertext.  
`python3 tools.py --bruteforce "KHOOR ZRUOG"`

**Examples**

1. Encode (Encrypt) with shift 5  
`python3 tools.py --encode 5 "ctf{its_crazy}"`  
Output: `hyg{nyx_hwfde}`

2. Decode (Decrypt) with shift 5  
`python3 tools.py --decode 5 "hyg{nyx_hwfde}"`  
Output: `ctf{its_crazy}`

3. Brute-force (Try all possible shifts)  
`python3 tools.py --bruteforce "hyg{nyx_hwfde}"`  
Output example:  
`[Shift  1] gxf{mwx_gvecd}`  
`[Shift  2] fwe{lvw_fubdc}`  
`[Shift  3] evd{kuv_etabc}`  
`[Shift  4] duc{jtu_dszab}`  
`[Shift  5] ctf{its_crazy}`  
...  
`[Shift 25] zih{juz_ibgbx}`

**Help**  
To view the help message:  
`python3 tools.py --help`

**Notes**
- Only alphabetic characters are shifted (A–Z, a–z).  
- Non-alphabetic characters (such as `{`, `}`, `_`, etc.) are preserved.  
- Use quotes around your text if it contains spaces or special characters.

**License**  
This tool is open for educational use only.

# CTF Automation Tools and notes


## Index

### Automation
- `automation/auto_clicker.py` - automated click/type loop driven by the dictionary list, with Tab+Q safe stop.
- `automation/mouse_capture.py` - captures mouse click coordinates for automation setup.
- `automation/dictionary.txt` - word list used by automation scripts.

### Crypto
- `crypto/bruteunzip.py` - brute-force 4-digit ZIP passwords against `flag.zip`.
- `crypto/decrypng.py` - XOR-decrypts an encrypted PNG using the known header bytes.
- `crypto/Coppersmith's_attack_RSA.py` - low-exponent RSA root attack using values in `message.txt`.

### Forensics
- `forensics/wmi/README.md` - WMI forensics tools overview and usage.
- `forensics/wmi/CCM_RUA_Finder.py` - extracts CCM RecentlyUsedApps records from WMI `OBJECTS.DATA`.
- `forensics/wmi/PyWMIPersistenceFinder.py` - finds WMI FilterToConsumerBindings in `OBJECTS.DATA`.

### Notes
- `notes/tshark_play_usb_audio.md` - steps to extract USB audio from a PCAP.
- `notes/XML External Entity.md` - XXE notes and sample payloads.
- `notes/simple-php-webshell-htaccess.md` - `.htaccess` PHP execution notes and a sample webshell.

### Archive
- `archive/autoTextCTF.py` - older click/text automation that records actions then replays them.


## Warning

Use responsibly and only on systems you own or have permission to automate. These tools can perform actions on your system automatically.

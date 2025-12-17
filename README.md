# CTF Automation Tools and notes


## Index

- `auto_clicker.py` - automated click/type loop driven by `dictionary.txt`, with Tab+Q safe stop.
- `mouse_capture.py` - captures mouse click coordinates for automation setup.
- `bruteunzip.py` - brute-force 4-digit ZIP passwords against `flag.zip`.
- `decrypng.py` - XOR-decrypts an encrypted PNG using the known header bytes.
- `Coppersmith's_attack_RSA.py` - low-exponent RSA root attack using values in `message.txt`.
- `Archive/autoTextCTF.py` - older click/text automation that records actions then replays them.
- `dictionary.txt` - word list used by automation scripts.
- `tshark_play_usb_audio.md` - steps to extract USB audio from a PCAP.
- `XML External Entity.md` - XXE notes and sample payloads.
- `simple-php-webshell-htaccess.md` - `.htaccess` PHP execution notes and a sample webshell.
- `Tool Objects.data file viewer WMI_Forensics/README.md` - WMI forensics tools overview and usage.
- `Tool Objects.data file viewer WMI_Forensics/CCM_RUA_Finder.py` - extracts CCM RecentlyUsedApps records from WMI `OBJECTS.DATA`.
- `Tool Objects.data file viewer WMI_Forensics/PyWMIPersistenceFinder.py` - finds WMI FilterToConsumerBindings in `OBJECTS.DATA`.


## Warning

Use responsibly and only on systems you own or have permission to automate. These tools can perform actions on your system automatically.

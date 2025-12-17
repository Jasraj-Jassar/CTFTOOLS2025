## Extract USB audio data from a PCAP and convert it into raw binary audio.

PCAP → hex bytes → binary bytes → audio file

```
tshark -r talktome.pcap -T fields -e usb.iso.data \
| tr -cd '0-9a-fA-F' \
| python3 -c 'import sys,binascii; sys.stdout.buffer.write(binascii.unhexlify(sys.stdin.read()))' \
> audio.raw
```
## Breakdown

tshark ... -e usb.iso.data
Extracts USB isochronous payloads as hex.

tr -cd '0-9a-fA-F'
Keeps only valid hex characters.

python3 ... unhexlify(...)
Converts hex → raw binary bytes.

> audio.raw
Saves the raw PCM audio.

Notes:
Use Audacity to play go to file> import> raw data

ExifTool is a metadata extractor/editor used in CTFs, mainly for forensics and stego. Below is a practical, CTF-focused cheat sheet with exact commands.

1. Basic Usage (Always Start Here)  
`exiftool file.jpg`  
Shows all metadata: camera info, timestamps, software, GPS, comments.  
CTF mindset: look for odd fields like Comment, UserComment, Artist, Software, Description.

2. Show Everything (Including Duplicates)  
`exiftool -a -u -g1 file.jpg`  
`-a` → show duplicate tags  
`-u` → show unknown tags  
`-g1` → group by category  
Catches hidden or malformed fields.

3. Extract Only Interesting Fields  
`exiftool -Comment -UserComment -Description -Artist file.jpg`  
Quickly surfaces embedded hints or flags.

4. Search for Flags Directly  
`exiftool file.jpg | grep -i flag`  
Works more often than people expect.

5. Extract GPS Data  
`exiftool -GPS* file.jpg`  
Convert to map coordinates: `exiftool -GPSLatitude -GPSLongitude -n file.jpg`  
Common CTF trick: location → Google Maps → clue.

6. Dump Raw Binary Metadata  
`exiftool -b -ThumbnailImage file.jpg > thumb.jpg`  
Also try `exiftool -b -PreviewImage file.jpg > preview.jpg`  
Sometimes the flag is in the thumbnail/preview, not the main image.

7. Check File Type Lies  
`exiftool file`  
If it reports something unexpected (PNG pretending to be JPG, PDF embedded in image, ZIP inside metadata), follow up with `binwalk file`.

8. Extract All Embedded Files (CTF Gold)  
`exiftool -ee -a -u -b file > dump.bin`  
Then run `strings dump.bin`.

9. Batch Scan a Directory  
`exiftool *.jpg`  
Recursive scan: `exiftool -r .`  
Great for multi-file challenges.

10. Modify Metadata (Practice / Payloads)  
`exiftool -Comment="picoCTF{test_flag}" file.jpg`  
Verify with `exiftool file.jpg`.

11. Strip Metadata (Defense Knowledge)  
`exiftool -all= file.jpg`  
Creates `file.jpg_original`.
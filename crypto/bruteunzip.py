import zipfile

ZIP_FILE = "flag.zip"


def brute_force_zip():
    for i in range(10000):  # 0000 to 9999
        pwd = f"{i:04d}"
        pwd_bytes = pwd.encode("utf-8")
        try:
            print(f"[*] Trying password: {pwd}")
            with zipfile.ZipFile(ZIP_FILE) as zf:
                zf.setpassword(pwd_bytes)
                # testzip() lets us verify the password without partially
                # extracting files, which avoids CRC errors being reported
                # as BadZipFile after many failed attempts.
                if zf.testzip() is None:
                    zf.extractall(pwd=pwd_bytes)
                    print(f"[+] Password found: {pwd}")
                    return
        except RuntimeError:
            # Wrong password, move on
            continue
        except FileNotFoundError:
            print(f"[-] ZIP file '{ZIP_FILE}' not found.")
            return
        except zipfile.BadZipFile as exc:
            print(f"[-] The ZIP file is corrupted or invalid: {exc}")
            return
    print("[-] Tried all 4-digit combinations, no password worked.")


if __name__ == "__main__":
    brute_force_zip()

# Small public exponent means m^e < n, so Coppersmith/low-e attack reduces to an integer e-th root.

import re
from pathlib import Path

import gmpy2


def main() -> None:
    text = Path("message.txt").read_text()
    vals = {}
    for line in text.splitlines():
        m = re.match(r"\s*(\w+)\s*=\s*(\d+)", line)
        if m:
            vals[m.group(1)] = int(m.group(2))

    n = vals["n"]
    e = vals["e"]
    c = vals["c"]

    m, exact = gmpy2.iroot(c, e)
    if not exact:
        raise ValueError("Plaintext is not a perfect e-th root; assumptions broken.")

    flag_bytes = int(m).to_bytes((int(m).bit_length() + 7) // 8, "big")
    print(flag_bytes.decode())


if __name__ == "__main__":
    main()

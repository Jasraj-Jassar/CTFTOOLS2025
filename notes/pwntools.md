# Pwntools quick notes

Pwntools is a Python library for CTF pwn tasks. It also ships a `pwn` CLI with handy helpers.

## CLI commands (`pwn`)
- `pwn asm` - assemble instructions into bytes for a target architecture.
  Example: `pwn asm 'xor eax, eax; ret' -c i386`
- `pwn checksec` - show binary security mitigations (RELRO, Canary, NX, PIE).
  Example: `pwn checksec ./vuln`
- `pwn constgrep` - search constants from system headers by name/expression.
  Example: `pwn constgrep -c linux -m '^PROT_' '3 + 4'`
- `pwn cyclic` - generate or search a cyclic pattern (e.g., `pwn cyclic 200`).
  Example: `pwn cyclic 200`
- `pwn debug` - launch a binary in GDB with pwntools helpers.
  Example: `pwn debug ./vuln`
- `pwn disasm` - disassemble bytes into assembly text.
  Example: `pwn disasm 31c0c3 -c i386`
- `pwn disablenx` - remove NX from an ELF binary.
  Example: `pwn disablenx ./vuln`
- `pwn elfdiff` - compare two ELF files and show differences.
  Example: `pwn elfdiff ./vuln ./vuln_patched`
- `pwn elfpatch` - patch bytes at a virtual address in an ELF file.
  Example: `pwn elfpatch ./vuln 0x401000 9090c3`
- `pwn errno` - print errno names and messages.
  Example: `pwn errno 13`
- `pwn hex` - hex-encode data from args or stdin.
  Example: `pwn hex "hello"`
- `pwn libcdb` - inspect libc symbols and build info.
  Example: `pwn libcdb ./libc.so.6`
- `pwn phd` - pretty hex dump with offsets.
  Example: `pwn phd ./payload.bin`
- `pwn pwnstrip` - strip binaries for CTF usage.
  Example: `pwn pwnstrip ./vuln -o ./vuln.stripped`
- `pwn scramble` - encode shellcode to avoid bad bytes.
  Example: `printf '\\x90\\x90\\xc3' | pwn scramble -z -f hex`
- `pwn shellcraft` - generate shellcode templates for common tasks.
  Example: `pwn shellcraft amd64.linux.sh -f asm`
- `pwn template` - generate a starter exploit script.
  Example: `pwn template ./vuln --host chall.example --port 1337`
- `pwn unhex` - hex-decode data from args or stdin.
  Example: `pwn unhex 68656c6c6f`
- `pwn update` - check for pwntools updates.
  Example: `pwn update`
- `pwn version` - print pwntools version info.
  Example: `pwn version`

## Python quick hits
- `cyclic()` / `cyclic_find()` - pattern/offset helpers for buffer overflows.
- `ELF("./bin")` - parse symbols, GOT/PLT, sections, and security flags.
- `ROP(elf)` - build ROP chains from gadgets in an ELF.
- `process()` / `remote()` - spawn a local process or connect to a service.
- `gdb.attach(p)` - attach GDB to a running process.
- `asm()` / `disasm()` / `shellcraft` - assemble, disassemble, or generate shellcode.
- `p32()` / `p64()` / `u32()` / `u64()` - pack/unpack integers by endianness.
- `sendline()` / `recvuntil()` / `interactive()` - I/O helpers for exploit scripts.

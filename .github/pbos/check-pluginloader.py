#!/usr/bin/env python3
"""PB-OS: check a PluginLoader-arm64 build before it becomes a release.

  check-pluginloader.py BINARY VERSION MAX_GLIBC

Fails unless the binary is an aarch64 ELF, the decky_loader it bundles is
exactly VERSION (what the updater compares with the release tag), and no
library it bundles needs a glibc newer than MAX_GLIBC (SteamOS on PB-OS
devices). Reads the PyInstaller archive; never runs the binary.
"""
import re
import sys

from PyInstaller.archive.readers import CArchiveReader


def main() -> int:
    binary, version, max_glibc = sys.argv[1], sys.argv[2].lstrip("v"), sys.argv[3]
    ok = True

    with open(binary, "rb") as f:
        head = f.read(20)
    if head[:4] != b"\x7fELF" or int.from_bytes(head[18:20], "little") != 183:  # EM_AARCH64
        print(f"FAIL: {binary} is not an aarch64 ELF")
        return 1

    archive = CArchiveReader(binary)
    infos = {m[1] for n in archive.toc if (m := re.match(r"decky_loader-([^/]+)\.dist-info/", n))}
    if infos != {version}:
        print(f"FAIL: bundled decky_loader version {sorted(infos)}, want {version}")
        ok = False
    else:
        print(f"version: {version}")

    def key(v: str) -> tuple[int, ...]:
        return tuple(int(x) for x in v.split("."))

    need, worst = "0.0", ""
    for name in archive.toc:
        if ".so" not in name:
            continue
        for v in set(re.findall(rb"GLIBC_(2\.\d+)\x00", archive.extract(name))):
            v = v.decode()
            if key(v) > key(need):
                need, worst = v, name
    if key(need) > key(max_glibc):
        print(f"FAIL: {worst} needs glibc {need}, PB-OS has {max_glibc}")
        ok = False
    else:
        print(f"glibc: needs {need} ({worst}), PB-OS has {max_glibc}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

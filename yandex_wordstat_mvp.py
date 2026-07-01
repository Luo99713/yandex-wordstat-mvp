# -*- coding: utf-8 -*-
"""
Yandex Wordstat MVP v0.6 launcher.

The full source is stored in source_parts/source.b64.partXX to keep repository
uploads stable. This launcher reconstructs the source in memory and runs it.
No API key is stored in this repository.
"""
from __future__ import annotations

import base64
import pathlib
import zlib


def load_embedded_source() -> str:
    root = pathlib.Path(__file__).resolve().parent
    parts_dir = root / "source_parts"
    parts = sorted(parts_dir.glob("source.b64.part*"))
    if not parts:
        raise FileNotFoundError("source_parts/source.b64.partXX not found")
    encoded = "".join(p.read_text(encoding="ascii").strip() for p in parts)
    return zlib.decompress(base64.b64decode(encoded.encode("ascii"))).decode("utf-8")


def main() -> None:
    code = load_embedded_source()
    namespace = {"__name__": "__main__", "__file__": __file__}
    exec(compile(code, __file__, "exec"), namespace)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Git clean filter for ipynb: strip outputs and ensure LF."""
import sys, json

raw = sys.stdin.buffer.read()
try:
    nb = json.loads(raw)
    for cell in nb.get("cells", []):
        if "outputs" in cell:
            cell["outputs"] = []
        if "execution_count" in cell:
            cell["execution_count"] = None
    if "metadata" in nb:
        for cell in nb.get("cells", []):
            md = cell.get("metadata", {})
            for key in list(md.keys()):
                if key.lower() in ("executetime", "collapsed", "scrolled", "slideshow"):
                    del md[key]
    out = json.dumps(nb, ensure_ascii=False, indent=1) + "\n"
    sys.stdout.buffer.write(out.encode("utf-8"))
except Exception:
    sys.stdout.buffer.write(raw)

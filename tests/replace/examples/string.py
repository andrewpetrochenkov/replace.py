#!/usr/bin/env python
import replace

source = "package/module.py"
new = replace.replace(source, {"/": ".", ".py": ""})
assert new == "package.module"

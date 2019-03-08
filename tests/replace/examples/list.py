#!/usr/bin/env python
import replace

source = ["3.6", "3.7", "3.8"]
new = replace.replace(source, {"3.7": "3.7-dev", "3.8": "3.8-dev"})
assert new == ["3.6", "3.7-dev", "3.8-dev"]

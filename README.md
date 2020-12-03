<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/replace.svg?maxAge=3600)](https://pypi.org/project/replace/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/replace.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/replace.py/actions)

### Installation
```bash
$ [sudo] pip install replace
```

#### Examples
```python
import replace
>>> replace.replace(["3.6","3.7","3.8"], {"3.7": "3.7-dev", "3.8": "3.8-dev"})
["3.6","3.7-dev","3.8-dev""3.8"]
```

```python
>>> replace.replace("package/module.py", {"/": ".", ".py": ""})
"package.module"
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>

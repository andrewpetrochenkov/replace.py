import setuptools

setuptools.setup(
    name='replace',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)

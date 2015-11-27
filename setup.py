from setuptools import setup, Extension

spi = Extension('spi', sources = ['pcduino/spi_multi.c'])

setup(
    name="pcduino",
    version="0.1.0",
    author="kyumoka",
    author_email="qmh524@qq.com",
    url="https://github.com/kyumoka/python-pcduino",
    packages=["pcduino"],
    ext_modules=[spi],
)

from setuptools import find_packages, setup

from platformio import (
    __author__,
    __description__,
    __email__,
    # __license__,
    __title__,
    __url__,
    __version__,
)
from platformio.compat import PY2, WINDOWS


minimal_requirements = [
    "bottle==0.12.*",
    "click>=5,<8%s" % (",!=7.1,!=7.1.1" if WINDOWS else ""),
    "colorama",
    "marshmallow%s" % (">=2,<3" if PY2 else ">=2,<4"),
    "pyelftools>=0.27,<1",
    "pyserial==3.*",
    "requests==2.*",
    "semantic_version==2.8.*",
    "tabulate==0.8.*",
]

if not PY2:
    minimal_requirements.append("zeroconf==0.28.*")

home_requirements = [
    "aiofiles==0.6.*",
    "ajsonrpc==1.1.*",
    "starlette==0.14.*",
    "uvicorn==0.13.*",
    "wsproto==1.0.*",
]

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    # long_description=open("README.rst").read(),
    author=__author__,
    author_email=__email__,
    url=__url__,
    # license=__license__,
    install_requires=minimal_requirements + ([] if PY2 else home_requirements),
    packages=find_packages(exclude=["tests.*", "tests"]) + ["scripts"],
    package_data={
        "platformio": [
            "ide/tpls/*/.*.tpl",
            "ide/tpls/*/*.tpl",
            "ide/tpls/*/*/*.tpl",
            "ide/tpls/*/.*/*.tpl",
        ],
        "scripts": ["99-qitas-udev.rules"],
    },
    entry_points={
        "console_scripts": [
            "platformio = platformio.__main__:main",
            "pio = platformio.__main__:main",
            "qio = platformio.__main__:main",
            "piodebuggdb = platformio.__main__:debug_gdb_main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Compilers",
    ],
    keywords=[
        "iot",
        "embedded",
        "arduino",
        "mbed",
        "esp8266",
        "esp32",
        "fpga",
        "firmware",
        "continuous-integration",
        "cloud-ide",
        "avr",
        "arm",
        "ide",
        "unit-testing",
        "hardware",
        "verilog",
        "microcontroller",
        "debug",
    ],
)


import sys

VERSION = (5, 1, "1a1")
__version__ = ".".join([str(s) for s in VERSION])

__title__ = "OS-Q"
__description__ = (
    "A professional collaborative platform for embedded development. "
    "Cross-platform IDE and Unified Debugger. "
    "Static Code Analyzer and Remote Unit Testing. "
    "Multi-platform and Multi-architecture Build System. "
    "Firmware File Explorer and Memory Inspection. "
    "IoT, Arduino, CMSIS, ESP-IDF, FreeRTOS, libOpenCM3, mbedOS, Pulp OS, SPL, "
    "STM32Cube, Zephyr RTOS, ARM, AVR, Espressif (ESP8266/ESP32), FPGA, "
    "MCS-51 (8051), MSP430, Nordic (nRF51/nRF52), NXP i.MX RT, PIC32, RISC-V, "
    "STMicroelectronics (STM8/STM32), Teensy"
)
__url__ = "http://www.OS-Q.com"

__author__ = "OS-Q"
__email__ = "qitas@qitas.cn"

__license__ = "Apache Software License"
__copyright__ = "Copyright 2021 OS-Q"

__accounts_api__ = "https://api.accounts.platformio.org"
__registry_api__ = [
    "https://api.registry.platformio.org",
    "https://api.registry.ns1.platformio.org",
]
__pioremote_endpoint__ = "ssl:host=remote.platformio.org:port=4413"

__default_requests_timeout__ = (10, None)  # (connect, read)

__core_packages__ = {
    "contrib-piohome": "~3.3.3",
    "contrib-pysite": "~2.%d%d.0" % (sys.version_info.major, sys.version_info.minor),
    "tool-unity": "~1.20500.0",
    "tool-scons": "~2.20501.7" if sys.version_info.major == 2 else "~4.40100.2",
    "tool-cppcheck": "~1.230.0",
    "tool-clangtidy": "~1.100000.0",
    "tool-pvs-studio": "~7.11.0",
}

__check_internet_hosts__ = [
    "185.199.110.153",  # Github.com
    "88.198.170.159",  # platformio.org
    "github.com",
    "platformio.org",
]

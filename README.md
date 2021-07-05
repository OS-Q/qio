### [协同开发](https://github.com/OS-Q)

* [Q1研发现场](https://github.com/OS-Q/Q1)
    * [M01硬件设计](https://github.com/OS-Q/M01)
    * [M02原型验证](https://github.com/OS-Q/M02)
    * [M03协同开发](https://github.com/OS-Q/M03)

[![sites](http://182.61.61.133/link/resources/OSQ.png)](http://www.OS-Q.com)

[M03协同开发](https://github.com/OS-Q/M03) 工程源自 [platformio](https://github.com/platformio/platformio-core)，通过改变组织方式，实现类似容器的嵌入式环境，便于工程的拆解组装标准化实现。

以目标为导向的标准模板组织方式：platform/hardware/framework

通过硬件索引完成对平台的推导，降低配置项目(明确的硬件版本，不适用于同步替换的设计逻辑)

### [QIO拓扑](https://github.com/M03)

| Class 1 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 | platform 7 | platform 8 | platform 9 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| hardware 1 | [AVR](https://github.com/OS-Q/P111) | [STC](https://github.com/OS-Q/P121) | [STM8S](https://github.com/OS-Q/P131) | [WCH](https://github.com/OS-Q/P141) | [LGT](https://github.com/OS-Q/P151) |    X    |    X    |    X    |    X    |
| hardware 2 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 3 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 4 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 5 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 6 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 7 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 8 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 9 |     √   |    √    |    √    |    X    |     X   |    X    |

| Class 2 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 | platform 7 | platform 8 | platform 9 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| hardware 1 | [STM32](https://github.com/OS-Q/P211) | [GD32V](https://github.com/OS-Q/P221) | [PIC32](https://github.com/OS-Q/P231) |
| hardware 2 |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 3 |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 4 |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 5 |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 6 |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 7 |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 8 |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 9 |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |

| Class 3 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 | platform 7 | platform 8 | platform 9 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| hardware 1 | [RP2040](https://github.com/OS-Q/P311) | X | [STM32](https://github.com/OS-Q/P331) |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 2 | [Pico](https://github.com/OS-Q/P312)  |    √    |    √    |    X    |     X   |    X    |
| hardware 3 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 4 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 5 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 6 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 7 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 8 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 9 |     √   |    √    |    √    |    X    |     X   |    X    |

| Class 4 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 | platform 7 | platform 8 | platform 9 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| hardware 1 | [nRF52](https://github.com/OS-Q/P411) | [ASR6501](https://github.com/OS-Q/P421) | [CC1350](https://github.com/OS-Q/P431) |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 2 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 3 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 4 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 5 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 6 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 7 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 8 |     √   |    √    |    √    |    X    |     X   |    X    |
| hardware 9 |     √   |    √    |    √    |    X    |     X   |    X    |

| Class 5 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 | platform 7 | platform 8 | platform 9 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| hardware 1 | [ESP32](https://github.com/OS-Q/P511) |    X    |    X    |    X    |    X    |    X    |    X    |
| hardware 2 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 3 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 4 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 5 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 6 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 7 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 8 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 9 |    √    |    √    |    √    |    X    |     X   |    X    |

| Class 6 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 | platform 7 | platform 8 | platform 9 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| hardware 1 |    √    |    √    |    √    |    X    |     X   |    X    |    X    |     X   |    X    |
| hardware 2 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 3 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 4 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 5 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 6 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 7 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 8 |    √    |    √    |    √    |    X    |     X   |    X    |
| hardware 9 |    √    |    √    |    √    |    X    |     X   |    X    |


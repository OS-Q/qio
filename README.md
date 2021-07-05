### [协同开发](https://github.com/OS-Q)

* [Q1研发现场](https://github.com/OS-Q/Q1)
    * [M01硬件设计](https://github.com/OS-Q/M01)
    * [M02原型验证](https://github.com/OS-Q/M02)
    * [M03协同开发](https://github.com/OS-Q/M03)

[![sites](http://182.61.61.133/link/resources/OSQ.png)](http://www.OS-Q.com)

[M03协同开发](https://github.com/OS-Q/M03) 工程源自 [platformio](https://github.com/platformio/platformio-core)，通过改变组织方式，实现类似容器的嵌入式环境，便于工程的拆解组装标准化实现。

以目标为导向的标准模板组织方式：platform/hardware/framework

通过硬件索引完成对平台的推导，降低配置项目(明确的硬件版本，不适用于同步替换的设计逻辑)

3-6-9种设计规格,融合板级文件，便于实现一些板级功能定义

### [QIO拓扑](https://github.com/M03)

| 低阶控制 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [328P](https://github.com/OS-Q/P111) | [STC8G](https://github.com/OS-Q/P121) | [STM8S](https://github.com/OS-Q/P131) | [CH55P](https://github.com/OS-Q/P141) | [LGT](https://github.com/OS-Q/P151) | [STM8L](https://github.com/OS-Q/P161) |
| tiny | [TINY](https://github.com/OS-Q/P112) | [STC8H](https://github.com/OS-Q/P122) | [STM8S](https://github.com/OS-Q/P132) | [CH55L](https://github.com/OS-Q/P142) | [LGT](https://github.com/OS-Q/P152) | [STM8L](https://github.com/OS-Q/P162) |
| huge | [2560](https://github.com/OS-Q/P113) | [STC12](https://github.com/OS-Q/P123) | [STM8S](https://github.com/OS-Q/P133) | [CH55Q](https://github.com/OS-Q/P143) | [LGT](https://github.com/OS-Q/P153) | [STM8L](https://github.com/OS-Q/P163) |


| 通用控制 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [STM32](https://github.com/OS-Q/P211) | [GD32V](https://github.com/OS-Q/P221) | [PIC32](https://github.com/OS-Q/P231) | [GD32F](https://github.com/OS-Q/P211) | [SWM32](https://github.com/OS-Q/P221) | [CH32F](https://github.com/OS-Q/P231) |
| tiny |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |
| huge |     √   |    √    |    √    |    X    |    X    |    X    |    X    |    X    |    X    |

| 高阶控制 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [RP2040](https://github.com/OS-Q/P311) | X | [STM32](https://github.com/OS-Q/P331) |    X    |    X    |    X    |
| tiny | [Pico](https://github.com/OS-Q/P312)  |    √    |    √    |    X    |     X   |    X    |
| huge |     √   |    √    |    √    |    X    |     X   |    X    |

| 无线私域 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [nRF52](https://github.com/OS-Q/P411) | [ASR6501](https://github.com/OS-Q/P421) | [CC1350](https://github.com/OS-Q/P431) |    X    |    X    |    X    |
| tiny |     √   |    √    |    √    |    X    |     X   |    X    |
| huge |     √   |    √    |    √    |    X    |     X   |    X    |

| 无线局域 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [ESP32](https://github.com/OS-Q/P511) |    X    |    X    |    X    |
| tiny |    √    |    √    |    √    |    X    |     X   |    X    |
| huge |    √    |    √    |    √    |    X    |     X   |    X    |

| 无线广域 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main |    √    |    √    |    √    |    X    |     X   |    X    |
| tiny |    √    |    √    |    √    |    X    |     X   |    X    |
| huge |    √    |    √    |    √    |    X    |     X   |    X    |


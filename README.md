### [协同开发](https://github.com/OS-Q)

* [Q1研发现场](https://github.com/OS-Q/Q1)
    * [M01硬件设计](https://github.com/OS-Q/M01)
    * [M02原型验证](https://github.com/OS-Q/M02)
    * [M03协同开发](https://github.com/OS-Q/M03)

[![sites](http://182.61.61.133/link/resources/OSQ.png)](http://www.OS-Q.com)

[M03协同开发](https://github.com/OS-Q/M03) 工程源自 [platformio](https://github.com/platformio/platformio-core)，通过改变组织方式，实现类似容器的嵌入式环境，便于工程的拆解组装标准化实现。

以目标为导向的标准模板组织方式：platform/hardware/framework

通过硬件索引完成对平台的推导，降低配置项目(明确的硬件版本，不适用于同步替换的设计逻辑)

3-6-9种设计规格便于实现一些板级功能定义，每个平台下具有数量不定的模板工程，通过获取模板可以直接获得起点工程，类arduino编程风格和相关接口定义。

### [QIO拓扑](https://github.com/M03)

| 低阶控制 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P111](https://github.com/OS-Q/P111) | [P121](https://github.com/OS-Q/P121) | [P131](https://github.com/OS-Q/P131) | [P141](https://github.com/OS-Q/P141) | [P151](https://github.com/OS-Q/P151) | [P161](https://github.com/OS-Q/P161) |
| tiny | [P112](https://github.com/OS-Q/P112) | [P122](https://github.com/OS-Q/P122) | [P132](https://github.com/OS-Q/P132) | [P142](https://github.com/OS-Q/P142) | [P152](https://github.com/OS-Q/P152) | [P162](https://github.com/OS-Q/P162) |
| huge | [P113](https://github.com/OS-Q/P113) | [P123](https://github.com/OS-Q/P123) | [P133](https://github.com/OS-Q/P133) | [P143](https://github.com/OS-Q/P143) | [P153](https://github.com/OS-Q/P153) | [P163](https://github.com/OS-Q/P163) |

| 通用控制 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P211](https://github.com/OS-Q/P211) | [P221](https://github.com/OS-Q/P221) | [P231](https://github.com/OS-Q/P231) | [P241](https://github.com/OS-Q/P241) | [P251](https://github.com/OS-Q/P251) | [P261](https://github.com/OS-Q/P261) |
| tiny | [P212](https://github.com/OS-Q/P212) | [P222](https://github.com/OS-Q/P222) | [P232](https://github.com/OS-Q/P232) | [P242](https://github.com/OS-Q/P242) | [P252](https://github.com/OS-Q/P252) | [P262](https://github.com/OS-Q/P262) |
| huge | [P213](https://github.com/OS-Q/P213) | [P223](https://github.com/OS-Q/P223) | [P233](https://github.com/OS-Q/P233) | [P243](https://github.com/OS-Q/P243) | [P253](https://github.com/OS-Q/P253) | [P263](https://github.com/OS-Q/P263) |

| 高阶控制 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P311](https://github.com/OS-Q/P311) | [P321](https://github.com/OS-Q/P321) | [P331](https://github.com/OS-Q/P331) | [P341](https://github.com/OS-Q/P341) | [P351](https://github.com/OS-Q/P351) | [P361](https://github.com/OS-Q/P361) |
| tiny | [P312](https://github.com/OS-Q/P312) | [P322](https://github.com/OS-Q/P322) | [P332](https://github.com/OS-Q/P332) | [P342](https://github.com/OS-Q/P342) | [P352](https://github.com/OS-Q/P352) | [P362](https://github.com/OS-Q/P362) |
| huge | [P313](https://github.com/OS-Q/P313) | [P323](https://github.com/OS-Q/P323) | [P333](https://github.com/OS-Q/P333) | [P343](https://github.com/OS-Q/P343) | [P353](https://github.com/OS-Q/P353) | [P363](https://github.com/OS-Q/P363) |

| 无线私域 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P411](https://github.com/OS-Q/P411) | [P421](https://github.com/OS-Q/P421) | [P431](https://github.com/OS-Q/P431) | [P441](https://github.com/OS-Q/P441) | [P451](https://github.com/OS-Q/P451) | [P461](https://github.com/OS-Q/P461) |
| tiny | [P412](https://github.com/OS-Q/P412) | [P422](https://github.com/OS-Q/P422) | [P432](https://github.com/OS-Q/P432) | [P442](https://github.com/OS-Q/P442) | [P452](https://github.com/OS-Q/P452) | [P462](https://github.com/OS-Q/P462) |
| huge | [P413](https://github.com/OS-Q/P413) | [P423](https://github.com/OS-Q/P423) | [P433](https://github.com/OS-Q/P433) | [P443](https://github.com/OS-Q/P443) | [P453](https://github.com/OS-Q/P453) | [P463](https://github.com/OS-Q/P463) |

| 无线局域 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P511](https://github.com/OS-Q/P511) | [P521](https://github.com/OS-Q/P521) | [P531](https://github.com/OS-Q/P531) | [P541](https://github.com/OS-Q/P541) | [P551](https://github.com/OS-Q/P551) | [P561](https://github.com/OS-Q/P561) |
| tiny | [P512](https://github.com/OS-Q/P512) | [P522](https://github.com/OS-Q/P522) | [P532](https://github.com/OS-Q/P532) | [P542](https://github.com/OS-Q/P542) | [P552](https://github.com/OS-Q/P552) | [P562](https://github.com/OS-Q/P562) |
| huge | [P513](https://github.com/OS-Q/P513) | [P523](https://github.com/OS-Q/P523) | [P533](https://github.com/OS-Q/P533) | [P543](https://github.com/OS-Q/P543) | [P553](https://github.com/OS-Q/P553) | [P563](https://github.com/OS-Q/P563) |

| 无线广域 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P611](https://github.com/OS-Q/P611) | [P621](https://github.com/OS-Q/P621) | [P631](https://github.com/OS-Q/P631) | [P641](https://github.com/OS-Q/P641) | [P651](https://github.com/OS-Q/P651) | [P661](https://github.com/OS-Q/P661) |
| tiny | [P612](https://github.com/OS-Q/P612) | [P622](https://github.com/OS-Q/P622) | [P632](https://github.com/OS-Q/P632) | [P642](https://github.com/OS-Q/P642) | [P652](https://github.com/OS-Q/P652) | [P662](https://github.com/OS-Q/P662) |
| huge | [P613](https://github.com/OS-Q/P613) | [P623](https://github.com/OS-Q/P623) | [P633](https://github.com/OS-Q/P633) | [P643](https://github.com/OS-Q/P643) | [P653](https://github.com/OS-Q/P653) | [P663](https://github.com/OS-Q/P663) |

| 低阶分析 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P711](https://github.com/OS-Q/P711) | [P721](https://github.com/OS-Q/P721) | [P731](https://github.com/OS-Q/P731) | [P741](https://github.com/OS-Q/P741) | [P751](https://github.com/OS-Q/P751) | [P761](https://github.com/OS-Q/P761) |
| tiny | [P712](https://github.com/OS-Q/P712) | [P722](https://github.com/OS-Q/P722) | [P732](https://github.com/OS-Q/P732) | [P742](https://github.com/OS-Q/P742) | [P752](https://github.com/OS-Q/P752) | [P762](https://github.com/OS-Q/P762) |
| huge | [P713](https://github.com/OS-Q/P713) | [P723](https://github.com/OS-Q/P723) | [P733](https://github.com/OS-Q/P733) | [P743](https://github.com/OS-Q/P743) | [P753](https://github.com/OS-Q/P753) | [P763](https://github.com/OS-Q/P763) |

| 通用分析 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P811](https://github.com/OS-Q/P811) | [P821](https://github.com/OS-Q/P821) | [P831](https://github.com/OS-Q/P831) | [P841](https://github.com/OS-Q/P841) | [P851](https://github.com/OS-Q/P851) | [P861](https://github.com/OS-Q/P861) |
| tiny | [P812](https://github.com/OS-Q/P812) | [P822](https://github.com/OS-Q/P822) | [P832](https://github.com/OS-Q/P832) | [P842](https://github.com/OS-Q/P842) | [P852](https://github.com/OS-Q/P852) | [P862](https://github.com/OS-Q/P862) |
| huge | [P813](https://github.com/OS-Q/P813) | [P823](https://github.com/OS-Q/P823) | [P833](https://github.com/OS-Q/P833) | [P843](https://github.com/OS-Q/P843) | [P853](https://github.com/OS-Q/P853) | [P863](https://github.com/OS-Q/P863) |

| 高阶分析 | platform 1 | platform 2 | platform 3 | platform 4 | platform 5 | platform 6 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| main | [P911](https://github.com/OS-Q/P911) | [P921](https://github.com/OS-Q/P921) | [P931](https://github.com/OS-Q/P931) | [P941](https://github.com/OS-Q/P941) | [P951](https://github.com/OS-Q/P951) | [P961](https://github.com/OS-Q/P961) |
| tiny | [P912](https://github.com/OS-Q/P912) | [P922](https://github.com/OS-Q/P922) | [P932](https://github.com/OS-Q/P932) | [P942](https://github.com/OS-Q/P942) | [P952](https://github.com/OS-Q/P952) | [P962](https://github.com/OS-Q/P962) |
| huge | [P913](https://github.com/OS-Q/P913) | [P923](https://github.com/OS-Q/P923) | [P933](https://github.com/OS-Q/P933) | [P943](https://github.com/OS-Q/P943) | [P953](https://github.com/OS-Q/P953) | [P963](https://github.com/OS-Q/P963) |

# Kotlin 单文件命令行编译工具

一个简单的 Kotlin 单文件命令行编译工具，使用 Gradle 作为套壳，旨在提高编译速度，将编译时间缩短至约 1.9 秒左右。

**说明：** Kotlin 官方提供的命令行编译工具速度较慢，即使是编译运行极小的代码片段也需要超过 8 秒。然而，我又不想为每个小代码片段都创建一个独立的 Gradle 项目来进行编译和运行。

Gradle 配置文件位于 template 文件夹中，修改其中的参数调整命令行编译的设置。

## 使用方法

查看 `test.bat` 文件以

```bash
python mykotlinc.py test.kt  # 第一个参数必须是代码文件路径
python mykotlinc.py test.kt clear  # 清理生成的 ./build/build，clear 参数必须跟在文件路径后面
```

您还可以在后面添加原本的 Gradle 命令行参数：

```bash
python mykotlinc.py test.kt -w --no-rebuild --configuration-cache --parallel --daemon --build-cache
```

或者使用直接执行生成的可执行文件：

```bash
"./mykotlinc" test.kt
"./mykotlinc" test.kt -w --no-rebuild --configuration-cache --parallel --daemon --build-cache
```

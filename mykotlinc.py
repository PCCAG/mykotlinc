import os
import subprocess
import sys
from shutil import rmtree

# from httpx import delete
from cherk_file_modify import update_hash, template_file_is_modify

# 目录结构
"""
|+-- src/
    |    |+-- main/
    |    |    |+-- kotlin/
    |    |    |    |-- Helloworld.kt
    |    |    |+-- resources/
    |-- build.gradle
    |-- gradlew
    |-- gradlew.bat
    |-- run.bat
    |-- settings.gradle
"""


Content = {}
Content_templat_path_dict = {}
template_files_name = {
    "Helloworld.kt",
    "build.gradle",
    "gradlew",
    "gradlew.bat",
    "run.bat",
    "settings.gradle",
    "gradle.properties",
}
for i in template_files_name:
    template_path = os.path.join(os.getcwd(), "template", i)
    with open(
        template_path,
        "r",
        encoding="UTF-8",
        errors="ignore",
    ) as f:
        Content[i] = f.read()
        Content_templat_path_dict[i] = template_path


def make_most_simple_gradle_kotlin_project(current_path: str = os.getcwd()):
    # 从模板读取

    contentdict: dict = Content

    try:
        path_hello_kotlin: str = os.path.join(current_path, "src", "main", "kotlin")
        path_hello_resources: str = os.path.join(
            current_path, "src", "main", "resources"
        )
        # ...\src\main\kotlin\Helloworld.kt
        os.makedirs(path_hello_kotlin, exist_ok=True)
        # print(path_hello_kotlin)
        os.makedirs(path_hello_resources, exist_ok=True)
        # print(path_hello_resources)

        #
        #
        path_Helloworld = os.path.join(path_hello_kotlin, "Helloworld.kt")
        # first write
        if not os.path.exists(path_Helloworld):
            with open(path_Helloworld, "w") as f:
                f.write(contentdict["Helloworld.kt"])
        else:
            # modify if update
            if template_file_is_modify(
                "Helloworld.kt", filename_filepath_dict=Content_templat_path_dict
            ):
                with open(path_Helloworld, "w") as ff:
                    ff.write(contentdict["Helloworld.kt"])
                print("更新 Helloworld.kt")
                update_hash(
                    filename_filepath_dict=Content_templat_path_dict,
                    update_file_name="Helloworld.kt",
                )
        # print(path_Helloworld)
        # or contentdict.pop()
        del contentdict["Helloworld.kt"]
        for k, v in contentdict.items():
            pathi = os.path.join(current_path, k)
            # first write
            if not os.path.exists(pathi):
                with open(
                    pathi,
                    "w",
                    encoding="UTF-8",
                    errors="ignore",
                ) as f2:
                    f2.write(v)
            else:
                # modify if update
                if template_file_is_modify(
                    k, filename_filepath_dict=Content_templat_path_dict
                ):
                    with open(
                        pathi,
                        "w",
                        encoding="UTF-8",
                        errors="ignore",
                    ) as f3:
                        f3.write(v)
                    print(f"更新 {k}")
                    update_hash(
                        filename_filepath_dict=Content_templat_path_dict,
                        update_file_name=k,
                    )
            # print(os.path.join(current_path, k))
        # print("创建成功")
    except Exception:

        print("发生未知错误!")
        sys.exit()

        # print("创建失败!")


def mycompilter(
    file_path: str,
    project_path: str = os.getcwd(),
    params: str = "",
    toclearbuild: bool = False,
):
    # 创建gradle项目
    make_most_simple_gradle_kotlin_project(project_path)

    def read_from_code(path: str = file_path) -> str:
        with open(path, "r", encoding="UTF-8", errors="ingore") as f:
            return f.read()

    def change_code(write_code: str, original_code_path: str) -> bool:
        # print(original_code_path)
        with open(original_code_path, "w+", encoding="UTF-8", errors="ignore") as f:
            if wirte_code == f.read():
                return False
            f.write(write_code)
            return True

    def delete_build(project_path=project_path):
        if project_path != os.getcwd():
            rmtree(project_path)
            print("删除已经构建")

    # 读取代码
    wirte_code = read_from_code(file_path)
    # 改变代码
    change_code(
        wirte_code,
        original_code_path=os.path.join(
            project_path, "src", "main", "kotlin", "Helloworld.kt"
        ),
    )

    # 使用subprocess运行命令，并捕获输出

    command = (
        # f"echo on && cd {project_path} && gradle run -w --daemon --build-cache --max-workers 6 "
        f"cd {project_path} && gradle run {params}"
    )
    # print(command)
    # command = f"""echo '{command}' && {command}"""

    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    # 打印输出结果
    # print("输出结果：\n")
    print(result.stdout)

    if result.stderr.strip().__len__() > 0 or toclearbuild:
        # 打印错误信息（如果有的话）
        print("错误信息：\n")
        print(result.stderr)
        delete_build()

    # 打印命令的返回码
    print("返回码：\n", result.returncode)


if __name__ == "__main__":

    arguments = sys.argv[1:]

    file_path = arguments[0]

    toclear = arguments[1]
    if toclear.strip() == "clear":

        toclear = True
    else:
        toclear = False

    params = " ".join(arguments[2:])

    if os.path.exists(file_path):
        mycompilter(
            file_path=file_path,
            project_path=os.path.join(os.getcwd(), "build", "build"),
            params=params,
            toclearbuild=toclear,
        )
    else:
        print(f"无法找到 {file_path}")

import os
from sys import platform

def main() -> None:
    with open('.gitignore', 'r') as file:
        for line in file:
            tmp: str = ""
            for x in line:
                if x != '\n':
                    tmp += x
            if tmp == "/.vscode":
                tmp = ""
                continue
            if platform == "linux" or platform == "linux2":
                os.system(f"rm -rf {tmp}")
            elif platform == "win32":
                os.system(f"del {tmp}")
            elif platform == "darwin":
                os.system(f"rm -rf {tmp}")
            else:
                os.system(f"rm -rf {tmp}")

if __name__ == '__main__':
    main()

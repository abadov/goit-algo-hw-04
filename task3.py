import os
from colorama import Fore, Style


def traverse_with_oswalk(root_path: str) -> None:
    """
    використання os.walk() для рекурсивного пробіганню по директорії
    """
    # видаляємо трейлінг слеш
    root_path = root_path[0:-1] if root_path.endswith(os.sep) else root_path

    for root, dirs, files in os.walk(root_path):
        # розрахувати рівень вкладеності
        level = root.replace(root_path, '').count(os.sep)
        indent = "  " * level

        # вивести назву директорії
        folder_name = os.path.basename(root)
        if level == 0:
            print(f"📁 {Fore.CYAN}{folder_name or root}/")
        else:
            print(f"{indent}📁 {Fore.CYAN}{folder_name}/")

        # вивести назви файлів у директорії
        sub_indent = "  " * (level + 1)
        for file in sorted(files):
            print(f"{sub_indent}📄 {Fore.GREEN}{file}")

    print(f"{Style.RESET_ALL}\nReset back to normal colors.")

if __name__ == '__main__':
    traverse_with_oswalk('E:\\tmp\\root\\')

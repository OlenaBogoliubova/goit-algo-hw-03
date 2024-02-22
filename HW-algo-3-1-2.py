import shutil
import argparse
from pathlib import Path


def copy_and_sort_recursive(src_path, dest_path='dist'):
    try:
        src_path = Path(src_path)
        dest_path = Path(dest_path)

        if src_path.is_dir():
            for item in src_path.iterdir():
                if item.is_dir():
                    copy_and_sort_recursive(item, dest_path)
                elif item.is_file():
                    _, file_extension = item.suffix, item.stem
                    dest_subdir = dest_path / file_extension[1:]
                    dest_file_path = dest_subdir / item.name

                    dest_subdir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, dest_file_path)

        print("Копіювання та сортування завершено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Копіювання та сортування файлів.')
    parser.add_argument(
        'src_path', help='Шлях до вихідної директорії або файлу')
    parser.add_argument('dest_path', nargs='?', default='dist',
                        help='Шлях до директорії призначення (за замовчуванням: dist)')
    args = parser.parse_args()

    copy_and_sort_recursive(args.src_path, args.dest_path)


if __name__ == "__main__":
    main()

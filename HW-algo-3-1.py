import os
import shutil
import argparse


def copy_and_sort(src_dir, dest_dir='dist'):
    try:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                src_path = os.path.join(root, file)
                _, file_extension = os.path.splitext(file)

                dest_subdir = os.path.join(dest_dir, file_extension[1:])
                dest_path = os.path.join(dest_subdir, file)

                os.makedirs(dest_subdir, exist_ok=True)
                shutil.copy2(src_path, dest_path)

        print("Копіювання та сортування завершено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Копіювання та сортування файлів.')
    parser.add_argument('src_dir', help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', nargs='?', default='dist',
                        help='Шлях до директорії призначення (за замовчуванням: dist)')
    args = parser.parse_args()

    copy_and_sort(args.src_dir, args.dest_dir)


if __name__ == "__main__":
    main()

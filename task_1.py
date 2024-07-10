from pathlib import Path
import shutil
import argparse

# ANSI escape codes for colored output
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"

def copy_and_sort_files(source_dir, dest_dir="dist"):
      # Конвертуємо шлях директорії у об'єкт Path
      source_dir = Path(source_dir)
      dest_dir = Path(dest_dir)
   
      # Перевіряємо, чи існує вихідна директорія
      if not source_dir.exists():
         print(f"{COLOR_BLUE}Source directory does not exist!{COLOR_RESET}")
         return # Якщо директорія не існує, виводимо повідомлення і завершуємо виконання функції
     # Перевіряємо, чи існує директорія призначення
      if not dest_dir.exists():
        #  директорія призначення не існує, створюємо її
         dest_dir.mkdir()
      # Ітеруємося по всіх елементах у вихідній директорії
      for item in source_dir.iterdir():
         if item.is_dir():
               # Рекурсивно обробляємо піддиректорії
               copy_and_sort_files(item, dest_dir)
         elif item.is_file():
               # Отримуємо розширення файлу
               extension = item.suffix[1:] # Видаляємо крапку з розширення
                # Створюємо піддиректорію для файлів з таким розширенням
               dest_subdir = dest_dir / extension
               dest_subdir.mkdir(exist_ok=True)
               # Копіюємо файл до відповідної піддиректорії
               shutil.copy2(item, dest_subdir)

def main():
    parser = argparse.ArgumentParser(description='Копіювання файлів з сортуванням за розширенням.')
    # Додаємо аргумент для вихідної директорії
    parser.add_argument('src', type=Path, help='Шлях до вихідної директорії')
    # Додаємо аргумент для директорії призначення
    parser.add_argument('dest', type=Path, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням "dist")')
    
    # Парсимо аргументи командного рядка
    args = parser.parse_args()
    
    # Перевіряємо, чи існує вихідна директорія і чи є вона директорією
    if not args.src.is_dir():
        print(f"Помилка: Директорія {args.src} не існує або не є директорією.")
        return
    args.dest.mkdir(parents=True, exist_ok=True)
    copy_and_sort_files(args.src, args.dest)
    print(f"Файли успішно скопійовані до {args.dest}")

if __name__ == "__main__":
    main()
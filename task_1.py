from pathlib import Path
import shutil
import argparse

# ANSI escape codes for colored output
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[91m"

def copy_and_sort_files(source_dir, dest_dir="dist"):
      # Конвертуємо шлях директорії у об'єкт Path
      source_dir = Path(source_dir)
      dest_dir = Path(dest_dir)
   
      if not source_dir.exists():   # Перевіряємо, чи існує вихідна директорія
         print(f"{COLOR_BLUE}Вихідна директорія не існує!{COLOR_RESET}")
         return # Якщо директорія не існує, виводимо повідомлення і завершуємо виконання функції
     
      if not dest_dir.exists(): # Перевіряємо, чи існує директорія призначення
          try:
             dest_dir.mkdir() #  директорія призначення не існує, створюємо її
          except Exception as e:
            print(f"{COLOR_RED}Не вдалося створити директорію призначення: {e}{COLOR_RESET}")
            return
          
      for item in source_dir.iterdir():# Ітеруємося по всіх елементах у вихідній директорії
          try:  
              if item.is_dir(): # Перевіряємо, чи є елемент директорією
               copy_and_sort_files(item, dest_dir) # Рекурсивно обробляємо піддиректорії
              elif item.is_file():
               # Отримуємо розширення файлу
               extension = item.suffix[1:] # Видаляємо крапку з розширення
               dest_subdir = dest_dir / extension  # Це шлях до піддиректорії, яку потрібно створити з іменем директорії таким як розширення у файлів
               dest_subdir.mkdir(exist_ok=True) # Створюємо піддиректорію, якщо вона не існує
               shutil.copy2(item, dest_subdir) # Копіюємо файл до відповідної піддиректорії
          except Exception as e:
            print(f"{COLOR_RED}Не вдалося обробити {item}: {e}{COLOR_RESET}")

def main():
    parser = argparse.ArgumentParser(description='Копіювання файлів з сортуванням за розширенням.')
    # Додаємо аргумент для вихідної директорії
    parser.add_argument('src', type=Path, help='Шлях до вихідної директорії')
    # Додаємо аргумент для директорії призначення
    parser.add_argument('dest', type=Path, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням "dist")')
    

    args = parser.parse_args() # Парсимо аргументи командного рядка
    
    if not args.src.is_dir(): # Перевіряємо, чи існує вихідна директорія і чи є вона директорією
        print(f"Помилка: Директорія {args.src} не існує або не є директорією.")
        return
    
     # Створюємо директорію призначення, якщо вона не існує
    try:
        args.dest.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"{COLOR_RED}Не вдалося створити директорію призначення: {e}{COLOR_RESET}")
        return
    copy_and_sort_files(args.src, args.dest)
    print(f"Файли успішно скопійовані до {args.dest}")

if __name__ == "__main__":
    main()
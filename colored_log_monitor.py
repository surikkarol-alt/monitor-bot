import time
from colorama import init, Fore

# Инициализация цветного вывода (для Windows/Linux)
init(autoreset=True)

log_file = "logs.txt"   # тот же файл, куда пишет log_writer.py

def color_line(line):
    """Функция выбирает цвет строки по типу"""
    if "ERROR" in line:
        return Fore.RED + line.strip()
    elif "WARNING" in line:
        return Fore.YELLOW + line.strip()
    elif "OK" in line or "RUNNING" in line:
        return Fore.GREEN + line.strip()
    else:
        return Fore.WHITE + line.strip()

# Основной цикл мониторинга
try:
    with open(log_file, "r") as f:
        # Сразу переходим в конец файла, чтобы следить за новыми записями
        f.seek(0, 2)
        print(Fore.CYAN + "📡 Starting colored log monitor...\n")

        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            print(color_line(line))
except FileNotFoundError:
    print(f"Ошибка: Файл {log_file} не найден. Сначала запустите скрипт, создающий логи.")

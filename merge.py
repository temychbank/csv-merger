import pandas as pd
from pathlib import Path

# Папка с исходными CSV
folder = Path("data")

# Находим все CSV-файлы в папке
files = list(folder.glob("*.csv"))
print(f"Найдено файлов: {len(files)}")

# Читаем каждый файл и складываем в список
frames = []
for f in files:
    df = pd.read_csv(f, sep=";", skiprows=1)
    frames.append(df)

# Склеиваем все таблицы в одну
result = pd.concat(frames, ignore_index=True)

# Сохраняем в Excel
result.to_excel("итог.xlsx", index=False)

print("Готово! Файл итог.xlsx создан.")
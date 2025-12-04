import sys
import os

print("=" * 60)
print("Проверка настроек PyCharm для QGIS")
print("=" * 60)

# Основная информация
print(f"Python: {sys.executable}")
print(f"Версия Python: {sys.version.split()[0]}")

# Проверка путей
print(f"\nПуть к qgis-ltr: D:\\Programs\\QGIS 3.40.13\\apps\\qgis-ltr")
print(f"Существует: {os.path.exists(r'D:\Programs\QGIS 3.40.13\apps\qgis-ltr')}")

# Добавляем путь к QGIS Python модулям
qgis_python_path = r'D:\Programs\QGIS 3.40.13\apps\qgis-ltr\python'
print(f"\nДобавляем путь: {qgis_python_path}")
print(f"Существует: {os.path.exists(qgis_python_path)}")

if qgis_python_path not in sys.path:
    sys.path.insert(0, qgis_python_path)

# Пробуем импортировать
print("\nПопытка импорта QGIS...")
try:
    # Простой импорт для проверки
    import qgis

    print("✓ Модуль 'qgis' найден")

    # Основной импорт
    from qgis.core import *

    print(f"✓ QGIS {Qgis.QGIS_VERSION} загружен!")

    # Проверка пути
    print(f"✓ QGIS prefix: {QgsApplication.prefixPath()}")

    print("\n" + "=" * 60)
    print("🎉 ВСЕ РАБОТАЕТ! Можно начинать разработку.")
    print("=" * 60)

except ImportError as e:
    print(f"✗ Ошибка импорта: {e}")
    print("\nРешение:")
    print("1. Убедитесь, что используете интерпретатор из QGIS")
    print("2. Путь: D:\\Programs\\QGIS 3.40.13\\apps\\Python312\\python.exe")

except Exception as e:
    print(f"✗ Другая ошибка: {e}")
    print(f"\nПолный sys.path:")
    for i, path in enumerate(sys.path[:10]):  # первые 10 путей
        print(f"  {i}. {path}")

print("=" * 60)
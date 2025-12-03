"""
Инициализация QGIS для работы в PyCharm
Запускайте этот скрипт в начале ваших проектов
"""

import sys
import os


def setup_qgis():
    """Настройка путей для QGIS"""

    # Путь к установке QGIS
    QGIS_ROOT = r'D:\Programs\QGIS 3.40.13'

    # Добавляем путь к Python модулям QGIS
    qgis_python_path = os.path.join(QGIS_ROOT, 'apps', 'qgis-ltr', 'python')
    if qgis_python_path not in sys.path:
        sys.path.insert(0, qgis_python_path)

    # Устанавливаем переменные окружения
    os.environ['QGIS_PREFIX_PATH'] = os.path.join(QGIS_ROOT, 'apps', 'qgis-ltr')
    os.environ['PATH'] = os.path.join(QGIS_ROOT, 'bin') + ';' + os.environ.get('PATH', '')

    print(f"✅ QGIS настроен из: {QGIS_ROOT}")
    return True


def init_qgis(gui_enabled=False):
    """Инициализация QGIS приложения"""

    if not setup_qgis():
        return None

    try:
        from qgis.core import QgsApplication

        # Устанавливаем путь
        QGIS_ROOT = r'D:\Programs\QGIS 3.40.13'
        prefix_path = os.path.join(QGIS_ROOT, 'apps', 'qgis-ltr')

        # Инициализируем QGIS
        QgsApplication.setPrefixPath(prefix_path, True)
        app = QgsApplication([], gui_enabled)
        app.initQgis()

        print(f"✅ QGIS {app.applicationVersion()} инициализирован")
        print(f"   Prefix path: {prefix_path}")

        return app

    except Exception as e:
        print(f"❌ Ошибка инициализации QGIS: {e}")
        return None


# Автоматическая настройка при импорте
setup_qgis()

# Пример использования:
if __name__ == "__main__":
    print("Тестирование QGIS...")

    # Инициализируем без GUI (для скриптов)
    qgs_app = init_qgis(gui_enabled=False)

    if qgs_app:
        from qgis.core import QgsProject, QgsVectorLayer

        print("\nДоступные провайдеры:")
        from qgis.core import QgsProviderRegistry

        for provider in QgsProviderRegistry.instance().providerList():
            print(f"  - {provider}")

        # Закрываем QGIS
        qgs_app.exitQgis()
        print("\n✅ QGIS успешно завершен")
# Драгоценная Лилия

Интернет-магазин ювелирных украшений на Django и SQLite. Страницы формируются серверными Django-шаблонами на основе Bisum.

Каталог содержит 190 позиций с фотографиями. Работают поиск и фильтры, варианты размеров, избранное, корзина, регистрация и оформление заказов.

## Запуск

Нужен Python 3.11 или новее.

```powershell
cd laba3_site
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py import_catalog
.\.venv\Scripts\python.exe manage.py runserver
```

Откройте http://127.0.0.1:8000/.

[Подробная инструкция и структура данных](laba3_site/README.md).

Исходные каталог Excel и изображения находятся в `laba3_site/source_data/`. Локальная база пользователей и заказов и виртуальное окружение в Git не включаются; база создаётся командами выше.

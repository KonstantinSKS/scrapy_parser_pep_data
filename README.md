# scrapy_parser_pep

## Описание
Паосер на базе фреймворка Scrapy предназначен для сбора данных документов PEP(Python Enhancement Proposals) с сайта https://www.python.org/.
Парсер cобирает номера, названия и статусы всех PEP и сохраняет списки в csv-файл(номер, название и статус),
также парсер сохраняет сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).

## Технолгии
- Python 3.9
- Scrapy 2.5

## Запуск проекта
Клонировать репозиторий и перейти в директорию проекта:
```
git clone https://github.com/KonstantinSKS/scrapy_parser_pep.git
```
```
cd scrapy_parser_pep
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
### Команда для Windows:
```
source venv/Scripts/activate
```
### Для Linux и macOS:
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
## Запуск парсера:
В активированном виртуальном окружении проекта ввести в консоли команду:
```
scrapy crawl pep
```
### Файды будут сохранены в дериктории /results

# Автор: 
Стеблев Константин

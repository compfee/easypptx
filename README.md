# easy.pptx  
![Static Badge](https://img.shields.io/badge/python-blue) ![Static Badge](https://img.shields.io/badge/FastAPI-blue) ![Static Badge](https://img.shields.io/badge/transformers-orange)

Этот проект на FastAPI представляет собой сервис, который поможет создавать красивые презентации из объемных PDF документов, 
таких как научные статьи, дипломы, отчеты о деятельности компании, бизнес-планы и многое другое. 
Сервис осуществляет парсинг PDF файлов, извлекает заголовки и изображения, создает краткое изложение текста и создает дизайн презентации с помощью искусственного интеллекта.  

<a name="Оглавление"></a>
## Оглавление
- [Структура проекта](#Структурапроекта)
- [Данные](#Данные)
- [Установка и запуск](#Установкаизапуск)
- [Суммаризация текста](#Суммаризациятекста)
- [Генерация графических элементов](#Генерацияграфическихэлементов)
- [Генерация слайдов](#Генерацияслайдов)
- [Дизайн](#Дизайн)

<a name="Структурапроекта"></a>
## Структура проекта
- pdf_parse.py: содержит класс PDFParser для парсинга документов в формате PDF.  
- pptx_generator.py: содержит класс PPTGenerator для создания слайдов из суммаризованного текста и других данных.  
- summarization.py: содержит модели для суммаризации текста с использованием библиотеки Transformers.  
- pipelines.py: содержит пайплайны для сервиса на базе FastAPI.  
- config.py: файл с конфигурациями проекта.  
- main.py: основной файл для запуска сервиса с использованием декораторов FastAPI.  

<a name="Данные"></a>
## Данные
- TEST_FILE.pdf: исходный файл в формате PDF для тестирования.  
- parsed.txt: извлеченный текст из исходного PDF файла.  
- parsed_df.csv: разделенный текст из исходного PDF файла.  
- summary.csv: результат суммаризации текста.  
- df_ru_2.parquet.gzip: датасет для тренировки и экспериментов с моделями.  

<a name="Установкаизапуск"></a>
## Установка и запуск
- Склонируйте репозиторий на локальную машину.  
- Установите необходимые зависимости, выполнив команду pip install -r requirements.txt.  
- Запустите сервис, выполнив команду python main.py.  
- Перейдите по ссылке http://localhost:8000 в браузере для использования сервиса.  

<a name="Суммаризациятекста"></a>
## Суммаризация текста  

<a name="Генерацияграфическихэлементов"></a>
## Генерация графических элементов 

<a name="Генерацияслайдов"></a>
## Генерация слайдов  

<a name="Дизайн"></a>
## Дизайн


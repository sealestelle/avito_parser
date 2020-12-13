# avito_parser
["Ссылка на задание"]https://github.com/avito-tech/mi-backend-trainee-assignment
## Запуск
### Используется Docker и запускатеся через:
`docker-compose up`
## Немного документации по методам
### /add
#### Пример использования:
`http://localhost:5057/add?search=компьютер&&area=moskva`
* `search`: Поисковая фраза
* `area`: Регион
#### Метод сгенерирует id в виде `search:area` в формате base64, создаст коллекцию в MongoDB и добавит документ со значением времени и количеством объявлений. Если id уже существует, то добавится только документ.  
#### Метод вернет:
`{"id":"Значение id"}`
### /stat
#### Пример использования:
`http://localhost:5057/stat?id_search_area=cGM6bW9za3Zh&&time_s=1607901928&&time_e=1607902658`
* `id_search_area`: id связки поисковая фраза + регион
* `time_s`: Начальное время
* `time_e`: Конечное время
#### Метод пройдет по документам выбранной связки и найдет записи, которые были созданы в выбранный промежуток времени. Если свзяки не существует или статистики за данный промежуток нет, то вернет пустой словарь
#### Метод вернет:
`[{"time":"count"},...,{"time:"count"}]`
### /top
#### Пример использования:
`http://localhost:5057/top?id_search_area=cGM6bW9za3Zh`
* `id_search_area`: id связки поисковая фраза + регион
#### Метод раскодирует id, распарсит сайт avito и найдет 5 первых объявлений 
#### Метод вернет:
`{"top":[{"title":"Заголовок объявления", "link":"Ссылка на объявление"}]}`

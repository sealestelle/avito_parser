# avito_parser
Тестовое задание для стажёра Backend в команду MI
## Запуск
Используется Docker и запускатеся через:
'docker-compose up'
## Немного документации по методам
### add
Пример использования:
`http://localhost:5057/add?search=компьютер&&area=moskva`
`search`: Поисковая фраза
`area`: Регион
Метод сгенерирует id в виде `search:area` в формате base64, создаст коллекцию в MongoDB и добавит документ со значением времени и количеством объявлений. Если id уже существует, то добавится только документ. Метод вернет:
`{"id":"Значение id"}`

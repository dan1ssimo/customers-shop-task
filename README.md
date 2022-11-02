# customers-shop-task

## Инструкции к репозиторию:

### Запуск сервисов
1. Клонируем репозиторий ```git clone https://github.com/dan1ssimo/customers-shop-task.git```
2. Проваливаемся в него ```cd customers-shop-task```
3. Поднимаем сервис ```docker build -t solution_service .```
### Запуск тестов
После того, как подняли сервис: 
1. Перейдите внутрь создавшегося контейнера ```docker exec -ti <id> bash```
2. Запустите тесты командой ```pytest tests/```

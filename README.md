# customers-shop-task

## Инструкции к репозиторию:
1. Клонируем репозиторий ```git clone https://github.com/dan1ssimo/customers-shop-task.git```
2. Проваливаемся в него ```cd customers-shop-task```
3. Создаемм докер-образ ```docker build -t solution_service .```
4. Запускаем контейнер ```docker run -d -t -p 8895 -v "<path_to_repo>":/app solution_service```
5. Заходим внутрь контейнера ```docker exec -ti <container_name> bash```
6. Можно проверить первое задание, зайдя в jupyterlab ```jupyter-lab --allow-root -ip 0.0.0.0 -port 8895```
7. Чтобы запустить сервис второй задачки нужно перейти в папку task_2 и запустить скрипт app.py: ```cd task_2``` ```python app.py```
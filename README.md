# customers-shop-task
solution for an interview task

```
cd ./task_2
docker build -t solution_2 .
docker run -d -t -v "C:\Users\Danil\Desktop\solution\solution_2_fastapi":/app
docker exec -ti <container_name> bash
```
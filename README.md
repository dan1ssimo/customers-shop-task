# customers-shop-task
solution for an interview task

```
cd ./task_2
docker build -t solution_2 .
docker run -d -t -p 8895 -v "C:\Users\Danil\Desktop\solution\customers-shop-task":/app solution_2
docker exec -ti <container_name> bash
jupyter-lab --allow-root -ip 0.0.0.0 -port 8895
```
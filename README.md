# APS Computação em Nuvem


## Rotas que podem ser usadas:
```
GET /Tarefa/ -> Lista todas as tarefas existentes.

POST /Tarefa/ -> Adiciona uma nova tarefa.

GET /Tarefa/id_tarefa -> Mostra uma tarefa especifica, definida pelo id da tarefa

PUT /Tarefa/id_tarefa -> Altera uma tarefa, definida pelo id da tarefa.

DELETE /Tarefa/id_tarefa -> Delete uma tarefa, definida pelo id da tarefa.

GET /healthcheck/ -> Verifica se o servidor esta funcionando devidamente.
```

## Utilizando o client

1) No arquivo [set_env](https://github.com/decoejz/APS-cloud-comp/blob/master/set_env) coloque o endereço em que o webserver esta sendo executado.

2) Execute o comando

```
source set_env
```

3) Para utilizar o client:

```
./tarefa help
```

Com isso é possível verificar todas as ações possíveis.

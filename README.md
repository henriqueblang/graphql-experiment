# GraphQL

## O que é

GraphQL é uma linguagem de consulta para APIs que, por meio de um esquema base, permite flexibilidade da resposta. Por ser *client-driven* e delegar mais controle dos dados aos usuários, é preferida por muitos desenvolvedores.

Dentre suas vantagens, GraphQL torna *payloads* mais leves, sendo este o motivo que levou sua criação pelo Facebook, e previsão da estruturada retornada. Com a possibilidade de especificar o retorno da API, evita-se o *over-fetching* comum em arquiteturas puramente RESTful.

Por outro lado, sua curva de aprendizado é maior, e não é possível realizar tanto upload de dados quanto caching.

Referências:
- https://fastapi.tiangolo.com/advanced/graphql/
- https://docs.graphene-python.org/en/latest/quickstart/
- https://graphql.org/
- http://blog.adnansiddiqi.me/getting-started-with-graphql-in-python-with-fastapi-and-graphene/

## Exemplos de queries para a API

### Criar uma nota
```
mutation {
  insertNote(title:"An example note", description:"An example description") {
    id
    title
  }
}
```

### Buscar uma nota
```
query {
  notes(id:1) {
    title
    description
  }
}
```

### Atualizar uma nota
```
mutation {
  updateNote(id:2, title:"A new title") {
    title
    description
  }
}
```

### Deletar todas as notas
```
mutation {
  deleteNotes {
    notes {
      title
      description
    }
  }
}
```


import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp


internal_counter = 0
mock_database = {}


def insert_note(title, description):
    global internal_counter
    id = internal_counter

    mock_database[id] = {
        "title": title,
        "description": description
    }

    internal_counter += 1

    return {
        "id": id,
        "title": title,
        "description": description
    }

def read_notes(id=None):
    return mock_database.values() if id is None else [mock_database.get(id)]

def update_note(id, title=None, description=None):
    if title is not None:
        mock_database[id]["title"] = title

    if description is not None:
        mock_database[id]["description"] = description

    return mock_database[id]

def delete_notes(id=None):
    global mock_database

    result = None
    if id is None:
        result = mock_database.values()

        mock_database = {}
    else:
        result = [mock_database.pop(id)]

    return result


class Note(graphene.ObjectType):
    title = graphene.String()
    description = graphene.String()

class QueryNote(graphene.ObjectType):
    notes = graphene.List(Note, id = graphene.Int())

    def resolve_notes(self, info, id=None):
        return read_notes(id)

class InsertNote(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()

    class Arguments:
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, title, description):
        note = insert_note(title, description)

        return InsertNote(id=note["id"], title=note["title"])

class UpdateNote(graphene.Mutation):
    title = graphene.String()
    description = graphene.String()

    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, title=None, description=None):
        note = update_note(id, title, description)

        return UpdateNote(title=note["title"], description=note["description"])

class DeleteNotes(graphene.Mutation):
    notes = graphene.List(Note)

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id=None):
        note = delete_notes(id)

        return DeleteNotes(notes=note)

class Mutation(graphene.ObjectType):
    insert_note = InsertNote.Field()
    update_note = UpdateNote.Field()
    delete_notes = DeleteNotes.Field()

 
insert_note("My First Note", "A cool note.")
insert_note("A random note I remembered", "Oh, nevermind")
insert_note("Aaah wait, it's on the tip of my tongue", "Jesus, I forgot")


app = FastAPI()
 
app.add_route("/notes", GraphQLApp(schema=graphene.Schema(query=QueryNote, mutation=Mutation)))
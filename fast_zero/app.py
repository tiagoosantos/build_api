from http import HTTPStatus
from fastapi import FastAPI
from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB

app = FastAPI()

database = []  # Simulação de um banco de dados em memória

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.post('/users', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):

    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id
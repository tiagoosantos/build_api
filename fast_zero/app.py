from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema
from fastapi import FastAPI
from http import HTTPStatus

app = FastAPI()

database = []  # Simulação de um banco de dados em memória


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.get('/users/', response_model=UserList, status_code=HTTPStatus.OK)
def get_users():
    return {'users': database}


@app.post('/users', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


# @app.post('/users', response_model=UserPublic, status_code=HTTPStatus.CREATED)
# def create_user(user: UserSchema):


@app.put('/users/{user_id}', response_model=UserPublic, status_code=HTTPStatus.OK)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id
    return user_with_id

    # for index, existing_user in enumerate(database):
    #     if existing_user.id == user_id:
    #         updated_user = UserDB(id=user_id, **user.model_dump())
    #         database[index] = updated_user
    #         return updated_user
    # return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

from fastapi import FastAPI,Body,Path,Query
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel, Field
from typing import Optional,List


app= FastAPI()
app.title = "Mi primera aplicacion con fastapi"
app.version = "0.0.1"

class Movie(BaseModel):
    id:Optional [int]=None
    title:str = Field( min_length=1, max_length=15)
    sipnosis:str= Field( min_length=15, max_length=50)
    year : int = Field (2022 ,le=2023)
    rating: float = Field(ge=1, le=5)
    category: str = Field(min_length=2, max_length= 15)
    
    class Config:
        schema_extra ={
            "example":{
                "id":1,
                "title":"mi pelicula",
                "sipnosis":"descripcion de la pelicula",
                "year": 2023,
                "rating":9.8,
                "category":"accion"
            }
        }
    
    

movies = [
    {
    "id": 1,
    "title":"avatar",
    "sipnosis":"en un planeta llamado pandora donde sucederan muchas cosas por un presiado elemento",
    "year":2008,
    "rating":7.8,
    "category":"ciencia ficcion"
    },
     {
    "id": 2,
    "title":"avatar",
    "sipnosis":"en un planeta llamado pandora donde sucederan muchas cosas por un presiado elemento",
    "year":2008,
    "rating":7.8,
    "category":"accion"
    }
]


@app.get('/', tags=['home'])
def message():
    return HTMLResponse ('<h1>hola mundo </h1>')


@app.get('/Movies',tags=['movies'],response_model=List[Movie])
def get_movies() ->List[Movie]:
    return JSONResponse(content=movies)

@app.get('/movies/{id}',tags=['movies'], responses_model= Movie)
def get_movie(id : int= Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item  ["id"]== id:
            return JSONResponse(content=item)
    return JSONResponse(content=['no se encontro informacion'])



@app.get('/movies/',tags=['movies'],response_model=List[Movie])
def get_movies_by_category(category:str= Query(min_length=1, max_length=12)) -> List[Movie]:
    data=[item for item in movies if item['category'] == category]
    return JSONResponse(content=data)


@app.post('/movies/',tags=['movies'],response_model=dict)
def create_new_Movie( movie:Movie) -> dict:
    movies.append(movie)
       
    return JSONResponse(content={"message":"se ha registrado satisfactoriamente la pelicula"})


@app.put('/movies/{id}',tags=['movies'],response_model=dict)
def update_movie(id:int,movie:Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            item['title']=movie.title
            item['sipnosis']=movie.sipnosis
            item['year']=movie.year
            item['rating']=movie.rating
            item['category']=movie.category
    return JSONResponse(content={"message":"se ha modificado satisfactoriamente la pelicula"})




@app.delete('/movies/{id}',tags=['movies'],response_model=dict)
def delete_movie(id=int) -> dict:
    for item in movies:
      if item["id"]==id:
          movies.remove(item)
          return JSONResponse(content={"message":"se ha elimnado satisfactoriamente la pelicula"})


          

    


    
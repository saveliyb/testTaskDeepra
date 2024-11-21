from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, constr, ValidationError

app = FastAPI()


class QueryParams(BaseModel):
    name: constr(min_length=1, max_length=200) = "World"
    message: constr(min_length=1, max_length=200) = "Let's be friends"


def get_query_params(
    name: str = Query("World", min_length=1, max_length=200),
    message: str = Query("Let's be friends", min_length=1, max_length=200)
) -> QueryParams:
    try:
        return QueryParams(name=name, message=message)
    except ValidationError:
        raise HTTPException(status_code=442, detail="Validation error")


@app.get("/", response_class=PlainTextResponse)
def read_root(params: QueryParams = Depends(get_query_params)):
    return f"Hello, {params.name.strip().capitalize()}! {params.message.strip().capitalize()}!"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
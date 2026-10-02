from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Car REST API")

# Разрешаем CORS (чтобы позже можно было делать запросы из веб-приложения)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модель данных автомобиля (поля: марка, модель, год выпуска, цена)
class Car(BaseModel):
    brand: str    # Марка (например, "BMW")
    model: str    # Модель (например, "X5")
    year: int     # Год выпуска (например, 2021)
    price: int    # Цена в евро (например, 45000)

# База данных в памяти с тестовыми данными
db = {
    1: {"brand": "BMW", "model": "X5", "year": 2021, "price": 45000},
    2: {"brand": "Audi", "model": "A4", "year": 2019, "price": 22000}
}

# 1. GET: Получить список всех автомобилей
@app.get("/cars")
def get_cars():
    return db

# 2. GET: Получить автомобиль по его ID
@app.get("/cars/{car_id}")
def get_car(car_id: int):
    if car_id not in db:
        raise HTTPException(status_code=404, detail="Автомобиль не найден")
    return db[car_id]

# 3. POST: Добавить новый автомобиль[cite: 2]
@app.post("/cars", status_code=201)
def create_car(car: Car):
    new_id = max(db.keys(), default=0) + 1
    db[new_id] = car.model_dump()
    return {"id": new_id, "car": db[new_id]}

# 4. PUT: Изменить данные автомобиля по ID[cite: 2]
@app.put("/cars/{car_id}")
def update_car(car_id: int, car: Car):
    if car_id not in db:
        raise HTTPException(status_code=404, detail="Автомобиль не найден")
    db[car_id] = car.model_dump()
    return {"id": car_id, "updated": db[car_id]}

# 5. DELETE: Удалить автомобиль по ID[cite: 2]
@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    if car_id not in db:
        raise HTTPException(status_code=404, detail="Автомобиль не найден")
    deleted = db.pop(car_id)
    return {"message": "Автомобиль успешно удален", "car": deleted}
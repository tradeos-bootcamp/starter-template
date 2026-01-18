from fastapi import FastAPI

app = FastAPI(title="TradeOS API", version="0.1.0")

@app.get("/")
async def root():
    # TODO: Верните сообщение "Добро пожаловать в TradeOS API"
    return {"message": ""}

@app.get("/health")
async def health_check():
    # TODO: Верните статус работы API: {"status": "ok"}
    return {}

# ЗАДАНИЕ ДЛЯ СТУДЕНТА:
# 1. Дописать возвращаемые значения в функциях root и health_check.
# 2. Создать новый endpoint GET /products, который возвращает пустой список [].
# 3. Запустить сервер и проверить работу в Swagger UI.
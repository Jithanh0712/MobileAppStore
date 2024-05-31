from fastapi import FastAPI, HTTPException
from cassandra.cluster import Cluster
import execute

app = FastAPI()

@app.get('/')
async def bat_dau():
    return {'cassandra'}

@app.post("/update_price_app")
async def update_app_by_id(price, id):
    return execute.AppRecommendation.update_app_by_id(price, id)

@app.get("/find_10_app_store_by_prime_genre")
async def find_10_app_store_by_prime_genre(prime_genre):
    return execute.AppRecommendation.find_10_app_store_by_prime_genre(prime_genre)

@app.delete("/delete_app_store")
async def delete_app(user_rating):
    return execute.AppRecommendation.delete_app(user_rating)




@app.delete("/delete_bad_apps/")
async def delete_bad_apps():
    return execute.AppRecommendation.delete_bad_apps()


@app.get("/tim_app_bang_genre_giatien")
async def find_app_by_genre_giatien(prime_genre, low_price, high_price):
    return execute.AppRecommendation.find_app_by_primegenre_and_price(prime_genre, low_price, high_price)

@app.get("/tim_app_bang_track_name")
async def find_app_by_track_name(track_name):
    return execute.AppRecommendation.find_app_by_track_name(track_name)

@app.get('/recommend_free_app')
async def recommend_free_app():
    return execute.AppRecommendation.recommend_free_apps()

@app.delete("/delete_expensive_apps/")
async def delete_expensive_apps():
    return execute.AppRecommendation.delete_expensive_apps()

@app.get("/tim_app_bang_genre")
async def find_app_by_genre(prime_genre):
    return execute.AppRecommendation.find_app_by_genre(prime_genre)














@app.post("/create_table")
async def create_emp_table():
    return execute.AppRecommendation.create_emp_table()

@app.post("/create_new_user")
async def create_new_user(emp_id, emp_name, emp_city, emp_sal, emp_phone):
    return execute.AppRecommendation.create_new_user(emp_id, emp_name, emp_city, emp_sal, emp_phone)

@app.delete('/delete_Emp_By_Id')
async def delete_emp_by_id(emp_id):
    return execute.AppRecommendation.delete_emp_by_id(emp_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

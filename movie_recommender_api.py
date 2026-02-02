from fastapi import FastAPI
from pydantic import BaseModel
from semantic_movie_recommendations import retrive_semantic_recommendations

app = FastAPI()


class MovieQuery(BaseModel):
    query: str
    category: str
    tone: str

@app.post("/recommend")
def recommend(q: MovieQuery):
    recs = retrive_semantic_recommendations(q.query, q.category, q.tone)
    results = []
    for _, row in recs.iterrows():
        results.append({
            "title": row["title"],
            "poster": row["poster"],
            "description": row["description"]
        })
    return results
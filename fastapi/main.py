"""
Build a course review API. Complete the endpoints below.
Assume valid input: ratings are 1-5 and the ratings list is non-empty.

Run: cd fastapi, then fastapi dev main.py
"""
from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Create your mock database here using a built-in data structure (no libraries).
# Use whichever structure you think fits best and explain your choice.


"""
1. GET /courses -- Get all course reviews.

Response: 200
{
    "items": [
        {
            "id": 1,
            "course": "CMSC420",
            "professor": "Justin",
            "grade": "A",
            "term": "Fall",
            "year": 2026,
            "rating": 4.0,
            "num_ratings": 2
        }
    ]
}
Return {"items": []} if there are no reviews.
"""
@app.get("/courses")
def get_courses():
    # TODO: Return all reviews.
    return JSONResponse(status_code=501, content={"error": "Not implemented"})


"""
2. POST /courses -- Create a review. Repeated courses are allowed.

Request body:
{
    "course": "CMSC420",
    "professor": "Justin",
    "grade": "B-",
    "term": "Fall",
    "year": 2026,
    "rating": 5
}

Response:
If valid: 201, {"id": <new ID>}
"""
@app.post("/courses", status_code=201)
def add_review(body: dict = Body(...)):
    new_review = {
        "id": None,  # TODO: Choose a unique integer ID.
        "course": body["course"],
        "professor": body["professor"],
        "grade": body["grade"],
        "term": body["term"],
        "year": body["year"],
        "rating": body["rating"],
        "num_ratings": 1,
    }
    # TODO: Save new_review and return its ID.
    return JSONResponse(status_code=501, content={"error": "Not implemented"})


"""
3. PUT /courses/1/rating -- Add ratings to a review.
Update the average and count, including previous ratings. Keep other fields unchanged.

Request body:
{
    "ratings": [5, 3, 1]
}

Response:
If valid: 200, {"id": <ID>, "rating": <new average>, "num_ratings": <new count>}
If ID not found: 404, {"error": "Course not found"}
"""
@app.put("/courses/{course_id}/rating")
def update_rating(course_id: int, body: dict = Body(...)):
    ratings = body["ratings"]
    # TODO: Find the review, update its rating and count, and return the result.
    return JSONResponse(status_code=501, content={"error": "Not implemented"})

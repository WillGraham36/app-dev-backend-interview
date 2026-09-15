"""
Build a course review API. Complete the three TODOs in order.
Assume request bodies have the shown fields/types and ratings are numbers from 1 to 5.
No input validation, duplicate checks, or real database setup is required.

Run: cd fastapi, then fastapi dev main.py
"""
from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Mock database = an ordinary Python collection, not a database library.
# Choose a list of dictionaries OR a dictionary keyed by ID. Explain your choice.
# Define it here, outside the handlers, so all requests share the same collection.
# GET reads it, POST adds to it, PUT finds and changes a stored record.
# Data resets when the server restarts. No SQL or database methods are needed.
example_course = {
    "id": 1, "course": "CMSC420", "professor": "Justin", "grade": "A",
    "term": "Fall", "year": 2026, "rating": 4.0, "num_ratings": 2,
}
# Put example_course in your collection so you can try GET immediately:

next_id = 2


# 1. GET /courses -- Return every stored course review.
# Response: 200, {"items": [<course records>]} (an empty collection returns []).
@app.get("/courses")
def get_courses():
    # TODO: Read your collection and return its records as a JSON list in "items".
    return JSONResponse(status_code=501, content={"error": "Not implemented"})


# 2. POST /courses -- Save a new course review.
# Body: {"course": "CMSC420", "professor": "Justin", "grade": "B-",
#        "term": "Fall", "year": 2026, "rating": 5}
# Each submission creates a separate record; repeated courses are allowed.
# Response: 201, {"id": <new ID>}
@app.post("/courses", status_code=201)
def add_review(body: dict = Body(...)):
    global next_id
    new_review = {
        "id": next_id,
        "course": body["course"],
        "professor": body["professor"],
        "grade": body["grade"],
        "term": body["term"],
        "year": body["year"],
        "rating": body["rating"],
        "num_ratings": 1,
    }
    next_id += 1
    # TODO: Store new_review in your collection and return its ID with status 201.
    return JSONResponse(status_code=501, content={"error": "Not implemented"})


# 3. PUT /courses/1/rating -- Add ratings to an existing record.
# Body: {"ratings": [5, 3, 1]} (assume a non-empty list of valid ratings).
# Include the previous ratings when computing the new average; do not replace them.
# Hint: the old average and count tell you the old total score.
# Example: average 4.0, count 2 + [5, 3, 1] => average 3.4, count 5.
# Grade and course details stay as submitted in the initial review.
# Response: 200, {"id": 1, "rating": 3.4, "num_ratings": 5}
# Unknown ID: 404, {"error": "Course not found"}
@app.put("/courses/{course_id}/rating")
def update_rating(course_id: int, body: dict = Body(...)):
    ratings = body["ratings"]
    # TODO: Find the record, update its average AND count, and return those fields + ID.
    return JSONResponse(status_code=501, content={"error": "Not implemented"})

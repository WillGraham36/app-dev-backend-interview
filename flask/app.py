"""
Build a course review API. Complete the endpoints below.
Assume valid input: ratings are 1-5 and the ratings list is non-empty.

Run: cd flask, then python -m flask run
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

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
    return jsonify({"error": "Not implemented"}), 501


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
@app.post("/courses")
def add_review():
    body = request.get_json()
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
    return jsonify({"error": "Not implemented"}), 501


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
@app.put("/courses/<int:course_id>/rating")
def update_rating(course_id):
    ratings = request.get_json()["ratings"]
    # TODO: Find the review, update its rating and count, and return the result.
    return jsonify({"error": "Not implemented"}), 501

/*
Build a course review API. Complete the endpoints below.
Assume valid input: ratings are 1-5 and the ratings list is non-empty.
*/
const express = require("express");
const app = express();
app.use(express.json());

// Create your mock database here using a built-in data structure (no libraries).
// Use whichever structure you think fits best and explain your choice.





/*
1. GET /courses -- Get ALL course reviews.

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
*/
app.get("/courses", (req, res) => {
  // TODO: Return all reviews.
  res.status(501).json({ error: "Not implemented" });
});

/*
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
*/
app.post("/courses", (req, res) => {
  // TODO: Read the request body and fill in the values below.
  const newReview = {
    id: null, // TODO: Choose a unique integer ID.
    course: null,
    professor: null,
    grade: null,
    term: null,
    year: null,
    rating: null,
    num_ratings: null,
  };
  // TODO: Save newReview and return its ID.
  res.status(501).json({ error: "Not implemented" });
});

/*
3. PUT /courses/1/rating -- Add ratings to a review.
Update the average and count, including previous ratings. Keep other fields unchanged.

Request body:
{
    "ratings": [5, 3, 1]
}

Response:
If valid: 200, {"id": <ID>, "rating": <new average>, "num_ratings": <new count>}
If ID not found: 404, {"error": "Course not found"}
*/
app.put("/courses/:id/rating", (req, res) => {
  const courseId = Number(req.params.id);
  const ratings = req.body.ratings;
  // TODO: Find the review, update its rating and count, and return the result.
  res.status(501).json({ error: "Not implemented" });
});

// Starting server code, do not edit
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

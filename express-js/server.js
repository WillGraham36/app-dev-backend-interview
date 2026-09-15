/*
Build a course review API. Complete the three TODOs in order.
Assume request bodies have the shown fields/types and ratings are numbers from 1 to 5.
No input validation, duplicate checks, or real database setup is required.
*/
const express = require("express");
const app = express();
app.use(express.json());

// Mock database = an ordinary JavaScript collection, not a database library.
// Choose an array of objects OR a Map/object keyed by ID. Explain your choice.
// Define it here, outside the handlers, so all requests share the same collection.
// GET reads it, POST adds to it, PUT finds and changes a stored record.
// Data resets when the server restarts. No SQL or database methods are needed.
const exampleCourse = {
  id: 1, course: "CMSC420", professor: "Justin", grade: "A",
  term: "Fall", year: 2026, rating: 4.0, num_ratings: 2,
};
// Put exampleCourse in your collection so you can try GET immediately:

let nextId = 2;

// 1. GET /courses -- Return every stored course review.
// Response: 200, {"items": [<course records>]} (an empty collection returns []).
app.get("/courses", (req, res) => {
  // TODO: Read your collection and return its records as a JSON list in "items".
  res.status(501).json({ error: "Not implemented" });
});

// 2. POST /courses -- Save a new course review.
// Body: {"course": "CMSC420", "professor": "Justin", "grade": "B-",
//        "term": "Fall", "year": 2026, "rating": 5}
// Each submission creates a separate record; repeated courses are allowed.
// Response: 201, {"id": <new ID>}
app.post("/courses", (req, res) => {
  const body = req.body;
  const newReview = {
    id: nextId,
    course: body.course,
    professor: body.professor,
    grade: body.grade,
    term: body.term,
    year: body.year,
    rating: body.rating,
    num_ratings: 1,
  };
  nextId += 1;
  // TODO: Store newReview in your collection and return its ID with status 201.
  res.status(501).json({ error: "Not implemented" });
});

// 3. PUT /courses/1/rating -- Add ratings to an existing record.
// Body: {"ratings": [5, 3, 1]} (assume a non-empty list of valid ratings).
// Include the previous ratings when computing the new average; do not replace them.
// Hint: the old average and count tell you the old total score.
// Example: average 4.0, count 2 + [5, 3, 1] => average 3.4, count 5.
// Grade and course details stay as submitted in the initial review.
// Response: 200, {"id": 1, "rating": 3.4, "num_ratings": 5}
// Unknown ID: 404, {"error": "Course not found"}
app.put("/courses/:id/rating", (req, res) => {
  const courseId = Number(req.params.id);
  const ratings = req.body.ratings;
  // TODO: Find the record, update its average AND count, and return those fields + ID.
  res.status(501).json({ error: "Not implemented" });
});

// Starting server code, do not edit
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

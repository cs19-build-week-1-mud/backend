# backend

# initial endpoint

GET: /api/rooms

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "title": "Coveted Door Spot",
        "content": "30 feet away glistening through the cool shade of a mighty oak tree is a coveted door spot. You've been craving the day when you could pull up, run into the store, and come back out to a nice shaded car. Too bad there is another car gunning for the same spot."
    }
]


POST: /api-token-auth

HTTP 200 OK
Allow POST, HEAD, OPTIONS
Content-Type: application/json

{
    "token": "**************************"
}

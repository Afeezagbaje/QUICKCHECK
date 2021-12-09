# quickcheck_api
# HACKER NEWS API MODIFICATION
This is a Django web application that retrieves data from Hacker News API and makes it easier to navigate the news items. It provides search and filter functionality and also enables clients, through six API endpoints, to create news items, modify and delete only the items they created and provide read-only access to news items generated from Hacker News API server.

TECHNOLOGIES
The following technologies were used in this project:
Python
Django
Django REST Framework
SQLite 3


# Getting Started
To run this application locally:
- Open up terminal (on MacOS) and switch directory to Desktop by running:
```
cd ~
```
- For Windows, open git bash and switch directory to Desktop by running:
```
cd Desktop
```
- Clone the repository by running:
```
git clone https://github.com/Adeakim/quickcheck_api.git
```
- Then run the following commands consecutively
```
cd hackernews_api
```
```
python3 -m venv venv 
```
- To activate virtual environment (MacOS users): 
```
source venv/bin/activate
```
- To activate virtual environment (Windows users):
```
source venv/Source/activate
```
- Install dependencies as follows (both MacOS & Windows):
```
pip3 install -r requirements.txt
```
- Make migrations by running the commands below in succession:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
- To start the Django server, run:
```
python3 manage.py runserver --noreload
```

this fetches and updates data from the hacker news api after the time specified in the scheduler
data becomes available in the endpoints only after then.

<!-- Endpoints -->
The endpoints, expected payloads, and responses are described below


<!-- .......................................READ ONLY ENDPOINTS................................................ -->
<!-- Get all news stories -->

METHOD : GET 
ROUTE:  api/stories/
ON LOCALHOST: http://127.0.0.1:8000/api/stories/
QUERY PARAMETERS: "type", "author"
SEARCH QUERY AVAILABLE


ILLUSTRATION 
send a get request to http://127.0.0.1:8000/api/stories/

RESPONSE FORMAT
{
    "count": 15,
    "next": "http://127.0.0.1:8000/api/stories/?page=2",
    "previous": null,
    "results": [
        {
            "id": "cd182687-e0f0-4f5b-9f3c-dde735f0818b",
            "author": "omolade",
            "descendants": 21,
            "score": 23,
            "type": "jobs",
            "title": "how to make money whie sleeping",
            "url": "https://www.goal.com/en-ng/news/car-v-nigeria-gernot-rohr-has-every-advantage-to-make-amends-for-/1w0z2wn53ul2y1eadhwpv7dnlj"
        }
}

<!-- Get a news items -->
METHOD : GET 
ROUTE:  api/stories/<uuid:id>
ON LOCALHOST: http://127.0.0.1:8000/api/stories/cd182687-e0f0-4f5b-9f3c-dde735f0818b/

RESPONSE FORMAT
{
    "id": "cd182687-e0f0-4f5b-9f3c-dde735f0818b",
    "author": "omolade",
    "descendants": 21,
    "score": 23,
    "type": "jobs",
    "title": "how to make money whie sleeping",
    "url": "https://www.goal.com/en-ng/news/car-v-nigeria-gernot-rohr-has-every-advantage-to-make-amends-for-/1w0z2wn53ul2y1eadhwpv7dnlj"
}

<!-- Get top level comments of a story item -->
METHOD : GET 
ROUTE:  api/stories/<uuid:id>/comments/
ON LOCALHOST: http://127.0.0.1:8000/api/stories/cd182687-e0f0-4f5b-9f3c-dde735f0818b/comments/

RESPONSE FORMAT
[
    {
        "id": "462cf145-499e-42a6-9ccd-5c5ed8220dff",
        "author": "JasonFruit",
        "text": "I know this is a bit of a tangent, but I&#x27;m getting tired of having everything good replaced by a mediocre version that offers debatable convenience.  A meh guitar tuner, a phone tree that <i>usually</i> understands my spoken choices, the opportunity to enter my claim information online and be questioned by an impersonal overseas operator later instead of just talking with my agent — none of these are developments that improve <i>my</i> life, though they do a lot to help the companies that want my business.<p>P.S. Get off my lawn."
    }
]

<!-- Get a particular comment of a story -->
METHOD : GET 
ROUTE:  api/stories/<uuid:id>/comments/<uuid:id>
ON LOCALHOST: http://127.0.0.1:8000/api/stories/cd182687-e0f0-4f5b-9f3c-dde735f0818b/comments/462cf145-499e-42a6-9ccd-5c5ed8220dff/

RESPONSE FORMAT

{
    "id": "462cf145-499e-42a6-9ccd-5c5ed8220dff",
    "author": "JasonFruit",
    "text": "I know this is a bit of a tangent, but I&#x27;m getting tired of having everything good replaced by a mediocre version that offers debatable convenience.  A meh guitar tuner, a phone tree that <i>usually</i> understands my spoken choices, the opportunity to enter my claim information online and be questioned by an impersonal overseas operator later instead of just talking with my agent — none of these are developments that improve <i>my</i> life, though they do a lot to help the companies that want my business.<p>P.S. Get off my lawn."
}

<!-- .................................THE WRITE ONLY ENDPOINTS........................................................... -->

<!-- Add a story item -->
METHOD : POST
ROUTE:  api/addstory/
ON LOCALHOST: http://127.0.0.1:8000/api/addstory/

PAYLOAD:
{
    "title": <String>,
    "descendants":<Integer>,
    "author": <String>,
    "type": <String>,
    "url": <String>,
    "score": <Integer>
}
RESPONSE FORMAT

{
    "id": "af135b88-2814-4859-a337-d717ceeea115",
    "author": "hhsahjaKJ",
    "descendants": 23,
    "score": 23,
    "type": "jobs",
    "title": "sahsKSNDASK",
    "url": "https://www.django-rest-framework.org/tutorial/3-class-based-views/"
}

<!-- Update atory item -->
METHOD : PUT
ROUTE:  api/addstory/<uuid:story_id>
ON LOCALHOST: http://127.0.0.1:8000/api/addstory/af135b88-2814-4859-a337-d717ceeea115/
PAYLOAD:
{
    "title": <String>,
    "descendants":<Integer>,
    "author": <String>,
    "type": <String>,
    "url": <String>,
    "score": <Integer>
}
RESPONSE FORMAT
{
    "id": "af135b88-2814-4859-a337-d717ceeea115",
    "author": "hhsahjaKJ",
    "descendants": 23,
    "score": 23,
    "type": "jobs",
    "title": "sahsKSNDASK",
    "url": "https://www.django-rest-framework.org/tutorial/3-class-based-views/"
}

<!-- Delete a story item -->
METHOD : DELETE
ROUTE:  api/addstory/<uuid:story_id>
ON LOCALHOST: http://127.0.0.1:8000/api/addstory/af135b88-2814-4859-a337-d717ceeea115/

RESPONSE FORMAT
STATUS 204


<!-- Add comment to a particular stories -->
METHOD : POST
ROUTE:  api/addcomment/<uuid:story_id>
ON LOCALHOST: http://127.0.0.1:8000/api/addcomment/af135b88-2814-4859-a337-d717ceeea115/

PAYLOAD:
{
    "author": <String>,
    "text": <String>,
}

RESPONSE FORMAT
{
    "id": "af135b88-2814-4859-a337-d717ceeea115",
    "author": "hhsahjaKJ",
    "text": "some text"
}

<!-- Update a comment -->
METHOD : PUT
ROUTE:  api/updatecomment/<uuid:comment_id>
ON LOCALHOST: http://127.0.0.1:8000/api/updatecomment/af135b88-2814-4859-a337-d717ceeea115/

PAYLOAD:
{
    "author": <String>,
    "text": <String>,
}

RESPONSE FORMAT
{
    "id": "af135b88-2814-4859-a337-d717ceeea115",
    "author": "hhsahjaKJ",
    "text": "some text"
}


<!-- Delete a comment item -->
METHOD : DELETE
ROUTE:  api/updatecomment/<uuid:comment_id>
ON LOCALHOST: http://127.0.0.1:8000/api/updatecomment/af135b88-2814-4859-a337-d717ceeea115/

RESPONSE FORMAT
STATUS 204








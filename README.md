# Billboard Recognition Service
An HTTP service to accurately predict, given a photograph of a billboard, which ad (out of a database of registered images) is currently showing.

## Getting started
1. `pip3 install -r requirements.txt`
2. `gunicorn wsgi:application`

## Usage
### Registering Ad Images
POST training image to `http://<address>/register` as an HTTP multipart argument named `image`.
The service will return a unique ID associated with that image to be used later for identification.

Curl Example: `curl -F image=@train/1.png http://127.0.0.1:8000/register`

### Identifying Which Ad is Showing
POST the image of the billboard to `http://<address>/register`, again as an HTTP multipart argument named `image`.
The service will return the unique ID associated with registered ad that is most probably a match (the same ID that was returned when that ad was registered).

Curl Example: `curl -F image=@test/1.png http://127.0.0.1:8000/predict`

## Tests
Run `python3 test.py`

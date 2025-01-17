# 0x11. Python - Network #1

To fetch internet resources in Python, `urllib` and `requests` are commonly used.
 `urllib` supports HTTP GET and POST requests, response decoding, and JSON handling,
but requires more manual setup, such as encoding data and decoding responses. For example, 
you can fetch a URL with `urllib.request.urlopen()` and decode the response using 
`.read().decode('utf-8')`. In contrast, `requests` is simpler and more user-friendly, 
offering methods like `requests.get()` and `requests.post()` with built-in JSON parsing 
via `.json()`. It also abstracts headers, encoding, and other complexities, making it ideal
for tasks like manipulating data fetched from external APIs. Use `requests` for ease and
readability unless minimal dependencies are essential.

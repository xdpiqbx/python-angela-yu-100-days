## Flask

```python
# --------------------- hello.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

- You can create FLASK_APP variable and start with `flask run`
    - `export FLASK_APP=./Day_54_flask/hello.py`
- If not
    - `flask --app ./Day_54_flask/hello.py run`
- Or start from `main`

```python
if __name__ == '__main__':
    app.run()
```

---

## Decorator

```python
current_time = time()
print(current_time)


def speed_calc_decorator(curr_time):
    def decorator(function):
        def wrapper():
            start = curr_time
            function()
            end = time()
            print(f"{function.__name__} run speed: {end - start}")

        return wrapper

    return decorator


@speed_calc_decorator(current_time)
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator(current_time)
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
```
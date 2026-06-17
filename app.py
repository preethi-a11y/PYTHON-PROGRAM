from flask import Flask

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

@app.route("/")
def home():
    prime_numbers = [str(num) for num in range(1, 101) if is_prime(num)]

    return f"""
    <html>
        <head>
            <title>Prime Numbers</title>
        </head>
        <body>
            <h1>Prime Numbers from 1 to 100</h1>
            <p>{', '.join(prime_numbers)}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

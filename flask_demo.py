from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Display the first poem
    return render_template("index.html")

@app.route("/second", methods=["GET", "POST"])
def second_poem():
    if request.method == "POST":
        # When the button is clicked, show the second poem
        return render_template("second_poem.html")
    else:
        # If somehow this URL is accessed without posting, redirect to home
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

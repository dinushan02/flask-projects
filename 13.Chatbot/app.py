from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    roadmap = ""
    
    if request.method == "POST":
        course = request.form.get("course")
        
        if course == "Python":
            message = "😄 Awesome choice! Python is super beginner-friendly and very powerful."
            wants_roadmap = request.form.get("roadmap")
            if wants_roadmap == "yes":
                try:
                    with open("python_roadmap.txt", "r") as file:
                        roadmap = file.read()
                except FileNotFoundError:
                    roadmap = "😔 Oops! Roadmap file not found."
        elif course == "Java":
            message = "💪 Nice! Java is rock solid, widely used in big enterprise systems."
        elif course == "C++":
            message = "🚀 Whoa! C++ is super fast and used in high-performance systems like games and OS kernels."
        else:
            message = f"🤔 Hmm... '{course}' isn’t on my list, but any language is a good start!"
    
    return render_template("index.html", message=message, roadmap=roadmap)

if __name__ == "__main__":
    app.run(debug=True)

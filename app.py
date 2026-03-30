from flask import Flask, jsonify

app = Flask(__name__)

databaza = {
    "students": [
        {
            "id": 1,
            "name": "Emma Švecová",
            "age": 20,
            "vyska": 168,
            "hobby": "fotografovanie",
            "image": "https://randomuser.me/api/portraits/women/1.jpg"
        },
        {
            "id": 2,
            "name": "Samuel Kováč",
            "age": 23,
            "vyska": 181,
            "hobby": "fitness",
            "image": "https://randomuser.me/api/portraits/men/2.jpg"
        },
        {
            "id": 3,
            "name": "Nina Hudecová",
            "age": 19,
            "vyska": 165,
            "hobby": "maľovanie",
            "image": "https://randomuser.me/api/portraits/women/3.jpg"
        },
        {
            "id": 4,
            "name": "Lukáš Benko",
            "age": 26,
            "vyska": 185,
            "hobby": "cestovanie",
            "image": "https://randomuser.me/api/portraits/men/4.jpg"
        },
        {
            "id": 5,
            "name": "Zuzana Bielová",
            "age": 22,
            "vyska": 170,
            "hobby": "tanec",
            "image": "https://randomuser.me/api/portraits/women/5.jpg"
        },
        {
            "id": 6,
            "name": "Jakub Farkaš",
            "age": 24,
            "vyska": 178,
            "hobby": "programovanie",
            "image": "https://randomuser.me/api/portraits/men/6.jpg"
        },
        {
            "id": 7,
            "name": "Laura Križanová",
            "age": 21,
            "vyska": 167,
            "hobby": "yoga",
            "image": "https://randomuser.me/api/portraits/women/7.jpg"
        },
        {
            "id": 8,
            "name": "Michal Urban",
            "age": 27,
            "vyska": 183,
            "hobby": "hudba",
            "image": "https://randomuser.me/api/portraits/men/8.jpg"
        },
        {
            "id": 9,
            "name": "Simona Černá",
            "age": 18,
            "vyska": 164,
            "hobby": "knihy",
            "image": "https://randomuser.me/api/portraits/women/9.jpg"
        },
        {
            "id": 10,
            "name": "Filip Marek",
            "age": 25,
            "vyska": 180,
            "hobby": "gaming",
            "image": "https://randomuser.me/api/portraits/men/10.jpg"
        }
    ]
}

@app.route("/")
def home():
    return jsonify({"message": "🔥 Zoznamka backend beží!"})

@app.route("/api")
def api():
    return jsonify(databaza)

@app.route("/api/students/<int:student_id>")
def find_students(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

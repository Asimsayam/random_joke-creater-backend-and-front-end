from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Random Joke Generator</title>

<style>

body{
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
font-family:Arial;
background:linear-gradient(135deg,#667eea,#764ba2);
color:white;
}

.container{
text-align:center;
background:rgba(255,255,255,0.1);
padding:40px;
border-radius:15px;
backdrop-filter:blur(10px);
box-shadow:0 10px 30px rgba(0,0,0,0.3);
width:400px;
}

h1{
margin-bottom:30px;
}

#setup{
font-size:20px;
margin-bottom:10px;
}

#punchline{
font-size:18px;
color:#ffd369;
}

button{
margin-top:25px;
padding:12px 25px;
font-size:16px;
border:none;
border-radius:25px;
background:#ffd369;
color:#333;
cursor:pointer;
transition:0.3s;
}

button:hover{
transform:scale(1.1);
background:#ffb347;
}

</style>
</head>

<body>

<div class="container">

<h1>😂 Random Joke Generator</h1>

<p id="setup">Click button to get a joke</p>
<p id="punchline"></p>

<button onclick="getJoke()">Get Joke</button>

</div>

<script>

function getJoke(){

fetch('/joke')
.then(response => response.json())
.then(data => {

document.getElementById("setup").innerText = data.setup
document.getElementById("punchline").innerText = data.punchline

})

}

</script>

</body>
</html>
"""

@app.route("/joke")
def joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()

    return jsonify({
        "setup": data["setup"],
        "punchline": data["punchline"]
    })

if __name__ == "__main__":
    app.run(debug=True)
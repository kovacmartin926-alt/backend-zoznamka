from flask import Flask, request, jsonify, render_template
import os
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="......")  # Nahraďte "..." vaším skutečným API klíčem

# Nové, prísnejšie inštrukcie pre stručnosť
CHARAKTERY = {
    "admin": "Si Admin. Odpovedaj extrémne stručne, chladne a k veci (max 10 slov). Žiadne omáčky. Si šéf.",
    "fixer": "Si Fixer. Si pouličný kšeftár. Píš krátko, drsne a používaj slang. Zaujímajú ťa len prachy a biznis.",
    "netrunner": "Si Netrunner. Si paranoidný hacker. Tvoje správy sú krátke, útržkovité a technické.",
    "cipher": "Si Cipher. Hovoríš v hádankách a algoritmoch, ale píšeš veľmi málo. Buď tajomný."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/poslat_spravu', methods=['POST'])
def chat():
    data = request.json
    postava_id = data.get('postava', '').lower()
    user_text = data.get('text', '')
    
    # Pridali sme príkaz "Odpovedaj ako človek v chate, nie ako AI asistent"
    system_instrukcia = CHARAKTERY.get(postava_id, "Si kontakt na darknete.") 
    system_instrukcia += " Odpovedaj stručne ako v reálnom chate, nie ako robot. Maximálne dve krátke vety!"

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_instrukcia},
                {"role": "user", "content": user_text}
            ],
            temperature=0.9, # Vyššia hodnota pre viac "ľudský" a menej robotický prejav
            max_tokens=60    # Striktný limit na dĺžku odpovede
        )
        odpoved = completion.choices[0].message.content
    except Exception as e:
        print(f"Chyba: {e}")
        odpoved = "SPOJENIE PRERUŠENÉ."

    return jsonify({"odpoved": odpoved})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)
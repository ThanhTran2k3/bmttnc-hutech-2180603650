from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods = ["POST"])

def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypt_message': encrypt_text})

@app.route("/api/caesar/decrypt", methods = ["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = caesar_cipher.decrypt_text(cipher_text,key)
    return jsonify({'decrypt_message': decrypt_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port =5000, debug = True)
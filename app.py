from flask import Flask, render_template

app = Flask(__name__)

# ---- Ubah data brand di sini ----
BRAND = {
    "name": "EFRYA",
    "tagline": "Oversized comfort, chrome attitude.",
    "instagram_username": "rrell_fhnn",
    "instagram_url": "https://instagram.com/rrell_fhnn",
    "whatsapp_number": "6281383873484",  # format internasional tanpa + atau 0 di depan
    "whatsapp_message": "Halo EFRYA! Saya mau tanya-tanya soal produknya kak.",
}

PRODUCTS = [
    {
        "name": "EFRYA Star Tee",
        "view": "Tampak Depan",
        "desc": "Oversized tee hitam dengan garis piping putih dan logo EFRYA kecil di dada.",
        "image": "images/depan.png",
        "price": "Rp 189.000",
    },
    {
        "name": "EFRYA Star Tee",
        "view": "Tampak Belakang",
        "desc": "Detail grafis bintang pecah di punggung, siluet drop-shoulder oversized.",
        "image": "images/belakang.png",
        "price": "Rp 189.000",
    },
]


@app.route("/")
def home():
    return render_template("index.html", brand=BRAND, products=PRODUCTS)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)

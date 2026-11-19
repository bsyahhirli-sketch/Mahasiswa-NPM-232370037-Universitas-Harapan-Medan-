from flask import Flask, render_template, request, redirect, url_for
from blockchain import Blockchain   # kode dosen, tidak diubah

app = Flask(__name__)
coin = Blockchain(difficulty=4)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sender = request.form["sender"].strip()
        receiver = request.form["receiver"].strip()
        try:
            amount = float(request.form["amount"])
        except ValueError:
            amount = None

        if sender and receiver and amount is not None and amount > 0:
            coin.add_transaction(sender, receiver, amount)
            coin.mine_pending_transactions("Miner1")
        return redirect(url_for("index"))   # supaya refresh tidak kirim ulang form

    return render_template("index.html",
                           chain=coin.chain,
                           valid=coin.is_chain_valid())


if __name__ == "__main__":
    app.run(debug=False)
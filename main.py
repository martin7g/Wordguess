from gensim.models import Word2Vec, KeyedVectors
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/index/")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/word/", methods=['GET', 'POST'])
def word():
    if request.method == 'POST':
        word1 = request.form["Word1"]
        word2 = request.form["Word2"]
        word3 = request.form["Word3"]
        model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=100000)
        vec = model[word1] - model[word2] + model[word3]
        ans = (model.most_similar([vec]))
        w1=ans[0][0]
        w2=ans[1][0]
        p1=round(ans[0][1], 2)*100
        p2=round(ans[1][1], 2)*100
        print(ans)

    return render_template("word.html", ans1=w1, perc1=p1,ans2=w2, perc2=p2)


if __name__ == '__main__':
    app.run(debug=True)

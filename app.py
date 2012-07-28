# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under the terms
# and conditions of the Expat license, a copy of which should be given to you
# with the source of this application.

from flask import Flask, render_template, request, url_for, redirect
from licenses.db import db


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', **{})


@app.route("/license/<license>/")
def license(license=None):
    lobj = db.licenses.find_one({"_id": license})
    if lobj is None:
        return redirect(url_for('index'))

    return render_template('license.html', **{
        "license": lobj
    })


if __name__ == "__main__":
    app.debug = True
    app.run()

# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under the terms
# and conditions of the Expat license, a copy of which should be given to you
# with the source of this application.

from flask import Flask, render_template, request, url_for, redirect
from licenses.db import db


app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for('list'))
    return render_template('index.html', **{})


@app.route("/license/<license>/")
def license(license=None):
    lobj = db.licenses.find_one({"_id": license})
    if lobj is None:
        return redirect(url_for('index'))

    if lobj['type'] == 'license':
        return render_template('license.html', **{
            "license": lobj,
            "info": {
                "dfsg": "DFSG Free",
                "fsf": "FSF Free",
                "gpl-compat": "GPL compatible",
                "osi": "OSI certified"
            }
        })
    elif lobj['type'] == 'disambiguation':
        return render_template('disambiguation.html', **{
            "license": lobj
        })

    return redirect(url_for('index'))


@app.route("/list/")
def list():
    spec = {}
    licenses = db.licenses.find(spec)
    return render_template('list.html', **{
        'licenses': licenses
    })


if __name__ == "__main__":
    app.debug = True
    app.run()

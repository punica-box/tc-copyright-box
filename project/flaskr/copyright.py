from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.db import get_db
from flask import current_app as app
from .helpers.cnt_util import create_copyright_to_contract, check_copyright_to_contract

bp = Blueprint('copyright', __name__)


@bp.route('/')
def index():
    """Intro"""
    return render_template('copyright/index.html')


@bp.route('/create', methods=('GET', 'POST'))
def create():
    """Create a new copyright."""
    if request.method == 'POST':
        ont_id = request.form['ont_id']
        password = request.form['password']
        copyright_hash = request.form['copyright_hash']
        error = None

        if not ont_id or not password or not copyright_hash:
            error = 'All fields required.'

        if error is not None:
            flash(error)
        else:
            default_identity_account = app.config['WALLET_MANAGER'].get_account(
                ont_id, password)
            if default_identity_account:
                tx_hash = create_copyright_to_contract(
                    default_identity_account, copyright_hash)
                flash("Created: {}".format(tx_hash))
            else:
                flash("Invalid Account.")
            return redirect(url_for('copyright.index'))

    return render_template('copyright/create.html')


@bp.route('/check', methods=('GET', 'POST'))
def check():
    """check copyright owner."""
    if request.method == 'POST':
        ont_id = request.form['ont_id']
        copyright_hash = request.form['copyright_hash']
        error = None

        if not ont_id or not copyright_hash:
            error = 'All fields required.'

        if error is not None:
            flash(error)
        else:
            try:
                tx_hash = check_copyright_to_contract(
                    ont_id, copyright_hash)
                flash("Result: {}".format(tx_hash))
            except Exception as e:
                flash("Error: {}, try again".format(e))

            return redirect(url_for('copyright.index'))

    return render_template('copyright/check.html')

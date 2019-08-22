from flask import Flask, g, request, jsonify
import sqlite3


app = Flask(__name__)

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect_db():
    sql = sqlite3.connect('gestioneleves.sqlite3')
    sql.row_factory = dict_factory #sqlite3.Row #avoir un dict plutôt qu’un tuple
    return sql


@app.route('/eleve', methods=['GET'])
def get_eleves():
    db = get_db()
    #eleve_cur = db.execute('select id, nom, prenom, adresse, idclasse from eleve')
    eleve_cur = db.execute('SELECT eleve.nom, eleve.prenom, eleve.adresse, eleve.id, classe.id AS idclasse, etablissement.id AS idetablissement, etablissement.nom AS nometablissement, classe.nom AS nomclasse, academie.nom AS nomacademie, academie.id AS idacademie FROM eleve INNER JOIN classe ON classe.id = eleve.idclasse INNER JOIN etablissement ON etablissement.id = classe.idetablisement INNER JOIN academie ON academie.id = etablissement.idacademie')
    eleve = eleve_cur.fetchall()
    return jsonify({'eleves':eleve})


@app.route('/eleve/<int:eleve_id>', methods=['GET'])
def get_eleve(eleve_id):
    db = get_db()
    eleve_cur = db.execute('SELECT eleve.nom, eleve.prenom, eleve.adresse, classe.id AS idclasse, etablissement.id AS '
                           'idetablissement, etablissement.nom AS nometablissement, classe.nom AS nomclasse, '
                           'academie.nom AS nomacademie, academie.id AS idacademie FROM eleve'
                           ' INNER JOIN classe ON classe.id = eleve.idclasse '
                           'INNER JOIN etablissement ON etablissement.id = classe.idetablisement '
                           'INNER JOIN academie ON academie.id = etablissement.idacademie '
                           'where eleve.id={}'.format(eleve_id))
    eleve = eleve_cur.fetchone()
    return jsonify({'eleve': eleve})


@app.route('/eleve/<int:eleve_id>', methods=['PUT'])
def put_eleve(eleve_id):
    nom = request.args.get('nom')
    prenom = request.args.get('prenom')
    adresse = request.args.get('adresse')

    if nom is None and prenom is None and adresse is None:
        return jsonify({'status': 'no data in the request'})

    db = get_db()

    if nom is not None:
        req = "UPDATE eleve set nom='{}' WHERE id='{}'".format(nom,eleve_id)
        db.execute(req)
        db.commit()

    if prenom is not None:
        db.execute("UPDATE eleve set prenom='{}' WHERE id='{}'".format(prenom,eleve_id))
        db.commit()

    if adresse is not None:
        db.execute("UPDATE eleve set adresse='{}' WHERE id='{}'".format(adresse,eleve_id))
        db.commit()

    return jsonify({'status':'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
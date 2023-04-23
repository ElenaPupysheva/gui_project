# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:05:44 2023

@author: nyank
"""

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///gui.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

class Values(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coneHeight = db.Column(db.Integer, nullable=False)
    cylinderHeight = db.Column(db.Integer,  nullable=False)
    Qufeed = db.Column(db.Integer,  nullable=False)
    Qfloc = db.Column(db.Integer,  nullable=False)
    Qunderfl = db.Column(db.Integer,  nullable=False)
    Fifeed = db.Column(db.Float, nullable=False)
    psolid = db.Column(db.Float,  nullable=False)
    pfluid = db.Column(db.Float,  nullable=False)
    muliqour = db.Column(db.Float,  nullable=False)
    date=db.Column(db.DateTime, default=datetime.utcnow)
    
    
@app.route('/val')
def val():
    values = Values.query.order_by(Values.date).all()
    return render_template('val.html',values=values)


@app.route('/gui', methods=['POST', 'GET'])
def GUI_HTML():
    if request.method == "POST":
        coneHeight = request.form['coneHeight']
        cylinderHeight = request.form['cylinderHeight']
        Qufeed = request.form['Qufeed']
        Qfloc = request.form['Qfloc']
        Qunderfl = request.form['Qunderfl']
        Fifeed = request.form['Fifeed']
        psolid = request.form['psolid']
        pfluid = request.form['pfluid']
        muliqour = request.form['muliqour']
        
        values = Values(coneHeight = coneHeight, cylinderHeight = cylinderHeight, Qufeed = Qufeed, Qfloc = Qfloc,Qunderfl = Qunderfl,Fifeed = Fifeed,psolid = psolid,pfluid = pfluid,muliqour = muliqour)
        try: 
            db.session.add(values)
            db.session.commit()
            return redirect('/val')
        except:
            return "При добавлении значений произошла ошибка"
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


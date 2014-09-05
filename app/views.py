# -*- coding: utf-8 -*-
from flask import request, render_template, jsonify, session, redirect, url_for, flash
from app import app, facebook, db
import pusher
from datetime import datetime
from time import time
from app.models import User


@app.route('/')
def index():
    return render_template('out_home.html')

@app.route('/out_home')
def out_home():
    return render_template('out_home.html')

@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))

@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return redirect(url_for('index'))
    session['oauth_token']  = (resp['access_token'], '')
    me = facebook.get('/me')
    session['username'] = me.data['name']
    session['user_id'] = me.data['id']
    session['user_link'] = me.data['link']
    session['email'] = me.data['email']
    user = User(
        name = me.data['name'],
        email = me.data['email'],
        access_token_facebook = resp['access_token'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('main_bucket'))

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/add_bucket')
def add_bucket():
    return render_template('add_bucket.html')

@app.route('/main_bucket')
def main_bucket():
    return render_template('main_bucket.html', profile_id=session['user_id'], profile_name=session['username'])

@app.route('/pusher/auth', methods=['POST'])
def push_auth():
    p = pusher.Pusher(app_id= '88182', key='56b28c3244cbd91831b8', secret='97cfa86eb69ef35ec43c')
    socket_id = request.form.get('socket_id')
    channel_name = request.form.get('channel_name')
    username = session['username']
    channel_data = {'user_info': {'username':username}}
    channel_data['user_id'] = session['user_id']
    response = p[channel_name].authenticate(socket_id, channel_data)
    return jsonify(response)

@app.route('/send_msg', methods=['POST'])
def send_msg():
    p = pusher.Pusher(app_id='88182', key='56b28c3244cbd91831b8', secret='97cfa86eb69ef35ec43c')
    user_id = session['user_id']
    username = session['username']
    user_link = session['user_link']
    msg = request.form.get('msg')
    ti = time()
    st = datetime.fromtimestamp(ti).strftime('%Y-%m-%d %H:%M:%S')
    p['presence-friki-room'].trigger('new_msg',{'msg':msg, 'username':username, 'time':st, 'user_id':user_id})
    return jsonify(success=True)

@app.route('/logout')
def logout():
    session.clear()
    # flash(u'로그아웃 되었습니다.','success')
    return redirect(url_for('out_home'))

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
        # return 'Access denied: reason =%s error=%s' %(
        #     request.args['error_reason'],
        #     request.args['error_description'])

    session['oauth_token']  = (resp['access_token'], '')
    me = facebook.get('/me')
    session['username'] = me.data['name']
    session['user_id'] = me.data['id']
    session['user_link'] = me.data['link']
    session['email'] = me.data['email']
 
    user = User(
        name = me.data['name'],
        email = me.data['email'],
        access_token_facebook = resp['access_token']
    )
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
    return render_template('main_bucket.html')




# @app.route('/pusher/auth', methods=['POST'])
# def push_auth():
#     p = pusher.Pusher(app_id='86077', key='dd2181a309fb7773ac46', secret='6085e5155c527c5e763b')
#     socket_id = request.form.get('socket_id')
#     channel_name = request.form.get('channel_name')
# # 위 2줄의 ()안은 따로 설정안해도 pusher에서 알아서 보냄(socket과 channel은 고유이름)
# # socket은 사용자 1명이 서버와 통신하는 것.
#     username = session['username']
#     channel_data = {'user_info': {'username':username}}
#     channel_data['user_id'] = session['user_id']
# # 위 2줄의 dic에서 key값 2개(info, id)는 바꾸면 인식을 못함. pusher에서 정해둔 것.
# # 윗 줄의 username이 중요하고, 아랫줄 = username은 덜중요-user마다 다르기만 하면됨
# # = username은 여기선 쉽게하려고 저렇게 씀(바꿔도됨). 개별 식별자로 사용되어야.
# # = username에 primary key를 쓰면 user끼리 중복안되고 사용가능
#     response = p[channel_name].authenticate(socket_id, channel_data)

#     return jsonify(response)


# @app.route('/send_msg', methods=['POST'])
# def send_msg():
#     p = pusher.Pusher(app_id='86077', key='dd2181a309fb7773ac46', secret='6085e5155c527c5e763b')
#     user_id = session['user_id']
#     username = session['username']
#     user_link = session['user_link']
# # 서버에 저장된 정보(session)를 아래 new_msg에서 사용함. 매번 id도 같이 보낼필요없음
#     msg = request.form.get('msg')
#     ti = time()
#     st = datetime.fromtimestamp(ti).strftime('%Y-%m-%d %H:%M:%S')
#     # st = datetime.fromtimestamp(ti).strftime('%Y년-%m월-%d일 %H:%M:%S')
# # 입력받은 시간을 strftime을 통해 string form으로 바꿔줌
#     p['presence-kjh-room'].trigger('new_msg',{'msg':msg, 'username':username, 'time':st, 'user_id':user_id})
#     return jsonify(success=True)

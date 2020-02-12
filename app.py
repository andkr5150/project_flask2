from flask import Flask, request, render_template
import data
import json


app = Flask(__name__)


def json_open():
    with open("teachers.json", "r") as f:
        contents = f.read()
    json_list = json.loads(contents)
    f.close()
    return json_list


@app.route('/')
def main():
    json_list = json_open()
    return render_template('index.html', goals=data.goals, json_list=json_list)


@app.route('/goals/<goal>')
def goals(goal):
    json_list = json_open()
    teach_goal = []
    for teach in json_list["teachers"]:
        if goal in teach["goals"]:
            teach_goal.append(teach)

    return render_template('goal.html', goal=data.goals[goal], teach_goal=teach_goal)


# /profiles/<id учителя>/
@app.route('/profiles/<id_teach>/')
def profiles(id_teach):
    json_list = json_open()
    teach = json_list["teachers"][int(id_teach)]
    time_free = teach['free']
    time_t = {
        '8:00': [],
        '10:00': [],
        '12:00': [],
        '14:00': [],
        '16:00': [],
        '18:00': [],
        '20:00': [],
        '22:00': [],
    }

    for it in time_free:
        time_t['8:00'].append(time_free[it]['8:00'])
        time_t['10:00'].append(time_free[it]['10:00'])
        time_t['12:00'].append(time_free[it]['12:00'])
        time_t['14:00'].append(time_free[it]['14:00'])
        time_t['16:00'].append(time_free[it]['16:00'])
        time_t['18:00'].append(time_free[it]['18:00'])
        time_t['20:00'].append(time_free[it]['20:00'])
        time_t['22:00'].append(time_free[it]['22:00'])

    return render_template('profile.html', id_teach=teach, time_free=time_free, time_t=time_t)


@app.route('/request/')
def request():
    return render_template('request.html')


@app.route('/request_done/')
def request_done():
    return render_template('request_done.html')


# /booking/<id учителя>/
@app.route('/booking/<id_teach>/<time>/<day>')
def booking(id_teach, time, day):
    json_list = json_open()
    id_teach = json_list["teachers"][int(id_teach)]
    if int(day) == 1:
        day_n = "Понедельник"
    elif int(day) == 2:
        day_n = "Вторник"
    elif int(day) == 3:
        day_n = "Среда"
    elif int(day) == 4:
        day_n = "Четверг"
    elif int(day) == 5:
        day_n = "Пятница"
    elif int(day) == 6:
        day_n = "Суббота"
    elif int(day) == 7:
        day_n = "Воскресенье"

    return render_template('booking.html', id_teach=id_teach, time=time, day=day_n)


@app.route('/booking_done/')
def booking_done():
    return render_template('booking_done.html')


app.run()

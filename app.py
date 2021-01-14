from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'clinic'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.secret_key = 'thisismysecretkey'

mysql = MySQL(app)

@app.route("/", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST": 
        if request.form['username_input'] == "db2admin" and request.form['pwd_input'] == "abc123":
            return redirect(url_for("options"))
        elif request.form['username_input'] != "db2admin" or request.form['pwd_input'] != "abc123":
            flash('Wrong username or password!')
            return render_template("login.html")
    return render_template("login.html", error=error)  
    
@app.route("/options")
def options():
    return render_template("options.html")

@app.route('/search', methods = ["POST", "GET"])
def search():
    search = None
    option = None
    if request.method == "POST":
        search = request.form["sr"]
        option = request.form["option"]
        return redirect(url_for("results", search = search, opt = option))
    
    return render_template("search.html", search = search, opt = option)
        


@app.route('/results/<search><opt>', methods = ["POST", "GET"])
def results(search,opt):

    SR = "%{0}%".format(search)

    if request.method == "POST" or "GET":
        if opt == "1":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * from patient WHERE pat_name LIKE '{0}'".format(SR))
            rv = list(cur.fetchall())
            count = len(rv)
            if count == 0:
                return render_template("no-results.html")
            return render_template("results.html", search = rv, count = count)
        elif opt == "2":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * from patient WHERE pat_ic LIKE %s", [search])
            rv = list(cur.fetchall())
            count = len(rv)
            if count == 0:
                return render_template("no-results.html")
            return render_template("results.html", search = rv, count = count)
        elif opt == "3":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * from patient WHERE pat_id LIKE %s", [search])
            rv = list(cur.fetchall())
            count = len(rv)
            if count == 0:
                return render_template("no-results.html")
            return render_template("results.html", search = rv, count = count)
        elif opt == "4":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * from patient WHERE past_visit LIKE %s", [search])
            rv = list(cur.fetchall())
            count = len(rv)
            if count == 0:
                return render_template("no-results.html")
            return render_template("results.html", search = rv, count = count)

@app.route('/add-patient', methods=["POST", "GET"])
def addp():
    if request.method == "POST":
        
        name = request.form["pat_name"]
        gender = request.form["pat_gender"]
        dob = request.form["pat_dob"]
        age = request.form["pat_age"]
        cont = request.form["pat_cont"]
        ic = request.form["pat_ic"]
        pvisit = request.form["past_visit"]
        pmed = request.form["past_med"]
        dose = request.form["med_dose"]
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from patient")
        rv = list(cur.fetchall())
        count = len(rv) + 1
        patno = count + 10000
        patid = "PA" + str(patno)

        cur.execute("INSERT INTO patient(PAT_ID, PAT_NAME, PAT_GENDER, PAT_DOB, PAT_AGE, PAT_CONTACT, PAT_IC, PAST_VISIT, PAST_MED, MED_DOSAGE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (patid, name, gender, dob, age, cont, ic, pvisit, pmed, dose))
        mysql.connection.commit()

        flash("Patient Record Added.")
        return render_template("add-patient.html")
    return render_template("add-patient.html")

@app.route('/booking', methods=["POST", "GET"])
def booking():
    if request.method == "POST":
        patid = request.form["pat_id"]
        date = request.form["book_date"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT fut_visit from patient WHERE PAT_ID like %s", [patid])
        rv = list(cur.fetchall())
        fut = str(rv[0]["fut_visit"])

        cur.execute("SELECT * from patient WHERE FUT_VISIT LIKE %s", [date])
        bookings = list(cur.fetchall())
        count = len(bookings)
        if count < 10:
            if fut == "None":
                cur = mysql.connection.cursor()
                cur.execute("UPDATE patient set FUT_VISIT = %s WHERE patient.PAT_ID = %s", (date, patid))
                mysql.connection.commit()
                flash("Patient record updated.")
                return render_template("booking.html")
            else:
                cur.execute("UPDATE patient SET PAST_VISIT = %s WHERE patient.PAT_ID = %s", (fut, patid))
                cur.execute("UPDATE patient SET fut_visit = %s WHERE patient.PAT_ID = %s", (date, patid))
                mysql.connection.commit()
                flash("Patient record updated.")
                return render_template("booking.html") 
        else:
            flash("Booking slots full.")
            return render_template("booking.html")  
    return render_template("booking.html")

@app.route('/calendar', methods=["POST", "GET"])
def calendar():
    if request.method == "POST":
        che = request.form["date-check"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from patient WHERE FUT_VISIT = %s", [che])
        rv = list(cur.fetchall())
        count = len(rv)
        return render_template("appt_view.html", search = rv, count = count)
    return render_template("calendar.html")

@app.route('/appt_view', methods=["POST", "GET"])
def appt_view(search, count):
    if request.method == "POST" or "GET":
        if count == 0:
            return render_template("no-results.html")
        return render_template("appt-view.html", search = search, count = count)

if __name__=='__main__':
	app.run(debug=True)


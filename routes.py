from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Doctor, Patient, Appointment

api = Blueprint('api', __name__)

# الصفحة الرئيسية اللي فيها الواجهة والبيانات كلها
@api.route('/', methods=['GET'])
def index():
    doctors = Doctor.query.all()
    patients = Patient.query.all()
    appointments = Appointment.query.all()
    return render_template('index.html', doctors=doctors, patients=patients, appointments=appointments)

# إضافة دكتور جديد
@api.route('/add_doctor', methods=['POST'])
def add_doctor():
    name = request.form.get('name')
    specialty = request.form.get('specialty')
    if name and specialty:
        new_doctor = Doctor(name=name, specialty=specialty)
        db.session.add(new_doctor)
        db.session.commit()
    return redirect(url_for('api.index'))

# إضافة مريض جديد
@api.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form.get('name')
    status = request.form.get('status')
    if name and status:
        new_patient = Patient(name=name, status=status)
        db.session.add(new_patient)
        db.session.commit()
    return redirect(url_for('api.index'))

# حجز موعد جديد
@api.route('/add_appointment', methods=['POST'])
def add_appointment():
    date = request.form.get('date')
    doctor_id = request.form.get('doctor_id')
    patient_id = request.form.get('patient_id')
    if date and doctor_id and patient_id:
        new_app = Appointment(date=date, doctor_id=int(doctor_id), patient_id=int(patient_id))
        db.session.add(new_app)
        db.session.commit()
    return redirect(url_for('api.index'))
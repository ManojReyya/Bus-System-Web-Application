import matplotlib
matplotlib.use('Agg')  # Set non-GUI backend for matplotlib

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_transport.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db = SQLAlchemy(app)

# Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    student_type = db.Column(db.String(20))  # 'day_scholar' or 'hosteler'
    address = db.Column(db.String(200))
    bus_assigned = db.Column(db.String(20))

# Create database tables
with app.app_context():
    db.create_all()
    # Add sample data if database is empty
    if Student.query.count() == 0:
        sample_students = [
    {'name': 'Rahul Sharma', 'student_id': 'DS001', 'student_type': 'day_scholar', 'address': 'Dwaraka Nagar, Visakhapatnam', 'bus_assigned': 'BUS01'},
    {'name': 'Priya Patel', 'student_id': 'DS002', 'student_type': 'day_scholar', 'address': 'MG Road, Visakhapatnam', 'bus_assigned': 'BUS01'},
    {'name': 'Amit Singh', 'student_id': 'H001', 'student_type': 'hosteler', 'address': 'College Hostel, Visakhapatnam', 'bus_assigned': 'BUS02'},
    {'name': 'Neha Gupta', 'student_id': 'H002', 'student_type': 'hosteler', 'address': 'Beach Road, Visakhapatnam', 'bus_assigned': 'BUS02'},
    {'name': 'Sandeep Kumar', 'student_id': 'DS003', 'student_type': 'day_scholar', 'address': 'Bhimili Beach, Visakhapatnam', 'bus_assigned': 'BUS03'},
    {'name': 'Anjali Mehta', 'student_id': 'DS004', 'student_type': 'day_scholar', 'address': 'Gajuwaka, Visakhapatnam', 'bus_assigned': 'BUS01'},
    {'name': 'Vikram Joshi', 'student_id': 'H003', 'student_type': 'hosteler', 'address': 'Pedagantyada, Visakhapatnam', 'bus_assigned': 'BUS02'},
    {'name': 'Madhavi Reddy', 'student_id': 'DS005', 'student_type': 'day_scholar', 'address': 'Waltair Uplands, Visakhapatnam', 'bus_assigned': 'BUS03'},
    {'name': 'Ravi Kumar', 'student_id': 'H004', 'student_type': 'hosteler', 'address': 'Madhurawada, Visakhapatnam', 'bus_assigned': 'BUS02'},
    {'name': 'Saritha Rani', 'student_id': 'DS006', 'student_type': 'day_scholar', 'address': 'Duvvada, Visakhapatnam', 'bus_assigned': 'BUS01'},
    
    # Vizianagaram Students
    {'name': 'Kiran Kumar', 'student_id': 'DS007', 'student_type': 'day_scholar', 'address': 'Peddapalli, Vizianagaram', 'bus_assigned': 'BUS04'},
    {'name': 'Priyanka Yadav', 'student_id': 'DS008', 'student_type': 'day_scholar', 'address': 'Sri Venkateswara Nagar, Vizianagaram', 'bus_assigned': 'BUS04'},
    {'name': 'Harsha Reddy', 'student_id': 'H005', 'student_type': 'hosteler', 'address': 'Pothinamallayya Palem, Vizianagaram', 'bus_assigned': 'BUS05'},
    {'name': 'Lakshmi Prasad', 'student_id': 'H006', 'student_type': 'hosteler', 'address': 'Ravada, Vizianagaram', 'bus_assigned': 'BUS05'},
    {'name': 'Sumanth Das', 'student_id': 'DS009', 'student_type': 'day_scholar', 'address': 'Zilla Parishad, Vizianagaram', 'bus_assigned': 'BUS06'},
    {'name': 'Srilakshmi', 'student_id': 'DS010', 'student_type': 'day_scholar', 'address': 'Malkapuram, Vizianagaram', 'bus_assigned': 'BUS06'},
    {'name': 'Ravi Teja', 'student_id': 'H007', 'student_type': 'hosteler', 'address': 'Arunachalam, Vizianagaram', 'bus_assigned': 'BUS07'},
    
    # Srikakulam Students
    {'name': 'Deepa Rani', 'student_id': 'DS011', 'student_type': 'day_scholar', 'address': 'Ravada, Srikakulam', 'bus_assigned': 'BUS08'},
    {'name': 'Suresh Kumar', 'student_id': 'H008', 'student_type': 'hosteler', 'address': 'Peddagantyada, Srikakulam', 'bus_assigned': 'BUS09'},
    {'name': 'Naveen Raj', 'student_id': 'DS012', 'student_type': 'day_scholar', 'address': 'Madhurawada, Srikakulam', 'bus_assigned': 'BUS08'},
    {'name': 'Meera Kumari', 'student_id': 'H009', 'student_type': 'hosteler', 'address': 'Bhimili Beach, Srikakulam', 'bus_assigned': 'BUS09'},
    {'name': 'Subrahmanyam', 'student_id': 'DS013', 'student_type': 'day_scholar', 'address': 'Sri Venkateswara Nagar, Srikakulam', 'bus_assigned': 'BUS10'},
    {'name': 'Anitha Devi', 'student_id': 'H010', 'student_type': 'hosteler', 'address': 'Dwaraka Nagar, Srikakulam', 'bus_assigned': 'BUS10'},
]

        for student in sample_students:
            db.session.add(Student(**student))
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/busmodule')
def busmodule():
    return render_template('busmodule.html')

@app.route('/transportsystem')
def transportsystem():
    students = Student.query.all()
    return render_template('transportsystem.html', students=students)


@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    student_id = request.form['student_id']
    student_type = request.form['student_type']
    address = request.form['address']
    bus_assigned = request.form['bus_assigned']
    
    new_student = Student(
        name=name,
        student_id=student_id,
        student_type=student_type,
        address=address,
        bus_assigned=bus_assigned
    )
    
    db.session.add(new_student)
    db.session.commit()
    return redirect(url_for('busmodule'))

@app.route('/delete_student/<int:id>') 
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('busmodule'))

@app.route('/trackingsystem')
def trackingsystem():
    return render_template('trackingsystem.html')

@app.route('/driver')
def driver_page():
    return render_template('driver.html')
bus_locations = {}

@app.route('/user')
def user_page():
    return render_template('user.html', buses=list(bus_locations.keys()))

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    bus_number = data.get('bus_number')
    if bus_number:
        bus_locations[bus_number] = {
            'lat': data['lat'],
            'lon': data['lon'],
            'accuracy': data.get('accuracy'),
            'speed': data.get('speed'),
            'heading': data.get('heading'),
            'timestamp': data.get('timestamp')
        }
        return jsonify({'status': 'updated'})
    return jsonify({'status': 'error', 'message': 'Bus number not provided'}), 400

@app.route('/get_location/<bus_number>')
def get_location(bus_number):
    return jsonify(bus_locations.get(bus_number, {}))

@app.route('/get_buses')
def get_buses():
    return jsonify(list(bus_locations.keys()))

@app.route('/stop_sharing', methods=['POST'])
def stop_sharing():
    data = request.get_json()
    bus_number = data.get('bus_number')
    if bus_number in bus_locations:
        del bus_locations[bus_number]
    return jsonify({'status': 'stopped'})

@app.route('/analysis')
def analysis():
    # Data for pie chart (student type distribution)
# Count each student type
    day_scholars = Student.query.filter_by(student_type='day_scholar').count()
    hostelers = Student.query.filter_by(student_type='hosteler').count()
    rtc_students = Student.query.filter_by(student_type='rtc').count()
    faculty_members = Student.query.filter_by(student_type='faculty').count()

# Data for bar chart (bus assignments)
    bus_assignments = db.session.query(
      Student.bus_assigned,
      db.func.count(Student.bus_assigned)
    ).group_by(Student.bus_assigned).all()

    bus_numbers = [assignment[0] for assignment in bus_assignments]
    student_counts = [assignment[1] for assignment in bus_assignments]

# Data for address distribution
    address_distribution = db.session.query(
      Student.address,
      db.func.count(Student.address)
    ).group_by(Student.address).all()

    addresses = [dist[0] for dist in address_distribution]
    address_counts = [dist[1] for dist in address_distribution]

# Generate pie chart (student type distribution)
    labels = ['Day Scholars', 'Hostelers', 'RTC', 'Faculty']
    counts = [day_scholars, hostelers, rtc_students, faculty_members]

    plt.figure(figsize=(8, 4))
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title('Student Type Distribution')

    # Save pie chart to bytes
    img_pie = BytesIO()
    plt.savefig(img_pie, format='png')
    img_pie.seek(0)
    plot_url_pie = base64.b64encode(img_pie.getvalue()).decode('utf8')
    plt.close()

    # Generate bar chart for bus assignments
    plt.figure(figsize=(8, 4))
    plt.bar(bus_numbers, student_counts)
    plt.xlabel('Bus Number')
    plt.ylabel('Number of Students')
    plt.title('Students per Bus')
    # Save bar chart to bytes
    img_bar = BytesIO()
    plt.savefig(img_bar, format='png')
    img_bar.seek(0)
    plot_url_bar = base64.b64encode(img_bar.getvalue()).decode('utf8')
    plt.close()

    # Generate address distribution chart
    plt.figure(figsize=(8, 4))
    plt.bar(addresses, address_counts)
    plt.xlabel('Address/Pickup Point')
    plt.ylabel('Number of Students')
    plt.title('Students per Pickup Point')
    # Save address chart to bytes
    img_address = BytesIO()
    plt.savefig(img_address, format='png')
    img_address.seek(0)
    plot_url_address = base64.b64encode(img_address.getvalue()).decode('utf8')
    plt.close()

    # Pass separate plot URLs to the template
    return render_template('analysis.html', 
                           plot_url_pie=plot_url_pie,
                           plot_url_bar=plot_url_bar,
                           plot_url_address=plot_url_address,
                           bus_assignments=bus_assignments,
                           address_distribution=address_distribution)

if __name__ == '__main__':
    app.run(debug=True)


# from urllib import request
# from flask import Flask,  render_template, flash, redirect, url_for
# from flask_mysqldb import MySQL

# app = Flask(__name__)
# app.config['MYSQL_HOST'] ='localhost'
# app.config['MYSQl_USER'] ='root'
# app.config['MYSQL_PASSWORD'] ='gabriela'
# app.config['MYSQL_DB'] ='aplicacion'

# mysql=MySQL(app)

# app.secret_key = 'mysecretkey'


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/add_contact' , methods=['POST'])
# def add_contact():
#     if request.method == 'POST':
#         nombre=request.form['nombre']
#         apellido=request.form['apellido']
#         correo=request.form['correo']
#         contraseña=request.form['contraseña']
#         cur = mysql.connection.cursor()
#         cur.execute('INSERT INTO registro(nombre, apellido, correo, contraseña) VALUES(%s, %s, %s, %s)', (nombre, apellido, correo, contraseña))
#         mysql.connection.commit()
#         return redirect(url_for('index'))
    
    
# @app.route('/nota')
# def nota():
#     return render_template('nota.html')

# @app.route('/nota', methods=['POST'])
# def nota():
#     if request.method == 'POST':
#         nombrenota=request.form['nombre de nota']
#         nota=request.form['nota']
#         cur = mysql.connection.cursor()
#         cur.execute('INSERT INTO nota(nombrenota, nota) VALUES(%s, %s)', (nombrenota, nota))
#         mysql.connection.commit()
#         return redirect(url_for('nota'))


# # @app.route('/edit')
# # def edit_contact():
# #     return'edit contact'
# # @app.route('/delete')
# # def delete_contact():
# #     return 'delete_contact'
 


# if __name__ == '__main__':   
#     app.run(port = 3000, debug=True)
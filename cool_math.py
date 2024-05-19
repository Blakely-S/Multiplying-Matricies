
<<<<<<< HEAD
from flask import Flask, request, render_template 
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/cool_math.py', methods =["GET", "POST"])
def cool_math():
    if request.method == "POST":
       matricies = request.form.get("matrix1")
       return "Your freq value is " + matrix
    return render_template("index.html")
if __name__=='__main__':
   app.run()
   
m1 = input("insert first matrix here:")
try: 
    print(int(m1))
except:
    print("Please insert numbers only") 


m2 = input("insert second matrix here:")
try:
    print(int(m2))
except:
    print("Please insert numbners only")
>>>>>>> dd84ab9d501b58c620de8effbb12f9dda9dd5dfc

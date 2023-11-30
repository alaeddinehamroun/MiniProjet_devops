from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_name():
   # Load current count
   f = open("count.txt", "r")
   count = int(f.read())
   f.close()
   # Increment the count
   count += 1
   # Overwrite the count
   f = open("count.txt", "w")
   f.write(str(count))
   f.close()

   return render_template('index.html' , count=count)

if __name__ == '__main__':
   app.run(host ='0.0.0.0', debug = True)
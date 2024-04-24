from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def calculate():
    if request.method=='POST':
        res = eval(request.form.get('all'))
        return render_template('hasil.html',res=res)
    return render_template('calcu.html')

if __name__=='__main__':
    app.run(debug=True)
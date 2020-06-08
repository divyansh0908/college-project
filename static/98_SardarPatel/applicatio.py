from flask import Flask, render_template, request 
def page_selector(a):
    ls=[]
    sum1=a
    while sum1<=450:
        ls.append(sum1)
        sum1+=100
    sum2=100
    while (sum2+a)//2<=450:
        ls.append((sum2+a)//2)
        sum2+=100
        
        
    return ls
page_selector(131)


app = Flask(__name__) #static_folder="D:\Code\Web\static"
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/Hello", methods=["POST", "GET"])
def Hello():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        num1=request.form.get("num1")
        
        name=page_selector(int(num1))
        return render_template("Hello.html", name=name)
        #print(base)


if __name__=="__main__":
    app.run(debug=True)

#print(base_changer(423.23,16))

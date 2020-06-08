from flask import Flask, render_template, request , redirect
def page_selector(a):
    ls=[]
    sum1=a
    while sum1<=450:
        ls.append(sum1)
        sum1+=100
    sum2=100
    while (sum2+a)//2<=550:
        ls.append((sum2+a)//2)
        sum2+=100
    ls.sort()
    return ls
with open("./gujaratiWords.txt", "r") as fh:
    zp=fh.read()
    kp=zp.split()
def page_viewr(i):
    file="./static/98_SardarPatel/"+str(i)
    new=[]
    try:
        with open(file, "r") as fh:
            z=fh.read()
            p=z.split()
        for words in p:
            if words not in kp:
                new.append(words)
        
        return new
    except FileNotFoundError:
        return ("file not found")
def page_view(i):
    xxx="./static/98_SardarPatel/"+str(i)
    try:
        with open(xxx, "r") as fh:
            z=fh.read()
            p=z.split()

        d={}
        kop=[]
        for i in p:
            if i in d:
                #print(i)
                d[i]+=1
            else:
                d[i]=1
        kp=list(d)[:14]
        k=list(d.values())[0:14]
        rd_less=dict(zip(kp,k))
        return (rd_less,d)
    except FileNotFoundError:
        return (1,"file not found")
app = Flask(__name__) #static_folder="D:\Code\Web\static"
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Requesto", methods=["POST", "GET"])
def Requesto():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        num1=request.form.get("num1")
        nam=request.form.get("name")
        name1=page_selector(int(num1))
        q=open("log",'w')
        q.write(str(num1))
        
        
    return render_template('Requesto.html', name=nam)
    

@app.route("/Hello", methods=["POST", "GET"])

def Hello():
    t=open('log','r')

    namet=page_selector(int(t.read()))
    def sele(i):
        return page_view(i)
            
            
    return render_template("Hello.html", name2=namet, ph=sele)
        #print(base)

@app.route("/Words", methods=["POST", "GET"])
def Words():

    t=open('log','r')

    namet=page_selector(int(t.read()))
    def sele(i):
        return page_viewr(i)
    return render_template("Words.html", name2=namet, ph=sele)

            



if __name__=="__main__":
    app.run(debug=True)

#print(base_changer(423.23,16))

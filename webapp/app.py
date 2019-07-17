from flask import Flask, render_template , request
import inspect
variables=['name','phone','email']
'''

'''
possible_variables=['name','email','phone','access_token','token_type','expires_in','refresh_token','scope']
pv=possible_variables
def rn(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]
def rn2(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]
def rn3(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return str([k for k, v in callers_local_vars if v is var][0])
def variable_list(data,possible_variables):
    nd=[]
    pv=possible_variables
    for i in pv:
        try:
            nd.append(data[i])
        except:
            nd.append(0)
    return nd


def checkhtml(file,variables):
    import os
    path=os.path.dirname(os.path.realpath(__file__))
    f=open(path+'\\templates\\'+file+'.plan','r')
    html=f.read()
    f.close()
    #htmlss is html split split
    #nv is needed variables (used for each line individually)
    #htmls is html split
    #linemods is line modifications which shows which lines to remove
    split='\n'
    html_split=html.splitlines()
   # print(html_split)
    htmls=html_split
    #for i in htmls:
        #print(i)

    htmlss=list(htmls)
    for i in range(0,len(htmls)):
        htmlss[i]=htmls[i].split()
    #for i in htmlss:
        #print(i)
    nv=[]
    for i in htmlss:
        nv.append([])
    for i in range(0,len(htmlss)):
        for o in range(0,len(htmlss[i])):
            try:
                if htmlss[i][o-1].index('{{')!=-1:
                    if htmlss[i][o+1].index('}}')!=-1:
                        nv[i].append(htmlss[i][o])
            except:
                None
                        
    '''               
    for i in range(0,len(htmls)):
        works=[]
        for o in range(0,len(variables)):

        
            try:
                if htmls[i].index(variables[o])!=-1:
                    works.append(True)
            except:
                works=works

        print(works)'''
    #print(nv)
    linemods=[]
    for i in nv:
        linemods.append([])
    for line in range(0,len(nv)):
        linesuccess=True
        for variable in range(0,len(nv[line])):
            if nv[line][variable] not in variables:
                linesuccess=False
                linemods[line]=False
                              
    #print(linemods)
    for i in range(0,len(htmls)):
        if linemods[i]==False:
            htmls[i]=''
    #print(htmls)
    html=''
    for i in htmls:
        if i!='':
            html=html+'\n' + i
    
    f=open(path+'\\templates\\'+file+'.html','w')
    f.write(html)
    f.close()
    return html

app = Flask(__name__)

@app.route('/')
def about():
    checkhtml('about',[])
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    #checkhtml('login',[])
    if request.method == 'POST':
        text = request.form['button']
        processed_text = text.upper()
    return render_template('login.html')
@app.route("/forward/", methods=['POST'])
def logging():
    #authorisation stuff
    print('do stuff')


@app.route('/endpoint')
def end():
    name='h,agf,jgaf,asgdfemjfgrymaymaymgarh,ayhdfga,hdfg,jadsf'
    email='ak,hdf,ahdsf,ajdhfjdhsvjfrshfja,rh,fasbhhfb,jr,srjabh'
    phone=',asrh,bsbhf,ashrbf,sjrhbfj,srbhfg,rsjhbfharbsbjfs,jfb'
    access_token='as.,hrkbahfb,arjhgrhgfrhrhfbbbbfhrhrhbhrbfarfsaf'
    token_type=',ashr,ahsbagfr,jabf,hraeghtjrea,jhgjarhg,ragaer,j'
    expires_in=',ahr,ahefrjebfjher,fbrejhfbrhefbrhjefbjfrehbfjerhfje'
    refresh_token='a,hrbf,eahb,jtrgtrht,jargh,jea,jeafbr,jhebea,jrb'
    scope='a.rhe,,,,,,,,,,,,,,,frgjeh,ag,jghea,jfrgheaf,jhrg,rhghragj'
    global pv
    data={"access_token":"MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
      "token_type":"bearer",
      "expires_in":3600,
      "refresh_token":"IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
      "scope":"create",
      'name':'anyone',
      'email':'me@gmail.co.uk',
      'phone':'007'
      }
    cv=[]
    nd=variable_list(data,possible_variables)
    for i in range(0,len(nd)):
        if nd[i]!=0:
            cv.append(pv[i])
    checker=nd[pv.index(rn(name)[0])]
    
    
    
    checkhtml('name',cv)
    return render_template('name.html',name=checker,email=nd[pv.index(rn(email)[0])],phone=nd[pv.index(rn(phone)[0])])
#@app.route('/hello/<name>')
#def hello(name):
    #return render_template('name.html', name=name)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

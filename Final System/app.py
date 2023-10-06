import numpy as np
from flask import *
import pickle
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('modelr1.pickle.pkl', 'rb'))

df_r1_main=""
bad_managers=['Steven Lane','Roy Chapman','Joanne Nelson','Stella Mckoy']



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    df_r1 = pd.read_csv('March2020.csv')
    df_r1_empcode = df_r1['Employee Code']
    
    
    df_r1.drop('Employee_Name', axis=1, inplace=True)
    df_r1.drop('Over18', axis=1, inplace=True)
    df_r1.drop('Stock Option Level', axis=1, inplace=True)
    df_r1.drop('Direct Report', axis=1, inplace=True)
    df_r1.drop('Date Of Joining', axis=1, inplace=True)
    df_r1.drop('Date of Attrition', axis=1, inplace=True)
    df_r1.drop('LWD', axis=1, inplace=True)
    df_r1.drop('Exit interview comments - HR', axis=1, inplace=True)
    df_r1.drop('Process', axis=1, inplace=True)
    df_r1_copy=df_r1
    df_r1.drop('Employee Code', axis=1, inplace=True)
    df_r1=df_r1.dropna()
    df_dummy = pd.get_dummies(df_r1)
    X = df_dummy
    X_scaled = X.copy()
    col_names = ['Age', 'Happiness index', 'Distance from current Address', 'Marital Status']
    features = X_scaled[col_names]
    #print(features.values)
    scaler = StandardScaler().fit(features.values)#Standardising the values, to perform consistetly.
    features = scaler.transform(features.values)
    X_scaled[col_names] = features
    #return X_scaled 
    loaded_model = pickle.load(open("modelr1.pickle.pkl", "rb"))
    y_pred = loaded_model.predict(X_scaled)
    y_pred = np.where(y_pred==0, 'No', y_pred)
    y_pred = np.where(y_pred=='1', 'Yes', y_pred)

    y_pred = pd.DataFrame(y_pred)
    df_r1_copy["Attrition Status"] = ""
    df_r1_copy["Employee Code"] = ""
    df_r1_copy["Attrition Status"] = y_pred
    df_r1_copy["Employee Code"] = df_r1_empcode
    df_r1_main=y_pred


    risklow=[]
    riskhigh =[]
    df_r11 = pd.read_csv('March2020.csv')
    df_r11.drop('Employee_Name', axis=1, inplace=True)
    df_r11.drop('Over18', axis=1, inplace=True)
    df_r11.drop('Stock Option Level', axis=1, inplace=True)
    df_r11.drop('Direct Report', axis=1, inplace=True)
    df_r11.drop('Date Of Joining', axis=1, inplace=True)
    df_r11.drop('Date of Attrition', axis=1, inplace=True)
    df_r11.drop('LWD', axis=1, inplace=True)
    df_r11.drop('Exit interview comments - HR', axis=1, inplace=True)
    df_r11.drop('Process', axis=1, inplace=True)
#Risk Calculation

    for i in range(10):
        score = 0
        if (df_r11['Band'][i] == 'A1') or  (df_r11['Band'][i] == 'A2'):
            #print("Band ",df_r1['Band'][i])
            score = score + 5
            #print(score)
        if df_r11['Band'][i] == 'A3':
            #print("Band ",df_r1['Band'][i])
            score = score + 3
            #print(score)
        if df_r11['Rating'][i] == 'D':
            #print("Rating ",df_r1['Rating'][i])
            score = 25
            #print(score)
        if df_r11['Rating'][i] == 'C':
            #print("Rating ",df_r1['Rating'][i])
            score = score + 5
            #print(score)
        if df_r11['Rating'][i] == 'B':
            #print("Rating ",df_r1['Rating'][i])
            score = score + 3
            #print(score)
        if df_r11['Rating'][i] == 'A':
            #print("Rating ",df_r1['Rating'][i])
            score = score + 2
            #print(score)
        if df_r11['Salary'][i] == 'Fair':
            #print("Salary ",df_r1['Salary'][i])
            score = score + 5
            #print(score)
        if df_r11['Salary'][i] == 'Good':
            #print("Salary ",df_r1['Salary'][i])
            score = score + 3
            #print(score)
        if 1<=df_r11['Happiness index'][i] <= 2:
            #print("Hindex ",df_r1['Happiness index'][i])
            score = score + 5
            #print(score)
        if df_r11['Happiness index'][i] == 3:
            #print("Hindex ",df_r1['Happiness index'][i])
            score = score + 2
            #print(score)
        if df_r11['Happiness index'][i] >3:
            #print("Hindex ",df_r1['Happiness index'][i])
            score = score + 0
            #print(score)
        if 7<=df_r11['Distance from current Address'][i]<= 8:
            #print("Distance ",df_r1['Distance from current Address'][i])
            score = score + 5
            #print(score)
        if 5<=df_r11['Distance from current Address'][i]<= 6:
            #print("Distance ",df_r1['Distance from current Address'][i])
            score = score + 4
            #print(score)
        if 2<=df_r11['Distance from current Address'][i]<= 4:
            #print("Distance ",df_r1['Distance from current Address'][i])
            score = score + 3
            #print(score)
        if df_r11['Distance from current Address'][i] == 1:
            #print("Distance ",df_r1['Distance from current Address'][i])
            score = score + 2
            #print(score)
        if df_r11['Interim Manager'][i] in bad_managers:
            #print("Distance ",df_r1['Interim Manager'][i])
            score = score + 5
            #print(score)
        #print("Final Score:")
        #print(score)
        if score<20:
            risklow.append(df_r11['Employee Code'][i])
        if score>20:
            riskhigh.append(df_r11['Employee Code'][i])

    risklow = pd.DataFrame(risklow,columns =['Low Risk Employees'])
    # risklow['Attrition Status']=""
    # risklow['Attrition Status']=df_r1_main

    riskhigh = pd.DataFrame(riskhigh,columns =['High Rish Employees'])
    # riskhigh['Attrition Status']=""
    # riskhigh['Attrition Status']=df_r1_main 

    display3 = riskhigh.loc[:10]

    display4 = risklow.loc[:10]
    
    display = df_r1_copy.loc[:10]
    return render_template('index.html',tables=[display.to_html(classes='display')],titles=[],tables4=[display3.to_html(classes='display3')],titles4=[],tables5=[display4.to_html(classes='display4')],titles5=[])


@app.route('/visualize',methods=['POST'])
def visualize():
    return render_template('model.html')


@app.route('/risk',methods=['POST'])
def risk():
    risklow=[]
    riskhigh =[]
    df_r1 = pd.read_csv('March2020.csv')
    df_r1.drop('Employee_Name', axis=1, inplace=True)
    df_r1.drop('Over18', axis=1, inplace=True)
    df_r1.drop('Stock Option Level', axis=1, inplace=True)
    df_r1.drop('Direct Report', axis=1, inplace=True)
    df_r1.drop('Date Of Joining', axis=1, inplace=True)
    df_r1.drop('Date of Attrition', axis=1, inplace=True)
    df_r1.drop('LWD', axis=1, inplace=True)
    df_r1.drop('Exit interview comments - HR', axis=1, inplace=True)
    df_r1.drop('Process', axis=1, inplace=True)
#Risk Calculation

    for i in range(10):
        score = 0
        if (df_r1['Band'][i] == 'A1') or  (df_r1['Band'][i] == 'A2'):
            #print("Band ",df_r1['Band'][i])
            score = score + 5
            #print(score)
        if df_r1['Band'][i] == 'A3':
            #print("Band ",df_r1['Band'][i])
            score = score + 3
            #print(score)
        if df_r1['Rating'][i] == 'D':
            #print("Rating ",df_r1['Rating'][i])
            score = 25
            #print(score)
        if df_r1['Rating'][i] == 'C':
            #print("Rating ",df_r1['Rating'][i])
            score = score + 5
            #print(score)
        if df_r1['Rating'][i] == 'B':
            #print("Rating ",df_r1['Rating'][i])
            score = score + 3
            #print(score)
        if df_r1['Rating'][i] == 'A':
            #print("Rating ",df_r1['Rating'][i])
            score = score + 2
            #print(score)
        if df_r1['Salary'][i] == 'Fair':
            #print("Salary ",df_r1['Salary'][i])
            score = score + 5
            #print(score)
        if df_r1['Salary'][i] == 'Good':
            #print("Salary ",df_r1['Salary'][i])
            score = score + 3
            #print(score)
        if 1<=df_r1['Happiness index'][i] <= 2:
            #print("Hindex ",df_r1['Happiness index'][i])
            score = score + 5
            #print(score)
        if df_r1['Happiness index'][i] == 3:
            #print("Hindex ",df_r1['Happiness index'][i])
            score = score + 2
            #print(score)
        if df_r1['Happiness index'][i] >3:
            #print("Hindex ",df_r1['Happiness index'][i])
            score = score + 0
            #print(score)
        if 7<=df_r1['Distance from current Address'][i]<= 8:
            #print("Distance ",df_r1['Distance from current Address'][i])
            score = score + 5
            #print(score)
        if 5<=df_r1['Distance from current Address'][i]<= 6:
            #print("Distance ",df_r1['Distance from current Address'][i])
            score = score + 4
            #print(score)
        if 2<=df_r1['Distance from current Address'][i]<= 4:
            #print("Distance ",df_r1['Distance from current Address'][i])
            score = score + 3
            #print(score)
        if df_r1['Distance from current Address'][i] == 1:
            #print("Distance ",df_r1['Distance from current Address'][i])
            score = score + 2
            #print(score)
        if df_r1['Interim Manager'][i] in bad_managers:
            #print("Distance ",df_r1['Interim Manager'][i])
            score = score + 5
            #print(score)
        #print("Final Score:")
        #print(score)
        if score<20:
            risklow.append(df_r1['Employee Code'][i])
        if score>20:
            riskhigh.append(df_r1['Employee Code'][i])

    risklow = pd.DataFrame(risklow,columns =['Employee Code'])
    # risklow['Attrition Status']=""
    # risklow['Attrition Status']=df_r1_main

    riskhigh = pd.DataFrame(riskhigh,columns =['Employee Code'])
    # riskhigh['Attrition Status']=""
    # riskhigh['Attrition Status']=df_r1_main 

    display = riskhigh.loc[:10]

    display2 = risklow.loc[:10]


    return render_template('index.html',tables2=[display.to_html(classes='display')],titles2=[],tables3=[display2.to_html(classes='display2')],titles3=[])



@app.route('/graph1',methods=['POST'])
def graph1():
    return render_template('attrition.html')

@app.route('/graph2',methods=['POST'])
def graph2():
    return render_template('hindex.html')

@app.route('/graph3',methods=['POST'])
def graph3():
    return render_template('happiness.html')

@app.route('/graph4',methods=['POST'])
def graph4():
    return render_template('salary.html')

@app.route('/graph5',methods=['POST'])
def graph5():
    return render_template('rating.html')

@app.route('/graph6',methods=['POST'])
def graph6():
    return render_template('ratingandsalary.html')

@app.route('/graph7',methods=['POST'])
def graph7():
    return render_template('salarydesignation.html')


@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)  

if __name__ == "__main__":
    app.run(debug=True)
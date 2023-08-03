import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task_4a.csv')

#Login for the system
username='Newhaven'
password='password','Dashboard123'

user=input("Enter username: ")
passwd=input("Enter Password: ")
if user == username and passwd == password:
    pass
else:
    exit()


#if username and passsword do not match then the system shuts. 

#Calles login function as start

def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Show data for property type in specific area')
    return int(input(""))


def alldata():
    print(df)



def region_check(region, startdate, enddate, ):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

def propertycheck():
	region = input("Enter the Region: ")
	property = input("Enter property type: ")
	df1 = df.loc[:, 'Jan-19':'May-22']
	df2 = df.loc[df['Property Type'] == property]
	result = pd.concat([df2, df1], axis=1,
	                   join='inner').where(df2["Region"] == region)
	result = pd.DataFrame(result)
	result.dropna(inplace=True)
	print(result)
	ave = result.mean()
	ave.plot()
	plt.show()
	return result

def property(region, propertytype, startdate, enddate):
    region=input("Enter region: ")
    propertytype=input("Enter property type")
    
    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'PropertyType':'Region']

    result = pd.concat([df2, df1], axis=1, join='inner').where([df2['Region'] == region])
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

x = mainmenu()
while x == 1 or x == 2 or x==3:
    if x == 1:
        alldata()
    if x == 3:
        propertycheck()
    elif x == 2:
        while True:
            print()

            region = input("Please enter the name of the region you would like to check:")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
   #My code for if x==3                    
            print("Region not found")

    
x = mainmenu()





import csv,pickle
from db import read_data
from datetime import datetime,timedelta

def write_details(code,status):
    with open(r"./details/details.csv","w") as file:
        writer=csv.writer(file)
        last_seen=datetime.now().strftime("%d:%m:%y")
        writer.writerow(["Employee ID","Last Seen","Logged In"])
        writer.writerow([code,last_seen,status])

def change_status(status=[True,False]):
    with open(r"./details/dshvhsih.dat","wb") as pqs_file:
        pickle.dump(status,pqs_file)


def check_status():
    with open(r"./details/dshvhsih.dat","rb") as pqs_file:
        status,session=pickle.load(pqs_file)
        return status,session


def get_current_user():
    with open(r"./details/details.csv","r") as file:
        reader=csv.DictReader(file)
        data=iter(reader)
        user_code=next(data)["Employee ID"]
        query=f"SELECT name,code,dept FROM employee WHERE code='{user_code}'"
        user=read_data(query)[0]
        return user


def write_session_details(**kwargs):

    with open(r"./details/user.dat","rb") as file:
        try :
            data=pickle.load(file)
            # print(data)
        except EOFError :
            data={}

    if kwargs:
        with open(r"./details/user.dat","wb+") as file:
            if kwargs.get("start",False) == True:
                sessionTime=datetime.now()
                day = str(data.get("week_start",sessionTime.day))
                week_start = datetime.strptime(day,"%d")
                weekend_check = week_start + timedelta(days=7) 
            
                if weekend_check.day == sessionTime.day :
                    day=sessionTime.day
                    data["last_week"] = week_start.day
                else :
                    day=data.get("week_start",sessionTime.day)         

                time_start = (sessionTime.hour , sessionTime.minute)
                '''Adding Values'''
                data["week_start"],data["last_week"] = day,0
                data["session_start"],data["session_end"] = time_start,(0,0)
                data["weekly_hour"],data["current_hour"]=data.get("weekly_hour",0),0
                pickle.dump(data,file)
                return data

            elif kwargs.get("end",False) == True:        
                assert data,"Null hash tables not allowed"
                sessionEnd = datetime.now()
                '''Calculating the number of hours worked'''
                start_hour,start_minute = data["session_start"]
                end_hour,end_minute = sessionEnd.hour,sessionEnd.minute
                time_difference = (timedelta(hours=end_hour,minutes=end_minute)-timedelta(hours=start_hour,minutes=start_minute))
                totalHours = (time_difference.seconds)/3600
                data["current_hour"] = round(totalHours,1)
                data["session_end"] = (end_hour,end_minute)
                '''Adding Hours in weekly'''
                added_time = datetime.strptime(str(data["week_start"]),"%d")+timedelta(days=7)
                if sessionEnd.day <= added_time.day:
                    time_weekly = data.get("weekly_hour",0)+round(totalHours,1)
                    data["weekly_hour"] = round(time_weekly,1)
                else :
                    data["weekly_hour"]=0 
                pickle.dump(data,file)

            elif kwargs.get("reset",False) == True:
                data = {}    
                pickle.dump(data,file)

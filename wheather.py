import tkinter as tk #for UI
import requests # for JSON Files 
import time # to format some variables

#define function to get data from api 
def getWeather(canvas):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=77f5ac35f1b546d2423f6b86f4a4e5c1"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int( json_data['main']['temp'] -273.15)#convert json data Kelvin to celsious
    min_temp = int( json_data['main']['temp_min'] -273.15)
    max_temp = int( json_data['main']['temp_max'] -273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] - 216000))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] - 216000))

    final_info =condition + "\n" +str(temp) +"°C"
    final_data ="\n" + "Max Temp:" +str(max_temp) + "\n" + "Min Temp:" + str(min-temp) + "\n"
    "pressure:" + str(pressure) + "\n" +"Humidity:" + str(humidity) +"\n"
    "wind speed:" + str(wind) + "\n" + "sunrise:" + sunrise +"\n"
    "sunset:" +sunset +"\n"
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("500x570")
canvas.title("Wheather App")

#fonts
f=("poopins",15,"bold")
t=("poopins",35,"bold")

#textfiled to get the city from user
textfield = tk.Entry(canvas,font=t)
textfield.pack(pady=20)
textfield.focus() #by using focus user cant enter city name directly witout moving curser.
textfield.bind("<Return>",getWeather)


#Label 1
label1 = tk.Label(canvas,font=t)
label1.pack()

#Label 2
label2 = tk.Label(canvas,font=t)
label2.pack()

canvas.mainloop()


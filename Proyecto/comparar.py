import datetime
from UI_main_final import *


# print("Fechas:")
# fecha1 = datetime.datetime.today()  # Asigna fecha actual
# print("\tFecha1:", fecha1)

# fecha2 = datetime.datetime(2022,10,16)

for i in range (len(tareas_separadas)):
    print(tareas_separadas[i][0])
    tareas_separadas[i][0].sort(key=lambda date: datetime.datetime.strptime(date, "%m-%Y"))
    print(tareas_separadas)


# input list of date strings
inputDateList = ['06-2014', '08-2020', '4-2003', '04-2005', '10-2002', '12-2021']

# sorting the input list by formatting each date using the strptime() function
inputDateList.sort(key=lambda date: datetime.datetime.strptime(date, "%m-%Y"))

# Printing the input list after sorting
print("The input list of date strings after sorting:\n", inputDateList)



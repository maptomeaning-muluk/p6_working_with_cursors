"Update the value of ESTAB if value is 0 to 1998"
"by siing update cursor"

import arcpy
import os

gdb_path = r"D:\SEM_III\Programming_3\p6_working_with_cursors\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdb_path,fc_name)

fields_list = ['NAME','ESTAB']

years_dictionary ={}

with arcpy.da.UpdateCursor(fc_path,fields_list) as u_cursor:
    for row in u_cursor:
        years_dictionary[row[0]] =row[1]
        if row[1]== 0:
            print("This attraction {} is update.".format(row[0]))
            row[1] = 1998

        u_cursor.updateRow(row)

print(years_dictionary)
print("process complete")
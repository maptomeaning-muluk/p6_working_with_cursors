"""Update the value of ESTAB if value is between 1960 and 1980 then it is historic
by using update cursor"""

import arcpy
import os

arcpy.env.workspace = "D:\SEM_III\Programming_3\p6_working_with_cursors\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

arcpy.management.AddField(fc_name,"HISTORIC","TEXT")
fields_list = ['NAME','ESTAB','HISTORIC']


with arcpy.da.UpdateCursor(fc_name,fields_list) as u_cursor:
    for row in u_cursor:
         estd_year = row[1]

         if 1960 < estd_year <1980:
             row[2] = "YES"
         else:
            row[2] ="NO"

         u_cursor.updateRow(row)

print("process complete")



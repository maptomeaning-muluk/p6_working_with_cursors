import arcpy
import os

gdb_path = r"D:\SEM_III\Programming_3\p6_working_with_cursors\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdb_path,fc_name)

fields_list = ['NAME','ESTAB','ADDR']

record = ("NEWATTRACTION",2023, "STREET 123")

i_cursor = arcpy.da.InsertCursor(fc_path,fields_list)
i_cursor.insertRow(record)
print("process complete")
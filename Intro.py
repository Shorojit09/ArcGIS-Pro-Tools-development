import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\yourDIR\Sample.gdb"

# fc= r"C:\Users\yourDIR\ne_10m_admin_0_countries.shp"
fc = arcpy.GetParameterAsText(0)
if fc == "":
    fc= r"C:\Users\yourDIR\ne_10m_admin_0_countries.shp"
numFeats = arcpy.GetCount_management(fc)
print_message("{0} has {1} feature(s)".format(fc,numFeats))

##arcpy.CreateFileGDB_management(r"C:\Users\shoro\OneDrive\Desktop\Udemy\ArcGISproPython\LPA\Data","Sample")
##arcpy.Select_analysis(fc,"Egypt","NAME = 'Egypt'")

print_message("Script Complted!")

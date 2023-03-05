import arcpy

arcpy.env.worksapce = r"C:\Users\yourDIR"
wsList = arcpy.ListWorkspaces()
print(wsList)

print("\nScript complteted!")

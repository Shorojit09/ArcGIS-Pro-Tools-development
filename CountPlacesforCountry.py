import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\yourDir\FrameworkProject.gdb"
#countryName = "China"
countryName = arcpy.GetParameterAsText(0)
arcpy.analysis.Select(r"C:\Users\yourDir\ne_10m_admin_0_countries.shp",
                      r"C:\Users\yourDir\FrameworkProject.gdb\SelCountry",
                      "NAME = '{0}'".format(countryName))
arcpy.analysis.Buffer("SelCountry","SelCountry_Buffer","200 Kilometers","FULL","ROUND","NONE",None,"PLANAR")
arcpy.analysis.Clip(r"C:\Users\YourDir\ne_10m_populated_places.shp",
                    "SelCountry_Buffer",
                    "Places_Clip",
                    None)
arcpy.AddMessage("There are {0} populated places in or within 200km of {1}".format(
    arcpy.management.GetCount("Places_Clip"),countryName))

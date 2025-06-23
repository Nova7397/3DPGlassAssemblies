
from os.path import *
# Python Script, API Version = V23

# ✅ Set your base directory containing the geometry files:
UserFilesPath = r"FOLDERPATH"

# 🔢 Read the parameter 't'
Val1 = int(Parameters.thickness*1000)

# 🧩 Construct the filename based on the parameter
FileName = "T{}.step".format(Val1) #Edit this based on your dataset naming

# 🚿 Clear existing geometry
GetRootPart().ClearAllPartData()

# 📦 Insert the new geometry
File.InsertGeometry(join(UserFilesPath, FileName))

print("Be sure to check if config.txt is valid first!")
import glob, os
import shutil

# CONFIG
if os.path.isfile("config.txt"):
    print("Config exists! Continue.")
else:
    print("No config.txt found. Creating...")
    config_file = open("config.txt", "w+")
    config_file.write("TF2 PATH; E:\Games\Steam\steamapps\common\Team Fortress 2\\tf")
    config_file.close()
config_file = open("config.txt").readlines()
TF2_Directory = ""
# USER DEFINES
mapname_input = input("Enter original mapname (EXAMPLE: dr_bog_v2):")
mapname_output = input("Enter new mapname (EXAMPLE: dr_bog_v2a):")

# DEFINES
file_particles = "_particles.txt"
file_level_sounds = "_level_sounds.txt"
file_nav = ".nav"

file_soundscapes = "soundscapes_"

file_vgui_texture = "menu_photos_"

# GARBAGE EWW
file_translation_english = "_english.txt"
file_translation_russian = "_russian.txt"
file_translation_finnish = "_finnish.txt"
file_translation_german = "_german.txt"

# GET CONFIG VALUE
for lines in config_file:
    if 'TF2 PATH;' in lines:                                                                                         
        TF2_Directory = lines.split(";")[-1].strip()
        print(TF2_Directory)

for file in glob.glob(f"{mapname_input}{file_particles}"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{mapname_output}{file_particles}')

# LEVEL SOUNDS
for file in glob.glob(f"{mapname_input}{file_level_sounds}"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{mapname_output}{file_level_sounds}')

# NAV
for file in glob.glob(f"{mapname_input}{file_nav}"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{mapname_output}{file_nav}')

# file_translation_english
for file in glob.glob(f"{mapname_input}{file_translation_english}"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{mapname_output}{file_translation_english}')

# file_translation_russian
for file in glob.glob(f"{mapname_input}{file_translation_russian}"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{mapname_output}{file_translation_russian}')

# file_translation_finnish
for file in glob.glob(f"{mapname_input}{file_translation_finnish}"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{mapname_output}{file_translation_finnish}')

# file_translation_german
for file in glob.glob(f"{mapname_input}{file_translation_german}"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{mapname_output}{file_translation_german}')

os.chdir(f'{TF2_Directory}/scripts')
# SOUNDSCAPES
for file in glob.glob(f"{file_soundscapes}{mapname_input}.txt"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{file_soundscapes}{mapname_output}.txt')

os.chdir(f'{TF2_Directory}/materials/vgui/maps')
# VGUI TEXTURE .VTF
for file in glob.glob(f"{file_vgui_texture}{mapname_input}.vtf"):
    print(f"{file} exists!")
    shutil.copyfile(file, f'{file_vgui_texture}{mapname_output}.vtf')


os.chdir(f'{TF2_Directory}/materials/vgui/maps') # TOOK ME 1 HOUR TO MAKE THIS SHIT LMAOOO
# VGUI TEXTURE .VMT
for file in glob.glob(f"{file_vgui_texture}{mapname_input}.vmt"):
    print(f"{file} exists!")
    newfile = shutil.copyfile(file, f'{file_vgui_texture}{mapname_output}.vmt')
    fin = open(newfile, "rt")
    #output file to write the result to
    fout = open(newfile, "r+")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        if '/' in line:  
            fout.write(line.replace(f'"$basetexture" "vgui/maps/{file_vgui_texture}{mapname_input}"', f'"$basetexture" "vgui/maps/{file_vgui_texture}{mapname_output}"')) 
        else:
            fout.write(line.replace(f'"$basetexture" "vgui\maps\{file_vgui_texture}{mapname_input}"', f'"$basetexture" "vgui\maps\{file_vgui_texture}{mapname_output}"'))
    #close input and output files
    fin.close()
    fout.close()
while True:
    ("sus")
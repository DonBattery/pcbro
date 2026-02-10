# Windows Brotherhood Secret Code  
# _A Windows Testvériség Titkos Kódja_

These are the secret codes our adepts should learn, so they can speak to **The Window**. The codes include navigation, files, searching, networking, processes, storage, and troubleshooting.  

_Ezek azok a titkos kódok, amelyeket tanoncainknak meg kell tanulniuk, hogy szólhassanak Az Ablakhoz. A kódok tartalmazzák a navigációt, fájlkezelést, keresést, hálózatot, folyamatokat, tárolást és hibakeresést._


## Navigation & filesystem basics
_Navigáció és fájlrendszer alapok_
```shell
cd                     # show current directory / aktuális mappa
dir                    # list files / fájlok listázása
dir /a                 # include hidden files / rejtett fájlokkal
cd folder              # change directory / mappaváltás
cd ..                  # up one level / egy szinttel feljebb
cd \                   # drive root / meghajtó gyökere
C:                     # change drive / meghajtó váltás
tree                   # folder tree / mappafa
```

## Working with files & folders
_Mappa és fájl kezelés_
```shell
mkdir dir              # create folder / mappa létrehozása
rmdir dir              # remove empty folder / üres mappa törlése
rmdir /s dir           # delete folder recursively / mappa törlése rekurzívan
rmdir /s /q dir        # force delete folder / kényszerített törlés (óvatosan)

del file.txt           # delete file / fájl törlése
del /f file.txt        # force delete file / fájl kényszerített törlése
copy a.txt b.txt       # copy file / fájl másolása
xcopy dir1 dir2 /e     # copy folder recursively / mappa másolása rekurzívan
move a.txt folder\     # move or rename / áthelyezés vagy átnevezés
type nul > file.txt    # create empty file / üres fájl létrehozása
```

## Viewing file contents
_Szöveges fájl tartalmának olvasása_
```shell
type file.txt          # show file content / fájl tartalma
more file.txt          # paged view / lapozható megjelenítés
```

## Finding things
_Mappák fájlok és parancsok keresése_
```shell
dir *.txt /s               # find files by name / fájl keresése név alapján
where python               # find program in PATH / program helye
find "hello" file.txt      # search text in file / szöveg keresése fájlban
findstr /s /i "word" *.txt # search text recursively / rekurzív szövegkeresés
```

## Editing files quickly
_Szöveges fájl gyors szerkesztése_
```shell
notepad file.txt       # open file in editor / fájl megnyitása szerkesztőben
```

## Environment variables (basics)
_Változók és Környezeti változók_
```shell
set                    # list variables / környezeti változók
set NAME=value         # set variable (temporary) / változó beállítása (ideiglenes)
echo %USERNAME%        # show username / felhasználónév
echo %PATH%            # show PATH / PATH megjelenítése
```

## User & system info
_Felhasználó és rendszer információ_
```shell
whoami                 # current user / aktuális felhasználó
hostname               # computer name / gépnév
ver                    # Windows version / Windows verzió
systeminfo             # system information / rendszerinformáció
```

## Processes (running programs)
_Folyamatok (futó alkalmazások)_
```shell
tasklist                # list running programs / futó programok
tasklist | more         # paged list / lapozható lista
taskkill /PID 1234      # stop program by PID / program leállítása PID alapján
taskkill /IM app.exe    # stop by name / leállítás név alapján
taskkill /F /IM app.exe # force stop / kényszerített leállítás
```

## Networking essentials
_Hálózati alapok_
```shell
ipconfig               # IP address info / IP cím információ
ipconfig /all          # detailed network info / részletes hálózati adatok
ping 8.8.8.8           # test internet / internet teszt
ping google.com        # test DNS / DNS teszt
tracert google.com     # route tracing / útvonal követés
netstat -ano           # connections + PIDs / kapcsolatok + PID-ek
```

## Network drives & sharing
_Hálózati meghajtók és megosztás_
```shell
net use                   # list network drives / hálózati meghajtók
net use Z: \\server\share # map network drive / hálózati meghajtó csatolása
net use Z: /delete        # remove network drive / meghajtó leválasztása
```

## Storage & disks
_File tárolás és meghajtók_
```shell
wmic logicaldisk get caption,freespace,size # disk space info / lemezterület
diskpart                                    # disk tool (dangerous) / lemezkezelő (veszélyes)
```

## Archives & compression
_Archiválós és tömörítés_
```shell
tar -cf backup.tar folder # create archive / archívum készítése
tar -xf backup.tar        # extract archive / archívum kibontása
```

## Useful everyday commands
_Hasznos mindennapi parancsok_
```shell
cls                    # clear screen / képernyő törlése
echo Hello             # print text / szöveg kiírása
pause                  # wait for keypress / várakozás billentyűre
exit                   # close command line / parancssor bezárása
```

## ⚠️ Be careful commands
_Veszélyes parancsok_
```shell
rmdir /s /q folder     # permanent delete / végleges törlés
del /f /s *            # mass delete / tömeges törlés
diskpart               # can destroy data / adatvesztést okozhat
```

## Quick “what’s wrong?” checklist
_Gyors hibakeresés_
```shell
ipconfig                       # do I have an IP? / van IP cím?
ping 8.8.8.8                   # internet works? / van internet?
ping google.com                # DNS works? / működik a DNS?
tasklist                       # is my app running? / fut a program?
wmic logicaldisk get freespace # disk full? / tele a lemez?
```

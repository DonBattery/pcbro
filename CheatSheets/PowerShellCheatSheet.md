# PowerShell Brotherhood Secret Code  
_Az ErőKagyló Testvériség Titkos Kódja_

These are the secret codes our adepts should learn, so they can speak to **The Shell of Power**. The codes include navigation, files, searching, networking, processes, storage, and troubleshooting.  

_Ezek azok a titkos kódok, amelyeket tanoncainknak meg kell tanulniuk, hogy szólhassanak **Az Erő Kagylójához**. A kódok tartalmazzák a navigációt, fájlkezelést, keresést, hálózatot, folyamatokat, tárolást és hibakeresést._


## Navigation & filesystem basics  
_Navigáció és fájlrendszer alapok_
```powershell
Get-Location           # where am I / hol vagyok
Get-ChildItem          # list files / fájlok listázása
Get-ChildItem -Force   # include hidden files / rejtett fájlokkal együtt
Set-Location folder    # change directory / mappaváltás
Set-Location ..        # up one level / egy szinttel feljebb
Set-Location C:\       # drive root / meghajtó gyökere
tree                   # folder tree / mappafa
```

Aliases you will often see:  
_Gyakori aliaszok:_  

- `ls` → `Get-ChildItem`
- `cd` → `Set-Location`
- `pwd` → `Get-Location`

## Working with files & folders  
_Mappa és fájl kezelés_
```powershell
New-Item dir -ItemType Directory # create folder / mappa létrehozása
Remove-Item dir                  # remove empty folder / üres mappa törlése
Remove-Item dir -Recurse         # delete folder recursively / mappa törlése rekurzívan
Remove-Item dir -Recurse -Force  # force delete / kényszerített törlés (óvatosan)

Remove-Item file.txt         # delete file / fájl törlése
Copy-Item a.txt b.txt        # copy file / fájl másolása
Copy-Item dir1 dir2 -Recurse # copy folder / mappa másolása
Move-Item a.txt folder\      # move or rename / áthelyezés vagy átnevezés
New-Item file.txt            # create empty file / üres fájl létrehozása
```

## Viewing file contents
_Szöveges fájl tartalmának olvasása_
```powershell
Get-Content file.txt           # show file content / fájl tartalma
Get-Content file.txt -First 10 # first lines / első sorok
Get-Content file.txt -Last 10  # last lines / utolsó sorok
Get-Content file.txt | more    # paged view / lapozható megjelenítés
```

## Finding things
_Mappák fájlok és parancsok keresése_
```powershell
Get-ChildItem -Filter *.txt -Recurse # find files by name / fájl keresése név alapján
Get-Command python                   # find command / parancs helye
Select-String "hello" file.txt       # search text in file / szöveg keresése fájlban
Select-String "word" *.txt -Recurse  # recursive text search / rekurzív szövegkeresés
```

## Editing files quickly
_Szöveges fájl gyors szerkesztése_
```powershell
notepad file.txt # open file in editor / fájl megnyitása szerkesztőben
```

## Variables & environment
_Változók és Környezeti változók_
```powershell
Get-Variable            # list variables / változók listázása
$var = "hello"          # create variable / változó létrehozása
$env:USERNAME           # show username / felhasználónév
$env:PATH               # show PATH / PATH megjelenítése
```

## User & system info
_Felhasználó és rendszer információ_
```powershell
whoami                  # current user / aktuális felhasználó
hostname                # computer name / gépnév
Get-ComputerInfo        # system information / rendszerinformáció
$PSVersionTable         # PowerShell version / PowerShell verzió
```

## Processes (running programs)
_Folyamatok (futó alkalmazások)_
```powershell
Get-Process                   # list processes / futó folyamatok
Get-Process | more            # paged list / lapozható lista
Stop-Process -Id 1234         # stop by PID / leállítás PID alapján
Stop-Process -Name app        # stop by name / leállítás név alapján
Stop-Process -Name app -Force # force stop / kényszerített leállítás
```

## Networking essentials
_Hálózati alapok_
```powershell
Get-NetIPAddress                 # IP addresses / IP címek
ipconfig                         # old CMD command still works / klasszikus parancs itt is működik
Test-Connection 8.8.8.8 -Count 4 # ping test / ping teszt
Test-Connection google.com       # DNS test / DNS teszt
tracert google.com               # route tracing / útvonal követés
Get-NetTCPConnection             # network connections / hálózati kapcsolatok
```

## Network drives & sharing
_Hálózati meghajtók és megosztás_
```powershell
Get-PSDrive                                                     # list drives / meghajtók listázása
New-PSDrive -Name Z -PSProvider FileSystem -Root \\server\share # map network drive / hálózati meghajtó csatolása
Remove-PSDrive Z                                                # remove network drive / meghajtó leválasztása
```

## Storage & disks
_File tárolás és meghajtók_
```powershell
Get-Volume                         # disk info / lemez információ
Get-PSDrive -PSProvider FileSystem # disk usage / lemezhasználat
```

## Archives & compression
_Archiválós és tömörítés_
```powershell
Compress-Archive folder backup.zip # create zip archive / zip archívum készítése
Expand-Archive backup.zip          # extract zip / zip kibontása
```

## Useful everyday commands
_Hasznos mindennapi parancsok_
```powershell
Clear-Host              # clear screen / képernyő törlése
Write-Output "Hello"    # print text / szöveg kiírása
Start-Sleep 3           # wait 3 seconds / várakozás 3 másodpercig
exit                    # close PowerShell / PowerShell bezárása
```

## ⚠️ Be careful commands
_Veszélyes parancsok_
```powershell
Remove-Item C:\path -Recurse -Force # permanent delete / végleges törlés
Format-Volume                       # wipes disk / lemez törlése
```

## Quick “what’s wrong?” checklist
_Gyors hibakeresés_
```powershell
Get-NetIPAddress           # do I have an IP? / van IP cím?
Test-Connection 8.8.8.8    # internet works? / van internet?
Test-Connection google.com # DNS works? / működik a DNS?
Get-Process                # is my app running? / fut a program?
Get-Volume                 # disk full? / tele a lemez?

# List the top 10 most memory intense processes / listázzuk ki a 10 legnagyobb memóriazabáló folyamatot
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, Id, @{Name="Memory(MB)";Expression={[math]::Round($_.WorkingSet64/1MB,2)}}
```

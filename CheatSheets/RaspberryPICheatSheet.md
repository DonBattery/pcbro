# Raspberry Brotherhood Secret Code
# _A Málnatestvériség Titkos Kódja_

These are the secret codes our adepts should learn, so they and talk to The Raspberry. The codes includes navigation, files, networking, services, storage, packages, and logs.  

_E titkos kódokat kell tanoncainknak elsajátítaniuk, hogy szólhassanak A Málnához. A kódok tartalmazzák a navigációt, aktákat, hálózatokat, szolgáltatásokat, csomagokat és a naplót._

## Navigation & filesystem basics  
_Navigáció és fájlrendszer alapok_
```bash
pwd                  # where am I / hol vagyok (aktuális mappa)
ls                   # list files / fájlok listázása
ls -la               # list include hidden + details / rejtett fájlok + részletek
cd /path             # change directory / mappaváltás
cd ..                # up one folder / egy szinttel feljebb
cd ~                 # home directory / saját (home) könyvtár
tree                 # folder tree (install: sudo apt install tree) / mappafa (telepítés: sudo apt install tree)
```

## Working with files & folders  
_Mappa és fájl kezelés_
```bash
mkdir dir            # create folder / mappa létrehozása
rmdir dir            # remove empty folder / üres mappa törlése
rm file              # delete file / fájl törlése
rm -r dir            # delete folder recursively (careful) / mappa törlése rekurzívan (óvatosan)
rm -rf dir           # force delete (VERY careful) / kényszerített törlés (NAGYON óvatosan)

cp a b               # copy file a -> b / fájl másolása a -> b
cp -r dir1 dir2      # copy folder / mappa másolása
mv a b               # rename/move / átnevezés vagy áthelyezés
touch file           # create empty file / update timestamp / üres fájl létrehozása / időbélyeg frissítése

cat file             # print file / fájl tartalmának kiírása
less file            # view with paging (q to quit) / lapozható nézet (q kilép)
head -n 20 file      # first lines / első sorok
tail -n 20 file      # last lines / utolsó sorok
tail -f file         # follow logs / napló követése (folyamatosan)
```

## Finding things
_Mappák fájlok és parancsok keresése_
```bash
find . -name "*.txt"                 # find by name / keresés név alapján
grep -R "needle" .                   # search text recursively / szöveg keresése rekurzívan
grep -RIn "needle" .                 # include line numbers / sorszámokkal együtt
which python3                        # where a command lives / hol van a parancs (elérési út)
whereis ssh                          # common locations / tipikus helyek (bináris + man)
```

## Editing config quickly
_Szöveges fájl gyors szerkesztése_
```bash
nano file            # simple editor / egyszerű szerkesztő
sudo nano /etc/hosts # edit as root / szerkesztés rootként
```

**Nano tips:** `Ctrl+O` save, `Ctrl+X` exit.  
**Nano tippek:** `Ctrl+O` mentés, `Ctrl+X` kilépés.

## Permissions & ownership
_Jogosultságok és hozzáférés_
```bash
ls -l               # see permissions / jogosultságok megtekintése
chmod +x script.sh  # make executable / futtathatóvá tesz
chmod 644 file      # rw-r--r-- / tipikus fájl jogosultság
chmod 755 dir       # rwxr-xr-x / tipikus mappa jogosultság

sudo chown pi:pi file        # change owner:group / tulajdonos:csoport módosítása
sudo chown -R pi:pi folder   # recursive / rekurzívan (mindenre)
sudo                          # run as root / futtatás root jogosultsággal
```

## Users & groups (common on Pi)
_Felhasználók és csoportok_
```bash
whoami              # current user / aktuális felhasználó
groups              # groups you’re in / csoportjaid
id                  # uid/gid + groups / uid/gid + csoportok

sudo adduser bob                # create user / felhasználó létrehozása
sudo usermod -aG sudo bob       # give sudo / sudo jog adása
sudo usermod -aG gpio bob       # GPIO access (if gpio group exists) / GPIO hozzáférés (ha van gpio csoport)
```

## System info & monitoring
_Rendszer információ_
```bash
uname -a            # kernel/system info / kernel és rendszer infó
cat /etc/os-release # distro info / disztribúció infó
uptime              # load + uptime / terhelés + futási idő
free -h             # memory / memória
df -h               # disk usage by filesystem / lemezhasználat fájlrendszerenként
du -sh *            # size of items in current dir / elemek mérete az aktuális mappában
top                 # live processes (q to quit) / futó folyamatok (q kilép)
htop                # nicer top (install: sudo apt install htop) / szebb top (telepítés: sudo apt install htop)
```

## Processes: start/stop/kill
_Folyamatok listázása és leállítása_
```bash
ps aux | less                    # list processes / folyamatok listázása
pgrep -a python                  # find pids by name / PID keresés név alapján
kill PID                         # ask process to stop / folyamat leállításának kérése
kill -9 PID                      # force stop (last resort) / kényszerített leállítás (utolsó mentsvár)
sudo reboot                      # reboot / újraindítás
sudo shutdown -h now             # power off / leállítás (kikapcsolás)
```

## Networking essentials
_Hálózati alapok_
```bash
ip a                 # IP addresses / IP címek
ip r                 # routes / útvonalak (routing)
ping -c 4 8.8.8.8    # test connectivity / kapcsolat teszt
ping -c 4 google.com # test DNS / DNS teszt
hostname -I          # quick local IP / gyors helyi IP

ss -tulpn            # listening ports (modern netstat) / hallgató portok (netstat helyett)
curl -I https://example.com      # HTTP headers / HTTP fejlécek
wget URL             # download / letöltés
```

### SSH (remote login)
_A Biztonság Kagylójának megnyitása egy távoli gépen_
```bash
ssh pi@raspberrypi.local              # login by mDNS name / belépés mDNS névvel
ssh pi@192.168.1.50                   # login by IP / belépés IP-vel
scp file pi@192.168.1.50:/home/pi/    # copy to Pi / másolás a Pi-ra
scp pi@192.168.1.50:/home/pi/file .   # copy from Pi / másolás a Pi-ról
```

## Packages (Debian/Raspberry Pi OS)
_Az operációs rendszer csomagjainak kezelése_
```bash
sudo apt update                  # refresh package lists / csomaglista frissítése
sudo apt upgrade                 # upgrade installed packages / telepített csomagok frissítése
sudo apt full-upgrade            # may remove/replace packages if needed / szükség esetén cserél/eltávolít
sudo apt install PACKAGE         # install / telepítés
sudo apt remove PACKAGE          # remove / eltávolítás
sudo apt autoremove              # clean unused deps / felesleges függőségek törlése
apt search KEYWORD               # find packages / csomag keresés
apt show PACKAGE                 # package info / csomag infó
```

## Services (systemd) — super important on Pi
_Szolgáltatások kezelése a rendszer démon segítségével_
```bash
systemctl status SERVICE         # service status / szolgáltatás állapota
sudo systemctl start SERVICE     # start now / indítás most
sudo systemctl stop SERVICE      # stop now / leállítás most
sudo systemctl restart SERVICE   # restart / újraindítás
sudo systemctl enable SERVICE    # start on boot / induljon bootkor
sudo systemctl disable SERVICE   # don’t start on boot / ne induljon bootkor
```

Common services: `ssh`, `NetworkManager`, `dhcpcd`, `bluetooth`.  
Gyakori szolgáltatások: `ssh`, `NetworkManager`, `dhcpcd`, `bluetooth`.

## Logs & troubleshooting
_Napló és hibaelhárítás_
```bash
journalctl -xe                   # recent errors + context / friss hibák + kontextus
journalctl -u SERVICE -e         # logs for a service / szolgáltatás naplói
journalctl -u SERVICE -f         # follow service logs / napló követése élőben
dmesg | tail -n 50               # kernel messages (USB, drivers, etc.) / kernel üzenetek (USB, driverek, stb.)
```

## Storage: drives, partitions, mounts
_Tárolás: meghajtók, partíciók és hátasok (csatolt meghajtók)_
```bash
lsblk                 # disks/partitions overview / lemezek és partíciók áttekintése
blkid                 # UUIDs (useful for /etc/fstab) / UUID-k (hasznos az /etc/fstab-hoz)
sudo fdisk -l         # partition tables (careful) / partíciós táblák (óvatosan)

sudo mount /dev/sda1 /mnt         # mount a drive / meghajtó csatolása
sudo umount /mnt                  # unmount / leválasztás
```

## Archives & compression
_Archiválós és tömörítés_
```bash
tar -czf backup.tgz folder/       # create .tgz / .tgz készítése
tar -xzf backup.tgz               # extract .tgz / .tgz kicsomagolása
zip -r file.zip folder/           # zip / zip készítése
unzip file.zip                    # unzip / zip kicsomagolása
```

## Useful one-liners (Pi-flavored)
_Hasznos mindennapi parancsok_
```bash
vcgencmd measure_temp             # CPU temp (Pi firmware tool) / CPU hőmérséklet (Pi firmware eszköz)
watch -n 1 vcgencmd measure_temp  # update every second / frissítés másodpercenként
python3 -m http.server 8000       # quick web server in current dir / gyors webszerver az aktuális mappában
```

## “Be careful” commands
_Veszélyes parancsok_
```bash
sudo rm -rf /something   # can wipe your system if wrong path / rossz útvonal esetén rendszer törlése is lehet
sudo dd if=... of=...    # can overwrite disks instantly / pillanatok alatt felülírhat lemezeket
chmod -R 777 ...         # usually a bad idea / általában rossz ötlet
```

## Quick “what’s wrong?” checklist
_Gyors hibakeresés_
```bash
ip a && ip r                         # do I have IP + route? / van IP + útvonal?
ping -c 2 8.8.8.8                    # internet? / van internet?
ping -c 2 google.com                 # DNS? / működik a DNS?
df -h                                # disk full? / tele a lemez?
free -h                              # memory pressure? / kevés a memória?
systemctl status SERVICE             # is my service running? / fut a szolgáltatás?
journalctl -u SERVICE -e             # what does it say? / mit ír a napló?
```
# Python Cheat Sheet (English / Magyar)

These are the secret codes every Python adept should learn, so they can talk to The Python.  
_E titkos kódokat kell elsajátítania minden jövendőbeli Piton növendéknek, hogy szólni tudjanak A Pitonhoz_

---

## Starting the Python interpreter  
_Python értelmező indítása_
```bash
python
python3
```

```python
import this     # The Zen of Python / A Python filozófiája
```

```python
exit()          # exit interpreter / kilépés az értelmezőből
quit()          # same as exit() / ugyanaz, mint az exit()
```

---

## Printing output  
_Kimenet kiírása_
```python
print("Hello world")          # print text / szöveg kiírása
print(123)                    # print number / szám kiírása
print("Age:", 42)             # multiple values / több érték
print(f"Age: {42}")           # formatted string / formázott szöveg
```

---

## Primitive variables & types  
_Alap változók és típusok_
```python
x = 10              # int (integer) / egész szám
y = 3.14            # float / lebegőpontos szám
name = "Alice"      # str (string) / szöveg
is_ok = True        # bool / logikai érték
nothing = None      # NoneType / nincs érték
```

```python
type(x)             # check type / típus lekérdezése
```

---

## Basic operators  
_Alap operátorok_
```python
a + b     # addition / összeadás
a - b     # subtraction / kivonás
a * b     # multiplication / szorzás
a / b     # division / osztás (float)
a // b    # integer division / egész osztás
a % b     # remainder / maradék
a ** b    # power / hatvány
```

---

## Flow control – if / else  
_Vezérlés – feltételek_
```python
if x > 10:
    print("big")
elif x == 10:
    print("exactly ten")
else:
    print("small")
```

```python
# comparison operators / összehasonlító operátorok
==   !=   <   >   <=   >=
```

---

## Basic loops  
_Alap ciklusok_

### while loop  
_Elöltesztelős ciklus_
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### for loop  
_For ciklus (iterálás)_
```python
for i in range(5):
    print(i)
```

```python
range(5)        # 0..4
range(1, 5)     # 1..4
range(0, 10, 2) # step by 2 / kettesével
```

### loop control  
_Ciklus vezérlés_
```python
break     # exit loop / ciklus megszakítása
continue  # next iteration / következő lépés
```

---

## Basic functions  
_Alap függvények_
```python
def greet(name):
    print("Hello", name)
```

```python
greet("Bob")     # function call / függvény hívás
```

```python
def add(a, b):
    return a + b

result = add(2, 3)
```

---

## Built-in useful functions  
_Hasznos beépített függvények_
```python
len("hello")         # length / hossz
int("123")           # convert to int / átalakítás int-re
float("3.14")        # convert to float / átalakítás float-ra
str(42)              # convert to string / átalakítás szöveggé
```

---

## Input from user  
_Felhasználói bemenet_
```python
name = input("Your name: ")
print("Hello", name)
```

---

## Comments  
_Megjegyzések_
```python
# This is a comment
# Ez egy megjegyzés
```

---

## Helpful tips  
_Hasznos tippek_

- Python is **indentation-sensitive**  
  A Python **behúzásérzékeny**
- Use 4 spaces for indentation  
  4 szóközt használj behúzáshoz
- Read error messages carefully  
  Olvasd el figyelmesen a hibaüzeneteket

---


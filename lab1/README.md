# backup.sh

## Descriere
Acest script shell realizează backup pentru un director specificat.  
Creează o arhivă comprimată (`.tar.gz`) care conține directorul sursă și o salvează într-un director destinație.

---

## Utilizare

```bash
./backup.sh <sursa> [destinatie]
```
## Exemplu 
1. Backup cu destinație implicită

```bash
./backup.sh /mnt/d/Automatizare/lab1
```
Creează o arhivă cu numele în formatul:
`lab1YYYYMMDDHHMMSS.tar.gz`
 
Salvată în `/mnt/d/backup` (D:\backup în Windows)

2. Backup cu destinație implicită

```bash
./backup.sh /mnt/d/Automatizare/lab1 /mnt/d/BackupsProiect
```
Creează o arhivă cu numele în formatul:
`lab1YYYYMMDDHHMMSS.tar.gz`
 
Salvată în `/mnt/d/BackupsProiect`.
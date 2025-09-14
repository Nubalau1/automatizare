#!/bin/bash

# Verificare dacă a fost dat primul argument (directorul sursă)
if [ -z "$1" ]; then
    echo "Eroare: Nu ai specificat directorul de backup."
    echo "Exemplu: $0 <sursa> [destinatie]"
    exit 1
fi

SRC_DIR="$1"                          # Directorul de backup
DEST_DIR="${2:-/mnt/d/backup}"        # Default: D:\backup

# Verificare existență director sursă
if [ ! -d "$SRC_DIR" ]; then
    echo "Eroare: Directorul sursă '$SRC_DIR' nu există."
    exit 2
fi

# Creare director destinație dacă nu există
if [ ! -d "$DEST_DIR" ]; then
    echo "Directorul destinație '$DEST_DIR' nu există. Se creaza"
    mkdir -p "$DEST_DIR" || {
        echo "Eroare: Nu pot crea directorul destinație."
        exit 3
    }
fi

# Creare arhivă tar.gz cu data curentă
DATE=$(date +%Y%m%d%H%M%S)
BASENAME=$(basename "$SRC_DIR")
ARCHIVE_NAME="${BASENAME}${DATE}.tar.gz"
ARCHIVE_PATH="$DEST_DIR/$ARCHIVE_NAME"

tar -czf "$ARCHIVE_PATH" -C "$(dirname "$SRC_DIR")" "$BASENAME"

if [ $? -eq 0 ]; then
    echo "Backup realizat cu succes: $ARCHIVE_PATH"
else
    echo "Eroare: Backup-ul nu a reușit."
    exit 4
fi

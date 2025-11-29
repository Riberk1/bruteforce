#!/bin/bash

WORDLIST="wordlist.txt"

if [ ! -f "$WORDLIST" ]; then
    echo "Arquivo $WORDLIST não encontrado!"
    exit 1
fi

echo "Lendo wordlist..."

while IFS= read -r linha; do
    echo "Entrada: $linha"
done < "$WORDLIST"

echo "Finalizado."

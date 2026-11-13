
#!/bin/sh

HOST="servidor-web-dmz-lgarcia.onrender.com"

echo "=========================================="
echo "MODULO 02 - VERIFICACION DE PUERTO TCP"
echo "Estudiante: Laura Garcia"
echo "Servidor objetivo: $HOST"
echo "=========================================="

echo "Resolviendo nombre del servidor..."
nslookup "$HOST" || true

echo "Comprobando conectividad TCP al puerto 443..."

if nc -zv -w 5 "$HOST" 443 2>&1; then
    echo "[RESULTADO] Puerto 443 accesible"
else
    echo "[RESULTADO] No se pudo establecer conexion TCP"
fi

echo "=========================================="
echo "VERIFICACION FINALIZADA"
echo "=========================================="

exec python3 -m http.server 8080

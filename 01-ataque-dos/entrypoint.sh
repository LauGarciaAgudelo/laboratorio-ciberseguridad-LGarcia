
#!/bin/sh

TARGET="https://servidor-web-dmz-lgarcia.onrender.com"

echo "======================================"
echo "MODULO 01 - SIMULACION DE TRAFICO HTTP"
echo "Estudiante: Laura Garcia"
echo "Destino: $TARGET"
echo "======================================"

echo "Iniciando prueba controlada..."

for i in 1 2 3 4 5
do
    echo "Solicitud $i de 5"

    curl --silent --show-error \
      --max-time 15 \
      --output /dev/null \
      --write-out "HTTP %{http_code}\n" \
      "$TARGET/"

    sleep 2
done

echo "======================================"
echo "SIMULACION FINALIZADA"
echo "======================================"

# Mantiene disponible el servicio en Render.
exec python3 -m http.server 8080

# get-rssi

Este proyecto escanea las redes WiFi disponibles, obtiene su SSID, MAC y RSSI, y los guarda en un archivo CSV

## Instalacion

1. Clona este repositorio:

```bash
git clone https://github.com/diegoroca/get-rssi.git
cd get-rssi
```

2. Crea un entorno virtual (virtual enviroment):

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

3. Installa las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el script get_rssi.py con permisos de administrador

```bash
sudo python get-rssi.py # En Windows usa python get-rssi.py en powershell o cmd abierto como administrador
```

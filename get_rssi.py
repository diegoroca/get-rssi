import time
from pywifi import PyWiFi, const

def scan_wifi_networks():
    wifi = PyWiFi()
    iface = wifi.interfaces()[1]  # El numero del array selecciona la interfaz de red que se usa para el escaneo
    print(f"Using network interface: {iface.name()}")

    iface.scan()  # Realiza el escaneo de redes
    time.sleep(10)

    scan_results = iface.scan_results()  # Guarda los resultados
    #print(scan_results)

    networks = []

    for network in scan_results:
        ssid = network.ssid
        rssi = network.signal
        mac_address = network.bssid

        networks.append({
            "SSID": ssid,
            "RSSI": rssi,
            "MAC Address": mac_address
        })

    return networks

# Imprime los detalles de cada red
for network in scan_wifi_networks():
    print(f"SSID: {network['SSID']}, RSSI: {network['RSSI']} dBm, MAC Address: {network['MAC Address']}")

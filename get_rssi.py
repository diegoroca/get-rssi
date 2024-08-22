import time
import csv
from pywifi import PyWiFi, const

GREEN = '\033[92m'
RESET = '\033[0m'  # Reset to default color

def scan_wifi_networks():
    wifi = PyWiFi()
    iface = wifi.interfaces()[1]  # En Windows probablemente solo exista la intefaz 0
    print("")
    print(f"Escaneando con la interfaz de red: {iface.name()}")
    print("Tomara 10s ...")

    iface.scan()  # Realiza el escaneo de redes
    time.sleep(10)

    scan_results = iface.scan_results()  # Guarda los resultados

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

def save_to_csv(networks, filename="wifi_scan_results.csv"):
    # Define the header
    header = ["SSID", "MAC Address", "RSSI"]

    # Open the CSV file for writing
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)

        # Write the header to the CSV file
        writer.writeheader()

        # Write the network data
        for network in networks:
            writer.writerow(network)

# Scan for networks and save the results to a CSV file
parcel = input("Ingresa el nombre de la parcela o seccion que estas escaneando: ")
networks = scan_wifi_networks()
save_to_csv(networks, (parcel + ".csv"))

# Print out the details of each network
print("")
for i, network in enumerate(networks):
    print(f"SSID: {network['SSID']}, RSSI: {network['RSSI']} dBm, MAC Address: {network['MAC Address']}")

    if i > 8:
        print("... more")
        break

print("")
print(f"{GREEN}Archivo CSV generado{RESET}")

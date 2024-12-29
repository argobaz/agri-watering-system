# Solar-Powered Irrigation Automation Design

## Components and Connections
1. Solar Panel Array (300-500 W panels)
2. Charge Controller
3. Battery Bank (12V/100Ah x 2 or 24V system)
4. Inverter (if AC components are needed)
5. Soil Moisture Sensors (placed in 2-3 locations across the field)
6. Water Level Sensor (inside the 5-ton water tank)
7. Water Pump (12V DC, connected to the water tank)
8. Solenoid Valve (controls water flow)
9. Control Unit (Arduino or Raspberry Pi with GSM/Wi-Fi module for remote control)
10. PVC pipes (for water distribution)

## System Overview
The solar-powered irrigation system works as follows:
- **Energy Generation and Storage:** Solar panels generate power, which is stored in the battery bank via the charge controller.
- **Soil Monitoring:** Soil moisture sensors continuously measure the soil's water content.
- **Irrigation Activation:** When moisture falls below a threshold, the control unit activates the pump and opens the solenoid valve to irrigate.
- **Water Management:** The water pump draws from the tank, ensuring water is distributed evenly across the field.
- **Automatic Shutoff:** Once sufficient moisture is detected, the pump stops, and the valve closes.
- **Remote Access:** The entire system is controllable via Wi-Fi or GSM for monitoring and manual overrides.
- **Tank Monitoring:** A water level sensor prevents dry running by alerting the user when the tank is low.

### Visual Flow Diagram
1. **Solar Panels**:
    - Capture sunlight and convert it into electricity.
    - Connected to the charge controller.
2. **Charge Controller**:
    - Regulates the energy flow to the battery bank, preventing overcharging.
3. **Battery Bank**:
    - Stores energy for powering the system.
4. **Control Unit**:
    - Collects data from sensors and executes logic to manage irrigation.
5. **Soil Moisture Sensors**:
    - Measure soil hydration levels.
6. **Water Pump and Solenoid Valve**:
    - Operate together to irrigate the field when needed.
7. **Water Tank**:
    - Supplies water for irrigation and is monitored for level.
8. **Remote Monitoring**:
    - Provides status updates and control options.

### Example System Workflow Diagram
1. **Solar Energy** → Battery Bank (via Charge Controller)
2. **Soil Sensor Data** → Control Unit → Decision (Irrigate or Not)
3. **If Irrigate:** Pump ON → Solenoid Valve OPEN → Water Flow → Soil Hydrated → Stop
4. **Water Level Low:** Notify User

---

## Python-Based Pseudocode for Automation Logic

```python
from machine import Pin, ADC
import time
import network
import ujson

# Initialize sensors and devices
soil_moisture_sensor = ADC(Pin(36))  # Example pin
water_level_sensor = ADC(Pin(39))  # Example pin
pump_relay = Pin(25, Pin.OUT)
solenoid_valve = Pin(26, Pin.OUT)

# Thresholds
moisture_threshold = 30  # Example value (adjust based on calibration)
water_level_threshold = 10  # Example value (adjust based on calibration)

# Configurable delay parameter
delay_interval = 10  # Default delay interval in seconds

# Wi-Fi setup (for remote control)
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    try:
        with open('wifi_config.json', 'r') as config_file:
            config = ujson.load(config_file)
            wifi.connect(config['ssid'], config['password'])
    except Exception as e:
        print("Error reading Wi-Fi configuration:", e)
        return

    while not wifi.isconnected():
        pass
    print('Wi-Fi connected:', wifi.ifconfig())

# Create a Wi-Fi configuration file if it doesn't exist
def create_wifi_config():
    config = {
        "ssid": "Your_SSID",
        "password": "Your_Password"
    }
    with open('wifi_config.json', 'w') as config_file:
        ujson.dump(config, config_file)
    print("Default Wi-Fi configuration file created.")

# Ensure configuration file exists
try:
    with open('wifi_config.json', 'r') as _:
        pass
except FileNotFoundError:
    create_wifi_config()

connect_wifi()

# Main loop
while True:
    soil_moisture = soil_moisture_sensor.read()  # Read soil moisture level
    water_level = water_level_sensor.read()  # Read water level in tank

    if soil_moisture < moisture_threshold and water_level > water_level_threshold:
        print("Starting irrigation...")
        pump_relay.value(1)  # Turn on water pump
        solenoid_valve.value(1)  # Open solenoid valve
    else:
        print("Stopping irrigation...")
        pump_relay.value(0)  # Turn off water pump
        solenoid_valve.value(0)  # Close solenoid valve

    # Add remote control functionality (via MQTT or HTTP server)

    time.sleep(delay_interval)  # Configurable delay
```



# Güneş Enerjisiyle Çalışan Sulama Otomasyonu Tasarımı

## Bileşenler ve Bağlantılar
1. Güneş Paneli Dizisi (300-500 W paneller)
2. Şarj Kontrol Cihazı
3. Akü Bankası (12V/100Ah x 2 veya 24V sistem)
4. İnvertör (AC bileşenler gerekiyorsa)
5. Toprak Nem Sensörleri (tarlanın farklı bölgelerinde 2-3 yerde yerleştirilmiş)
6. Su Seviyesi Sensörü (5 tonluk su tankının içinde)
7. Su Pompası (12V DC, su tankına bağlı)
8. Solenoid Vana (su akışını kontrol eder)
9. Kontrol Ünitesi (Uzaktan kontrol için GSM/Wi-Fi modüllü Arduino veya Raspberry Pi)
10. PVC Borular (su dağıtımı için)

## Sistem Genel Yapısı
Güneş enerjisiyle çalışan sulama sistemi şu şekilde çalışır:
- **Enerji Üretimi ve Depolama:** Güneş panelleri enerji üretir ve bu enerji şarj kontrol cihazı aracılığıyla akü bankasında depolanır.
- **Toprak İzleme:** Toprak nem sensörleri sürekli olarak toprağın su içeriğini ölçer.
- **Sulama Aktivasyonu:** Nem bir eşik değerinin altına düştüğünde, kontrol ünitesi pompayı çalıştırır ve solenoid vanayı açar.
- **Su Yönetimi:** Su pompası tanktan su çeker ve suyun tarlaya eşit şekilde dağıtılmasını sağlar.
- **Otomatik Kapatma:** Yeterli nem algılandığında pompa durur ve vana kapanır.
- **Uzaktan Erişim:** Tüm sistem Wi-Fi veya GSM üzerinden izlenebilir ve manuel kontrol edilebilir.
- **Tank İzleme:** Su seviyesi sensörü, tanktaki su azaldığında kullanıcıyı uyarır ve kuru çalışmayı önler.

### Görsel Akış Diyagramı
1. **Güneş Panelleri**:
    - Güneş ışığını yakalar ve elektriğe dönüştürür.
    - Şarj kontrol cihazına bağlanır.
2. **Şarj Kontrol Cihazı**:
    - Enerji akışını düzenler ve akü bankasının aşırı şarj olmasını önler.
3. **Akü Bankası**:
    - Sistemi çalıştırmak için enerji depolar.
4. **Kontrol Ünitesi**:
    - Sensörlerden veri toplar ve sulamayı yönetmek için gerekli mantığı uygular.
5. **Toprak Nem Sensörleri**:
    - Toprak nem seviyelerini ölçer.
6. **Su Pompası ve Solenoid Vana**:
    - Sulama gerektiğinde birlikte çalışır.
7. **Su Tankı**:
    - Sulama için su sağlar ve seviyesi izlenir.
8. **Uzaktan İzleme**:
    - Durum güncellemeleri ve kontrol seçenekleri sunar.

### Örnek Sistem Akış Diyagramı
1. **Güneş Enerjisi** → Şarj Kontrol Cihazı üzerinden Akü Bankası
2. **Toprak Sensör Verileri** → Kontrol Ünitesi → Karar (Sulama Yap veya Yapma)
3. **Eğer Sulama:** Pompa AÇIK → Solenoid Vana AÇIK → Su Akışı → Toprak Nemlendirilir → Dur
4. **Su Seviyesi Düşük:** Kullanıcıya Bildir

---

## Python Tabanlı Otomasyon Mantığı İçin Örnek Kod

```python
from machine import Pin, ADC
import time
import network
import ujson

# Sensörleri ve cihazları başlat
soil_moisture_sensor = ADC(Pin(36))  # Örnek pin
water_level_sensor = ADC(Pin(39))  # Örnek pin
pump_relay = Pin(25, Pin.OUT)
solenoid_valve = Pin(26, Pin.OUT)

# Eşik değerleri
moisture_threshold = 30  # Örnek değer (kalibrasyona göre ayarlayın)
water_level_threshold = 10  # Örnek değer (kalibrasyona göre ayarlayın)

# Yapılandırılabilir gecikme parametresi
delay_interval = 10  # Varsayılan gecikme süresi saniye cinsinden

# Wi-Fi ayarları (uzaktan kontrol için)
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    try:
        with open('wifi_config.json', 'r') as config_file:
            config = ujson.load(config_file)
            wifi.connect(config['ssid'], config['password'])
    except Exception as e:
        print("Wi-Fi yapılandırma okuma hatası:", e)
        return

    while not wifi.isconnected():
        pass
    print('Wi-Fi bağlantısı başarılı:', wifi.ifconfig())

# Wi-Fi yapılandırma dosyası yoksa oluştur
def create_wifi_config():
    config = {
        "ssid": "SSID'inizi_Girin",
        "password": "Şifrenizi_Girin"
    }
    with open('wifi_config.json', 'w') as config_file:
        ujson.dump(config, config_file)
    print("Varsayılan Wi-Fi yapılandırma dosyası oluşturuldu.")

# Yapılandırma dosyasının mevcut olduğundan emin olun
try:
    with open('wifi_config.json', 'r') as _:
        pass
except FileNotFoundError:
    create_wifi_config()

connect_wifi()

# Ana döngü
while True:
    soil_moisture = soil_moisture_sensor.read()  # Toprak nem seviyesini oku
    water_level = water_level_sensor.read()  # Tanktaki su seviyesini oku

    if soil_moisture < moisture_threshold and water_level > water_level_threshold:
        print("Sulama başlatılıyor...")
        pump_relay.value(1)  # Su pompasını aç
        solenoid_valve.value(1)  # Solenoid vanayı aç
    else:
        print("Sulama durduruluyor...")
        pump_relay.value(0)  # Su pompasını kapat
        solenoid_valve.value(0)  # Solenoid vanayı kapat

    # Uzaktan kontrol işlevselliği ekleyin (MQTT veya HTTP sunucusu üzerinden)

    time.sleep(delay_interval)  # Yapılandırılabilir gecikme
```

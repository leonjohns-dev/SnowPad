# SnowPad

**SnowPad is a 3x4 macro pad made for the Stardance Hack Club challenge**


### Features

- 12 Switches
- RGB Backlight
- OLED Screen
- RGB Lamp
- Water Drink Reminder *Upcoming Feature*
  

## Shematic
<img width="1062" height="728" alt="image" src="https://github.com/user-attachments/assets/748c0cff-741e-467c-9010-873bffb51dd2" />

## PCB

- The PCB was designed using KiCad
- The 3d model was made using assets from Scotto Keeb's library of items
- Footprints come from KiCad and the Stardance care package

| Normal PCB View | Kicad 3D view |
| --------------- | ------------- |
| <img width="392" height="604" alt="Normal PCB View" src="https://github.com/user-attachments/assets/2e02a0ba-220d-4ff4-96fb-c425876aff74" /> | <img width="564" height="624" alt="KiCad 3D View" src="https://github.com/user-attachments/assets/ca09c24c-031c-41cc-aa15-52874b94059f" /> |


### BOM

| Part | Quantity |
| --------------- | ------------- |
| Mx Switches | 12 |
| Keycaps | 12 |
| 1N4148 Diodes | 12 | 
| SK6812MINI-E RGB LEDs | 18 |
| Seeed Studio XIAO RP2040 | 1 |
| 0.91 inch OLED display | 1 |




## CAD

- For the CAD, I am using Fusion 360 with the imported KiCad models
- The CAD consists of a bottom case and a top plate, which are both joined through 4 m3 screws and 4 heat inserts.

| Altogether | Bottom | Top Plate |
| --------------- | ------------- | ------------- | 
| <img width="557" height="515" alt="hackpadv3" src="https://github.com/user-attachments/assets/09ac291f-b562-4997-b9a8-35c73496a7ba" /> | <img width="608" height="474" alt="image" src="https://github.com/user-attachments/assets/2ba13f03-c033-4a5d-8320-8f241dd950df" /> | <img width="691" height="534" alt="image" src="https://github.com/user-attachments/assets/4bbdda4f-cf91-4af5-bad7-0f473d315516" />

 



### Case parts

| Part | Quantity |
| --------------- | ------------- |
| Top Plate | 1 |
| Bottom Container | 1 |
| M3x16mm screws | 4 | 
| M3x5mx4mm heatset inserts | 4 |


## Firmware

- Firmware took me a while to figure out😭
- I first tried QMK, but it had no 4x3 layouts; I tried making my own layout, which failed
- The current firmware is built on kmk which is pretty straightforward



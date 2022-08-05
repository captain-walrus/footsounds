# Homage to Long Walk

Installation info Danielle Giudici Wallis

## Parts:

-   Foot pedal
-   Cardboard box tower
-   Bluetooth speaker, cord and power adaptor/charging brick
-   Arduino
-   Raspberry pi with monitor power cord
-   Keyboard and usb cord
-   Screen
-   Mouse
-   Power cables
-   Breadboard
-   Jumper wires
-   mat

Pedal: Top and bottom of wooden foot pedal are pressure fit only. To assemble, align cover and cord (there is a small hole at the top for the cord); press firmly. To disassemble, lift wooden foot pedal and press firmly on wooden bottom.

![](media/930ae93b42e4ff6dfebda2787f808426.jpeg)![](media/5e81359f33621a8bcfec5fabef1ea703.jpeg)

## Arduino and bread board connections

![](media/0e11f66bb403778bc955fcfaac0951b1.jpeg)

## Bread Board diagram
![](media/a78871bb03d8279f9dfdfc51a1a97f04.jpeg)

-   Wires from Pedal to Bread Board
  -   Brown to i6
  -   Blue to i7
  -   Red to f6
  -   White to f7
  -   Black to f10
  -   resistor h7-h10

## Arduino Diagram

![](media/74e5614e5e10ee411a07eb602873b589.jpeg)

-   Red into 5V
-   Black to GND
-   White to A0; USB to USB of Raspberry Pi monitor

## Rasberry Pi connections:
![](media/630f2d592a96b0334bb0eaa5841539f8.jpeg)

-   Power supply

## Raspberry Pi connections, cont’d.
![](media/3ff5eb32cf95c2ab045cb3a4d57cf24e.jpeg)

-   Blue is cord to Arduino 
-   Red is cord to keyboard
-   Green is cord to mouse

![](media/c0a76e7f3bc4d86d3d5d0ecdc8b9f4c0.jpeg)

-   The pedal sits centered upon the dirt/pine needle mat
-   The bottom box houses all of the electronics; gently nest them inside
-   The stack of boxes fit over the bottom box
-   The top box houses the wireless speaker.
-   position the pedal in front of and slightly to the right of the stack of boxes

## Power Up / Turn Up the Bluetooth Speaker

-   Open the top box -- connect the cable to the speaker
-   Turn the speaker on (line shaped button)
-   Turn the volume up (+ button)… it will start beeping when it is all the way up

![A picture containing indoor Description automatically generated](media/cd033ab76986b529b40826126275f0ac.jpeg)![A picture containing indoor, gear Description automatically generated](media/44fb1964b04b38be6f4286c53ada27b8.jpeg)![A picture containing metalware, gear Description automatically generated](media/0ca3ecb7465315962ed656d7ab2aa141.png)![A picture containing person, indoor, hand Description automatically generated](media/f86bbadde17d954637c12000e087e967.jpeg)

## Turn on the Rasberry Pi

-   ![Graphical user interface, website Description automatically generated](media/8b8c1a2ae221b4bef02d617fbd67f5eb.jpeg)Press the Power Button (on the cord)
-   The Pi will boot up
-   This is what the home screen looks like

## Configure Pi Audio Output
![](media/a4dd12cfb0ed4c4286051766d27cfd4d.jpeg)

-   Right Click the Speaker icon
-   Select Audio Outputs
-   Select ‘Wonderboom 2’ if not already selected
1.  RIGHT Click speaker icon
2.  Select Wonderboom2
3.  If 'Wonderboom2' is not an option you'll need to go to Bluetooth Settings to connect to the speaker (see next step)

## Connect the Bluetooth Speaker
![](media/449e52fa6d25730f80b52edaf1569443.jpeg)

-   Click the BLE Icon using the mouse
-   Ensure ‘Wonderboom 2’ speaker is connected
1.  Click BLE icon
2.  Select Wonderboom2 if not already selected
## Starting the Python IDE

![Graphical user interface, website Description automatically generated](media/8a2cb73fc082581284c921036855702b.jpeg)

-   Select the Raspberry Pi button in the upper left
-   Select ‘Programming’
-   Select ‘Thony Python IDE’

## Playing the ‘newfootsounds.py’ Program

![Graphical user interface, text, application, email Description automatically generated](media/e26541c10b415a59b6e9247687eaa095.jpeg)

-   The ‘newfootsounds.py’ file should already be loaded
-   Press the green ‘Play’ button to start the script

## Playing the ‘newfootsounds.py’ Program

![Graphical user interface, text, application, email Description automatically generated](media/42bbb81ffd6f85d9edfb2f855c885cf1.png)

-   The ‘newfootsounds.py’ file should already be loaded
-   Press the green ‘Play’ button to start the script
-   Once started readings from the pedal will come in

## Testing the ‘newfootsounds.py’ Program

![Graphical user interface, text, application, email Description automatically generated](media/2687c5fc5320548cb66d0a2f0cbfc65a.jpeg)

-   The ‘newfootsounds.py’ file should already be loaded
-   Press the green ‘Play’ button to start the script
-   Once started readings from the pedal will come in
-   Test the connection by pressing the foot pedal
-   Check for sound from speaker
-   If too high turn down speaker
-   if too low turn up speaker

## Dealing with ‘newfootsounds.py’ errors

![Graphical user interface, text, application, email Description automatically generated](media/2687c5fc5320548cb66d0a2f0cbfc65a.jpeg)

-   if script stops and there is a red error message in terminal window on the bottom of the Thonny interface, press red stop button then press play button again.
-   if that doesn’t work, press stop, then close the Thonny program by clicking x in upper right corner of the application. Then restart Thonny and press play on program as described in previous slide.

## ‘newfootsounds.py’ code (read only / for reference only) .

![](media/b0941f5952eb2b7506f0cfd7cd94705d.jpeg)

[https://github.com/captain-walrus/footsounds](https://github.com/captain-walrus/footsounds/blob/main/newfootsounds.py)

## Backup .wav file for the footsounds 

![](/media/walktalk_01_16bit.wav)

## Power supply options:

-   Both the Pi and speaker can be powered via the Anker battery pack, however it will need recharging every couple of days depending on usage.
-   Alternately, the Pi and speaker can be directly plugged in via the supplied cords, however cords and outlet should be hidden beneath the shoebox tower.

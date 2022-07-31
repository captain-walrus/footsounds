# footsounds
code for the footsounds sculpture

Homage to Long Walk

Installation info Danielle Giudici Wallis

# Parts:

-   Foot pedal
-   Cardboard box tower
-   Bluetooth speaker
-   Arduino
-   Raspberry pi and monitor
-   Keyboard
-   Screen
-   Mouse
-   Power cables
-   Breadboard
-   Jumper wires

Pedal: Top and bottom of wooden foot pedal are pressure fit only. To assemble, align cover and cord (there is a small hole at the top for the cord); press firmly. To disassemble, lift wooden foot pedal and press firmly on wooden bottom.

![](media/a16a7c2753d4bb3b9818c5f19fc764ce.jpeg)![](media/9e874c0f38db6f5c142ee892c9ccc53c.jpeg)

# Arduino and bread board connections

![](media/97d7a7b4b75ffe46032afd7142476048.jpeg)

![](media/24a9987f6dc1457b19797dbebd03e6b0.jpeg)Bread Board diagram

Wires from Pedal to Bread Board: Brown to i6; Blue to i7; Red to f6; White to f7; Black to f10; resistor h7-h10

Arduino Diagram

![](media/e9511b947c517291e9516cc5023b7918.jpeg)

Red into 5V; Black to GND; White to A0; USB to USB of Raspberry Pi monitor

# ![](media/585edfa7201f65718c6f6cdcab8aad9d.jpeg)Rasberry Pi connections:

Top: Power supply

# ![](media/88fd71bc04891e7f71499b07ab8820ef.jpeg)Raspberry Pi connections, cont’d.

Right Side:

Blue is cord to Arduino Red is cord to keyboard Green is cord to mouse

-   The stack of boxes fits over the bottom box which houses all of the electronics
-   The top box houses the wireless speaker

# Power Up / Turn Up the Bluetooth Speaker

-   Open the top box -- connect the cable to the speaker
-   Turn the speaker on
-   Turn the volume up … it will start beeping when it is all the way up

![A picture containing indoor  Description automatically generated](media/71de6cdeb968de97d0231bfe9fa36e2e.jpeg)![A picture containing indoor, gear  Description automatically generated](media/aa29a1a28e61b245f3b864a884d41e3b.jpeg)![A picture containing metalware, gear  Description automatically generated](media/ea5c26ff772d23cc99255a2a7f722ce0.jpeg)![A picture containing person, indoor, hand  Description automatically generated](media/37e07c41c1e8dd8bd29912991ec4af1c.jpeg)

# Turn on the Rasberry Pi

![Graphical user interface, website  Description automatically generated](media/1c67c593c44b3bf34f104dc7fc6b1e2d.jpeg)
-   Press the Power Button
-   The Pi will boot up
-   This is what the home screen looks like

# Connect the Bluetooth Speaker
![](media/c831d1d5c569bea4d44d100a1bddb86b.jpeg)

-   Click the BLE Icon
-   Ensure ‘Wonderboom 2’ speaker is connected
1.  Click BLE icon
1.  Select Wonderboom2 if not already selected

# ![](media/e28e5055d07042d9edf6f452af0127d6.jpeg)Configure Pi Audio Output

-   Right Click the Speaker icon
-   Select Audio Outputs
-   Select ‘Wonderboom 2’ if not already selected
1.  RIGHT Click speaker icon
1.  Select Wonderboom2

# Starting the Python IDE

-   ![Graphical user interface, website  Description automatically generated](media/71c3d3f29de7ebfde3bd6d44d229db2d.jpeg)Select the Pi button in the upper left
    -   Select ‘Programming’
        -   Select ‘Thony Python IDE’

# Playing the ‘newfootsounds.py’ Program

-   ![Graphical user interface, text, application, email  Description automatically generated](media/dd68d4d4c75141bc4cede7c0c8897fd9.jpeg)The ‘newfootsounds.py’ file should already be loaded
    -   Press the green ‘Play’ button to start the script

# Playing the ‘newfootsounds.py’ Program

-   ![Graphical user interface, text, application, email  Description automatically generated](media/0d91dc16f82c4c7365662d830e94fad4.png)The ‘newfootsounds.py’ file should already be loaded
    -   Press the green ‘Play’ button to start the script
        -   Once started readings from the pedal will come in

# Testing the ‘newfootsounds.py’ Program

-   ![Graphical user interface, text, application, email  Description automatically generated](media/234409bbfafb2525e9ae9f1ed8c66a84.jpeg)The ‘newfootsounds.py’ file should already be loaded
    -   Press the green ‘Play’ button to start the script
        -   Once started readings from the pedal will come in
        -   Test the connection by pressing the foot pedal
        -   Check for sound from speaker
        -   If too high turn down speaker
        -   if too low turn up speaker

# ‘newfootsounds.py’ code

-   ![](media/7a9dd8e8c16022a50477cef73fef0870.jpeg)The ‘newfootsounds.py’ file should already be loaded
    -   Press the green ‘Play’ button to start the script
        -   Once started readings from the pedal will come in
        -   Test the connection by pressing the foot pedal
        -   Check for sound from speaker
        -   If too high turn down speaker
        -   if too low turn up speaker

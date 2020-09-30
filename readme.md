# Circuitry-Based Sound

"Circuitry-Based Sound" is an ongoing seminar at [University of Arts and Design Karlsruhe](https://www.hfg-karlsruhe.de/ "University of Arts and Design Karlsruhe"). It focuses on electronic sound synthesis and parametric interfacing. It's examining musical characteristics of electronic instruments and comparing different approaches on how to design electronic sound modules. Due to the measures against the coronavirus spread in 2020, the seminar’s workflow had been adapted to the restrictions and is held on-line.

Based on previous's semesters studies of logic chips for sound creation and its musical applications, the course focused on computer aided circuit design and professional PCB manufacturing processes to build custom-made instruments. Participants were guided to use the latest technology, production chain and global logistics to develop, design and produce circuit boards for musical use. This allowed the participants to easily create circuit boards with more variable features and adjustable parameters than hand soldered protoboards or solderless breadboards. During the seminar, several experimenter boards for CMOS logic chips were conceived and built. The boards were used for a live performance in front of the Federal Prosecutor's office in Karlsruhe. The developement of this project is documented here.


# Unconventional Electronic Sound
## Classical Sound Synthesis

Aside from the established way of using electronics to generate and process sound, which can be found in analog synthesizers, there are also unconventional applications of electronics to create sound or experimental music, which will be introduced below. Analog synthesizers apply techniques like subtractive synthesis to produce audio. A common concept of the analog signal flow is filtering the output of an oscillator and shaping the overall volume. Variations of this concept can be found in most synthesizers, both analog and digital. Parameters can be altered through control signals. This offers a wide range of musical expression, like tuning oscillators in a 12-tone musical scale or key triggered envelopes for amplifiers, filters or other effect processors. To obtain these functionalities, circuits of analog synthesizers are relatively complex, involve a high part count and often require precision components.

## CMOS Chips for Sound Creation

Another concept of creating sound with electronics derived from techniques like hardware hacking and circuit bending. Especially the use of digital integrated logic circuits outside of their typical field of application is a remarkable approach to build customized instruments for artistic sound production and interactive music. The required components are easy to source and low cost.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CMOS-chips.jpg">

[CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute boolean functions. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like NOT, AND, OR, NAND, XOR, XNOR or implement multiplexers, counters, dividers and registers. When logical operations and their relation to voltage and sound are understood, CMOS-logic chips are an inexhaustible source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced and many more. Combining different logic functions allows generating a multitude of unique sounds and temporal music structures, while they produce the richness of analog sound. These circuits also yield unpredictable behavior, produce rhythmic glitches or digital noise.

Due to its simplicity, CMOS chips can be used for educational reasons, since most of its technical operations can easily be understood and relate to basic electronic knowledge. This subject is also a matter of various publications, most notably Nicolas Collins' „Handmade Electronic Music, The Art of Hardware Hacking" (2006). American Composer David Tudor (1926 - 1996) is considered a pioneer of self-made electronic circuits and instruments, which he used for his compositions.

## Basic Example of Unconventional Synthesis

The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the following picture:

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Basic_Oscillator_CD40106.jpg">

It shows a square wave sound generator that can be built with only three components:  
* inverting Schmitt trigger IC, e.g. CD40106
* capacitor C
* resistor R

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, while the positive trigger threshold differs from the negative one. Feeding back the output voltage to its input and connecting the input via a capacitor to ground creates a relaxation oscillator or astable multivibrator.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/ST_inv.gif">

The frequency can be roughly calculated with this formula:

f=0,72/RC

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear. But the formula shows that bigger RC values produce lower frequencies and vice versa.


The frequency is determined through the capacitor C and the resistor R. Therefore, a potentiometer instead of the latter enables pitch control. Other ways of controlling the frequency may be inserting photoresistors, force-sensitive resistors (FSR) or flex sensors. Adding circuit points to alter the sound through interaction allows building customized and versatile instruments. 


## CMOS Experimenter Board

The motivation behind this project is to offer a set of PCBs to evaluate logic ICs for sound creation and composition in artistic and educational fields. The idea of providing a CMOS experimenter board was initiated particularly with regard to todays availability of PCB manufacturers and affordable prizes. PCB prototyping and production is now completely based on computer aided electronic design (EDA) while manufacturers offer professional quality at very low costs, even for small board quantities.

Each PCB is designed around individual standard CMOS chips and their particular functions in order to create sound. The boards provide inlets and outlets, testing points, sockets, vias and pads for changing values of electronic parts and wiring alternative external circuitry. The modules can be easily extended and interconnected. This allows the user to manipulate circuit points with potentiometers, buttons, switches or sensors and to apply control voltages at appropriate input points.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CMOS_Synthesizer.jpg">

It simplifies prototyping and makes customized configurations highly flexible. The experimenter boards can serve as sound modules for interactive music in live performance or installative environments as well as for algorithmic compositions. By combining several boards with different logic functions, complex switching performance can be achieved, ranging from  modulated frequencies and interesting audio spectra to slow, rhythmic pulses or tone sequences. For interconnecting the boards, jumper cables can be used as patch cords. A wide range of circuit examples with CMOS chips can be found on DIY websites and are a subject of discussion in various internet forums. These circuits can be a good basis for experimenting with CMOS chips. In addition, it is recommendable to use data sheets for all active components used in electronic projects.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Experimenter_Modules.jpg">

Furthermore, the project includes laser-cutting files for a console on which the modules can be mounted. [...] intended for musical performance. The frame's surface has mounting holes for the experimenter boards and for power distribution.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/acrylic_transparent.jpg">

All involved files are made available online. This includes [ECAD](https://github.com/SCLW/Circuitry-Based-Sound/tree/master/PCB_Hardware/Schematics "Schematics"), [Gerber](https://github.com/SCLW/Circuitry-Based-Sound/tree/master/PCB_Hardware/Schematics "Gerber") and [vector files](https://github.com/SCLW/Circuitry-Based-Sound/tree/master/Case "Case") as well as [bill of materials](https://github.com/SCLW/Circuitry-Based-Sound#bill-of-material "BOM").


### Logic Control


Some basic information about digital electronics may act as a short introduction. 

In digital electronics, binary numbers are represented by two defined voltage levels that are specified by the used technology and circuit. For example signal ground in a given circuit can represent "0" while the positive voltage rail can represent "1". The two states "0" and "1" are also often referred to as "(logical) high" and "(logical) low", "true" and "false" or "ON" and "OFF".

A logic gate is a single input - output device, designed to carry out a specific boolean operation, mapped to two voltage levels. Over time, the two  alternating voltage levels may form a periodical rectangular waveform and the speed of switching between the two levels is perceived as pitch. Aperiodical switching will produce other sonic qualities such as noise or all kinds of texturized sounds. The ratio between the on-and-off states is by default 1:1, a 50% duty cycle. Further circuitry is needed to change this ratio, which alters the audio spectrum of the square wave.



### Power Supply

Power supply for the boards should comply with the power ratings of the used ICs, which is typically between 3V - 18V DC. LED series resistors need to be calculated accordingly. For the experimenter console, 9V power supply for guitar effects work well.


### PCB Sizes

76mm (length) x 76mm (wide)
Mounting holes: 66mm x 66mm
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/SIZE.jpg>


## CD40106

The inverter is a basic part in digital electronics and performs the logic operation of negation. When the input is connected to ground, the output is pulled to V<sub>DD</sub> and vice versa. The CD40106 hex Schmitt trigger inverter offers six separate inverters in one chip that can be wired externally to build square wave oscillators. The board allows to insert an offset resistor for use with potentiometers in order to prevent zero resistance between output and input.

*Applications:*
* oscillator

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106.jpg>

Truth table
|Inputs|Outputs|
|----|----|
|0|1|
|1|0|

"1" = High Level  
"0" = Low Level



<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106_Board.jpg>

[CD40106 Data Sheet](https://www.ti.com/lit/ds/symlink/cd40106b.pdf?ts=1599062729936&ref_url=https%253A%252F%252Fwww.google.com%252F "CD40106")

## CD4093

The CD4093 contains 4 NAND Schmitt triggers, each providing 2 inputs and 1 output. 

It acts as a square wave oscillator when the inputs are connected to form an inverter. The last two rows of the truth table indicate that one input has to be set to a logical high in order to attain inversion. When the second input is wired like the CD40106, the CD4093 generates square waves too. Bringing the first one down to a logical low, inhibits oscillations. A break out section allows for logic control of the first input of each NAND gate. Therefore, gating the output can be achieved by controlling the first input with another digital signal, square wave or a simple switch.

*Applications:*
* gated oscillator

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093.jpg>

Truth table for NAND

|A|B|J=A NAND B|
|----|----|:----:|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|



<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093_Board.jpg>


[CD4093 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4093b.pdf?ts=1599062791398&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4093")


## CD4022

CD4022 IC implements a binary counter/divider function. The positive edge of an incoming square wave, usually referred to as "clock signal", triggers successively the outputs. "Carry out" is outputting one cycle over 8 clock pulses.

*Applications:*
* counter
* wave shaper and staircase wave form generator
* sequencer

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022.jpg>



<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_Timing_Diagram.jpg>

[CD4022 Data Sheet](https://www.ti.com/lit/ds/schs027c/schs027c.pdf?ts=1599062824246&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4022")

## CD4040

This IC performs frequency division. If a square wave is applied to the input, each output creates square waves at half the frequency of its preceeding output, at which the first output Q1 applies its division to the input signal and oscillates at a rate at one half, Q2 at one quarter, Q3 at one eighth Q4 at one sixteenth and so on.

Control input "reset" triggers all output stages to "low". For continuously frequency division it should be kept at a logical low.

*Applications:*
* subharmonic oscillator

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040.jpg>


Each output producing one octave lower than its previous output, respectivly input.

[CD4040 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4040b.pdf?ts=1600261370155&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4040B "CD4040")

The timing diagram shows the relation of voltage levels between all outputs of the CD4024 IC, a 7 output stage version:
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_Timing_Diagram.jpg>

## CD4046


Phase locked loop

*Applications:*
* tone distortion
* pitch tracking
* frequency multiplication


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4046.jpg>

[CD4046 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4046b.pdf?ts=1599062962750&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4046")


## CD4051

Multiplexer/Demultiplexer

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4051.jpg>

Truth table
|C|B|A|ON CHANNEL(S)|
|----|----|----|:----:|
|0|0|0|0|
|0|0|1|1|
|0|1|0|2|
|0|1|1|3|
|1|0|0|4|
|1|0|1|5|
|1|1|0|6|
|1|1|1|7|

[CD4051 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4051b.pdf?ts=1599079621658&ref_url=https%253A%252F%252Fwww.google.com%252F "CD405xB")



## Mixer

There are several ways of mixing signals together. Passive mixing is a very simple method that can be accomplished by using diodes or resistors for each source. 
To avoid interaction between the signals and to obtain individual gain control, active mixing using an operational amplifier is preferred.
An op amp is another class of active electronic component. Its purpose and function is out of the scope of this documentation. The basic wiring is shown below. Besides it function as a mixer with gain control over every individual input by adding voltage dividers, it can also be used to achieve a desired output gain by modifying the the feedback resistor R<sub>F</sub> in relation to the input resistors R<sub>IN</sub> of each input. The minus sign in the formula indicates that the output voltage is inversed. To undo inversion, a second stage following the shown circuit can be used.

*Applications:*
* signal mixing
* gain control

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Summing_Inverting_OpAmp.jpg>

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Summing.jpg>



## Bill of Material

In the following are examples of parts and values, that can be used for this project.
All parts can be substituted with alternative components and same packages or foot prints.




No|Description|Package/Pitch|Value|Manufacturer Part Number|Mouser-Nr.
 --- | --- | --- | --- |--- | --- 
1|Inverter Hex Schmitt Trigger|DIP-14||CD40106BE|[595-CD40106BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD40106BE?qs=YhsVCygOPE1CyKyInx%252Bh3Q%3D%3D&gclid=EAIaIQobChMIgtOchp_K6wIVBt-yCh0zXgXAEAAYASAAEgIDAPD_BwE/ "CD40106BE")
2|Counter IC CMOS Octal Counter|DIP-16||CD4022BE|[595-CD4022BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD4022BE?qs=LU5rZWrBGo2Wnh%252BM60ZqEA%3D%3D "CD4022")
3|Counter IC 10 Decade/Divider|DIP-16||CD4017BE|[595-CD4017BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD4017BE?qs=IF4wzcbwb3rdXSZhHlgcJw%3D%3D "CD4017")
4|NAND Logic Gates Schmitt Trigger|DIP-14||CD4093BE|[595-CD4093BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD4093BE?qs=X1HXWTtiZ0QxcrKuDdZ5rg%3D%3D "CD4093")
5|Phase Locked Loop|DIP-16||CD4046BE|[595-CD4046BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD4046BE?qs=fvkeCqCHl3AX2sxIYB2bdg%3D%3D "CD4046")
6|Dual Op Amp|DIP-8||TL072IP|[595-TL072IP](https://www.mouser.de/ProductDetail/Texas-Instruments/TL072IP?qs=5BZzbFV4k2v7IBrcArRPQw%3D%3D "TL072")
7|Dual Op Amp|DIP-8||LM358P|[595-LM358P](https://www.mouser.de/ProductDetail/Texas-Instruments/LM358P?qs=X1HXWTtiZ0QtOTT8%252BVnsyw%3D%3D "LM358")
8|Component Sockets|DIP-8||1-2199298-2|[571-1-2199298-2](https://www.mouser.de/ProductDetail/TE-Connectivity/1-2199298-2?qs=%2Fha2pyFadugJp%2F0oQpeWgcdKbmhfM%252BG5f2aD9jt0RGQdskDEwvmLNQ%3D%3D "Component Sockets 8P DIP")
9|Component Sockets|DIP-14||1-2199298-3|[571-1-2199298-3](https://www.mouser.de/ProductDetail/TE-Connectivity/1-2199298-3?qs=%2Fha2pyFadugJp%2F0oQpeWgR9Lzm5j4WzFAMc1jcrVNfu7vZxg2U3Y3Q%3D%3D "Component Sockets 14P DIP")
10|Component Sockets|DIP-16||1-2199298-4|[571-1-2199298-4](https://www.mouser.de/ProductDetail/TE-Connectivity/1-2199298-4?qs=%2Fha2pyFadugJp%2F0oQpeWgVBpv3LzMBBwVqoB59rQ35Apde3oZfgpGA%3D%3D "Component Sockets 16P DIP")
11|Photoresistor|||161|[485-161](https://www.mouser.de/ProductDetail/Adafruit/161?qs=GURawfaeGuDpQ5XPTNqKUw%3D%3D "Photoresistor")
12|Photoresistor|||SEN-09088|[474-SEN-09088](https://www.mouser.de/ProductDetail/SparkFun/SEN-09088?qs=WyAARYrbSnbNBfpKra%2FIvQ%3D%3D "Photoresistor")
13|Force Sensitive Resistor|||1075|[485-1075](https://www.mouser.de/ProductDetail/Adafruit/1075?qs=GURawfaeGuDaOmXus2Zwlg%3D%3D "Force Sensitive Resistor")
14|Aluminum Electrolytic Capacitors|2mm |10µF|ECE-A1HKA100I|[667-ECE-A1HKA100I](https://www.mouser.de/ProductDetail/Panasonic/ECE-A1HKA100I?qs=rMMd5vBiahpRBI%252BQ5jocrQ%3D%3D "Aluminum Electrolytic Capacitors")
15|MLCC|2.5mm |0.1µF|K104K15X7RF53K2|[594-K104K15X7RF53K2](https://www.mouser.de/ProductDetail/Vishay-BC-Components/K104K15X7RF53K2?qs=%2Fha2pyFadujQ%252Bv0xHOEo91Fp6rFGP5krxuyVhQ%252B1w%252BsnJ7knhvdeQDps3CPFUP6U "Keramik-Vielschichtkondensator MLCC")
16|Jumper Cable|15cm||MIKROE-513|[932-MIKROE-513](https://www.mouser.de/ProductDetail/932-MIKROE-513 "Jumper Cable")
17|Pin Header|1 x 36 2.54mm ||10129378-936002BLF|[649-1012937893602BLF](https://www.mouser.de/ProductDetail/649-1012937893602BLF "Sockel & Kabelgeh√§use ECONOSTIK HEADER SR VT TH 1X36")
18|Pin Header|1 x 36 2.54mm ||68797-436HLF|[649-68797-436HLF](https://www.mouser.de/ProductDetail/649-68797-436HLF "Sockel & Kabelgeh√§use BREAKAWAY HEADER 36")
19|Pin Socket|1 x 8 2.54mm ||8Fx1L-254mm|[992-8FX1L-254MM](https://www.mouser.de/ProductDetail/992-8FX1L-254MM "8-pin wire wrap fem header")
20|Pin Socket|1 x 32 2.54mm ||61303211821|[710-61303211821](https://www.mouser.de/ProductDetail/710-61303211821 "2.54mm 32Pin Socket Header")
21|Pin Socket|1 x 36 2.54mm ||801-87-036-10-001101|[437-8018703610001101](https://www.mouser.de/ProductDetail/437-8018703610001101 "Sockel & Kabelgeh√§use")
22|Socket||1 Row 21 Positions|801-83-021-10-001101|[437-8018302110001101](https://www.mouser.de/ProductDetail/Preci-dip/801-83-021-10-001101?qs=FtMuP6KVi2SB4UyszASQfQ%3D%3D "Headers & Wire Housings")
23|3mm LED||Blue|151033BS03000|[710-151033BS03000](https://www.mouser.de/ProductDetail/Wurth-Elektronik/151033BS03000?qs=2kOmHSv6VfSefdpzrMLWSw%3D%3D "Standard LEDs - Through Hole WL-TMRW THT Mono Waterclr Rnd 3mmBlue")
24|3mm LED||Red|LTL-4222|[859-LTL-4222](https://www.mouser.de/ProductDetail/Lite-On/LTL-4222?qs=PaUBgWdAOGEl%252Bf85PeEXqA%3D%3D "Standard LEDs - Through Hole Red Transparent")
25|3mm LEDs||Assorted Values|COM-12062|[474-COM-12062](https://www.mouser.de/ProductDetail/SparkFun/COM-12062?qs=WyAARYrbSnZzv4I0CztaEg%3D%3D "SparkFun Accessories LED - Assorted (20 pack)")
26|Leaded Resistors (Metal or Carbon Film)|| Assorted Values (12 Ω - 1 MΩ) ||
27|Leaded Capacitors (Ceramic, Film and Electrolytic)|| Assorted Values (56pF - 47µF)||
28|Push Button|5,9mm|OFF - (ON)|1-1825910-4|[506-1-1825910-4](https://www.mouser.de/ProductDetail/TE-Connectivity-PB/1-1825910-4?qs=pffCcXpkxLwYJJd3DYaJ7Q%3D%3D "Tactile Switches 6MM ACTHIGH TEMP TACT SWITCH")
29|Potentiometer|9mm|10kΩ|PTV09A-6230F-B103|[652-PTV09A-6230FB103](https://www.mouser.de/ProductDetail/Bourns/PTV09A-6230F-B103?qs=pxDZlBjcsCg8U96haor%252BfA%3D%3D "Potentiometers PANEL CONTROL - 9MM-ST-CARBON 10 kohms 30 mm")
30|Potentiometer|9mm|20kΩ|PTV09A-1015U-B203|[652-PTV09A-1015UB203](https://www.mouser.de/ProductDetail/Bourns/PTV09A-1015U-B203?qs=pxDZlBjcsCjw%252BRGNXMHqEQ%3D%3D "Potentiometers PANEL CONTROL - 9MM-ST-CARBON 20 kohms 15 mm")
31|Potentiometer|9mm|50kΩ|RK09D113000K|[688-RK09D113000K](https://www.mouser.de/ProductDetail/Alps-Alpine/RK09D113000K?qs=oKW7zmyQiO5%2FMNsP8zcsfA%3D%3D "Potentiometers 9MM 50K V/ADJ")
32|Potentiometer|9mm|100kΩ|PTV09A-4015U-B104|[652-PTV09A-4015UB104](https://www.mouser.de/ProductDetail/Bourns/PTV09A-4015U-B104?qs=pxDZlBjcsCi2tw983aFXVQ%3D%3D "Potentiometers PANEL CONTROL - 9MM-ST-CA 100 kohms 15 mm")
33|Potentiometer|9mm|500kΩ|PTV09A-4015U-B504|[652-PTV09A-4015UB504](https://www.mouser.de/ProductDetail/Bourns/PTV09A-4015U-B504?qs=pxDZlBjcsCherlTtJcuegw%3D%3D "Potentiometers PANEL CONTROL - 9MM-ST-CA 500 kohms 15 mm")
34|Potentiometer|9mm|1MΩ|PTV09A-4020F-B105|[652-PTV09A4020FB105](https://www.mouser.de/ProductDetail/Bourns/PTV09A-4020F-B105?qs=%252B9%2Fcbd0IE0TagBKq%252BGRbqw%3D%3D "Potentiometers 1M 20% 9MM CARBON POT")
35|Diode|DO-35	||1N4148|[512-1N4148](https://www.mouser.de/ProductDetail/ON-Semiconductor-Fairchild/1N4148?qs=i4Fj9T%2FoRm8RMUhj5DeFQg%3D%3D "Dioden (Allzweck, Leistung, Schaltung) 100V Io/200mA BULK")
 
## Requirements

The workshop requires some tools and materials

* Good light.
* Small mixing desk.
* Loudspeaker.
* Worktables.
* Screw drivers.
* ESD electronic diagonal cutter.
* Precision cutter.
* Stranded wires.
* Laboratory power supply + connectors (preferable 4mm banana laboratory connectors).
* Jumper cables and jumper wires.
* Digital multimeter (DVM).
* Digital storage oscilloscope (DSO).
* Temperature-controlled soldering station.
* Breadboards.



## Authors

Zhen Bian  
Hangyan Chen  
Jeongmin Han  
Anna Helsen  
Jihye Jang  
Xingchen Liu  
Su Lu  
Ruoyi Qiu  
Vivian Reuter  
Christina Vinke  
Yunfei Zhang  

**Lorenz Schwarz** - *lecturer* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgment

* Thanks to Dr. Paul Modler

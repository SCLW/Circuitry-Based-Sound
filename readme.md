# Circuitry-Based Sound

Circuitry-Based sound is an ongoing seminar at [University of Arts and Design Karlsruhe](https://www.hfg-karlsruhe.de/ "University of Arts and Design Karlsruhe"). 

It focuses on electronic sound synthesis and parametric interfacing. It's examining musical characteristics of electronic sound generators and processors and comparing different approaches on how to design electronic sound modules. Due to the measures against the coronavirus spread in 2020, the seminar’s workflow had been adapted to the restrictions and therefore was hold on-line.

Based on previous's semesters studies of logic chips for sound creation and its musical applications, the course focused on computer aided circuit design and professional PCB manufacturing processes to build custom-made instruments. Participants were guided to use the latest technology, production chain and global logistics to develop, design and produce circuit boards for musical use. This allowed the participants to easily create circuit boards with more variable features and adjustable parameters than hand soldered protoboards or breadboards. During the seminar, several experimenter boards for CMOS logic chips were designed and documented.

# Unconventional Electronic Sound
## Classical Sound Synthesis

Besides the established ways of using electronics to synthesize sound, which can be found in analog synthesizers, there are also unconventional applications of electronics to create sound or experimental music, which will be introduced below. Analog synthesizers apply techniques like subtractive synthesis to generate audio. A common concept of the analog signal flow is filtering the output of an oscillator and shaping the overall volume. Variations of this concept can be found in most synthesizers, both analog and digital. Various parameters can be altered through control signals, which offer a wide range of musical expression, like tuning oscillators in a 12-tone musical scale or key triggered envelopes for volume, filters or other effect processors. To obtain these functionalities, circuits of analog synthesizers are relatively complex, involve a high part count and require often precision components.

## CMOS Chips for Sound Creation

Another concept of creating sound with electronics derived from techniques like hardware hacking and circuit bending. Especially the use of digital integrated logic circuits outside of their typical field of application is a remarkable approach to build customized instruments for artistic sound production and interactive music. The required components are easy to source and low cost. This makes it also interesting for multichannel sound creation and processing.

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CMOS-chips.jpg">

[CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute boolean functions. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like NOT, AND, OR, NAND, XOR, XNOR or implement multiplexers and registers. When logical operations and their relation to voltage and sound are understood, CMOS-logic chips are an inexhaustible source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced and many more. Combining different logic functions allows generating a multitude of unique sounds. These circuits yield a high variability and a wide range of control parameters, [...] including randomness, while they produce the richness of analog sound. Due to its simplicity, the unconventional approach of building electronic sound systems can be used for educational reasons, since most of its technical operations can easily be understood and relate to basic electronic knowledge. This subject is also a matter of various publications, most notably Nicolas Collins' „Handmade Electronic Music, The Art of Hardware Hacking" (2006). American Composer David Tudor (1926 - 1996) is considered a pioneer of self-made electronic circuits and instruments, which he used for his compositions.

unpredictable behavior
-> sonically rewarding.
Rhythmic glitches, slow clicking sounds, digital noise, rich overtones,


## Basic Example of Unconventional Synthesis

The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the following picture:

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/Basic_Oscillator_CD40106.jpg">

It shows a square wave sound generator that can be built with only three components:  
* inverting Schmitt trigger IC, e.g. CD40106
* capacitor C
* resistor R

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, whereas the positive trigger threshold differs from the negative trigger threshold. Feeding back the output voltage to its input and tying the input via a capacitor to ground creates a relaxation oscillator or astable multivibrator.

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/ST_inv.gif">

The frequency can be roughly calculated with this formula:

f=0,72/RC

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear. But the formula shows that bigger RC values produce lower frequencies and vice versa.


Since the frequency is determined through the capacitor C and the resistor R, a potentiometer instead of the latter enables pitch control. Other ways of controling the frequency may be a photoresistor, force-sensitive resistor (FSR) or flex sensor. Adding circuit points to alter the sound through interaction allows building customized and versatile instruments. The above example is documented in the IC's data sheet. It's recommendable to use data sheets for all active components used in projects.


## CMOS Experimenter Board

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CD4093_PCB.jpg">

Prizes for professionally produced PCB are affordable

The motivation behind this project is to offer a set of building blocks to evaluate logic ICs for sound creation and composition in artistic and educational fields. 

With todays availability of PCB manufactureres, there is no need for making your own PCB, which usually includes toxic chemical products for etching and developing as well as manual steps like drilling and cutting, which all results only in very rough designs. PCB prototyping and production is now completly based on computer aided electronic design (EDA) while cost effective manufacturers offer professional quality even for small board quantities at very low costs. 

Each building block is designed around individual standard CMOS chips and their particular functions under the (for sound) . The boards provide inlets and outlets, testing points, sockets, vias and pads for changing values of electronic parts and alternative external wirings. The modules can be easily extended and interconnected. This allows the user to manipulate circuit points with potentiometers, buttons, switches or sensors and to apply control voltages at appropriate input points. It simplifies prototyping and makes customized configurations highly flexible.

Additionally, as a part of this project, a mounting system...
for mounting the PCBs is available... files
Jumper cables can be used as patch cords
interface and control
The boards are provided with mounting holes that match the according case. Jumper cables can be used as patch cords.

The experimenter boards can serve as sound modules for interactive music in live performance or installative environments as well as for algorithmic compositions.

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/Experimenter_Modules.jpg">

-> all files, EGALE .brd .sch, Gerber files are available online 

unconventional circuits for sound with CMOS chips can be found in internet forums or DIY pages. These circuits can be the basis


table of content
### Logic Control

In digital electronics, binary numbers are represented by two defined voltage levels that are specified by the used technology and circuit. For example signal ground in a give circuit can represent "0" while the positive voltage rail can represent "1". The two states "0" and "1" are also often referred to as "(logical) high" and "(logical) low", "true" and "false" or "ON" and "OFF".

A logic gate is a single input - output device, designed to carry out a specific boolean operation, mapped to two voltage levels. Over time, the two alternating voltage levels form a rectangular waveform and the speed of switching between the two levels is perceived as pitch. By combining several logic functions, complex switching performance can be achieved, ranging from  modulated frequencies and interesting spectras to slow, rhythmic pulses oder repeating tones or scales (gated). or sequences

IMAGE Oscilloscope SQUAREWAVE with EXPLANATION



rectangular waveforms or square waves have a distinct sound
duty cycle


Example: NOR
Voltage controlled inputs


active low - active high


external wiring

unused inputs

pull-up resistor or pull-down resistor

### Experimenter console

The case offers a surface with mounting holes for the experimenter boards

<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CMOS_Synthesizer.jpg">


<img src="https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/acrylic_transparent.jpg">
©Zhen Bian

### Power Supply

Power supply for the boards should comply with the power ratings of the used ICs, which is between 3V - 18V. LED series resitors need to be calculated accordingly. For the experimenter console, 9V power supply for guitar effects work well.


### Tool Requirements

For more details on


### PCB Sizes

76mm (length) x 76mm (wide)
Mounting holes: 66mm x 66mm
<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/PCB_Size.jpg>

## CD40106

<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CD40106.jpg>

The CD40106 hex Schmitt trigger inverter offers six seperate inverters in one chip that can be wired externaly to generate square waves. The board allows to setup an offset resistor for use with potentiometers in order to prevent zero resistance between output and input and can be populated alternatively with photoresistors. Furthermore, LEDs and photoresistor can be used and the LED can control the frequency via a light sensitive resistor.

Truth table
|Inputs|Outputs|
|----|----|
|0|1|
|1|0|

[CD40106 Data Sheet](https://www.ti.com/lit/ds/symlink/cd40106b.pdf?ts=1599062729936&ref_url=https%253A%252F%252Fwww.google.com%252F "CD40106")

## CD4093

The CD4093 contains 4 NAND Schmitt triggers, each providing 2 inputs and 1 output. It is outputting square waves when the first input is set to a logical high and the second input is wired as the CD40106. Bringing the 1 input down to a logical low, inhibits oscillations. Therfore, gating the ouput can be achieved by controlling the first input with another digital signal, square wave or a simple switch for the input pin fo changing between power or signal ground. Bringing the first input to high via a push button works like a keyboard.

<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CD4093.jpg>

Truth table for NAND

|A|B|J=A NAND B|
|----|----|:----:|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|

The last two rows of this truth table indicate that the first inputs needs to be set to high to make the CD4093 work as an astable mutlivibrator when the output is fed back to its second input which is additionaly connected to ground via a capacitor. It's basicilly the same operation as the inverter configuration.

[CD4093 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4093b.pdf?ts=1599062791398&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4093")

## CD4022



<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CD4022.jpg>

counter, waveshaper, Reset function

[CD4022 Data Sheet](https://www.ti.com/lit/ds/schs027c/schs027c.pdf?ts=1599062824246&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4022")

## CD4040

<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CD4040.jpg>

(quoted) The 4040 is a binary counter / divider. 
. It has a single input. 
Control input Reset should be kept low
If a square wave is applied to this input, the outputs (labelled Q1 to Q12) each oscillate at a rate related to the input freqeuncy. 

(quoted) Q1 oscillates at a frequency that is half of the input frequency. Q1 at one quarter. Q3 at one eighth and so on. If the output frequencies are within the human hearing range, they will sound one octave apart - with Q1 being the highest and Q12 being the lowest (eleven octaves below Q1).

[CD4040 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4040b.pdf?ts=1600261370155&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4040B "CD4040")

The timing diagram shows the relation of voltage levels between all outputs:


## CD4046

<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CD4046.jpg>
Phase locked loop

[CD4046 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4046b.pdf?ts=1599062962750&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4046")

## CD4049

<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CD4049.jpg>
note: power supply pins

Hex Inverting Buffer and Converter

Truth table
|Inputs|Outputs|
|----|----|
|0|1|
|1|0|

## CD4051

Multiplexer/Demultiplexer

<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/CD4051.jpg>

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

<img src=https://github.com/clswa/Circuitry-Based-Sound/blob/master/img/Summing_Inverting_OpAmp.jpg>

There are severaly ways of mixing signals together. Passive mixing is a very simple method that can be accomplished by using diodes or resitors for each source. 
To avoid interaction between the signals and to obtain individual gain control, active mixing using an operational amplifier is preferred.
An opamp is another class of active electronic component. Its purpose and function is out of the scope of this documentation. The basic wiring is shown below. Besides it function as a mixer with gain control over every individual input by adding voltage dividers, it can also be used to achieve a desired output gain by modifying the the feedback resistor in relation to the input resistors of each input. The minus in the formula indicates its inversed voltage level. To undo inversion, a second stage following the shwon circuit can be used.

In this contxt, when the signal level is close to the operating voltage level, distortion might quite likely occure when adding several CMOS signals. When the signal level excesses the supply voltage of the op amp. Voltage divider (potentiometers) before the Rin might solve that problem. Otherwise, lowering the value of Rf in relation to Rin would also reduce the level.


## Trigger Board

A PCB with push buttons for setting inputs to high or low


## Bill of Material

examples of parts, but not limited to.
as long as the packages fit or the pitch is..
A of required components.

Potentiometers
Switches


No|Description|Package/Pitch|Value|Manufacturer Part Number|Mouser-Nr.
 --- | --- | --- | --- |--- | --- 
1|Inverter Hex Schmitt Trigger|DIP-14||CD40106BE|[595-CD40106BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD40106BE?qs=YhsVCygOPE1CyKyInx%252Bh3Q%3D%3D&gclid=EAIaIQobChMIgtOchp_K6wIVBt-yCh0zXgXAEAAYASAAEgIDAPD_BwE/ "CD40106BE")|
2|Counter IC CMOS Octal Counter|DIP-16||CD4022BE|[595-CD4022BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD4022BE?qs=LU5rZWrBGo2Wnh%252BM60ZqEA%3D%3D "CD4022")|
3|Counter IC 10 Decade/Divider|DIP-16||CD4017BE|[595-CD4017BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD4017BE?qs=IF4wzcbwb3rdXSZhHlgcJw%3D%3D "CD4017")|
4|NAND Logic Gates Schmitt Trigger|DIP-14||CD4093BE|[595-CD4093BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD4093BE?qs=X1HXWTtiZ0QxcrKuDdZ5rg%3D%3D "CD4093")|
5|Phase Locked Loop|DIP-16||CD4046BE|[595-CD4046BE](https://www.mouser.de/ProductDetail/Texas-Instruments/CD4046BE?qs=fvkeCqCHl3AX2sxIYB2bdg%3D%3D "CD4046")|
6|Dual Op Amp|DIP-8||TL072IP|[595-TL072IP](https://www.mouser.de/ProductDetail/Texas-Instruments/TL072IP?qs=5BZzbFV4k2v7IBrcArRPQw%3D%3D "TL072")|
7|Dual Op Amp|DIP-8||LM358P|[595-LM358P](https://www.mouser.de/ProductDetail/Texas-Instruments/LM358P?qs=X1HXWTtiZ0QtOTT8%252BVnsyw%3D%3D "LM358")|
8|Component Sockets|DIP-8||1-2199298-2|[571-1-2199298-2](https://www.mouser.de/ProductDetail/TE-Connectivity/1-2199298-2?qs=%2Fha2pyFadugJp%2F0oQpeWgcdKbmhfM%252BG5f2aD9jt0RGQdskDEwvmLNQ%3D%3D "Component Sockets 8P DIP")|
9|Component Sockets|DIP-14||1-2199298-3|[571-1-2199298-3](https://www.mouser.de/ProductDetail/TE-Connectivity/1-2199298-3?qs=%2Fha2pyFadugJp%2F0oQpeWgR9Lzm5j4WzFAMc1jcrVNfu7vZxg2U3Y3Q%3D%3D "Component Sockets 14P DIP")|
10|Component Sockets|DIP-16||1-2199298-4|[571-1-2199298-4](https://www.mouser.de/ProductDetail/TE-Connectivity/1-2199298-4?qs=%2Fha2pyFadugJp%2F0oQpeWgVBpv3LzMBBwVqoB59rQ35Apde3oZfgpGA%3D%3D "Component Sockets 16P DIP")|
11|Photoresistor|||161|[485-161](https://www.mouser.de/ProductDetail/Adafruit/161?qs=GURawfaeGuDpQ5XPTNqKUw%3D%3D "Photoresistor")|
12|Photoresistor|||SEN-09088|[474-SEN-09088](https://www.mouser.de/ProductDetail/SparkFun/SEN-09088?qs=WyAARYrbSnbNBfpKra%2FIvQ%3D%3D "Photoresistor")|
13|Force Sensitive Resistor|||1075|[485-1075](https://www.mouser.de/ProductDetail/Adafruit/1075?qs=GURawfaeGuDaOmXus2Zwlg%3D%3D "Force Sensitive Resistor")|
14|Aluminum Electrolytic Capacitors|2mm |10uF|EEU-FR1H100|[667-EEU-FR1H100](https://www.mouser.de/ProductDetail/Panasonic/EEU-FR1H100?qs=tfZGHB2PWd1NAbdNSgjToQ%3D%3D "Aluminum Electrolytic Capacitors")|
15|MLCC|2.5mm |0.1uF|K104K15X7RF53K2|[594-K104K15X7RF53K2](https://www.mouser.de/ProductDetail/Vishay-BC-Components/K104K15X7RF53K2?qs=%2Fha2pyFadujQ%252Bv0xHOEo91Fp6rFGP5krxuyVhQ%252B1w%252BsnJ7knhvdeQDps3CPFUP6U "Keramik-Vielschichtkondensator MLCC")|
16|Jumper Cable|15cm||MIKROE-513|[932-MIKROE-513](https://www.mouser.de/ProductDetail/932-MIKROE-513 "Jumper Cable")|
17|Pin Header|1 x 36 2.54mm ||10129378-936002BLF|[649-1012937893602BLF](https://www.mouser.de/ProductDetail/649-1012937893602BLF "Sockel & Kabelgehäuse ECONOSTIK HEADER SR VT TH 1X36")|
18|Pin Header|1 x 36 2.54mm ||68797-436HLF|[649-68797-436HLF](https://www.mouser.de/ProductDetail/649-68797-436HLF "Sockel & Kabelgehäuse BREAKAWAY HEADER 36")|
19|Pin Socket|1 x 8 2.54mm ||8Fx1L-254mm|[992-8FX1L-254MM](https://www.mouser.de/ProductDetail/992-8FX1L-254MM "8-pin wire wrap fem header")|
20|Pin Socket|1 x 32 2.54mm ||61303211821|[710-61303211821](https://www.mouser.de/ProductDetail/710-61303211821 "2.54mm 32Pin Socket Header")|
21|Pin Socket|1 x 36 2.54mm ||801-87-036-10-001101|[437-8018703610001101](https://www.mouser.de/ProductDetail/437-8018703610001101 "Sockel & Kabelgehäuse")|
22|Switch|||||
23|3mm LED|||||
24|5mm LED. Ultra Bright|||||
25|Leaded Resistors (Metal or Carbon Film)|| Assorted Values |||
26|Leaded Capacitors|| Assorted Values |||
27|Stranded Wire|||||
28|Push Button|7.4 x 7.3 x 5.37 mm||KSJ0V41180SHLFTR|[611-KSJ0V41180SHLFT](https://www.mouser.de/ProductDetail/CK/KSJ0V41180SHLFTR?qs=wpKP3X6Fz6rOTpKOA5n8pw%3D%3D "Sensorschalter SWITCH TACTILE")|
29|Push Button|SKHHDAA010|||[688-SKHHDAA010](https://www.mouser.de/ProductDetail/Alps-Alpine/SKHHDAA010?qs=6EGMNY9ZYDTDig1hGWofxQ%3D%3D "Sensorschalter 50 mAmps at 12 Volts")|
30|Push Button|7.4 x 7.4 x 9.9 mm||KSL0M412 LFT|[611-KSL0M412-LFT](https://www.mouser.de/ProductDetail/CK/KSL0M412-LFT?qs=nrpkpS80q8GfGWfXZwdZgg%3D%3D "Sensorschalter Switch Tact Long Man ual Markii")|



## Authors

Zhen Bian  
Hangyan Chen  
Anna Helsen  
Jihye Jang  
Xingchen Liu  
Su Lu  
Ruoyi Qiu  
Christina Vinke  
Yunfei Zhang  

**Lorenz Schwarz** - *lecturer* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgment

* Thanks to Dr. Paul Modler

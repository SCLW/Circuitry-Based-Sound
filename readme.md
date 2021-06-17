
# Circuitry-Based Sound


<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Bread_Board.jpg">

<!--
<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Header.jpg">
-->

"Circuitry-Based Sound" is an ongoing seminar at [University of Arts and Design Karlsruhe](https://www.hfg-karlsruhe.de/ "University of Arts and Design Karlsruhe"). It focuses on electronic sound synthesis and parametric interfacing. It's examining musical characteristics of electronic instruments and comparing different approaches on how to design electronic sound modules. Due to the measures against the coronavirus spread in 2020, the seminar’s workflow had been adapted to the restrictions and is partially held online.

The course is covering electrical and electronic basics, computer aided circuit design and professional printed circuit board (PCB) manufacturing processes with the aim of building custom-made instruments. The emphasis is on studies of logic chips for sound creation and its musical applications. Participants are guided to use the latest technology, production chain and global logistics to develop, design and produce circuit boards for musical use. This allows the participants to easily create circuit boards with more variable features and adjustable parameters than hand soldered protoboards or solderless breadboards.


The following is a documentation of the seminar's study materials and findings.
<br>
<br>
<br>
<br>

<div align="center">
 
[**TABLE OF CONTENTS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#table-of-contents)
</div>


***
[**INTRODUCTION**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#introduction)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Unconventional Electronic Sound](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#unconventional-electronic-sound)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CMOS Chips for Sound Creation](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cmos-chips-for-sound-creation)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Basic Example](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#basic-example)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Logic Control](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#logic-control)
<br>

***
[**WORKS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#works)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Live Electronic Music](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#live-electronic-music)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CMOS Experimenter Boards](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cmos-experimenter-boards)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Relay Oscillators](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#relay-oscillators)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Experimental Oscillators](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#experimental-oscillators)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Crackle Circuits](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#crackle-circuits)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pi Day](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#pi-day)
<!--
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NSynth Super](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#nsynth-super)
<br>
[**SELECTED CMOS CHIPS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#understanding-cmos-chips)\
-->

***
[**ELECTRONIC COMPONENTS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#electronic-components)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Numerical Index of CMOS Chips](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#numerical-index)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Additional ICs](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#additional-ics)
<br>

***
[**BASIC PRINCIPLES AND APPLICATIONS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#basic-principles-and-applications)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Signal Mixing](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#mixing)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Passive Filters](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#passive-filters)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Potentiometers](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#potentiometers)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Touch Circuits](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#touch-circuits)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pull-up and Pull-down Resistors](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#pull-up-and-pull-down-resistors)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Linear Feedback Shift Register](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#linear-feedback-shift-register)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Voltage Starve](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#voltage-starve)
<br>

***
[**MATERIALS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#Materials)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Requirements](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#requirements)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bill of Materials](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#bill-of-materials)
<br>
***
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[License](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#license)
<!--
[Disclaimer](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#disclaimer)\
[License](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#license)\
[Acknowledgment](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#acknowledgment)\
[References](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#references)\
[Links](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#links)
-->

<br>



# Disclaimer

The authors accept no responsibility for damages that are caused by or in connection with the use of the information shown on this website. We are committed to ensure that the content provided is complete and accurate. However, unintended errors may occur. We urge the respective user to cross-check and verify the content before use.
<br>
<br>


# Introduction

Aside from the established way of using electronics to generate and process sound, which can be found in analog synthesizers, there are also unconventional applications of electronics to create sound or experimental music, which will be introduced below. Analog synthesizers apply techniques like [subtractive synthesis](https://en.wikipedia.org/wiki/Subtractive_synthesis "subtractive synthesis") to produce audio. A common concept of the analog signal flow is filtering the output of an oscillator and shaping the overall volume. Variations of this concept can be found in most synthesizers, both analog and digital. Parameters can be altered through control signals. This offers a wide range of musical expression, like tuning oscillators in a 12-tone musical scale or key triggered [envelopes](https://en.wikipedia.org/wiki/Envelope_(music) "envelope") for amplifiers, filters or other effect processors. To obtain these functionalities, circuits of analog synthesizers are relatively complex, involve a high part count and often require precision components.

### Unconventional Electronic Sound

Another concept of creating sound with electronics derived from techniques like hardware hacking and circuit bending. In particular the use of digital integrated logic circuits outside of their typical field of application is a remarkable approach to build customized instruments for artistic sound production and interactive music. The required components are easy to source and low cost. What makes these types of chips even more handy is that they don't need much external components and wiring. They can be used for generating and processing sound without large expenditure.

### CMOS Chips for Sound Creation


![CMOS-chips](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CMOS-chips.jpg)
*Various CMOS chips*
<br>
<br>


[CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute Boolean functions. Complementary metal–oxide–semiconductor (CMOS) is a technique where p-type and n-type MOSFETs are used for manufacturing logic gates. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like [NOT](https://en.wikipedia.org/wiki/Inverter_(logic_gate) "Inverter"), [AND](https://en.wikipedia.org/wiki/AND_gate "AND gate"), [OR](https://en.wikipedia.org/wiki/OR_gate "Or gate"), [NAND](https://en.wikipedia.org/wiki/NAND_gate "NAND gate"), [XOR](https://en.wikipedia.org/wiki/XOR_gate "XOR gate"), [XNOR](https://en.wikipedia.org/wiki/XNOR_gate "XNOR gate") or implement [multiplexers](https://en.wikipedia.org/wiki/Multiplexer "multiplexer"), [counters](https://en.wikipedia.org/wiki/Counter_(digital) "counter"), dividers, [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop") and [registers](https://en.wikipedia.org/wiki/Shift_register "shift register"). When logical operations and their relation to voltage and sound are understood, CMOS-logic chips are an inexhaustible source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced and many more. Combining different logic functions allows generating a multitude of unique sounds and temporal music structures, while they produce the richness of analog sound. These circuits also yield unpredictable behavior, produce rhythmic glitches or digital noise.

Due to its simplicity, CMOS chips can be used for educational reasons, since most of its technical operations can easily be understood and relate to basic electronic knowledge. This subject is also a matter of various publications, most notably [Nicolas Collins'](https://en.wikipedia.org/wiki/Nicolas_Collins "Collins") „Handmade Electronic Music, The Art of Hardware Hacking" (2006). American Composer [David Tudor](https://de.wikipedia.org/wiki/David_Tudor "David Tudor") (1926 - 1996) is considered a pioneer of self-made electronic circuits and instruments, which he used for his compositions. Stanley Lunetta (1937 - 2016), avant-garde composer and artist, incorporated in the 70s digital electronics into his compositions and sound art sculptures and shared his techniques with other artists. In the experimental music community, CMOS synthesizers are therefore often referred to as "Lunettas".


### Basic Example

![CD40106_Fritzing](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106_Fritzing.jpg)
*Simplified depiction of a Schmitt trigger oscillator on a breadboard*
<br>
<br>


The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the picture above. It shows a [square wave](https://en.wikipedia.org/wiki/Square_wave "square wave") sound generator that can be built with only three components, jumper wires and a power supply:
* inverting [Schmitt trigger](https://en.wikipedia.org/wiki/Schmitt_trigger "Schmitt trigger") IC, e.g. CD40106
* capacitor C
* resistor R

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, while the positive trigger threshold differs from the negative one, which is called hysteresis. Feeding the output back to its input via a resistor and connecting a capacitor between the input and ground, known as RC circuit, creates a relaxation oscillator or [astable multivibrator](https://en.wikipedia.org/wiki/Multivibrator#Astable_multivibrator "astable multivibrator"). The resistor limits the current for charging the capacitor and both together determine the [charging time](https://en.wikipedia.org/wiki/RC_time_constant "RC time constant").


![Schmitt_Trigger_Oscillator](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Schmitt_Trigger_Oscillator.gif)
<!--
*Caption*
<br>
<br>
-->

<br>
<br>

The frequency can be roughly calculated with this formula, where V<sub>P</sub> is the positive trigger threshold voltage and V<sub>N</sub> the negative trigger threshold voltage:

<div align="center">

![Formula](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Formula.jpg)
</div>
<!--
*Caption*
<br>
<br>
-->

<br>
<br>

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear. But the formula shows that bigger RC values produce lower frequencies and vice versa. The frequency is determined through the capacitor C and the resistor R. Therefore, a [potentiometer](https://en.wikipedia.org/wiki/Potentiometer "potentiometer") instead of the latter enables pitch control. Other ways of controlling the frequency may be inserting [photoresistors](https://en.wikipedia.org/wiki/Photoresistor "photoresistor"), [force-sensitive resistors](https://en.wikipedia.org/wiki/Force-sensing_resistor "FSR") (FSR) or [flex sensors](https://en.wikipedia.org/wiki/Flex_sensor "flex sensor"). Adding circuit points to alter the sound through interaction allows building customized and versatile instruments.


### Logic Control

A logic gate is a single input - output device, designed to carry out a specific [Boolean operation](https://en.wikipedia.org/wiki/Boolean_algebra "Boolean algebra"), mapped to two voltage levels. Over time, the two alternating voltage levels may form a periodic rectangular waveform and the speed of switching between the two levels is perceived as pitch. Aperiodic switching will produce other sonic qualities such as noise or all kinds of texturized sounds. The ratio between the on- and off-states is by default close to 1:1, a 50% [duty cycle](https://en.wikipedia.org/wiki/Duty_cycle "duty cycle"). Further circuitry is needed to change this ratio, which alters the ratio of the harmonic components to the fundamental.


In digital electronics 2-level logic, [binary numbers](https://en.wikipedia.org/wiki/Binary_number "binary number") are represented by two defined voltage levels that are specified by the used technology and circuit. Everything below a certain voltage threshold level is recognized as 0 and everything above a certain threshold level is recognized as 1. A voltage level in between the two thresholds is not defined and will produce false output triggers. The two states "0" and "1" are also often referred to as "(logical) high" and "(logical) low", "true" and "false" or "ON" and "OFF".


![Square-Wave](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Square-Wave.jpg)
*Analytical description of a square wave*
<br>
<br>
<br>


# Works

The artistic range of applications for electronic projects in the fields of experimental sound, interactive music and sound art is quite large. The next sections feature works made in the context of this seminar.


### Live Electronic Music

The simplicity of CMOS-circuits for sound production makes them a good fit for building customized sound generators. In 2020, on Valentine's Day, the concert performance MK Ultra Sound for eight loudspeakers with self-built circuits took place in the halls of the HfG. Interactive visuals were projected on two perpendicularly placed walls.


![Concert_2020_MK-Ultra-Sound_01](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Concert_2020_MK-Ultra-Sound_01.jpg)
*MK Ultra Sound setup. Photos: Jonas Piroth et al.*
<br>
<br>




![Concert_2020_MK-Ultra-Sound_02_edit](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Concert_2020_MK-Ultra-Sound_02_edit.JPG)
*Photo: Jihye Jang*
<br>
<br>

 
 
Each performer tried out various circuits and chose a combination of CMOS building blocks to create specific sound effects such as drones, glitchy rhythms, noise etc. While rehearsing, we played with various sequences of players playing together or playing one by one, depending on the contributed sound material. During the show we spatialized each performer's signal to a ring of eight loudspeakers through a mixing desk with 8 inputs and 8 outputs.


[Watch the video](https://www.youtube.com/watch?v=N06RBw-_2Q8 "MK Ultra Sound") 

Another group live performance was given in July as an open-air concert between the HfG and the Federal Prosecutor's office as part of the Roundabout 2020, the Media Art Sound semester presentation. For this event, we developed individual printed circuit boards (PCBs) for sound synthesis, including a concept for music interfaces with potentiometers, switches, and sensors that allowed for musical expression.

![Concert_CBS_Roundabout2020](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Concert_CBS_Roundabout2020.jpg)
*Group live performance in summer 2020. Photo: Su Lu*
<br>
<br>

<!--
<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Concert_CBS_Roundabout2020.jpg">
 <p align=center> Photos: Susu Lu
<br>
<br>
-->

<!--
![]()
*Caption*
<br>
<br>
-->

[Watch the video](https://youtu.be/eHiamumLI-0 "Roundabout") 
 
### CMOS Experimenter Boards

The motivation behind this project was to produce a set of PCBs to evaluate logic ICs for sound creation and composition in artistic and educational fields. The idea of providing a CMOS experimenter board was initiated particularly with regard to today's availability of PCB manufacturers and affordable prizes. PCB prototyping and production is now completely based on computer aided electronic design (EDA) while manufacturers offer professional quality at very low costs, even for small board quantities.

<!--
| ![Experimenter_Board](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Experimenter_Board_03.jpg) | 
|:--:| 
| *Photos: Su Lu* |
-->

![Experimenter_Board_03](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Experimenter_Board_03.jpg)
*Rehearsal with DIY CMOS synthesizer. Photo: Su Lu*
<br>
<br>


Each PCB is designed around individual standard CMOS chips and their particular functions in order to create sound. The boards provide inlets and outlets, testing points, sockets, vias and pads for changing values of electronic parts and wiring alternative external circuitry. The modules can be easily extended and interconnected. This allows the user to manipulate circuit points with potentiometers, buttons, switches or sensors and to apply control voltages at appropriate input points.


![CMOS_Synthesizer](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CMOS_Synthesizer.jpg)
*Experimenter boards*
<br>
<br>




It simplified prototyping and made customized configurations highly flexible. The experimenter boards can serve as sound modules for interactive music in live performance or installative environments as well as for algorithmic compositions. By combining several boards with different logic functions, complex switching performance can be achieved, ranging from modulated frequencies and interesting audio spectra to slow, rhythmic pulses or tone sequences. Audio and control signals are exchanged between boards via jumper cables or wires. A wide range of circuit examples with CMOS chips can be found on DIY websites and are widely discussed in various internet forums. These circuits can be a good basis for experimenting with CMOS chips. In addition, it is recommendable to use data sheets for all active components used in electronic projects. Power supply for the boards should comply with the power ratings of the used ICs, which is typically between 3V - 18V DC. LED series resistors need to be calculated accordingly. For the experimenter console, 9V power supply for guitar effects work well.


![Experimenter_Modules](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Experimenter_Modules.jpg)
*Detail of CMOS synthesizer*
<br>
<br>


<br>
<br>

Furthermore, the project includes laser-cutting files for a desktop console on which the boards can be mounted with screws. A power supply can be connected through the frame via banana connectors and distributed to each board.



![acrylic_transparent](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/acrylic_transparent.jpg)
*3D Model: Zhen Bian*
<br>
<br>





## Relay Oscillators


[Relays](https://en.wikipedia.org/wiki/Relay "Relay") are voltage controlled switches that operate electromechanically. One common type of relay uses an electromagnet to move an armature which makes or breaks a contact in a circuit. An electromagnet consists of a coil wound around a ferromagnetic material which generates a magnetic field when an electric current is applied to the coil. Therefore, the magnetic field can be controlled electronically. The movable armature is pulled back to the initial position by a spring force. The two positions of the armature define the on-state (contact closed) and off-state (contact opened) of the switch. A SPDT (single-pole, double-throw) switch allows a common terminal connecting to either of two other terminals. The term NO (normally open) refers to the open contact that will close and conduct electricity when the device is energized. NC (normally closed) will open and stop conducting electricity when the device is energized. In either case, applying an electric current to the electromagnet will change their state. Relays are generally used to switch high currents in one circuit with another low voltage circuit, which is also a form of galvanic isolation.


![Relay_Oscillator](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Relay_Oscillator.jpg)
*Relay oscillator configurations*
<br>
<br>



A SPDT relay has usually 5 terminals as the figure on the left shows. One common terminal, the NC and NO terminal and the two control terminals. When controlled by an additional circuit (microcontroller or control logic), a SPDT comes with 6 terminals. In addition to the SPDT switch, the control circuit consists of a power connection (terminal + and -/GND) and the control pin (s).


![Relay_Oscillator_setup](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Relay_Oscillator_setup.jpg)
*Photo: Victoria Mikhaylova*
<br>
<br>
 
The experiment was designed to employ the clicking sound of an electromagnetic relay for a sound installation and performance. Some relays were modified with capacitors, resistors, and light sensors in order to built astable multivibrators. When a capacitor is connected in series with the NO, and a power source is connected to the common terminal, an astable multivibrator can be built. An additional resistor in series can vary the frequency (RC component).


![Relay_Installation_diagram](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Relay_Installation_diagram.jpg)
*Graphic: Victoria Mikhaylova*
<br>
<br>

Some of the relays were used to control the logic gate of a CD4093 oscillator configuration. Other relays were powered on and off simultaneously by another relay to synchronize or gate them. Other relays were just switched by simple logic circuits (CD4093). When connecting with a CMOS chip, a pull down resistor is needed. Cascading relays and forming various connections between these systems allowed to explore the sound creation possibilities. Dedicated circuit points were defined and coupled with 4 loudspeakers in total via two mixing desks. The general idea of the setup was to research the combination of the clicking sounds of a number of relays together with amplified switching signals played back via loudspeakers.


![Relay_Installation](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Relay_Installation.jpg)
*Photo: Victoria Mikhaylova*
<br>
<br>


Since each relay functioned as a physical sound generator, together with the 4-channel loudspeaker setup, an experimental sound field had been created. The result showed us that the setup produced has a dark and rich noise or drone sound and can be even better represented in some dark environment or on a dark stage. An abandoned factory or some industrial area could be an appropriate location for the performance. The setup should be organized in a way to be easily reached to improvise during the performance.




![Relay_Installation_front-view](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Relay_Installation_front-view.jpg)
*Photo: Victoria Mikhaylova*
<br>
<br>
[Watch the video](https://youtu.be/OkDDaWhSzgk "Relay Oscillators") 
<br>
<br>

<!-- Table of Contents
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Wireless Sound Modules](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#wireless-sound-modules)\
-->

<!--
### Wireless Sound Modules
![Wireless_Sound_Module_02](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Wireless_Sound_Module_02.JPG)
*Wireless sound modules and audio circuits*
<br>
<br>
This sound art installation involves musical interaction between a performer and a number of smaller “sound objects“, also called modules. The setup consists of a table or pedestal on which the modules are placed. The modules are operated through wireless power transfer (WPT). A multichannel sound field can be easily generated and modulated by placing several sound objects in proximity to the induction coils.
![WMS_Installation_01](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/WMS_Installation_01.jpg)
*Sound art installation. Photo: Vivian Reuter*
<br>
<br>
Alterations in sound are caused by repositioning, moving or grouping the sound modules. Although the objects are not physically linked to each other, they start interacting electro-acoustically when they share the same magnetic field. The sound modules contain electronic sound generators and loudspeakers, and therefore work independently from a sound studio situation. The sound synthesis is carried out by CMOS ICs. Each object functions as a sealed chamber for a single dynamic loudspeaker. We used 3D printing as an effective method to create various shapes, tailored to the needs of our application.
![Simplified_WPT_Diagramm](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Simplified_WPT_Diagramm.jpg)
*Simplified WPT diagramm*
<br>
<br>
When the objects are placed into the magnetic field of the current-carrying induction coils, which are integrated into a table, the circuits are put into operation and produce sound which is played back via the built-in loudspeakers. The direct relation between the physical parameters of the induction field and the sound gives the user an audible feedback. Here, to play with the sound, the objects can be tilted or even held above the magnetic field, which works up to a distance of approximately 2,5". For example, the frequency of the oscillators rises with distance while the amplitude decays. If several Objects are placed into the same magnetic field, the chips start colluding and "battling" about the available power.
-->


### Experimental Oscillators


![Organic_Synthesizer](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Organic_Synthesizer.jpg)
*Photos: Jihye Jang, Huiyeon Yun*
<br>
<br>

 
<!--
<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Diagram_Sketch.jpg">
-->

 
### Crackle Circuits

In addition to sensors or other control elements like potentiometers, force-sensing resistors, or similar components, touching directly dedicated connection points in a circuit will also affect its behavior. The human body can add various parameters like resistance or capacitance. The conductivity of the human skin introduced into a circuit varies greatly just like the capacitance of the human body. Moisture (sweat), pressure or even the surroundings define the actual electrical values and make it difficult to predict their effect on a circuit. In this context, the crackle box should be mentioned as a remarkable example.



![Crackle_Box](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Crackle_Box.jpg)
*Crackle Box. Photo: Till Kniola*
<br>
<br>

 
The crackle box is a touch-controlled electronic instrument, developed in the 70s by Michel Waisvisz (\*1949 Leiden † 2008 Amsterdam) at STEIM in Amsterdam. Its beginnings date back to the 60s. It's a battery operated small wooden case (14 x 8 x 3 cm), like a cigar box, a visible circuitboard with six distinctive touch points, ~1cm<sup>2</sup> each, and an on/off switch. Underneath the touch surface is a built-in loudspeaker. The vibrating air can pass through a number of holes in the PCB between the touch surface. The instruments produces random noise, clicks and plops or oscillates when touched with fingers. The circuit inside is just an op amp in an inverting configuration, while many circuit points and most pins of the op amp are made available on the outside of the device as conductive touch pads.
 

![LM709_TO-5](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LM709_TO-5.jpg)
*LM709 TO-5 metal can packages*
<br>
<br>



 
The device makes use of the LM709/μA709 op-amp (originally National Semiconductor, then Texas Instruments), one of the earliest monolithic operational amplifiers, created by [Robert Widlar](https://en.wikipedia.org/wiki/Bob_Widlar "Bob Widlar"). Its design concept and performance were already surpassed by its successor LM741. While the ladder is still in production, the LM709 has been discontinued. Compared with modern op-amps, it lacked of an output buffer stage. This means it is not short circuit proof. Furthermore, the LM709 did not have an internal frequency compensation. External components need to be added to limit the op-amps bandwidth to prevent unwanted oscillation. Richard Kaußler made a detailed analysis of the LM709, which can be found [here](https://www.richis-lab.de/Opamp20.htm "LM709"). His [website](https://www.richis-lab.de/ "Richi´s Lab") (in German) is a good resource for in-depth information about the internal structure of various ICs.



![LM709_Die](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LM709_Die.jpg)
*Die of an LM709 op-amp. Photo: Richard Kaußler*
<br>
<br>


 
The image on the left shows the [die](https://en.wikipedia.org/wiki/Die_(integrated_circuit)) of the LM709, embedded in a TO-5 package. On the right is a close up of the die. The die is called the integrated circuit made of silicon. The design of the crackle box focuses on the imperfections of the LM709 and its special features, particularly its external frequency compensation. Michel Waisvisz’s Crackle box is therefore an early example of circuit bending and unconventional use of electronic components. The crackle box had been reissued over the past decades as assembly kits and can still be ordered from STEIM on request.


![Crackle_Box_Circuit](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Crackle_Box_Circuit.jpg)
*LM709 pin out and schematic of Michel Waisvisz’s crackle box*
<br>
<br>


<br>
<br>

As mentioned above, the LM709 is out of production and most modern op amps are internally frequency compensated and achieve a high stability during performance. For the crackle box, the LM709 can't be substituted with other op amps. Which means it also addresses the problem of obsolescence in the field of historical electronic instruments. One approach to circumvent this problem is to look closer into the LM709. The internal schematic can be found in its data-sheet.


![Crackle_Discrete](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Crackle_Discrete.jpg)
*Schematic with LM709 equivalent internal circuit*
<br>
<br>



For most applications, building an integrated circuit with discrete parts leads to a significant degradation of its performance. Because the dedicated parts within an IC are produced precisely to the needs of the circuit. 


![Crackle_Circuit_Prototype](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Crackle_Circuit_Prototype.jpg)
*Breadboard with discrete components substituting the LM709*
<br>
<br>



Since the crackle box doesn't rely on a precise operation but on randomness, standard transistors can be used. Both schematics presented here omit the push-pull speaker driver using two complementary pairs of transistors. Substituting the obsolete LM709 with discrete components, specifically transistors and resistors, brings an equivalent crackle circuit into being.

![Crackle_Circuit_Prototype](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Crackle_Board.jpg)
*Crackle board*
<br>
<br>


Download BOM [here](https://github.com/SCLW/Projects/tree/main/BOMs "BOM Crackle Circuit")

Download Gerber files [here](https://github.com/SCLW/Circuitry-Based-Sound/tree/master/Gerber "Crackle Circuit Gerber Files")



### Pi Day


![Pi_Day_2021](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Pi_Day_2021.jpg)
*Torta della Nonna*
<br>
<br>


**For the shortcrust:**
* 450 g all-purpose flour
* 1 pinch of salt
* 200 g cold butter, cubed
* 2 eggs
* 150 g sugar
* Zest of 1 organic lemon

**For the Crema Pasticcera:**
* 1 L milk
* 250 g sugar
* 6 egg yolks
* 80 g cornstarch
* Zest of 1 organic lemon
* 60 g butter
* 2 vanilla beans
* 50 g pine nuts
* powdered sugar for the Pi



<!--
### NSynth Super

NSynth Super is an open source hardware synthesizer, based on Magenta’s NSynth algorithm. It uses the open-source software library TensorFlow and the OpenFrameworks toolkit. All information is avilable on Github. It is not an official Google product, but most software components are Google developments and based on research by Google Brain. The project is a very good example for analysing concepts of embedded instruments and interface design. Single parts can be recontextualize or modified for other projects. The board's schematics and layout files are available for KiCad EDA (free software) as well as the generated gerber files.


![NSynth_HDF_Case](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/NSynth_HDF_Case.jpg)
*Open hardware project NSynth with HDF casing*
<br>
<br>


<br>
<br>


NSynth is able to combine sounds, like a bass and flute, into a new, hybrid bass-flute sound. This experiment lets anyone explore these sounds and make music with them. NSynth is built using Tensorflow, Tone.js and a [WaveNet-style autoencoder](https://arxiv.org/pdf/1704.01279.pdf "Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders")


![NSynth_Board_Bottom](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/NSynth_Board_Bottom_01.jpg)
*NSynth bottom view*
<br>
<br>

<br>
<br>


The WaveNet-style autoencoder is extracting temporal features from a dataset, interpolating linearly and decoding into new sounds
The NSynth (Neural audio synthesis) is a deep neural network that learns the characteristics of a sound (embedding) and is creating new sounds based on these characteristics.

For this, the Open NSynth dataset is available. It is an open-source sound library with:
* 305,979 musical notes
* 1,006 different instruments
* ~ 65,4 pitches per instrument
* Five different velocities
* Monophonic
* Four seconds each
* 16 kilohertz, 16 Bit

The Open NSynth physical interface has 4 different sounds in each corner, accessible through an X/Y-pad. The Open NSynth Super application runs on a Raspberry Pi (Raspberry Pi 3 Mod. B+) using OpenFrameworks. The Raspberry Pi is also communicating with the NSynth PCB mainboard.
The user inputs are four rotary encoders in the corners of an X/Y pad as instrument sound selectors. The central X/Y touch interface provides the sound interpolation. Six potentiometers along the bottom edge of the PCB are used for envelope and sample control. Pitch and velocity are introduces via MIDI Keyboard.

![NSynth_Board_Top_01](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/NSynth_Board_Top_01.jpg)
*NSynth top view*
<br>
<br>


<br>
<br>

NSynth PCB mainboard and chipset:
* AT42QT2120-XU touch sensor IC
* stm32f030k6 lqfp32 MCU ARM Cortex-M0
* PCM512X audio DAC (PCM5122PW)
* Adafruit 1.3" OLED display
* 5-pin DIN MIDI input jack
* 3.5mm Audio output
* Micro USB power inlet

 
The Raspberry Pi communicates via I²C with the monochrome 1.3" 128x64 OLED graphic display (Adafruit) and the STM32f030k6 microcontroller (Arm Cortex M0 32-bit) which reads the touch sensor, encoder, and potentiometer values. The Audio stereo DAC is the PCM512X (Texas Instruments) and controlled via I²S

Open NSynth Super Device provisioning:
* Create the SD card (cross-platform)
* Prepare the OS
* Copy audio files
* Set up the firmware
* Set up the application


We found that the sound of the NSynth is quite distinct. Some reconstructed sounds also seem to fluctuate in fundamental frequency, which is described as frequency wobble by google. In addition the spectral resolution seems to be limited. The Input source is 16 bit, 16 kHz. Although the morphing is based on computed sound files generated by a neural algorithm, what remains is just a sample player with a X/Y-touch field. 
-->
<br>
<br>


# Electronic Components

The following is a list of CMOS chips and other integrated circuits for sound creation and processing. This list will be constantly extended during the seminar. It outlines for each chip its main applications and gives a short explanation. Pinout, functional diagram, truth tables and some basic example circuits are also shown. However, the overview is not completed with these examples and the main approach is to find variations, modifications or new creative combinations for experimental sound and music. Please refer to the manufacturer's technical data sheet for more detailed information.

## Numerical Index
[CD40106](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd40106)\
[CD4093](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4093)\
[CD4070](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4070)\
[CD4015](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4015)\
[CD4022](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4022)\
[CD4040](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4040)\
[CD4046](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4046)\
[CD4051](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4051)\
[CD4066](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4066)\
[CD4060](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4060)\
[CD4013](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4013)\
[CD4018](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4018-under-construction)\
[555 Timer](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#555-timer-under-construction)

### CD40106

The inverter is a basic part in digital electronics and performs the logic operation of negation. When the input is connected to ground, the output is pulled to V<sub>DD</sub> and vice versa. The CD40106 hex Schmitt trigger inverter offers six separate inverters in one chip. The Schmitt trigger action permits unlimited rise and fall times on the input. The chip can be wired externally to build one or more square wave oscillators (see illustration). When using a potentiometer for frequency control, a resistor should be placed in series in order to prevent too low resistance between output and input.

*Applications:*
* Square Wave Generator
* Inverting Buffer


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106.jpg>

Truth table for NOT
|Inputs|Outputs|
|----|----|
|0|1|
|1|0|

"1" = High Level  
"0" = Low Level


[CD40106 Sheet](https://www.ti.com/lit/ds/symlink/cd40106b.pdf?ts=1599062729936&ref_url=https%253A%252F%252Fwww.google.com%252F "CD40106")
<br>
<br>

### CD4093

The CD4093 contains 4 NAND Schmitt triggers, each providing 2 inputs and 1 output.

It acts as a square wave oscillator when the inputs are connected to form an inverter. The last two rows of the truth table indicate that one input has to be set to a logical high in order to attain inversion of the signal being present at the other input. When one of the inputs is wired like the CD40106 in the previous example, while the remaining input is set to high, the CD4093 generates square waves too. In this configuration, oscillation can be inhibited by setting the input to a logical low. This way, the input acts as a control input for gating the oscillator.

*Applications:*
* Square Wave Generator
* Gated Oscillator


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093.jpg>

Truth table for NAND

|A|B|J=A NAND B|
|----|----|:----:|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|





[CD4093 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4093b.pdf?ts=1599062791398&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4093")
<br>
<br>



### CD4070

The CD4070 contains four Exclusive-OR logic gates. Each gate has two inputs and one output. The output is high when only one of the inputs is high and the other is low and vice versa. If both inputs are high or low, the output is low. If two square wave signals are connected to the input, the output extracts the difference which results in a frequency mixer like output signal. Frequency doubling can be achieved if one square wave is applied directly to one input and connected via a resistor to its second input with a capacitor to ground. The rising and falling edge of an incoming square wave force the output to high, hence doubles the incoming frequency. The pulse width of the output signal depends on the chosen values and is shorter than the width of the input signal; approximately the length of the RC time constant. Shifting a tone up by an octave may only sound satisfactorily within a small value range.

CD4077 is the Exclusive-NOR version.

*Applications:*
* Digital Frequency Mixer
* Frequency Doubler



<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4070.jpg>

Truth table for XOR (CD4070)

|A|B|Y = A XOR B|
|----|----|:----:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

Truth table for XNOR (CD4077)

|A|B|Y = A XNOR B|
|----|----|:----:|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|1|


[CD4070 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4077b.pdf?ts=1606308007892&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4070")
<br>
<br>


### CD4015

CD4015 IC consists of two four stage shift registers.

A shift register is built of a series of interconnected [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop"). A flip-flop or latch is a bistable multivibrator circuit. This means it has two stable states which represent either 0 or 1. The state of a flip-flop can be controlled by a clock. The value to be stored is based on the signal's input state at the transition of the clock signal. A flip-flop is used to store 1 bit. In a shift register the incoming serial input data **D** is transferred to a parallel output register **Qn**. More specifically, when a memory content is stored in the first flip-flop, it is shifted to the next one, synchronized to the rising edge of a dedicated clock signal **CL**. A logical high at the reset pin is setting all outputs to zero. The reset pin should be set to low for a continuous operation.


*Applications:*
* Sequencer
* Noise Generator
* Linear-feedback Shift Register ([LFSR](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#linear-feedback-shift-register "LFSR"))


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4015.jpg>

Truth table for four stage shift register

|CL|D|R|Q1|Qn|
|:----:|:----:|:----:|:----:|:----:|
|/|0|0|0|Qn-1|
|/|1|0|1|Qn-1|
|⧹|X|0|Q1|Qn|
|X|X|1|0|0|

X   = Don't Care Case  
/   = Rising Edge  
⧹   = Falling Edge  



[CD4015 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4015b.pdf?ts=1607676770686&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4015")
<br>
<br>


### CD4022

CD4022 and CD4017 ICs implement a binary counter/divider function with 8 outputs in the CD4022 and 10 outputs in the CD4017. The positive edge of an incoming square wave, usually referred to as "clock signal", triggers successively the outputs. "Carry out" is outputting one cycle over 8 (CD4022) respectively 10 (CD4017) clock pulses. A logical high at "clock inhibit" pauses the counting process. A logical high at the "reset" pin sets the counter pulse back to the first output.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_anim.gif>


*Applications:*
* Sequencer
* Staircase Wave Form Generator
* Wave Shaper


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_animated.gif>



<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_Timing_Diagram.jpg>

[CD4022 Data Sheet](https://www.ti.com/lit/ds/schs027c/schs027c.pdf?ts=1599062824246&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4022")
<br>
<br>

### CD4040

This IC performs frequency division and comes with 12 outputs in the CD4020 and the CD4040 versions and 7 outputs in the CD4022 version, whereby the CD4020 is a 14-stage device. Output stages 2 and 3 (divide by 4 and 8) are not accessible. The CD4024 has 3 pins without internal connection (pin 8, 10, 13). If a square wave is applied to the input, each output creates square waves at half the frequency of its preceding output, at which the first output Q1 applies its division to the input signal and oscillates at a rate at one half, Q2 at one quarter, Q3 at one eighth Q4 at one sixteenth and so on. Several units can be cascaded for higher counting.

Control input "reset" triggers all output stages to "low". For continuous frequency division it should be kept at a logical low.


*Applications:*
* Frequency Divider
* Sub Octave Generator
* Representation of Binary Numbers

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040.jpg>


In terms of generating sound, each output producing one octave lower than its previous output, respectively input.


The timing diagram shows the relation of voltage levels between all outputs of the CD4024 IC, a 7-output stage version:
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_Timing_Diagram.jpg>

[CD4040 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4040b.pdf?ts=1600261370155&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4040B "CD4040")
<br>
<br>

### CD4046


Phase locked loop

*Applications:*
* Tone Distortion
* Pitch Tracking
* Frequency Multiplication
* Voltage Controlled Square Wave Generator


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4046.jpg>

[CD4046 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4046b.pdf?ts=1599062962750&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4046")

<br>
<br>

### CD4051

CD405x Multiplexer/Demultiplexer series comes in a 16 DIP package and is useful for switching and routing analog or digital signals.
CD4051 is a switch in a single pole octal throw configuration with three binary control inputs for setting the contacts. CD4052 can be used for multiplexing one differential channel in a double-pole quad-throw configuration and has two binary control inputs. CD4053 offers individual control over 3 channels in a single-pole double-throw configuration with an independent binary control input for each channel.

All channels are off when inhibit input is set to "high" (active low).

*Applications:*
* Wave Shaper
* Digitally-controlled Analog Switching
* Signal Routing

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4051_animated.gif>

Truth table for the CD4051
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


<br>
<br>

### CD4066

Quad Bilateral Switch

IC CD4066 includes four identical digitally controlled switches for analog or digital signals.
Inputs and outputs are interchangeable as with conventional switches. Each switch can be controlled independently by a control input.

control logic 1 = switch on  
control logic 0 = switch off


*Applications:*
* Signal Gating
* Signal Routing


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4066_anim.gif>



[CD4066 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4066b.pdf?ts=1608449210166&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4066")

<br>
<br>

### CD4060

14 stage ripple-carry binary counter/divider and oscillator. Q1, Q2, Q3 and Q11 are not connected to the outside of the package.



*Applications:*
* Frequency Divider
* Square Wave Generator





<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4060.jpg>



[CD4060 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4060b.pdf "CD4060")

<br>
<br>

### CD4013
 
The CD4013 IC flip-flop is called a D flip-flop type to characterize its behavior, while D stands for "data" or "delay". It contains two identical D flip-flop arrangements. The device stores a digital state 0 or 1, which is accessible at the output **Q**. The second output **/Q** presents the inverse of **Q**. The control input **Clock** transfers the input state **D** to the output **Q** respectively **/Q**. The CD4013 is positive-edge-triggered, which means that the positive-going transition of a clock impulse triggers the device to hold the state that is present at the input and provides it at the output until the next positive-going clock signal. The additional control inputs **Set** and **Reset** have priority over the clock. With a high level on the **Set** input, the output follows its state and goes low with a high level on the **Reset** input, ignoring **D** and **Clock**.



*Applications:*
* Frequency Divider
* Counter
* Toggle Switch

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4013.jpg>


D flip-flop truth table

|C|D|R|S|Q|/Q|
|:----:|:----:|:----:|:----:|:----:|:----:|
|/|0|0|0|0|1|
|/|1|0|0|1|0|
|⧹|X|0|0|no change|no change|
|X|X|1|0|0|1|
|X|X|0|1|1|0|
|X|X|1|1|1|1|

X   = Don't Care  
/   = Rising Edge  
⧹   = Falling Edge  



[CD4013 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4013b.pdf?ts=1609946760296&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4013")

<br>
<br>

### CD4018 (under construction)

Divide-By-'N' Counter

When the outputs are fed back to the input Data, divide by 10, 8, 6, 4, 2, is calculated. For odd numbers 9, 7, 5, 3, simply use CD4011 or CD4093 to NAND two corresponding output stages and feed the inverted result back into Data. By combining multiple devices, higher divide-by functions can be calculated. Preset enable will transfer Data on the input Jam to its corresponding /Q (inverted). A logical high on the reset input causes all /Q Outputs to high.


Divide by 9: **/Q4** & **/Q5** via 1/2 CD4011 connected to input Data  
Divide by 7: **/Q3** & **/Q4** via 1/2 CD4011 connected to input Data  
Divide by 5: **/Q**2 & **/Q3** via 1/2 CD4011 connected to input Data  
Divide by 3: **/Q1** & **/Q2** via 1/2 CD4011 connected to input Data  

Divide by 10: **/Q5** connected to input Data  
Divide by 8: **/Q4** connected to input Data  
Divide by 6: **/Q3** connected to input Data  
Divide by 4: **/Q2** connected to input Data  
Divide by 2: **/Q1** connected to input Data  





*Applications:*
* Divide by 10, 8, 6, 4, 2
* Divide by 9, 7, 5, 3
* Chord Generator


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4018.jpg>

FUNCTIONAL TRUTH TABLE FOR CD4018

|Clock|Reset|Preset Enable|Jam Input|/Qn|
|:----:|:----:|:----:|:----:|:----:|
|⧹|0|0|X|/Qn|
|/|0| 0| X|/Dn|
|X| 0| 1| 0|1|
|X| 0| 1| 1|0|
|X| 1| X| X|1|

/Dn = Data input for that stage  
X   = Don't Care  
/   = Rising Edge  
⧹   = Falling Edge  


[CD4018 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4018b.pdf?ts=1610571153497&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4018B "CD4018")
<br>
<br>

### 555 Timer (under construction)

Note: The bipolar version (NE555) and the CMOS version (TLC555, LMC555) have the same pinout and are exchangeable. The CMOS version consumes significantly less power. Its name derives from the three 5kΩ resistors that form a voltage divider network.

*Applications:*
* Frequency Divider
* Timer
* Pulse Delay
* Square Wave Generator
* Pulse Width Modulator

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Timer.jpg>

<!---


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Astable_Operation.jpg>
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Bistable_Operation.jpg>
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Monostable_Operation.jpg>
-->

[LMC555 Data Sheet](https://www.ti.com/lit/ds/symlink/lmc555.pdf?ts=1609974121158&ref_url=https%253A%252F%252Fwww.google.com%252F "LMC555")
<br>
<br>

## Additional ICs

### LM386 - Power Operational Amplifier (under construction)

Although not part of the CMOS logic family this ubiquitous power op amp is a very versatile component when it comes to amplification or driving small speakers.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LM386.jpg>

[LM386 Data Sheet](https://www.ti.com/lit/ds/symlink/lm386.pdf?ts=1613028335418&ref_url=https%253A%252F%252Fwww.google.com%252F "LM386")
<br>
<br>
|Pin|Function|
|----|----|
|1|Gain setting|
|2|Inverting input|
|3|Noninverting input|
|4|Ground reference|
|5|Output|
|6|Power supply voltage|
|7|Bypass decoupling path|
|8|Gain setting pin|

|Pin|min Voltage|max Voltage|
|----|----|----|
|Supply Voltage|4V|12V|
|Analog input voltage|-0.4V|0.4V|






# Basic Principles and Applications

## Mixing

There are two ways of mixing signals together, active and passive mixing. Active mixing involves components, such as operational amplifiers, that need a power supply. Passive mixing works without an additional power supply, but introduces a voltage drop.

### Passive Mixing

Passive mixing is a very simple method that can be accomplished by using resistors for each source. The mixing resistors work as a voltage divider network and lower the amplitude of each signal. Therefore, the passive mixer doesn't give the sum of all input signals but the [average](https://en.wikipedia.org/wiki/Millman%27s_theorem "Millman's theorem"). Small resistance values will drain more current and create distortion. Good values are between 10kΩ - 50kΩ. The advantage of this method is its low part count. To avoid attenuation and interaction between the signals and to obtain individual gain control, active mixing using an operational amplifier is preferred.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/passive_mixing.jpg>


### Active Mixing

For most audio applications it is desired to control the portion of each input signal in the sum of the output mix. For this, another class of active electronic components can be used, the [operational amplifier](https://en.wikipedia.org/wiki/Operational_amplifier "op amp") (op amp). The basic wiring is shown below. Besides its function as a mixer with gain control over every individual input by adding voltage dividers or potentiometers, it can also be used to achieve a desired output gain by modifying the feedback resistor R<sub>F</sub> in relation to the input resistors R<sub>IN</sub> of each input. The minus sign in the formula indicates that the output voltage is inversed. To undo inversion, a second stage following the shown circuit can be used.


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Summing_Inverting_OpAmp.jpg>

## Passive Filters

Tone control, modifying the frequency spectrum of a signal or creative equalization are very important processes when working with audio. A filter is frequency-selective and passes only a desired range of frequencies, which is called the pass band. Outside of this pass band, frequencies are attenuated or ideally completely reduced. The boundary between pass and stop band is called cutoff frequency. The simplest way to shape an electronic signal is the use of a combination of resistor and capacitor, an RC element. This forms a first order filter. The circuit can be considered as a frequency dependent potential divider. A band-pass filter can be built with two RC elements, as a combination of a high-pass and a low-pass configuration. Since no amplifying components are involved, the amplitude of the output is lower than the input amplitude. When a filter is designed with two passive components, the transition from pass to stop band is rather smooth. For instance, a first order low-pass filter will have a 6dB/octave roll-off with increasing frequency. Unfortunately, the properties of passive filters are not sufficient to achieve a higher steepness or musical effects like resonance, which requires active filter designs. However, the simplicity and the low part count make this method very attractive for subtle tone control.


<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Passive_Filter.jpg>


## Potentiometers

A potentiometer is a passive, mechanical component inside a housing. It consists of a resistive track and a movable contact, called wiper, whose position along the resistive element can be set with an actuator. The two ends of the resistive element and the end of the wiper can be accessed from outside the housing. The total resistance between the end terminals can be gradually divided into two resistance values between the respective ends of the element and the wiper.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Potentiometer_Actuator.jpg>
a) housing, b) terminals, c) actuator, d) resistive track, e) wiper

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Potentiometer_Equivalent.jpg>


If one end and the wiper are used, the potentiometer forms a variable resistor.
A variable voltage divider circuit can be configured by connecting a voltage (supply voltage or signal) to one of the outside pins, while the remaining outside pin is connected to GND. A voltage can be tapped at the middle pin that can be adjusted by setting the actuator. For instance, from one end point location to the other, the input voltage can be scaled from minimum to maximum. This can be used for volume control.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Volume_Control_Variable.jpg>

## Touch Circuits

Most approaches for touch-sensitive circuits make use of the resistance or conductivity of the human skin to alter the voltage of one section within a circuit compared to a defined voltage reference. A simple touch switch is based on a NAND logic gate with one of the inputs connected to V<sub>DD</sub> and the other connected in a pull-up configuration via a high value resistor (several MΩ) to V<sub>DD</sub> . A layout for a touch point consists of two conductive areas, electrically separated but close together, where one part is connected to the pulled-up input and the second part is connected to ground. Without touching the conductive area, both logic inputs are high. When a finger is shorting the touch point, the finger's resistance forms a voltage divider together with the pull-up resistor. The resistance of the human skin varies greatly depending on conditions like humidity. Values from several thousands to more than 100kΩ can be assumed. The resulting voltage at the respective input is fairly low and equates a logical 0. In a NAND gate, this condition forces the output to go high, as long as both inputs are different.


<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Resistive_Touch.jpg">



The piezo electric effect describes that a voltage is generated when a mechanical strain is applied to specific crystalline or ceramic materials. They are commercially manufactured as small discs for various shock/impact sensing applications and loudspeakers, since the inverse piezo electric effect is causing the material to vibrate when an electrical audio signal is applied. A comparator can compare the voltage of the piezo with a reference threshold voltage level. If the voltage level generated by the piezo disc exceeds or falls below the reference threshold, the comparator circuit outputs either a high or a low. 

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Piezo_Trigger_Comparator.jpg">

Most voltage comparators use open-collector output stages. If the inverting input has a higher potential than the non-inverting input, the output transistor is open and together with the pullup resistor, a dedicated trigger impulse is generated.


For many applications, the rather short voltage spike of a pizeo element needs to be transformed into a pulse with a determined on-time period. This can be done with a  monostabile multivibrator. It remains in this state for a time determined by the circuitry, then it flips back to its initial state. In this case, the comparator circuit of the 555 Timer can be used instead of a regular comparator. 

<!-- The next picture shows such a circuit:
<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Piezo_Trigger_555.jpg">
-->

Another approach for sensing a touch or the proximity of human fingers or hands is based on capacitance. In CMOS circuits it can be used for controlling pitch. This method of touch control uses the parasitic capacitance between two conductive areas (electrodes) within a circuit. When a high frequency is applied to the two conductive areas, they create an electric field that stores opposite electric charges and act like plates of a capacitor. The electrodes are placed in parallel to a capacitor that forms an RC network together with a resistor. The RC network in turn defines the time constant of an astable multivibrator. When a finger or stylus is brought in close proximity to the electric field, it changes the capacitance and therefore the frequency of the multivibrator. When the electrodes are touched, the finger or stylus changes the dielectric constant. The dielectric is the material between the electrodes. The alterations of capacitance is linear to the force of the touch. The electrodes should be insulated with conformal coating or a thin adhesive strip.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Capacitive_Touch_02_edit.JPG">


The [CD4060](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4060 "CD4060") has a built-in oscillator configuration that can be used to generate such a high frequency that is applied to, for example, two copper areas. The output is then fed into the binary counter function for frequency division to generate an audio signal. Various forms of electrodes had been tested using thin copper strips using a cutting plotter.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Touch-Sensing_Diagram.jpg">


### Pull-up and Pull-down Resistors

When external circuits or devices are added to a logic input, care must be taken to keep the inputs in a defined state. When switches or transistors are used to control a logic gate, they can physically disconnect the inputs. For example, when a normally-open push button is in its default position, the high impedance input is open. This causes the pin to act like an antenna that is very susceptible to electromagnetic noise and forces the output to do unwanted operations like generating random highs or lows. This is called "floating" and introduces undesired effects.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/pull-up_pull-down.jpg">

To avoid this unpredicted behavior, a resistor should be connected to ground or to the high voltage, so that the input pin will see a defined state even when nothing else is connected, for example when a switch is opened. The pin will be able to accept an input signal when the switch is closed. A connection to V<sub>CC</sub> is called "pull-up" and a connection to ground "pull-down". For CMOS-logic, the resistor values can be several thousand ohms.

Even unused logic gates can cause problems since coupled-in interference voltages result in unwanted triggers and excess current draw. If a proper operation is desired, all unused inputs should not be left floating and connected together to GND or V<sub>CC</sub>.

### Linear Feedback Shift Register

A linear feedback shift register (LFSR) can be used for generating deterministic pseudorandomness. In terms of electronic sound production it can be used to build a noise source. An LFSR consists of n numbers of flip-flops which are connected in series to form a shift register as described for the [CD4015](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4015). This shift register is controlled by a clock that triggers the shift process. Two junctions at a specific position within that chain of flip-flops are directed into an XOR logic gate. The resulting value is fed back into the first register. The number of stages can be extended by connecting multiple devices. The produced values are determined by the shift register's current states and total length. Since the states are finite it will repeat after a certain number of steps. The goal is to choose those taps that form the longest possible sequence of zeros and ones before they repeat. Other implementations of an LFSR exist and work similarly. To activate an LFSR each stage needs to be loaded with an initial value. This is called the seed. By using an XOR function for the feedback, having the value 0 in all flip-flops is forbidden. By using an XNOR function it is forbidden to set all flip-flops to 1. A maximum-length sequence is therefor 2<sup>n</sup> - 1. Additional operations can be introduced to produce a length of 2<sup>n</sup>. No matter if XOR or XNOR functions are used, the sequences will have the same length, while the succession of values differs. The duration of one cycle is determined by the clock frequency. When looked at a shift register from the viewpoint of a musician, the long LFSR arrangements will create white and pink noise when controlled with a high frequency (several ten thousands of hertz). Shorter cycles produce grainy tones, stuttering textures or short noise loops.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LFSR.jpg>

The Xilinx application note XAPP210 (V1.3) shows a table for maximum length sequences, which is presented here for up to 24 bits:

|n|taps from||n|taps from|
|:----:|:----:|:----:|:----:|:----:|
|3|3,2||14|14,5,3,1|
|4|4,3||15|15,14|
|5|5,3||16|16,15,13,4|
|6|6,5||17|17,14|
|7|7,6||18|18,11|
|8|8,6,5,4||19|19,6,2,1|
|9|9,5||20|20,17|
|10|10,7||21|21,19|
|11|11,9||22|22,21|
|12|12,6,4,1,||23|23,18|
|13|13,4,3,1||24|24,23,22,17|


Depending on the desired operation, other applicable devices may be CD4094, CD4014, CD4021 which are all 8-stage shift registers.
 

## Voltage Starve

"Voltage starve" or "voltage sag" can be used as an unconventional modulation technique for experimental music. It describes the effect that low supply voltage and limited current have on a circuit's behavior. Especially battery powered guitar pedals create unique dynamic distortion when the battery's voltage and current delivering capacity is unstable due to aging factors.

Changing the supply voltage will have different effects on a signal, depending on the actual circuit and the used components. Bypassing capacitors will mitigate these effects. For instance, the hysteresis thresholds in Schmitt trigger elements vary with the supply voltage. Lowering the supply voltage affects the frequency and the signal amplitude of Schmitt trigger oscillators. 

When working with an adjustable power supply or an according circuit, the impacts of limited current and voltage levels around or below the minimum requirements of an IC can be examined. A similar performance can be simulated with a simple series resistor in the power rail. 500Ω - 10kΩ potentiometers may be worth experimenting with to create odd sounds.

# Materials

Instructions, parts, tools, shopping lists, components, assemblies, and other materials required to create electronic projects in this field.

## Requirements

Helpful tools and useful materials:


* Small mixing desk.
* Active loudspeakers.
* Worktables.
* Pen and paper for drawing schematics.
* Screw drivers.
* ESD electronic diagonal cutter.
* Precision cutter.
* Stranded wires.
* Crocodile clips.
* Laboratory power supply & connectors (preferable 4mm banana laboratory connectors).
* Jumper cables and jumper wires.
* Digital multimeter (DVM).
* Digital storage oscilloscope (DSO).
* Temperature-controlled soldering station.
* Breadboards.
* 9V Batteries.
* Battery clips.
* Good light conditions.



## Bill of Materials

A list with parts that can be used for this project, is available in the folder [BOM](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/BOM/Readme.md#bill-of-material "Bill of Material")
All parts can be substituted with alternative components and equivalent foot prints.






## Authors

<!--
Marc Bendt  
-->
Zhen Bian  
Yinxuan Chen  
Hangyan Chen  
Haram Choi  
Hongyu Guo  
Jeongmin Han  
Anna Helsen  
Jihye Jang  
Minsu Kim  
Jung Eun Lee  
Sangyi Lee  
Xingchen Liu  
Su Lu  
Victoria Mikhaylova  
Jiun-You Ou  
Ruoyi Qiu  
<!--
Bob Reinert  
-->
Vivian Reuter  
Arno Schlipf  
Florian Schwarz
<!--
Yifan Su  
-->
Christina Vinke  
Julian Vollmert  
Dakang Wang  
<!--
Siting Wang  
-->
Huiyeon Yun  
Rui Zhang  
Yunfei Zhang  
Xinyi Zhao  
Pei Zhou  





**Lorenz Schwarz** - *lecturer*
<br>
<br>
<br>





## Acknowledgment

Thanks to Holger Förterer and Dr. Paul Modler
<br>
<br>
<br>

# References


B. Lojek. History of semiconductor engineering, 2007.\
N. Collins. Handmade Electronic Music: The Art of Hardware Hacking, 2009.\
A. Hamilton. Pianos, Toys, Music and Noise: Conversations with Steve Beresford, 2021.\
F. Schuiling. The Instant Composers Pool and Improvisation Beyond Jazz, 2018.\
R. Ghazala. Circuit-Bending: Build Your Own Alien Instruments, 2005.\
D. Lancaster. CMOS Cookbook, 1997.\
R. Baker. CMOS: Circuit Design, Layout, and Simulation, 2010.\
C. Maxfield. Bebop to the Boolean Boogie: An Unconventional Guide to Electronics, 2003.\
C. Roads. Composing Electronic Music: A New Aesthetic, 2015.
<br>
<br>
<br>

# Links
https://sound-au.com/articles/logic.htm<br>
https://electricdruid.net/a-study-of-sub-oscillators/<br>
https://en.wikipedia.org/wiki/Resistor_ladder<br>
https://electronics.koncon.nl/oscillators/<br>
https://electro-music.com/forum/forum-160.html<br>
http://nomni.com/<br>



## License

The content of this documentation is licensed under the [Creative Commons Attribution 3.0 Unported license](https://creativecommons.org/licenses/by/3.0/ "CC BY 3.0"), software is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. Copyright remains with the author(s)
<br>
<br>
<br>

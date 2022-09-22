
# Circuitry-Based Sound


![Circuitry_Based_Sound_Foto_Yunfei_Zhang](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Circuitry_Based_Sound_Foto_Yunfei_Zhang.jpg)
*Photo: Yunfei Zhang*
<br>
<br>




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
[**ELECTRONIC COMPONENTS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#electronic-components)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Numerical Index of CMOS Chips](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#numerical-index)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Additional ICs](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#additional-ics)
<br>

***
[**BASIC PRINCIPLES AND APPLICATIONS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#basic-principles-and-applications)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Signal Mixing](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#mixing)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Passive Filters](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#passive-filters)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pull-up and Pull-down Resistors](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#pull-up-and-pull-down-resistors)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Linear Feedback Shift Register](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#linear-feedback-shift-register)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Step Sequencer](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#step-sequencer-under-construction)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Voltage Starve](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#voltage-starve)
<br>

***
[**WORKS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#works)\
<br>

***
[**MATERIALS**](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#Materials)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Requirements](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#requirements)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bill of Materials](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#bill-of-materials)
<br>

***
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[License](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#license)


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


[CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute Boolean functions. Complementary metal–oxide–semiconductor (CMOS) is a technique where p-type and n-type MOSFETs are used for manufacturing logic gates. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like [NOT](https://en.wikipedia.org/wiki/Inverter_(logic_gate) "Inverter"), [AND](https://en.wikipedia.org/wiki/AND_gate "AND gate"), [OR](https://en.wikipedia.org/wiki/OR_gate "Or gate"), [NAND](https://en.wikipedia.org/wiki/NAND_gate "NAND gate"), [XOR](https://en.wikipedia.org/wiki/XOR_gate "XOR gate"), [XNOR](https://en.wikipedia.org/wiki/XNOR_gate "XNOR gate") or implement [multiplexers](https://en.wikipedia.org/wiki/Multiplexer "multiplexer"), [counters](https://en.wikipedia.org/wiki/Counter_(digital) "counter"), dividers, [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop") and [registers](https://en.wikipedia.org/wiki/Shift_register "shift register"). When logical operations and their relation to voltage and sound are understood, CMOS-logic chips are an inexhaustible source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced, layered, and many more. Combining different logic functions allows generating a multitude of unique sounds and temporal music structures, while they produce the richness of analog sound. These circuits also yield unpredictable behavior, produce rhythmic glitches or digital noise.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Switching_Circuit_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Switching_Circuit_LIGHT.svg">
  <img alt="Boolean logic as switching circuit." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Switching_Circuit_LIGHT.svg">
</picture>



Logical operations can be implemented as switching circuits with single pole single throw switches representing the input and an LED indicating the result. The switch and the LED can have two distinct states: on and off. The open switch corresponds to a logical 0 and the closed position stands for a logical 1. A lit LED means 1 and a non-lit 0.


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Logic_Gates_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Logic_Gates_LIGHT.svg">
  <img alt="Illustration of electronic logic gate symbols." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Logic_Gates_LIGHT.svg">
</picture>



A truth table is used in Boolean algebra to show all possible values of a logical expression. 

Output comparison of 2-input logic gates:

| INPUT A | INPUT B | AND | NAND | OR | NOR | XOR | XNOR |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0` | `0` | 0 | 1 | 0 | 1 | 0 | 1 |
| `0` | `1` | 0 | 1 | 1 | 0 | 1 | 0 |
| `1` | `0` | 0 | 1 | 1 | 0 | 1 | 0 |
| `1` | `1` | 1 | 0 | 1 | 0 | 0 | 1 |


Due to its simplicity, CMOS chips can be used for educational reasons, since most of its technical operations can easily be understood and relate to basic electronic knowledge. This subject is also a matter of various publications, most notably [Nicolas Collins'](https://en.wikipedia.org/wiki/Nicolas_Collins "Collins") „Handmade Electronic Music, The Art of Hardware Hacking" (2006). American Composer [David Tudor](https://de.wikipedia.org/wiki/David_Tudor "David Tudor") (1926 - 1996) is considered a pioneer of self-made electronic circuits and instruments, which he used for his compositions. Stanley Lunetta (1937 - 2016), avant-garde composer and artist, incorporated in the 70s digital electronics into his compositions and sound art sculptures and shared his techniques with other artists. In the experimental music community, CMOS synthesizers are therefore often referred to as "Lunettas".


### Basic Example


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Breadboard_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Breadboard_LIGHT.svg">
  <img alt="Simplified depiction of a Schmitt trigger oscillator on a breadboard." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Breadboard_LIGHT.svg">
</picture>

<!--
![CD40106_Fritzing](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106_Fritzing.jpg)
*Simplified depiction of a Schmitt trigger oscillator on a breadboard*
<br>
<br>
-->

The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the picture above. It shows a [square wave](https://en.wikipedia.org/wiki/Square_wave "square wave") sound generator that can be built with only three components, jumper wires and a power supply:
* inverting [Schmitt trigger](https://en.wikipedia.org/wiki/Schmitt_trigger "Schmitt trigger") IC, e.g. CD40106
* capacitor C
* resistor R

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, while the positive trigger threshold differs from the negative one, which is called hysteresis. Feeding the output back to its input via a resistor R and connecting a capacitor C between the input and ground, known as RC circuit, creates a relaxation oscillator or [astable multivibrator](https://en.wikipedia.org/wiki/Multivibrator#Astable_multivibrator "astable multivibrator"). The resistor limits the current for charging the capacitor and both together determine the [charging time](https://en.wikipedia.org/wiki/RC_time_constant "RC time constant").


<!-- ANIMATED GIF -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Schmitt_Trigger_DARK.gif">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Schmitt_Trigger_LIGHT.gif">
  <img alt="Animated iIllustration of a Schmitt trigger oscillator and its waveforms." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Schmitt_Trigger_LIGHT.gif">
</picture>

<!--
![Schmitt_Trigger_Oscillator](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Schmitt_Trigger_DARK.gif)
-->

<br>
<br>

The frequency can be roughly calculated with this formula $f=\frac{1}{T}=\frac{1}{RC ln [(\frac{V_P}{V_N})(\frac{V_{DD}-V_N}{V_{DD}-V_P})]}$, where V<sub>P</sub> is the positive trigger threshold voltage and V<sub>N</sub> the negative trigger threshold voltage.





<br>
<br>

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear. But the formula shows that bigger RC values produce lower frequencies and vice versa. The frequency is determined through the capacitor C and the resistor R. Therefore, a [potentiometer](https://en.wikipedia.org/wiki/Potentiometer "potentiometer") instead of the latter enables pitch control. Other ways of controlling the frequency may be inserting [photoresistors](https://en.wikipedia.org/wiki/Photoresistor "photoresistor"), [force-sensitive resistors](https://en.wikipedia.org/wiki/Force-sensing_resistor "FSR") (FSR) or [flex sensors](https://en.wikipedia.org/wiki/Flex_sensor "flex sensor"). Adding circuit points to alter the sound through interaction allows building customized and versatile instruments.


### Logic Control

A logic gate is a single input - output device, designed to carry out a specific [Boolean operation](https://en.wikipedia.org/wiki/Boolean_algebra "Boolean algebra"), mapped to two voltage levels. Over time, the two alternating voltage levels may form a periodic rectangular waveform and the speed of switching between the two levels is perceived as pitch. Aperiodic switching will produce other sonic qualities such as noise or all kinds of texturized sounds. The ratio between the on- and off-states is by default close to 1:1, a 50% [duty cycle](https://en.wikipedia.org/wiki/Duty_cycle "duty cycle"). Further circuitry is needed to change this ratio, which alters the ratio of the amplitudes of the harmonic components to the fundamental.


In digital electronics 2-level logic, [binary numbers](https://en.wikipedia.org/wiki/Binary_number "binary number") are represented by two defined voltage levels that are specified by the used technology and circuit. Everything below a certain voltage threshold level is recognized as 0 and everything above a certain threshold level is recognized as 1. A voltage level in between the two thresholds is not defined or forbdden and will produce false output triggers. CMOS digital inputs have a high impedance and pick up thermal noise voltages if left floating. Unused inputs should be tied to a defined voltage. Other input configurations (e.g. taster, toggle switches,) require [pull-up or pull-down resistors](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#pull-up-and-pull-down-resistors "pull-up or pull-down"). The two states "0" and "1" are also often referred to as "(logical) high" and "(logical) low", "true" and "false" or "ON" and "OFF". 


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Logic_Signal_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Logic_Signal_LIGHT.svg">
  <img alt="Common CMOS input voltage levels without and with Schmitt trigger implementation." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Logic_Signal_LIGHT.svg">
</picture>

<!-- 
![Logic_Signal](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Logic_Signal.jpg)
*Common CMOS input voltage levels without and with Schmitt trigger implementation*
<br>
-->

V<sub>IH</sub> is the minimum input voltage that will be interpreted as a logical high, while V<sub>IL</sub> is the maximum input voltage that will be interpreted as a logical low. The region in between is undefined and may trigger unpredictable highs or lows (chattering). This problem is solved by implementing a Schmitt trigger with different thresholds for negative-going and positive-going input voltages, depending on whether the input signal is changing from high to low (V<sub>N</sub>) or low to high (V<sub>P</sub>). When the input is between the two thresholds the output retains its value.


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Square_Wave_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Square_Wave_LIGHT.svg">
  <img alt="Analytical description of a square wave logic signal." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Square_Wave_LIGHT.svg">
</picture>

<!--
![Square-Wave](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Square_Wave.svg)
*Analytical description of a square wave logic signal*
<br>
<br>
<br>
-->


The [square wave](https://en.wikipedia.org/wiki/Square_wave "Square wave") contains only overtones with odd numbered harmonics (⅓, ⅕, ⅐, etc). The relative amplitudes of the harmonics are equal to 1/harmonic number n.

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
[CD405x](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd405x)\
[CD4066](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4066)\
[CD4060](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4060)\
[CD4018](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4018-under-construction)\
[555 Timer](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#555-timer-under-construction)\
[LM386](https://github.com/SCLW/Circuitry-Based-Sound#lm386---power-operational-amplifier-under-construction)



### CD40106

The inverter is a basic part in digital electronics and performs the logic operation of negation. When the input is connected to ground, the output is pulled to V<sub>DD</sub> and vice versa. The CD40106 hex Schmitt trigger inverter offers six separate inverters in one chip. The Schmitt trigger action permits unlimited rise and fall times on the input. The chip can be wired externally to build one or more square wave oscillators (see illustration). When using a potentiometer for frequency control, a resistor should be placed in series in order to prevent too low resistance between output and input.

*Applications:*
* Square Wave Generator
* Inverting Buffer



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106_LIGHT.svg">
  <img alt="CD40106 hex Schmitt trigger inverter." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD40106_LIGHT.svg">
</picture>



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

It acts as a square wave oscillator when the inputs are connected to form an inverter. The last two rows of the truth table indicate that one input has to be set to a logical high in order to attain inversion of the signal being present at the other input. When one of the inputs is wired like the CD40106 in the previous example, while the remaining input is set to high, the CD4093 generates square waves too.

*Applications:*
* Square Wave Generator
* Gated Oscillator


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093_Button_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093_Button_LIGHT.svg">
  <img alt="Schematic of an oscillator controlled by a push button." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093_Button_LIGHT.svg">
</picture>



Oscillators built with 2 input NAND Schmitt triggers can be switched on and off manually by using a push button. If the push button is not pressed (normally open) the logical low at the second input will always cause a logical hight at the output, no matter which state is present at the other input (see NAND truth table). The image above shows how to set up a normally open push button as an ON switch to control the sound. A [pull down resistor](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#pull-up-and-pull-down-resistors) defines the logic state at the input when the push button is open. When the push button is closed, the power supply produces a logical high and the NAND gate oscillates. This way, the second input acts as a control input for gating the oscillator. Instead of a manually controlled push button, a logic signal can be applied to the second input.


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093_Gated_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093_Gated_LIGHT.svg">
  <img alt="Schematic of a gated oscillator." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4093_Gated_LIGHT.svg">
</picture>








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


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4070_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4070_LIGHT.svg">
  <img alt="Digital frequency mixing with CD4070." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4070_LIGHT.svg">
</picture>




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

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4015_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4015_LIGHT.svg">
  <img alt="CD4015 four stage shift register." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4015_LIGHT.svg">
</picture>



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

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4070_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4070_LIGHT.svg">
  <img alt="Digital frequency mixing." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4070_LIGHT.svg">
</picture>

<!--
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_anim.gif>
-->

*Applications:*
* Sequencer
* Staircase Wave Form Generator
* Wave Shaper

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_LIGHT.svg">
  <img alt="CD4022 binary counter/divider." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_LIGHT.svg">
</picture>

<!--
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_animated.gif>
-->


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_Outputs_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_Outputs_LIGHT.svg">
  <img alt="CD4022 timing diagram." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4022_Outputs_LIGHT.svg">
</picture>




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

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_LIGHT.svg">
  <img alt="CD4040 frequency divider." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_LIGHT.svg">
</picture>




In terms of generating sound, each output producing one octave lower than its previous output, respectively input.


The timing diagram shows the relation of voltage levels between all outputs of the CD4024 IC, a 7-output stage version:

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_Outputs_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_Outputs_LIGHT.svg">
  <img alt="CD4040 timing diagram." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4040_Outputs_LIGHT.svg">
</picture>



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


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4046_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4046_LIGHT.svg">
  <img alt="CD4046 phase locked loop." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4046_LIGHT.svg">
</picture>



[CD4046 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4046b.pdf?ts=1599062962750&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4046")

<br>
<br>

### CD405x

CD405x Multiplexer/Demultiplexer series comes in a 16 DIP package and is useful for switching and routing analog or digital signals.  

The contact resistance (R<sub>ON</sub>) of a CMOS switch in the closed position depends on the input voltage, power supply voltage, and temperature. For the CD405x types this on-resistance is approximately in the range of 120Ω - 200Ω or more ohms and can distort the input signal in some cases. This value is quite low and negligible for the field of applications described in this article.

If any of the control pins of the CD405x are not used, it must be connected to GND or V<sub>DD</sub>.

All channels are off when inhibit input is set to "high" (active low).

V<sub>EE</sub> (Pin 7) is for dual supply operation. It is tied to ground in single supply mode.


*Applications:*
* Wave Shaper
* Digitally-controlled Analog Switching
* Signal Routing
* controlling LEDs

#### CD4051

CD4051 is a switch in a single pole octal throw configuration with three binary control inputs for setting the contacts. 




<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4051_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4051_LIGHT.svg">
  <img alt="Schematic of CD4051 single pole octal throw CMOS switch." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4051_LIGHT.svg">
</picture>


<!--
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4051_animated.gif>
-->


Truth table for the CD4051  

|INHIBIT|C|B|A|ON CHANNEL(S)|
|:---:|:---:|:---:|:---:|:---:|
|0|0|0|0|0|
|0|0|0|1|1|
|0|0|1|0|2|
|0|0|1|1|3|
|0|1|0|0|4|
|0|1|0|1|5|
|0|1|1|0|6|
|0|1|1|1|7|
|1|X|X|X|None|  

X = Don't Care

#### CD4052

CD4052 can be used for multiplexing one differential channel in a double-pole quad-throw configuration and has two binary control inputs.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4052_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4052_LIGHT.svg">
  <img alt="Schematic of CD4052 double-pole quad-throw CMOS switch." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4052_LIGHT.svg">
</picture>


Truth table for the CD4052  

|INHIBIT|B|A|ON CHANNEL(S)|
|:---:|:---:|:---:|:---:|
|0|0|0|X0, Y0|
|0|0|1|X1, Y1|
|0|1|0|X2, Y2|
|0|1|1|X3, Y3|
|1|X|X|None|

X = Don't Care

#### CD4053

CD4053 offers individual control over 3 channels in a single-pole double-throw configuration with an independent binary control input for each channel.  

<!--
When the control signal is less than 1/3 V<sub>DD</sub>, z is connected to x0. When the control signal is more than 2/3 V<sub>DD</sub>, z is connected to y1.
 -->


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4053_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4053_LIGHT.svg">
  <img alt="Schematic of CD4053, containing three single-pole double-throw CMOS switches." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4053_LIGHT.svg">
</picture>

Truth table for the CD4053  

|INHIBIT|C|B|A|ON CHANNEL(S)|
|:---:|:---:|:---:|:---:|:---:|
|0|X|X|0|ax|
|0|X|X|1|ay|
|0|X|0|X|bx|
|0|X|1|X|by|
|0|0|X|X|cx|
|0|1|X|X|cy|
|1|X|X|X|None|

X = Don't Care

[CD405x Data Sheet](https://www.ti.com/lit/ds/symlink/cd4051b.pdf?ts=1599079621658&ref_url=https%253A%252F%252Fwww.google.com%252F "CD405xB")

<br>
<br>

### CD4066

Quad Bilateral Single Pole Single Throw Switch

IC CD4066 includes four identical digitally controlled switches for analog or digital signals.
Inputs and outputs are interchangeable as with conventional switches. Each switch can be controlled independently by a control input.

On-state resistance is between few hundred ohms to one thousands ohms, depending on V<sub>DD</sub>. Absolute maximum current into any input is 10mA.

control logic 1 = switch on  
control logic 0 = switch off


*Applications:*
* Signal Gating
* Signal Routing
* Transmission Gate Inverter



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4066_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4066_LIGHT.svg">
  <img alt="Schematic of CD4066, containing four single-pole single-throw CMOS switches." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4066_LIGHT.svg">
</picture>

<!--
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4066_anim.gif>
-->


The following example shows a single pole double throw (SPDT) configuration built with two bilateral switches of the CD4066 (lower section, SW2 and SW3). SW1 is set up to do logic and acts as an inverter: A high at the control input makes a connection to ground and "pulls" the output node down, while a logical low opens the switch and the pull-up resistor ensures a high at the same node. The non-inverted and the inverted control signals are then connected to the respective control inputs of the remaining switches SW2 and SW3. If one switch is open, the other is closed and vice versa. A common signal will be routed to either one of the outputs. This setup can be used for ping-pong stereo effects. Interchanging the input and output in this SPDT example makes a signal selector. The CD4053 contains already three SPDT switches.

<!--
<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4066_Ping-pong_Stereo.jpg>
-->

[CD4066 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4066b.pdf?ts=1608449210166&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4066")

<br>
<br>

### CD4060

14 stage ripple-carry binary counter/divider and oscillator. Q1, Q2, Q3 and Q11 are not connected to the outside of the package. A high level on input pin 12 resets the counter and disables the oscillator.



*Applications:*
* Frequency Divider
* Square Wave Generator




<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4060_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4060_LIGHT.svg">
  <img alt="Schematic of CD4060, 14 stage binary counter/divider and oscillator." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4060_LIGHT.svg">
</picture>


[CD4060 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4060b.pdf "CD4060")

<br>
<br>

<!--
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
-->

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
* Rhythm/Chord Generator



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4018_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4018_LIGHT.svg">
  <img alt="Schematic of CD4018, Divide-By-'N' Counter." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/CD4018_LIGHT.svg">
</picture>



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

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Timer_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Timer_LIGHT.svg">
  <img alt="Functional diagram of the 555 timer." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Timer_LIGHT.svg">
</picture>


|Pin|Function|
|----|----|
|1|Ground.|
|2|Start of timing input. TRIG < ½ CONT sets output high and discharge open.|
|3|High current timer output signal.|
|4|Active low reset input forces output and discharge low.|
|5|Controls comparator thresholds, Outputs 2/3 VCC, allows bypass capacitor connection.|
|6|End of timing input. THRES > CONT sets output low and discharge low.|
|7|Open collector output to discharge timing capacitor.|
|8|Input supply voltage, 4.5 V to 16 V.|




<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Astable_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Astable_LIGHT.svg">
  <img alt="Astable operation." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Astable_LIGHT.svg">
</picture>


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Mono_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Mono_LIGHT.svg">
  <img alt="Monostable operation." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/555_Mono_LIGHT.svg">
</picture>




[LMC555 Data Sheet](https://www.ti.com/lit/ds/symlink/lmc555.pdf?ts=1609974121158&ref_url=https%253A%252F%252Fwww.google.com%252F "LMC555")  
[TLC555 Data Sheet](https://www.ti.com/lit/ds/symlink/tlc555.pdf "TLC555")
<br>
<br>

## Additional ICs

### LM386 - Power Operational Amplifier (under construction)

Although not part of the CMOS logic family this ubiquitous power op amp is a very versatile component when it comes to amplification or driving small speakers.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LM386_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LM386_LIGHT.svg">
  <img alt="LM386 - Power Operational Amplifier." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/LM386_LIGHT.svg">
</picture>



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

|  |min Voltage|max Voltage|
|----|----|----|
|Supply Voltage|4V|12V|
|Analog input voltage|-0.4V|0.4V|






# Basic Principles and Applications

## Mixing

There are two ways of mixing signals together, active and passive mixing. Active mixing involves components, such as operational amplifiers, that need a power supply. Passive mixing works without an additional power supply, but introduces a voltage drop.

### Passive Mixing

Passive mixing is a very simple method that can be accomplished by using resistors for each source. The mixing resistors work as a voltage divider network and lower the amplitude of each signal. Therefore, the passive mixer doesn't give the sum of all input signals but the [average](https://en.wikipedia.org/wiki/Millman%27s_theorem "Millman's theorem"). Small resistance values will drain more current and create distortion. Good values are between 10kΩ - 50kΩ. The advantage of this method is its low part count. To avoid attenuation and interaction between the signals and to obtain individual gain control, active mixing using an operational amplifier is preferred.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/passive_mixing_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/passive_mixing_LIGHT.svg">
  <img alt="Passive mixer." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/passive_mixing_LIGHT.svg">
</picture>


### Active Mixing

For most audio applications it is desired to control the portion of each input signal in the sum of the output mix. For this, another class of active electronic components can be used, the [operational amplifier](https://en.wikipedia.org/wiki/Operational_amplifier "op amp") (op amp). The basic wiring is shown below. 


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Active_Mixing_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Active_Mixing_LIGHT.svg">
  <img alt="Single supply active mixing." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Active_Mixing_LIGHT.svg">
</picture>


By adding voltage dividers or potentiometers, it allows for gain control over every individual input. Besides its function as a mixer, it can also be used to achieve the desired output gain by modifying the feedback resistor R<sub>F</sub> in relation to the input resistors R<sub>IN</sub> of each input. The minus sign in the formula indicates that the output voltage is inverted. To undo inversion, a second stage following the shown circuit can be used.

$V_{OUT} = - [ \frac{R_F} {R_{IN1}} V_{IN1} + \frac{R_F} {R_{IN2}} V_{IN2} + \frac{R_F} {R_{IN3}} V_{IN3} + etc.]$  
$- V_{OUT} = \frac{R_F} {R_{IN}} [V_{IN1} + V_{IN2} + V_{IN3} + etc.]$ if all $R_{IN}$ are the same.


It should be underlined that the example shown is a single supply based circuit, which is uncommon for audio mixing where usually symmetrical dual supply voltages are used. It is important therefore to create a reference voltage of 1/2 V<sub>CC</sub> at the non-inverting input. When working with logic circuits, the signals are almost at the supply levels. Even with rail-to-rail op amps caution is required to keep the summed signals below the working range of the op amp.




## Passive Filters

Tone control, modifying the frequency spectrum of a signal or creative equalization are very important processes when working with audio. A filter is frequency-selective and passes only a desired range of frequencies, which is called the pass band. Outside of this pass band, frequencies are attenuated or ideally completely reduced. The boundary between pass and stop band is called cutoff frequency. The simplest way to shape an electronic signal is the use of a combination of resistor and capacitor, an RC element. This forms a first order filter. The circuit can be considered as a frequency dependent potential divider. A band-pass filter can be built with two RC elements, as a combination of a high-pass and a low-pass configuration. Since no amplifying components are involved, the amplitude of the output is lower than the input amplitude. When a filter is designed with two passive components, the transition from pass to stop band is rather smooth. For instance, a first order low-pass filter will have a 6dB/octave roll-off with increasing frequency. Unfortunately, the properties of passive filters are not sufficient to achieve a higher steepness or musical effects like resonance, which requires active filter designs. However, the simplicity and the low part count make this method very attractive for subtle tone control.



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Passive_Filter_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Passive_Filter_LIGHT.svg">
  <img alt="Passive Filter." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Passive_Filter_LIGHT.svg">
</picture>


<!--
## Potentiometers

A potentiometer is a passive, mechanical component inside a housing. It consists of a resistive track and a movable contact, called wiper, whose position along the resistive element can be set with an actuator. The two ends of the resistive element and the end of the wiper can be accessed from outside the housing. The total resistance between the end terminals can be gradually divided into two resistance values between the respective ends of the element and the wiper.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Potentiometer_Actuator.jpg>
a) housing, b) terminals, c) actuator, d) resistive track, e) wiper

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Potentiometer_Equivalent.jpg>


If one end and the wiper are used, the potentiometer forms a variable resistor.
A variable voltage divider circuit can be configured by connecting a voltage (supply voltage or signal) to one of the outside pins, while the remaining outside pin is connected to GND. A voltage can be tapped at the middle pin that can be adjusted by setting the actuator. For instance, from one end point location to the other, the input voltage can be scaled from minimum to maximum. This can be used for volume control.

<img src=https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Volume_Control_Variable.jpg>
-->

<!--
## Touch Circuits

Most approaches for touch-sensitive circuits make use of the resistance or conductivity of the human skin to alter the voltage of one section within a circuit compared to a defined voltage reference. A simple touch switch is based on a NAND logic gate with one of the inputs connected to V<sub>DD</sub> and the other connected in a pull-up configuration via a high value resistor (several MΩ) to V<sub>DD</sub> . A layout for a touch point consists of two conductive areas, electrically separated but close together, where one part is connected to the pulled-up input and the second part is connected to ground. Without touching the conductive area, both logic inputs are high. When a finger is shorting the touch point, the finger's resistance forms a voltage divider together with the pull-up resistor. The resistance of the human skin varies greatly depending on conditions like humidity. Values from several thousands to more than 100kΩ can be assumed. The resulting voltage at the respective input is fairly low and equates a logical 0. In a NAND gate, this condition forces the output to go high, as long as both inputs are different.


<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Resistive_Touch.jpg">



The piezo electric effect describes that a voltage is generated when a mechanical strain is applied to specific crystalline or ceramic materials. They are commercially manufactured as small discs for various shock/impact sensing applications and loudspeakers, since the inverse piezo electric effect is causing the material to vibrate when an electrical audio signal is applied. A comparator can compare the voltage of the piezo with a reference threshold voltage level. If the voltage level generated by the piezo disc exceeds or falls below the reference threshold, the comparator circuit outputs either a high or a low. 

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Piezo_Trigger_Comparator.jpg">

Most voltage comparators use open-collector output stages. If the inverting input has a higher potential than the non-inverting input, the output transistor is open and together with the pullup resistor, a dedicated trigger impulse is generated.


For many applications, the rather short voltage spike of a pizeo element needs to be transformed into a pulse with a determined on-time period. This can be done with a  monostabile multivibrator. It remains in this state for a time determined by the circuitry, then it flips back to its initial state. In this case, the comparator circuit of the 555 Timer can be used instead of a regular comparator. 



Another approach for sensing a touch or the proximity of human fingers or hands is based on capacitance. In CMOS circuits it can be used for controlling pitch. This method of touch control uses the parasitic capacitance between two conductive areas (electrodes) within a circuit. When a high frequency is applied to the two conductive areas, they create an electric field that stores opposite electric charges and act like plates of a capacitor. The electrodes are placed in parallel to a capacitor that forms an RC network together with a resistor. The RC network in turn defines the time constant of an astable multivibrator. When a finger or stylus is brought in close proximity to the electric field, it changes the capacitance and therefore the frequency of the multivibrator. When the electrodes are touched, the finger or stylus changes the dielectric constant. The dielectric is the material between the electrodes. The alterations of capacitance is linear to the force of the touch. The electrodes should be insulated with conformal coating or a thin adhesive strip.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Capacitive_Touch_02_edit.JPG">


The [CD4060](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4060 "CD4060") has a built-in oscillator configuration that can be used to generate such a high frequency that is applied to, for example, two copper areas. The output is then fed into the binary counter function for frequency division to generate an audio signal. Various forms of electrodes had been tested using thin copper strips using a cutting plotter.

<img src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Touch-Sensing_Diagram.jpg">

-->


### Pull-up and Pull-down Resistors

When external circuits or devices are added to a logic input, care must be taken to keep the inputs in a defined state. When switches or transistors are used to control a logic gate, they can physically disconnect the inputs. For example, when a normally-open push button is in its default position, the high impedance input is open. This causes the pin to act like an antenna that is very susceptible to electromagnetic noise and forces the output to do unwanted operations like generating random highs or lows. This is called "floating" and introduces undesired effects.



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/pull-up_pull-down_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/pull-up_pull-down_LIGHT.svg">
  <img alt="Schematic of pull-up and pull-down resistors with logic gate inputs." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/pull-up_pull-down_LIGHT.svg">
</picture>




To avoid this unpredicted behavior, a resistor should be connected to ground or to the high voltage, so that the input pin will see a defined state even when nothing else is connected, for example when a switch is opened. The pin will be able to accept an input signal when the switch is closed. A connection to V<sub>CC</sub> is called "pull-up" and a connection to ground "pull-down". For CMOS-logic, the resistor values can be several thousand ohms.

Even unused logic gates can cause problems since coupled-in interference voltages result in unwanted triggers and excess current draw. If a proper operation is desired, all unused inputs should not be left floating and connected together to GND or V<sub>CC</sub>.

### Linear Feedback Shift Register

A linear feedback shift register (LFSR) can be used for generating deterministic pseudorandomness. In terms of electronic sound production it can be used to build a noise source. An LFSR consists of n numbers of flip-flops which are connected in series to form a shift register as described for the [CD4015](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4015). This shift register is controlled by a clock that triggers the shift process. Two junctions at a specific position within that chain of flip-flops are directed into an XOR logic gate. The resulting value is fed back into the first register. The number of stages can be extended by connecting multiple devices. The produced values are determined by the shift register's current states and total length. Since the states are finite it will repeat after a certain number of steps. The goal is to choose those taps that form the longest possible sequence of zeros and ones before they repeat. Other implementations of an LFSR exist and work similarly. To activate an LFSR each stage needs to be loaded with an initial value. This is called the seed. By using an XOR function for the feedback, having the value 0 in all flip-flops is forbidden. By using an XNOR function it is forbidden to set all flip-flops to 1. A maximum-length sequence is therefor 2<sup>n</sup> - 1. Additional operations can be introduced to produce a length of 2<sup>n</sup>. No matter if XOR or XNOR functions are used, the sequences will have the same length, while the succession of values differs. The duration of one cycle is determined by the clock frequency. When looked at a shift register from the viewpoint of a musician, the long LFSR arrangements will create white and pink noise when controlled with a high frequency (several ten thousands of hertz). Shorter cycles produce grainy tones, stuttering textures or short noise loops.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/basic_LFSR_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/basic_LFSR_LIGHT.svg">
  <img alt="Simplified schematic of an LFSR." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/basic_LFSR_LIGHT.svg">
</picture>




The Xilinx application note [XAPP210](https://www.xilinx.com/support/documentation/application_notes/xapp210.pdf "Xilinx application note XAPP210") (V1.3) and the Maxim Integrated (now Analog Devices) application note [APP4400](https://pdfserv.maximintegrated.com/en/an/AN4400.pdf "application note APP4400") (Jun 30, 2010) show tables for maximum length sequences, which are presented here for up to 32 bits:

|n|tapsfrom|length| |n|tapsfrom|length| |n|tapsfrom|length|
|:---|:---|---:|-|:---|:---|---:|-|:---|:---|---:|
|3|3,2|7||13|13,4,3,1|8,191||23|23,18|8,388,607|
|4|4,3|15||14|14,5,3,1|16,383||24|24,23,22,17|16,777,215|
|5|5,3|31||15|15,14|32,767||25|25,22|33,554,431|
|6|6,5|63||16|16,15,13,4|65,535||26|26,6,2,1|67,108,863|
|7|7,6|127||17|17,14|131,071||27|27,5,2,1|134,217,727|
|8|8,6,5,4|255||18|18,11|262,143||28|28,25|268,435,455|
|9|9,5|511||19|19,6,2,1|524,287|29||29,27|536,870,911|
|10|10,7|1,023||20|20,17|1,048,575||30|30,6,4,1|1,073,741,823|
|11|11,9|2,047||21|21,19|2,097,151||31|31,28|2,147,483,647|
|12|12,6,4,1|4,095||22|22,21|4,194,303||32|32,22,2,1|4,294,967,295|





















Depending on the desired operation, other applicable devices may be CD4094, CD4014, CD4021 which are all 8-stage shift registers.
 

## Step Sequencer (under construction)

This circuit for a step sequencer is shown in N. Collins book 'Handmade Electronic Music'. It makes use of the built-in voltage controlled oscillator (VCO) of the [CD4046](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4046 "CD4046") Phase-Locked Loop. The voltage levels of the output pulses of the [CD4022](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/readme.md#cd4022 "CD4022") counter can be scaled down by the potentiometer voltage dividers and are mixed together via the [diodes](https://en.wikipedia.org/wiki/Diode "Diode") D1-D8 (1N4148). The CD4046’s voltage controlled oscillator is then generating a frequency according to the input voltage level. Therefore, each step Q0-Q7 of the CD4022 can be used to produce a single tone.


![Step_Sequencer_Waveform](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Step_Sequencer_Waveform_DSO.jpg)
*Input voltage (blue graph) and VCO frequency (yellow graph) of the CD4046.*
<br>
<br>


A logical high on the 'Clock Inhibit' of the CD4022 stops the counter advancement and hence the sequence. A manual push button switch with a pull down resistor to GND or a control logic circuit can be used to pause the sequence for rhythmic effects. A logical high on the 'Reset' input restarts the counter. Connecting one of the outputs of the counter to the 'Reset' pin shortens the length of the sequence by one in regard to the number of the used output. (Step length = Qx-1, if Qx is connected to 'Reset'). More complex patterns can be created when the reset and the inhibit functionality is dynamically controlled by logic circuits.

A clock source is needed for triggering the CD4022. When the clock is set to an audio frequency, the step sequencer works as a wave shaper.
Pin 5 (Inhibit) of the CD4046 must be set to a logical low for operation. The two resistors R4 and R5 together with the capacitor C1 determine the frequency range of the VCO. A potentiometer and a fixed resitor at pin 11 allow to change the oscillators overall frequency range.



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Step-Sequencer_DARK.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Step-Sequencer_LIGHT.svg">
  <img alt="CMOS step sequencer after N. Collins." src="https://github.com/SCLW/Circuitry-Based-Sound/blob/master/img/Step-Sequencer_LIGHT.svg">
</picture>



## Voltage Starve

"Voltage starve" or "voltage sag" can be used as an unconventional modulation technique for experimental music. It describes the effect that low supply voltage and limited current have on a circuit's behavior. Especially battery powered guitar pedals create unique dynamic distortion when the battery's voltage and current delivering capacity is unstable due to aging factors.

Changing the supply voltage will have different effects on a signal, depending on the actual circuit and the used components. Bypassing capacitors will mitigate these effects. For instance, the hysteresis thresholds in Schmitt trigger elements vary with the supply voltage. Lowering the supply voltage affects the frequency and the signal amplitude of Schmitt trigger oscillators. 

When working with an adjustable power supply or an according circuit, the impacts of limited current and voltage levels around or below the minimum requirements of an IC can be examined. A similar performance can be simulated with a simple series resistor in the power rail. 500Ω - 10kΩ potentiometers may be worth experimenting with to create odd sounds.

# Works

The artistic range of applications for electronic projects in the fields of experimental sound, interactive music and sound art is quite large. The next sections feature works made in the context of this seminar.






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

Marc Bendt  
Bent van den Berg  
Zhen Bian  
Yinxuan Chen  
Hangyan Chen  
Siting Chen  
Haram Choi  
Qianqian	Feng   
Zufilkar	Filandra   
Hongyu Guo  
Jeongmin Han  
Juhee Han  
Anna Helsen  
Jihye Jang  
Hoin Ji  
Minsu Kim  
Florian	Knöbl    
Jung Eun Lee  
Sangyi Lee  
Xingchen Liu  
Su Lu  
Daniel	Lythgoe   
Victoria Mikhaylova  
Jiun-You Ou  
Ruoyi Qiu  
Bob Reinert  
Vivian Reuter  
Arno Schlipf  
Florian Schwarz  
Yifan Su  
Eveline	Vervliet   
Christina Vinke  
Julian Vollmert  
Dakang Wang  
Siting Wang  
Yudong	Wang   
Lutz Ben	Wesch   
Eunchae	Won   
Le Yang  
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

<!--
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

-->
<br>
<br>

## License

The content of this documentation is licensed under the [Creative Commons Attribution 3.0 Unported license](https://creativecommons.org/licenses/by/3.0/ "CC BY 3.0"), software is licensed under the MIT License - see the [LICENSE.md](https://github.com/SCLW/Circuitry-Based-Sound/blob/master/MIT%20License.md) file for details. Copyright remains with the author(s)
<br>
<br>
<br>

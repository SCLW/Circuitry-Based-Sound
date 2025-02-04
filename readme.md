
# Circuitry-Based Sound


![Circuitry-Based Sound ZKM 2023](/Img/CBS2023_ZKM_Jihye-Jang_sm.jpg)
*Group live performance at the ZKM*

<br>
<br>

<!--
![Technical Setup with self built audio electronics, laboratory power supply, mixing desk, and loudspeaker](/Img/Circuitry_Based_Sound_Foto_Yunfei_Zhang.jpg)
*Photo: Yunfei Zhang*
<br>
<br>
-->




"Circuitry-Based Sound" is an artistic workshop at the intersection of electronic music, sound art, and performance. The course provides hands-on skills for building custom musical circuits and modifying existing audio hardware. Participants gain practical knowledge of electronics for sound creation, noise making, and music interaction. The workshop covers soldering, assembling circuits on breadboards and perfboards, and explores applications in audio composition, structured improvisation, live performance, and sound art.

A major focus is on hardware prototyping, including testing and fault finding, with an emphasis on designing electronic instruments, interfacing transducers, and developing alternative controllers. The artistic and practical use of the circuits is also explored and discussed.

Below is a documentation of the workshop's study materials and findings.
<br>
<br>
<br>
<br>

<div align="center">
 
[**TABLE OF CONTENTS**](/readme.md#table-of-contents)
</div>

---

[**INTRODUCTION**](/readme.md#introduction)
  - [Unconventional Electronic Sound](/readme.md#unconventional-electronic-sound)
  - [CMOS Chips for Sound Creation](/readme.md#cmos-chips-for-sound-creation)
  - [Basic Example](/readme.md#basic-example)
  - [Logic Control](/readme.md#logic-control)
<br>
<br>

[**ELECTRONIC COMPONENTS**](/readme.md#electronic-components)
  - [Numerical Index](/readme.md#numerical-index)
<br>
<br>

[**BASIC PRINCIPLES AND APPLICATIONS**](/readme.md#basic-principles-and-applications)
  - [Signal Mixing](/readme.md#mixing)
  - [Passive Filters](/readme.md#passive-filters)
  - [Pull-up and Pull-down Resistors](/readme.md#pull-up-and-pull-down-resistors)
  - [Linear Feedback Shift Register](/readme.md#linear-feedback-shift-register)
  - [Step Sequencer](/readme.md#step-sequencer-under-construction)
  - [Voltage Starve](/readme.md#voltage-starve)
<br>
<br>

[**PHOTOS**](/readme.md#photos)
<br>
<br>

[**MATERIALS**](/readme.md#Materials)
  - [Requirements](/readme.md#requirements)
  - [Bill of Materials](/readme.md#bill-of-materials)
  - [Literature](/readme.md#literature)
  - [License](/readme.md#license)

---


<br>

# Disclaimer

The authors accept no responsibility for any damages arising from or in connection with the use of the information provided on this website. While we strive to ensure that all content is accurate and complete, unintended errors may occur. Users are encouraged to cross-check and verify the information before applying it.
<br>
<br>



# Introduction

![Technical Setup with self built audio electronics, laboratory power supply, mixing desk, and loudspeaker](/Img/Circuitry_Based_Sound_Foto_Yunfei_Zhang.jpg)
*Photo: Yunfei Zhang*
<br>
<br>

Aside from the established way of using electronics to generate and process sound, which can be found in analog synthesizers, there are also unconventional applications of electronics to create sound or experimental music, which will be introduced below. Analog synthesizers apply techniques like [subtractive synthesis](https://en.wikipedia.org/wiki/Subtractive_synthesis "subtractive synthesis") to produce sound. A common concept of the analog signal flow is filtering the output of an oscillator and shaping the overall volume. Variations of this concept can be found in most synthesizers, both analog and digital. Parameters can be altered through control signals. This offers a wide range of musical expression, like tuning oscillators in a 12-tone musical scale or key triggered [envelopes](https://en.wikipedia.org/wiki/Envelope_(music) "envelope") for amplifiers, filters or other effect processors. To obtain these functionalities, circuits of analog synthesizers are relatively complex, involve a high part count and often require precision components.

<!--


Aside from the conventional use of electronics in analog synthesizers to generate and process sound, there are also unconventional applications for creating experimental music and sound, which will be introduced below. Analog synthesizers commonly use techniques like subtractive synthesis, where the signal flow involves filtering the output of an oscillator and shaping its volume.

This concept, with variations, is found in most synthesizers, both analog and digital. Parameters are altered using control signals, enabling a wide range of musical expression, such as tuning oscillators to a 12-tone scale or triggering envelopes for amplifiers, filters, and effects processors. However, achieving these functionalities requires relatively complex circuits, high component counts, and precision parts in analog synthesizers.

-->

### Unconventional Electronic Sound

Another concept of creating sound with electronics derived from techniques like hardware hacking and circuit bending. In particular the use of digital integrated logic circuits outside of their typical field of application is a remarkable approach to build customized instruments for artistic sound production and interactive music. The required components are easy to source and low cost. What makes these types of chips even more handy is that they don't need much external components and wiring. They can be used for generating and processing sound without large expenditure.



### CMOS Chips for Sound Creation


![Various CMOS-chips in SMD and through-hole technology and with different foot prints](/Img/CMOS-chips.jpg)
*Various CMOS chips*
<br>
<br>

A binary logic signal, which encodes 0 and 1 as two distinct voltage levels, can be represented as a square wave. A logic signal that continuously switches between these two voltage states can therefore be interpreted as a square wave—and thus as sound. Certain logic gates can be repurposed as oscillators in this way. In digital systems, this principle is used to generate clock signals, which are essential for synchronizing processes. Logic gates with two inputs compare the signals at their inputs and generate an output based on the corresponding logic function, enabling signal processing and modification. Other logic gates can count sequential square wave pulses, outputting a single pulse per cycle. Some function as frequency dividers, halving the input signal’s frequency. Additionally, various CMOS chips can act as binary-controlled switches. These and many other functions can be understood as modulation effects, which transform or modify the incoming audio signal—represented as a square wave.


The following diagram illustrates the waveform of a square wave and assigns the values 0 and 1 to its two voltage states.
<br>
<br>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Square_Wave_as_Binary_DARK.svg">
  <img alt="Demonstrating the relationship between a square wave and its equivalent binary representation (0s and 1s)." src="/Img/Square_Wave_as_Binary_DARK.svg">
</picture>



[CMOS chips](https://en.wikipedia.org/wiki/4000-series_integrated_circuits/ "4000-series integrated circuits") are designed to execute Boolean functions. Complementary metal–oxide–semiconductor (CMOS) is a technique where p-type and n-type MOSFETs are used for manufacturing logic gates. Voltage levels represent the binary states 0 and 1. Produced as integrated circuits, individual components relate to basic logical functions like [NOT](https://en.wikipedia.org/wiki/Inverter_(logic_gate) "Inverter"), [AND](https://en.wikipedia.org/wiki/AND_gate "AND gate"), [OR](https://en.wikipedia.org/wiki/OR_gate "Or gate"), [NAND](https://en.wikipedia.org/wiki/NAND_gate "NAND gate"), [XOR](https://en.wikipedia.org/wiki/XOR_gate "XOR gate"), [XNOR](https://en.wikipedia.org/wiki/XNOR_gate "XNOR gate") or implement [multiplexers](https://en.wikipedia.org/wiki/Multiplexer "multiplexer"), [counters](https://en.wikipedia.org/wiki/Counter_(digital) "counter"), dividers, [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop") and [registers](https://en.wikipedia.org/wiki/Shift_register "shift register"). When logical operations and their relation to voltage and sound are understood, CMOS-logic chips are an inexhaustible source for unconventional electronic sound. They produce digital signals - square waves - that can be modified, shaped, gated, sequenced, layered, and many more. Combining different logic functions allows generating a multitude of unique sounds and temporal music structures, while they produce the richness of analog sound. These circuits also yield unpredictable behavior, produce rhythmic glitches or digital noise.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Switching_Circuit_DARK.svg">
  <img alt="Boolean logic as switching circuit." src="/Img/Switching_Circuit_LIGHT.svg">
</picture>

 

Logical operations can be implemented as switching circuits with single pole single throw switches representing the input and an LED indicating the result. The switch and the LED can have two distinct states: on and off. The open switch corresponds to a logical 0 and the closed position stands for a logical 1. A lit LED means 1 and a non-lit 0.


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Logic_Gates_DARK.svg">
  <img alt="Illustration of electronic logic gate symbols." src="/Img/Logic_Gates_LIGHT.svg">
</picture>



A truth table is used in Boolean algebra to show all possible values of a logical expression. 

Output comparison of 2-input logic gates:

<br>
<div align="center">

| INPUT A | INPUT B | AND | NAND | OR | NOR | XOR | XNOR |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0` | `0` | 0 | 1 | 0 | 1 | 0 | 1 |
| `0` | `1` | 0 | 1 | 1 | 0 | 1 | 0 |
| `1` | `0` | 0 | 1 | 1 | 0 | 1 | 0 |
| `1` | `1` | 1 | 0 | 1 | 0 | 0 | 1 |
 
</div>
<br>
<br>

Due to its simplicity, CMOS chips can be used for educational reasons, since most of its technical operations can easily be understood and relate to basic electronic knowledge. This subject is also a matter of various publications, most notably [Nicolas Collins'](https://en.wikipedia.org/wiki/Nicolas_Collins "Collins") „Handmade Electronic Music, The Art of Hardware Hacking" (2006). American Composer [David Tudor](https://de.wikipedia.org/wiki/David_Tudor "David Tudor") (1926 - 1996) is considered a pioneer of self-made electronic circuits and instruments, which he used for his compositions. Stanley Lunetta (1937 - 2016), avant-garde composer and artist, incorporated in the 1970s digital electronics into his compositions and sound art sculptures and shared his techniques with other artists. In the experimental music community, CMOS synthesizers are therefore often referred to as "Lunettas".


### Basic Example


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CMOS_Oscillator_Breadboard_DARK.svg">
  <img alt="Simplified depiction of a Schmitt trigger oscillator on a breadboard." src="/Img/CMOS_Oscillator_Breadboard_LIGHT.svg">
</picture>



The „hello world“ of CMOS-Synthesizers as a measure of how simple it is to produce sound is illustrated through the picture above. It shows a [square wave](https://en.wikipedia.org/wiki/Square_wave "square wave") sound generator that can be built with only three components, jumper wires and a power supply:
* inverting [Schmitt trigger](https://en.wikipedia.org/wiki/Schmitt_trigger "Schmitt trigger") IC, e.g. CD40106
* capacitor C
* resistor R

An inverting Schmitt trigger is an active electronic component whose output state can be triggered complementarily through an input signal, while the positive trigger threshold differs from the negative one, which is called hysteresis. Feeding the output back to its input via a resistor R and connecting a capacitor C between the input and ground, known as RC circuit, creates a relaxation oscillator or [astable multivibrator](https://en.wikipedia.org/wiki/Multivibrator#Astable_multivibrator "astable multivibrator"). The resistor limits the current for charging the capacitor and both together determine the [charging time](https://en.wikipedia.org/wiki/RC_time_constant "RC time constant").


<!-- ANIMATED GIF -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Schmitt_Trigger_DARK.gif">
  <img alt="Animated iIllustration of a Schmitt trigger oscillator and its waveforms." src="/Img/Schmitt_Trigger_LIGHT.gif">
</picture>


<br>
<br>

The frequency can be roughly calculated with this formula $f=\frac{1}{T}=\frac{1}{RC ln [(\frac{V_P}{V_N})(\frac{V_{DD}-V_N}{V_{DD}-V_P})]}$, where V<sub>P</sub> is the positive trigger threshold voltage and V<sub>N</sub> the negative trigger threshold voltage.





<br>
<br>

However, manufacturing tolerances of all involved parts make it difficult to achieve exact results based on the formula. Since the field of application is artistic sound production, circuits should be evaluated by ear. But the formula shows that bigger RC values produce lower frequencies and vice versa. The frequency is determined through the capacitor C and the resistor R. Therefore, a [potentiometer](https://en.wikipedia.org/wiki/Potentiometer "potentiometer") instead of the latter enables pitch control. Other ways of controlling the frequency may be inserting [photoresistors](https://en.wikipedia.org/wiki/Photoresistor "photoresistor"), [force-sensitive resistors](https://en.wikipedia.org/wiki/Force-sensing_resistor "FSR") (FSR) or [flex sensors](https://en.wikipedia.org/wiki/Flex_sensor "flex sensor"). Adding circuit points to alter the sound through interaction allows building customized and versatile instruments.


### Logic Control

A logic gate is a single input - output device, designed to carry out a specific [Boolean operation](https://en.wikipedia.org/wiki/Boolean_algebra "Boolean algebra"), mapped to two voltage levels. Over time, the two alternating voltage levels may form a periodic rectangular waveform and the speed of switching between the two levels is perceived as pitch. Aperiodic switching will produce other sonic qualities such as noise or all kinds of texturized sounds. The ratio between the on- and off-states is by default close to 1:1, a 50% [duty cycle](https://en.wikipedia.org/wiki/Duty_cycle "duty cycle"). Further circuitry is needed to change this ratio, which alters the ratio of the amplitudes of the harmonic components to the fundamental.


In digital electronics 2-level logic, [binary numbers](https://en.wikipedia.org/wiki/Binary_number "binary number") are represented by two defined voltage levels that are specified by the used technology and circuit. Everything below a certain voltage threshold level is recognized as 0 and everything above a certain threshold level is recognized as 1. A voltage level in between the two thresholds is not defined or forbidden and will produce false output triggers. CMOS digital inputs have a high impedance and pick up thermal noise voltages if left floating. Unused inputs should be tied to a defined voltage. Other input configurations (e.g. taster, toggle switches,) require [pull-up or pull-down resistors](/readme.md#pull-up-and-pull-down-resistors "pull-up or pull-down"). The two states "0" and "1" are also often referred to as "(logical) high" and "(logical) low", "true" and "false" or "ON" and "OFF". 


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Logic_Signal_DARK.svg">
  <img alt="Common CMOS input voltage levels without and with Schmitt trigger implementation." src="/Img/Logic_Signal_LIGHT.svg">
</picture>



V<sub>IH</sub> is the minimum input voltage that will be interpreted as a logical high, while V<sub>IL</sub> is the maximum input voltage that will be interpreted as a logical low. The region in between is undefined and may trigger unpredictable highs or lows (chattering). This problem is solved by implementing a Schmitt trigger with different thresholds for negative-going and positive-going input voltages, depending on whether the input signal is changing from high to low (V<sub>N</sub>) or low to high (V<sub>P</sub>). When the input is between the two thresholds the output retains its value.


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Square_Wave_DARK.svg">
  <img alt="Analytical description of a square wave logic signal." src="/Img/Square_Wave_LIGHT.svg">
</picture>


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Gated_Oscillator_DARK.svg">
  <img alt="Schematic of a gated square wave oscillator with the CD4093, showing input control and output waveform." src="/Img/Gated_Oscillator_LIGHT.svg">
</picture>



The [square wave](https://en.wikipedia.org/wiki/Square_wave "Square wave") contains only overtones with odd numbered harmonics (⅓, ⅕, ⅐, etc). The relative amplitudes of the harmonics are equal to 1/harmonic number n.

# Building Circuits with Breadboards

Since assembling an electronic circuit on a breadboard does not require soldering (unlike working with printed circuit boards) it allows for quick prototyping and easy modifications. This makes breadboards particularly useful for testing and developing preliminary functional versions of circuit designs, which can then be used to verify circuit behavior and operating points. They serve as temporary platforms for functional verification and feasibility testing, while their flexibility and reusability make troubleshooting easier.

Typically, circuits built on breadboards are not suitable as permanent solutions, as the connections rely solely on spring contacts. These contacts can corrode over time or become loose, leading to unreliable connections. This is especially problematic during transport, as components may detach.

Nevertheless, breadboards are highly effective for DIY electronic music projects, as they allow for rapid prototyping and easy circuit adjustments to match sonic preferences. They can also be expanded with control elements, enabling intuitive sound manipulation and music interaction.


Breadboards are made of plastic and feature a standardized hole grid with metal spring contacts. The grid spacing is 2.54 mm (0.1 inch), making it compatible with most standard electronic components and allowing for easy insertion and interconnection.


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Breadboard_DARK.svg">
  <img alt="How a Breadboard Works: Functional Sections and Internal Wiring" src="/Img/Breadboard_LIGHT.svg">
</picture>


A typical breadboard consists of three main sections:

- **Power Rails:** Located along the outer edges, these two continuous strips are internally connected and typically used to distribute power across the board (usually indicated with the symbols + and - and/or the colors red and blue).
- **DIP Support:** A central gap that separates the two sides of the breadboard, designed to accommodate dual in-line package (DIP) components, such as integrated circuits (ICs).
- **Terminal Strips:** Arranged perpendicularly to the power rails, these rows of interconnected holes on either side of the centerline provide access to the pins of DIP components, enabling circuit connections.

# Identifying IC Pins

Manufacturers provide documentation for integrated circuits (ICs) and other electronic components in so-called datasheets, which describe the components' characteristics and functions. In an IC datasheet, the pinout diagram explains the function of each pin (or terminal) while also providing important information about operating conditions and supply voltage. When using ICs, it is important and highly recommended to have the datasheet readily available to ensure proper implementation of the component.

For Dual In-Line Packages (DIL or DIP ICs), the pins are numbered sequentially. When looking at a DIP IC from above, there is typically a marking or notch on one of the shorter sides of the package, which serves as an orientation guide.

To correctly identify the pin numbering:

- Align the IC so that the notch or marking is at the top.
- Start counting from the first pin on the left side of the notch (Pin 1).
- Continue numbering counterclockwise around the IC.

This standard numbering convention helps ensure correct connections when integrating the IC into a circuit.

CMOS chips often have 14, 16, or 18 pins.
With only few exceptions, the bottom-left pin is typically connected to ground (GND or Vss), while the top-right pin (the last pin) is connected to the positive supply voltage (VDD).


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/GH_IC_Pinout_DARK.svg">
  <img alt="A diagram illustrating how to identify the pinout of an IC and showing the typical power connections of a CMOS chip" src="/Img/GH_IC_Pinout_LIGHT.svg">
</picture>


# Electronic Components

The following is a list of CMOS chips and other integrated circuits used for sound creation and processing. This list will be continuously expanded throughout the seminar. Each chip’s primary applications are outlined, along with a brief explanation. Pinouts, functional diagrams, truth tables, and basic example circuits are also provided. However, these examples do not represent a comprehensive guide. The main objective is to explore variations, modifications, and new creative combinations for experimental sound and music. For detailed specifications, please refer to the manufacturer’s datasheet.

## Numerical Index


- [CD40106](/readme.md#cd40106)
- [CD4093](/readme.md#cd4093)
- [CD4070](/readme.md#cd4070)
- [CD4015](/readme.md#cd4015)
- [CD4022](/readme.md#cd4022)
- [CD4040](/readme.md#cd4040)
- [CD4046](/readme.md#cd4046)
- [CD405x](/readme.md#cd405x)
- [CD4066](/readme.md#cd4066)
- [CD4060](/readme.md#cd4060)
- [CD4013](/readme.md#cd4013)
- [CD4018](/readme.md#cd4018-under-construction)
- [555 Timer](/readme.md#555-timer-under-construction)
- [LM386](/readme.md#lm386---power-operational-amplifier-under-construction)




### CD40106

The inverter is a basic part in digital electronics and performs the logic operation of negation. When the input is connected to ground, the output is pulled to V<sub>DD</sub> and vice versa. The CD40106 hex Schmitt trigger inverter offers six separate inverters in one chip. The Schmitt trigger action permits unlimited rise and fall times on the input. The chip can be wired externally to build one or more square wave oscillators (see illustration). When using a potentiometer for frequency control, a resistor should be placed in series in order to prevent too low resistance between output and input.

*Applications:*
* Square Wave Generator
* Inverting Buffer



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD40106_DARK.svg">
  <img alt="Pinout of the CD40106 IC and a schematic of a CMOS oscillator built with CD40106 hex Schmitt trigger inverter." src="/Img/CD40106_LIGHT.svg">
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4093_Button_DARK.svg">
  <img alt="Pinout of the CD4093 IC and a schematic of an oscillator built with a CD4093 CMOS chip and controllable by a push button." src="/Img/CD4093_Button_LIGHT.svg">
</picture>



Oscillators built with 2 input NAND Schmitt triggers can be switched on and off manually by using a push button. If the push button is not pressed (normally open) the logical low at the second input will always cause a logical high at the output, no matter which state is present at the other input (see NAND truth table). The image above shows how to set up a normally open push button as an ON switch to control the sound. A [pull down resistor](/readme.md#pull-up-and-pull-down-resistors) defines the logic state at the input when the push button is open. When the push button is closed, the power supply produces a logical high and the NAND gate oscillates. This way, the second input acts as a control input for gating the oscillator. Instead of a manually controlled push button, a logic signal can be applied to the second input.


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4093_Gated_DARK.svg">
  <img alt="Pinout of the CD4093 IC and a schematic of an oscillator built with a CD4093 CMOS chip which in turn is controlled by a second oscillator configuration of the same chip. This is called a gated oscillator." src="/Img/CD4093_Gated_LIGHT.svg">
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4070_DARK.svg">
  <img alt="Pinout of the CD4070 IC and a schematic that shows sigital frequency mixing with the said chip." src="/Img/CD4070_LIGHT.svg">
</picture>


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/XOR_DARK.svg">
  <img alt="Timing diagram of the CD4070 XOR gate with two suqare waves as inputs, showing the resulting output waveform" src="/Img/XOR_LIGHT.svg">
</picture>

Truth table for XOR (CD4070)

|A|B|Y = A XOR B|
|----|----|:----:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

<!-- 
Truth table for XNOR (CD4077)

|A|B|Y = A XNOR B|
|----|----|:----:|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|1|
-->

[CD4070 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4077b.pdf?ts=1606308007892&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4070")
<br>
<br>


### CD4015

CD4015 IC consists of two four stage shift registers.

A shift register is built of a series of interconnected [flip-flops](https://en.wikipedia.org/wiki/Flip-flop_(electronics) "flip-flop"). A flip-flop or latch is a bistable multivibrator circuit. This means it has two stable states which represent either 0 or 1. The state of a flip-flop can be controlled by a clock. The value to be stored is based on the signal's input state at the transition of the clock signal. A flip-flop is used to store 1 bit. In a shift register the incoming serial input data **D** is transferred to a parallel output register **Qn**. More specifically, when a memory content is stored in the first flip-flop, it is shifted to the next one, synchronized to the rising edge of a dedicated clock signal **CL**. A logical high at the reset pin is setting all outputs to zero. The reset pin should be set to low for a continuous operation.


*Applications:*
* Sequencer
* Noise Generator
* Linear-feedback Shift Register ([LFSR](/readme.md#linear-feedback-shift-register "LFSR"))

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4015_DARK.svg">
  <img alt="Pinout of the CD4015 IC and a schematic symbol describing the functions of the two 4-stage shift registers included in one chip." src="/Img/CD4015_LIGHT.svg">
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




*Applications:*
* Sequencer
* Staircase Wave Form Generator
* Wave Shaper

<!-- IMAGE -->


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4022_DARK.svg">
  <img alt="Pinout of the CD4022 IC and a schematic symbol describing the functions of the counter/divider." src="/Img/CD4022_LIGHT.svg">
</picture>



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4022_Outputs_DARK.svg">
  <img alt="CD4022 timing diagram." src="/Img/CD4022_Outputs_LIGHT.svg">
</picture>




[CD4022 Data Sheet](https://www.ti.com/lit/ds/schs027c/schs027c.pdf?ts=1599062824246&ref_url=https%253A%252F%252Fwww.google.com%252F "CD4022")
<br>
<br>

### CD4040

This IC performs frequency division and comes with 12 outputs in the CD4020 and the CD4040 versions and 7 outputs in the CD4024 version, whereby the CD4020 is a 14-stage device. Output stages 2 and 3 (divide by 4 and 8) are not accessible. The CD4024 has 3 pins without internal connection (pin 8, 10, 13). If a square wave is applied to the input, each output creates square waves at half the frequency of its preceding output, at which the first output Q1 applies its division to the input signal and oscillates at a rate at one half, Q2 at one quarter, Q3 at one eighth Q4 at one sixteenth and so on. Several units can be cascaded for higher counting.

Control input "reset" triggers all output stages to "low". For continuous frequency division it should be kept at a logical low.


*Applications:*
* Frequency Divider
* Sub Octave Generator
* Representation of Binary Numbers

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4040_DARK.svg">
  <img alt="Pinout of the CD4040 IC and a schematic symbol describing the functions of the frequency divider." src="/Img/CD4040_LIGHT.svg">
</picture>




In terms of generating sound, each output producing one octave lower than its previous output, respectively input.


The timing diagram shows the relation of voltage levels between all outputs of the CD4024 IC, a 7-output stage version:

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4040_Outputs_DARK.svg">
  <img alt="CD4040 timing diagram." src="/Img/CD4040_Outputs_LIGHT.svg">
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4046_DARK.svg">
  <img alt="Pinout of the CD4046 IC and a schematic of the phase locked loop circuit built with the CD4046." src="/Img/CD4046_LIGHT.svg">
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4051_DARK.svg">
  <img alt="Pinout of the CD4051 IC and a schematic symbol representing the digitally controlled single pole octal throw function." src="/Img/CD4051_LIGHT.svg">
</picture>


<!--
<img src=/Img/CD4051_animated.gif>
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4052_DARK.svg">
  <img alt="Pinout of the CD4052 IC and a schematic symbol representing the digitally controlled double-pole quad-throw function." src="/Img/CD4052_LIGHT.svg">
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4053_DARK.svg">
  <img alt="Pinout of the CD4053 IC and a schematic symbol representing the digitally controlled CMOS chip, containing three single-pole double-throw CMOS switches." src="/Img/CD4053_LIGHT.svg">
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4066_DARK.svg">
  <img alt="Pinout of the CD4066 IC and a schematic symbol representing the digitally controlled CMOS chip, containing four single-pole single-throw switches." src="/Img/CD4066_LIGHT.svg">
</picture>



<!--
The following example shows a single pole double throw (SPDT) configuration built with two bilateral switches of the CD4066 (lower section, SW2 and SW3). SW1 is set up to do logic and acts as an inverter: A high at the control input makes a connection to ground and "pulls" the output node down, while a logical low opens the switch and the pull-up resistor ensures a high at the same node. The non-inverted and the inverted control signals are then connected to the respective control inputs of the remaining switches SW2 and SW3. If one switch is open, the other is closed and vice versa. A common signal will be routed to either one of the outputs. This setup can be used for ping-pong stereo effects. Interchanging the input and output in this SPDT example makes a signal selector. The CD4053 contains already three SPDT switches.
-->

<!--
<img src=/Img/CD4066_Ping-pong_Stereo.jpg>
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4060_DARK.svg">
  <img alt="Pinout of the CD4060 IC (on the left) and a schematic symbol representing the individual gates of the frequency divider (middle section). On the right is a circuit schematic of the RC oscillator circuit built with the CD4060." src="/Img/CD4060_LIGHT.svg">
</picture>


[CD4060 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4060b.pdf "CD4060")

<br>
<br>


### CD4013
 
The CD4013 IC flip-flop is called a D flip-flop type to characterize its behavior, while D stands for "data" or "delay". It contains two identical D flip-flop arrangements. The device stores a digital state 0 or 1, which is accessible at the output **Q**. The second output **/Q** presents the inverse of **Q**. The control input **Clock** transfers the input state **D** to the output **Q** respectively **/Q**. The CD4013 is positive-edge-triggered, which means that the positive-going transition of a clock impulse triggers the device to hold the state that is present at the input and provides it at the output until the next positive-going clock signal. The additional control inputs **Set** and **Reset** have priority over the clock. With a high level on the **Set** input, the output follows its state and goes low with a high level on the **Reset** input, ignoring **D** and **Clock**.



*Applications:*
* Frequency Divider
* Counter
* Toggle Switch


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4013_DARK.svg">
  <img alt="Pinout of the CD4013 IC (on the left) and a schematic symbol representing the individual gates of the CD4013 IC flip-flop (right side)." src="/Img/CD4013_LIGHT.svg">
</picture>


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
* Rhythm/Chord Generator



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/CD4018_DARK.svg">
  <img alt="On the left: Pinout of the CD4018 IC. In the middle: a schematic symbol representing the individual gates of the divide-by-'N' counter. On the right: Circuit configuration for building a divide-by-3 counter." src="/Img/CD4018_LIGHT.svg">
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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Divide_by_odd_DARK.svg">
  <img alt="Timing diagram of the CD4018 CMOS counter/divider demonstrating odd division ratios (÷3, ÷5, ÷7)." src="/Img/Divide_by_odd_LIGHT.svg">
</picture>

[CD4018 Data Sheet](https://www.ti.com/lit/ds/symlink/cd4018b.pdf?ts=1610571153497&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FCD4018B "CD4018")
<br>
<br>

### 555 Timer

Note: The bipolar version (NE555) and the CMOS version (TLC555, LMC555) have the same pinout and are exchangeable. The CMOS version consumes significantly less power. Its name derives from the three 5kΩ resistors that form a voltage divider network. This IC generates output pulses for precision timing or works as an oscillator with adjustable duty cycle. The timing function can be configured with just a few external components.

*Applications:*
* Frequency Divider
* Timer
* Pulse Delay
* Square Wave Generator
* Pulse Width Modulator

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/555_Timer_DARK.svg">
  <img alt="On the left: Pinout of the 555 timer. On the right: Functional diagram of the internal circuit of the 555 timer." src="/Img/555_Timer_LIGHT.svg">
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
  <source media="(prefers-color-scheme: dark)" srcset="/Img/555_Astable_DARK.svg">
  <img alt="Schematic of the 555 timer IC connected as an astable multivibrator." src="/Img/555_Astable_LIGHT.svg">
</picture>

In the astable configuration or multivibrator mode, the circuit generates a string of pulses by retriggering itself. Different values for $R_A$ and $R_B$ allow for changing the ratio of the high time and the low time. A low at reset pin 4 stops the oscillation.
The time to complete one cycle (high and low) can be calculated with $T=  ln(2) \cdot (R_A + 2R_B)C$ and the frequency with $f=\frac{1}{T}$.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/555_Mono_Timing_DARK.svg">
  <img alt="Schematic of the 555 timer IC for monostable operation including timing diagram." src="/Img/555_Mono_Timing_LIGHT.svg">
</picture>




For mono stable operation, a negative going pulse at the trigger input causes the output to go high for a defined amount of time (one shot). A second pulse within that time period has no effect on the output pulse and will be ignored. This circuit can be used for debouncing switches. The time the output stays high is set through the RC circuit and can be calculated with $T_H = ln(3) \cdot R_1C_1  \approx 1.1 \cdot R_1 C_1$.

[LMC555 Data Sheet](https://www.ti.com/lit/ds/symlink/lmc555.pdf?ts=1609974121158&ref_url=https%253A%252F%252Fwww.google.com%252F "LMC555")  
[TLC555 Data Sheet](https://www.ti.com/lit/ds/symlink/tlc555.pdf "TLC555")
<br>
<br>

<!-- 

this link shows a circuit for an edge triggered monostable multivibrator by Jim Keith  
the duration of the output pulse is independent of the duration of the trigger pulse  
https://www.electroschematics.com/edge-triggered-555-monostable-multivibrator/ 

-->

### LM386 - Power Operational Amplifier (under construction)

Although not part of the CMOS logic family this ubiquitous power op amp is a very versatile component when it comes to amplification or driving small speakers.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/LM386_DARK.svg">
  <img alt="On the left: Pinout of the LM386 - Power Operational Amplifier IC. On the right: Circuit diagram showing the external configuration of the LM386 with a amplification factor of 200" src="/Img/LM386_LIGHT.svg">
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

There are various ways of mixing signals together. Using CMOS chips like the XOR CD4070 works for digital signals. If more than two signals should be mixed or merged, several logic gates can be chained together. Even though the resulting signal is not the sum of the source signals but some modulated result, the output signal is still compatible with digital electronics. This is not the case with active and passive mixing, which alters the amplitude of the output. Active mixing involves components, such as operational amplifiers, that need a power supply. Passive mixing works without an additional power supply, but introduces a voltage drop.

### Passive Mixing

Passive mixing is a very simple method that can be accomplished by using resistors for each source. The mixing resistors work as a voltage divider network and lower the amplitude of each signal. Therefore, the passive mixer doesn't give the sum of all input signals but the [average](https://en.wikipedia.org/wiki/Millman%27s_theorem "Millman's theorem"). Small resistance values will drain more current and create distortion. Good values are between 10kΩ - 50kΩ. The advantage of this method is its low part count. To avoid attenuation and interaction between the signals and to obtain individual gain control, active mixing using an operational amplifier is preferred.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/passive_mixing_DARK.svg">
  <img alt="On the left: Schematic diagram of a passive mixer with resistors. On the right: The formula to calculate the output voltage according to Millman's theorem." src="/Img/passive_mixing_LIGHT.svg">
</picture>


### Active Mixing

For most audio applications it is desired to control the portion of each input signal in the sum of the output mix. For this, another class of active electronic components can be used, the [operational amplifier](https://en.wikipedia.org/wiki/Operational_amplifier "op amp") (op amp). The basic wiring is shown below. 


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Active_Mixing_DARK.svg">
  <img alt="On the left: Pinout of the LM 358 operational amplifier. On the right: Schematic for a single supply active mixer." src="/Img/Active_Mixing_LIGHT.svg">
</picture>


By adding voltage dividers or potentiometers, it allows for gain control over every individual input. Besides its function as a mixer, it can also be used to achieve the desired output gain by modifying the feedback resistor R<sub>F</sub> in relation to the input resistors R<sub>IN</sub> of each input. The minus sign in the formula indicates that the output voltage is inverted. To undo inversion, a second stage following the shown circuit can be used.

$V_{OUT} = - [ \frac{R_F} {R_{IN1}} V_{IN1} + \frac{R_F} {R_{IN2}} V_{IN2} + \frac{R_F} {R_{IN3}} V_{IN3} + etc.]$  
$- V_{OUT} = \frac{R_F} {R_{IN}} [V_{IN1} + V_{IN2} + V_{IN3} + etc.]$ if all $R_{IN}$ are the same.


It should be underlined that the example shown is a single supply based circuit, which is uncommon for audio mixing where usually symmetrical dual supply voltages are used. It is important therefore to create a reference voltage of 1/2 V<sub>CC</sub> at the non-inverting input. When working with logic circuits, the signals are almost at the supply levels. Even with rail-to-rail op amps caution is required to keep the summed signals below the working range of the op amp.




## Passive Filters

Tone control, modifying the frequency spectrum of a signal or creative equalization are very important processes when working with audio. A filter is frequency-selective and passes only a desired range of frequencies, which is called the pass band. Outside of this pass band, frequencies are attenuated or ideally completely reduced. The boundary between pass and stop band is called cutoff frequency. The simplest way to shape an electronic signal is the use of a combination of resistor and capacitor, an RC element. This forms a first order filter. The circuit can be considered as a frequency dependent potential divider. A band-pass filter can be built with two RC elements, as a combination of a high-pass and a low-pass configuration. Since no amplifying components are involved, the amplitude of the output is lower than the input amplitude. When a filter is designed with two passive components, the transition from pass to stop band is rather smooth. For instance, a first order low-pass filter will have a 6dB/octave roll-off with increasing frequency. Unfortunately, the properties of passive filters are not sufficient to achieve a higher steepness or musical effects like resonance, which requires active filter designs. However, the simplicity and the low part count make this method very attractive for subtle tone control.



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Passive_Filter_DARK.svg">
  <img alt="On the upper left side: schematic of a passive low-pass filter. On the upper right side: Diagram showing the frequency response of an analog, passive low-pass filter. On the bottom left side: schematic of a passive high-pass filter. On the bottom right side: Diagram showing the frequency response of an analog, passive hight-pass filter" src="/Img/Passive_Filter_LIGHT.svg">
</picture>


# Potentiometers
A potentiometer is a passive, mechanical component enclosed in a housing. It consists of a resistive track and a movable contact called the wiper. The wiper’s position along the resistive track can be adjusted using an actuator.

The three terminals of a potentiometer provide access to:

- The two ends of the resistive element (fixed resistance between them)
- The wiper, which moves along the resistive track to divide the total resistance into two separate resistance values
  
Potentiometer Structure
<img src=/Img/Potentiometer_Actuator.jpg>

a) Housing, b) Terminals, c) Actuator, d) Resistive track, e) Wiper


Potentiometer as a Variable Resistor
If only one end terminal and the wiper are used, the potentiometer functions as a variable resistor, where the resistance varies based on the wiper’s position.

Potentiometer as a Voltage Divider
By connecting a voltage source (e.g., supply voltage or signal) to one of the outer terminals and ground (GND) to the other outer terminal, the potentiometer acts as a variable voltage divider. The output voltage can be tapped from the middle (wiper) terminal and adjusted by turning the actuator.

For example, as the wiper moves from one end to the other, the output voltage scales continuously from minimum to maximum—making this configuration ideal for applications such as volume control.


<img src=/Img/Volume_Control_Variable.jpg>




<!--
## Touch Circuits

Most approaches for touch-sensitive circuits make use of the resistance or conductivity of the human skin to alter the voltage of one section within a circuit compared to a defined voltage reference. A simple touch switch is based on a NAND logic gate with one of the inputs connected to V<sub>DD</sub> and the other connected in a pull-up configuration via a high value resistor (several MΩ) to V<sub>DD</sub> . A layout for a touch point consists of two conductive areas, electrically separated but close together, where one part is connected to the pulled-up input and the second part is connected to ground. Without touching the conductive area, both logic inputs are high. When a finger is shorting the touch point, the finger's resistance forms a voltage divider together with the pull-up resistor. The resistance of the human skin varies greatly depending on conditions like humidity. Values from several thousands to more than 100kΩ can be assumed. The resulting voltage at the respective input is fairly low and equates a logical 0. In a NAND gate, this condition forces the output to go high, as long as both inputs are different.


<img src="/Img/Resistive_Touch.jpg">



The piezo electric effect describes that a voltage is generated when a mechanical strain is applied to specific crystalline or ceramic materials. They are commercially manufactured as small discs for various shock/impact sensing applications and loudspeakers, since the inverse piezo electric effect is causing the material to vibrate when an electrical audio signal is applied. A comparator can compare the voltage of the piezo with a reference threshold voltage level. If the voltage level generated by the piezo disc exceeds or falls below the reference threshold, the comparator circuit outputs either a high or a low. 

<img src="/Img/Piezo_Trigger_Comparator.jpg">

Most voltage comparators use open-collector output stages. If the inverting input has a higher potential than the non-inverting input, the output transistor is open and together with the pull-up resistor, a dedicated trigger impulse is generated.


For many applications, the rather short voltage spike of a piezo element needs to be transformed into a pulse with a determined on-time period. This can be done with a  mono stable multivibrator. It remains in this state for a time determined by the circuitry, then it flips back to its initial state. In this case, the comparator circuit of the 555 Timer can be used instead of a regular comparator. 



Another approach for sensing a touch or the proximity of human fingers or hands is based on capacitance. In CMOS circuits it can be used for controlling pitch. This method of touch control uses the parasitic capacitance between two conductive areas (electrodes) within a circuit. When a high frequency is applied to the two conductive areas, they create an electric field that stores opposite electric charges and act like plates of a capacitor. The electrodes are placed in parallel to a capacitor that forms an RC network together with a resistor. The RC network in turn defines the time constant of an astable multivibrator. When a finger or stylus is brought in close proximity to the electric field, it changes the capacitance and therefore the frequency of the multivibrator. When the electrodes are touched, the finger or stylus changes the dielectric constant. The dielectric is the material between the electrodes. The alterations of capacitance is linear to the force of the touch. The electrodes should be insulated with conformal coating or a thin adhesive strip.

<img src="/Img/Capacitive_Touch_02_edit.JPG">


The [CD4060](/readme.md#cd4060 "CD4060") has a built-in oscillator configuration that can be used to generate such a high frequency that is applied to, for example, two copper areas. The output is then fed into the binary counter function for frequency division to generate an audio signal. Various forms of electrodes had been tested using thin copper strips using a cutting plotter.

<img src="/Img/Touch-Sensing_Diagram.jpg">

-->


### Pull-up and Pull-down Resistors

When external circuits or devices are added to a logic input, care must be taken to keep the inputs in a defined state. When switches or transistors are used to control a logic gate, they can physically disconnect the inputs. For example, when a normally-open push button is in its default position, the high impedance input is open. This causes the pin to act like an antenna that is very susceptible to electromagnetic noise and forces the output to do unwanted operations like generating random highs or lows. This is called "floating" and introduces undesired effects.



<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/pull-up_pull-down_DARK.svg">
  <img alt="Schematic of pull-up and pull-down resistors with logic gate inputs. Left: Pull-up configuration. Right: Pull-down configuration." src="/Img/pull-up_pull-down_LIGHT.svg">
</picture>




To avoid this unpredicted behavior, a resistor should be connected to ground or to the high voltage, so that the input pin will see a defined state even when nothing else is connected, for example when a switch is opened. The pin will be able to accept an input signal when the switch is closed. A connection to V<sub>CC</sub> is called "pull-up" and a connection to ground "pull-down". For CMOS-logic, the resistor values can be several thousand ohms.

Even unused logic gates can cause problems since coupled-in interference voltages result in unwanted triggers and excess current draw. If a proper operation is desired, all unused inputs should not be left floating and connected together to GND or V<sub>CC</sub>.

### Linear Feedback Shift Register

A linear feedback shift register (LFSR) can be used for generating deterministic pseudorandomness. In terms of electronic sound production it can be used to build a noise source. An LFSR consists of n numbers of flip-flops which are connected in series to form a shift register as described for the [CD4015](/readme.md#cd4015). This shift register is controlled by a clock that triggers the shift process. Two junctions at a specific position within that chain of flip-flops are directed into an XOR logic gate. The resulting value is fed back into the first register. The number of stages can be extended by connecting multiple devices. The produced values are determined by the shift register's current states and total length. Since the states are finite it will repeat after a certain number of steps. The goal is to choose those taps that form the longest possible sequence of zeros and ones before they repeat. Other implementations of an LFSR exist and work similarly. To activate an LFSR each stage needs to be loaded with an initial value. This is called the seed. By using an XOR function for the feedback, having the value 0 in all flip-flops is forbidden. By using an XNOR function it is forbidden to set all flip-flops to 1. A maximum-length sequence is therefore 2<sup>n</sup> - 1. No matter if XOR or XNOR functions are used, the sequences will have the same length. The duration of one cycle is determined by the clock frequency. When looked at a shift register from the viewpoint of a musician, the long LFSR arrangements will create white and pink noise when controlled with a high frequency (several ten thousands of hertz). Shorter cycles produce grainy tones, stuttering textures or short noise loops.

<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/basic_LFSR_DARK.svg">
  <img alt="Simplified schematic of an LFSR." src="/Img/basic_LFSR_LIGHT.svg">
</picture>




The Xilinx application note [XAPP210](https://www.xilinx.com/support/documentation/application_notes/xapp210.pdf "Xilinx application note XAPP210") (V1.3) and the Maxim Integrated (now Analog Devices) application note [APP4400](https://pdfserv.maximintegrated.com/en/an/AN4400.pdf "application note APP4400") (Jun 30, 2010) show tables for maximum length sequences, which are presented here for up to 32 bits:

|n|taps from|length| |n|taps from|length| |n|taps from|length|
|:---|:---|---:|-|:---|:---|---:|-|:---|:---|---:|
|3|3,2|7||13|13,4,3,1|8,191||23|23,18|8,388,607|
|4|4,3|15||14|14,5,3,1|16,383||24|24,23,22,17|16,777,215|
|5|5,3|31||15|15,14|32,767||25|25,22|33,554,431|
|6|6,5|63||16|16,15,13,4|65,535||26|26,6,2,1|67,108,863|
|7|7,6|127||17|17,14|131,071||27|27,5,2,1|134,217,727|
|8|8,6,5,4|255||18|18,11|262,143||28|28,25|268,435,455|
|9|9,5|511||19|19,6,2,1|524,287||29|29,27|536,870,911|
|10|10,7|1,023||20|20,17|1,048,575||30|30,6,4,1|1,073,741,823|
|11|11,9|2,047||21|21,19|2,097,151||31|31,28|2,147,483,647|
|12|12,6,4,1|4,095||22|22,21|4,194,303||32|32,22,2,1|4,294,967,295|







Depending on the desired operation, other applicable devices may be CD4094, CD4014, CD4021 which are all 8-stage shift registers.
 

This video displays an excerpt of a maximum sequence length of 2147483647 bits, generated with a 31 bit long shift register and the 28th tap. The clock rate is 5 Hz. 



https://github.com/SCLW/Circuitry-Based-Sound/assets/51890764/fa4ba6e8-b892-4d65-845a-6749760b0387




## Step Sequencer (under construction)

This circuit for a step sequencer is shown in N. Collins book 'Handmade Electronic Music'. It makes use of the built-in voltage controlled oscillator (VCO) of the [CD4046](/readme.md#cd4046 "CD4046") Phase-Locked Loop. The voltage levels of the output pulses of the [CD4022](/readme.md#cd4022 "CD4022") counter can be scaled down by the potentiometer voltage dividers and are mixed together via the [diodes](https://en.wikipedia.org/wiki/Diode "Diode") D1-D8 (1N4148). The CD4046’s voltage controlled oscillator is then generating a frequency according to the input voltage level. Therefore, each step Q0-Q7 of the CD4022 can be used to produce a single tone.



![Step_Sequencer Waveform](/Img/Step_Sequencer_Waveform_DSO.jpg)
*Input voltage (blue graph) and VCO frequency (yellow graph) of the CD4046.*
<br>
<br>




A logical high on the 'Clock Inhibit' of the CD4022 stops the counter advancement and hence the sequence. A manual push button switch with a pull down resistor to GND or a control logic circuit can be used to pause the sequence for rhythmic effects. A logical high on the 'Reset' input restarts the counter. Connecting one of the outputs of the counter to the 'Reset' pin shortens the length of the sequence by one in regard to the number of the used output. (Step length = Qx-1, if Qx is connected to 'Reset'). More complex patterns can be created when the reset and the inhibit functionality is dynamically controlled by logic circuits.

A clock source is needed for triggering the CD4022. When the clock is set to an audio frequency, the step sequencer works as a wave shaper.
Pin 5 (Inhibit) of the CD4046 must be set to a logical low for operation. The frequency range of the CD4046 VCO can be set via the two resistors connected between pin 12 and ground and pin 11 and ground. According to the schematic below, a rough approximation can be calculated with the following formula:

$f_{min} =  \frac{1} {{R_5}(C_1 + 32 pF)}$  
$f_{max} =  \frac{1} {({R_4}+VR)(C_1 + 32 pF)} + f_{min}$  

The output of the VCO can be gated with the clock source through a CMOS switch, e.g. CD4066. 


<!-- IMAGE -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/Img/Step-Sequencer_DARK.svg">
  <img alt="Schematic of a CMOS step sequencer after N. Collins." src="/Img/Step-Sequencer_LIGHT.svg">
</picture>



Bill of Material:  

| Designator  | Description | Value |
| ------------- | ------------- | ------------- |
| D1, D2, ... (for each step)| Diode | 1N4148  |
| VR | Potentiometer $f_{max}$ | 100K |
| VR1, VR2, ... (for each step)| Potentiometer | 100K |
| R1*, R2* | Resistor |1K - 10K |
| R3 | Resistor  | 100K |
| R4 | Resistor $f_{max}$  |10K |
| R5 | Resistor $f_{min}$ | |
| C1 | Capacitor | 100nF |
| SW1, SW2 (optional) |push button or toggle switch| on - off |
| CD4022 | Counter | |
| CD4046 | PLL | |
| Clock |  Clock Generator (eg. CD40106) | |

## Voltage Starve

"Voltage starve" or "voltage sag" can be used as an unconventional modulation technique for experimental music. It describes the effect that low supply voltage and limited current have on a circuit's behavior. Especially battery powered guitar pedals create unique dynamic distortion when the battery's voltage and current delivering capacity is unstable due to aging factors.

Changing the supply voltage will have different effects on a signal, depending on the actual circuit and the used components. Bypassing capacitors will mitigate these effects. For instance, the hysteresis thresholds in Schmitt trigger elements vary with the supply voltage. Lowering the supply voltage affects the frequency and the signal amplitude of Schmitt trigger oscillators. 

When working with an adjustable power supply or an according circuit, the impacts of limited current and voltage levels around or below the minimum requirements of an IC can be examined. A similar performance can be simulated with a simple series resistor in the power rail. 500Ω - 10kΩ potentiometers may be worth experimenting with to create odd modulation effects.

<!-- the content of this sections needs to be edited-->
# Photos

The artistic range of applications for electronic projects in the fields of experimental sound, interactive music and sound art is quite large. This section gives some impressions of the works made in the context of this seminar.

<!--
<br>

![Circuitry-Based Sound Langa 2024](/Img/Workshop_Langa_2024.jpg)
*Workshop preparations at Langa, Cape Town (ZA) 2024*

-->

<br>

![Circuitry-Based Sound !Khwa ttu 2024 2024](/Img/!Khwa_ttu_2024.jpg)
*Hybrid electronic group performance, integrating traditional African instruments at !Khwa ttu (ZA) 2024*

<br>

![Live electronics with DIY synthesizer at ZKM 2024](/Img/Yunfei_ZKM_2024.jpg)
*Live electronics with DIY synthesizer at ZKM 2024*

<br>

![Self-built CMOS synthesizer](/Img/Yunfei_Setup_Kinemathek_2022.jpg)
*Self-built CMOS synthesizer at Kinemathek Karlsruhe 2022*

<br>

<!--
![Circuitry-Based Sound](/Img/CBS.jpg)
*Photo: Yunfei Zhang*
-->

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



## Bill of Materials (BoM)

This [BOM](/BOM/Readme.md#bill-of-material "Bill of Material") helps to source necessary components for electronic art projects and self-built instruments.




## Artists

Circuitry-Based Sound are:

Marc Bendt<br>
Bent van den Berg<br>
Fangchao Bi<br>
Zhen Bian<br>
Yinxuan Chen<br>
Hangyan Chen<br>
Siting Chen<br>
Haram Choi<br>
Mark Damian<br>
Thabisa Dinga<br>
Kurt Diedericks<br>
Tobias Ehrhardt<br>
Jung Eun Lee<br>
Damiana Facen<br>
Bi Fangchao<br>
Qianqian Feng<br>
Zufilkar Filandra<br>
Hongyu Guo<br>
Jeongmin Han<br>
Juhee Han<br>
Anna-Lina Helsen<br>
Keita Hori<br>
Jihye Jang<br>
Hoin Ji<br>
Minsu Kim<br>
Florian Knöbl<br>
László Kőrösi<br>
Sangyi Lee<br>
Xingchen Liu<br>
Su Lu<br>
Daniel Lythgoe<br>
Ziyang Ma<br>
Mqhorhana Magqaza<br>
Simphiwe Matole<br>
Jason Mendiola<br>
Victoria Mikhaylova<br>
Lakheni Ntsodo<br>
Jiun-You Ou<br>
Isabella Panigada<br>
Azile Plaatjies<br>
Ukwanda Plaatjies<br>
Pavel Polenz<br>
Max Pospiech<br>
Ruoyi Qiu<br>
Bob Reinert<br>
Vivian Reuter<br>
Arno Schlipf<br>
Dario Schmid<br>
Florian Schwarz<br>
Yifan Su<br>
Anna Szilágyi<br>
Eveline Vervliet<br>
Christina Vinke<br>
Julian Vollmert<br>
Aaron Wagner<br>
Niklas Wallbaum<br>
Dakang Wang<br>
Yudong Wang<br>
Lutz Ben Wesch<br>
Eunchae Won<br>
Le Yang<br>
Sayuki Yoneda <br>
Jiahui Yong<br>
Huiyeon Yun<br>
Rui Zhang<br>
Yunfei Zhang<br>
Xinyi Zhao<br>
Yange Zheng<br>
Pei Zhou<br>




**Lorenz Schwarz** - *lecturer*
<br>
<br>
<br>





## Acknowledgment

Thanks to Dr. Paul Modler, Dizu Plaatjies, Dr. John Richards, Theo Herbst, Dr. Paul Rommelaere, and Holger Förterer.
<br>
<br>
<br>

## Literature

Anderton, Craig. *Electronic Projects for Musicians.* Amsco, 1980.

Barlow, Klarenz. *On Musiquantics.* Bereich Musikinformatik, Musikwissenschaftliches Institut, Johannes Gutenberg-Universität Mainz, 2012.   

Brindley, Keith. *Starting Electronics.* Newnes, 2011.

Collins, Nicolas. *Handmade Electronic Music: The Art of Hardware Hacking.* Taylor & Francis, 2009.

Horowitz, Paul and Winfield Hill. *The art of electronics.* Cambridge University Press, 2021.

Lancaster, Don. *Das CMOS-Kochbuch.* IWT-Verlag, 1980.

Maxfield, Clive. *Bebop to the Boolean Boogie: An Unconventional Guide to Electronics.* Newnes, 2003.

Roads, Curtis. *Computer Music Tutorial.* The MIT Press, 1996.

Self, Douglas. *Small Signal Audio Design.* Focal Press, 2020.

## Links

Below are a few links to resources from across the internet on topics of relevance to audio electronic and Synth DIY as well as inspiring websites from artists and researchers:

**Nicolas Collins** - Sound artist, composer and performer of electronic music.  
https://www.nicolascollins.com  

**Handmade Electronic Music** - Hands-on guide to DIY electronic instruments by Nicolas Collins.  
www.HandmadeElectronicMusic.com  

**Klarenz Barlow** -  Pioneer and celebrated composer in the field of computer music and influential teacher.   
http://clarlow.org/texts   

**Eberhard Sengpiel** - Sound engineer, musician, lecturer. Sound studio and audio calculations, audio and acoustics conversions.  
http://www.sengpielaudio.com  

**John Richards** - British musician and artist. Self-made instruments, installations and sound projects with electronics.  
https://www.dirtyelectronics.org/about.html  

**audiodiwhy** - DIY music technology, programming.  
https://audiodiwhy.blogspot.com  

**Electric Druid** - About audio electronics and analogue synthesizers.  
https://electricdruid.net  

**Synthesizer DIY website of René Schmitz**  
https://www.schmitzbits.de  

**Elliott Sound Products** - Professional results for the Do-It-Yourself enthusiast.  
https://sound-au.com  

**The Institute of Sonology** - Informational website from the Royal Conservatoire in Den Haag about electronics for art and education.  
https://electronics.koncon.nl  

**Adrian Freed** - Former Research Director of UC Berkeley's Center for New Music and Audio Technologies (CNMAT).  
Ideas, projects, examples regarding creative and artistic use of electronics in sound and music.  
http://www.adrianfreed.com  

**diyaudio forum** - DIY audio community forum for learning and sharing knowledge about music technology and audio electronics.  
https://www.diyaudio.com  

**electro-music forum** - Dedicated to experimental electro-acoustic and electronic music.  
https://electro-music.com  

**modwiggler forum** - Source of information about modular synthesizers and DIY analog circuits.  
https://www.modwiggler.com  
<br>
<br>

## License

The content of this documentation is licensed under the [Creative Commons Attribution 3.0 Unported license](https://creativecommons.org/licenses/by/3.0/ "CC BY 3.0"), software is licensed under the MIT License - see the [LICENSE.md](/MIT%20License.md) file for details. Copyright remains with the author(s)
<br>
<br>
<br>


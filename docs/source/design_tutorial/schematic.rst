Schematic validation
====================

Transconductance extraction (gm)
--------------------------------

The PDK doesn't provide details on the electron mobility or on the effective channel length.
Thus, we have to run simulations to find the MOSFETs transconductance gm.

On a simple MOSFET Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^

First, we want to find gm, Gds and the MOS capacitor values with a simple circuit including a single MOS.
|

To fetch components parameters coming from the IHP PDK (e.g. Gds or gm), the component SPICE name has
to be specified. This can be done by adding include scripts and equations in the schematic. These scripts 
consists of including PDK libraries into the schematic, select the parameters the component and save it 
as a variable to plot it afterwards. Here is and example of scripts if we want to retrieve the 
transconductance gm :

.. code-block::
    Nutmeg
    gm_mos=@n.XXXX.x1.nsg13_YYYY[ZZZZ]

    INCLUDE SCRIPT
    SpiceCode= .save all @n.XXXX.x1.nsg13_YYYY[ZZZZ]
               .save all @n.XXXX.x1.nsg13_YYYY[ZZZZ]
    .save i(VPr1)

Here, you can edit the command lines to adjust depending on your instance name (XXXX), its 
type (YYYY) and the wanted parameter (ZZZZ). For example, if we want to retrieve Gds, gm and Cgs and the 
current probe Pr1 :

.. code-block::
    Nutmeg
    gm_mos=@n.xmn0.x1.nsg13_lv_nmos[gm]
    gds_mos=@n.xmn0.x1.nsg13_lv_nmos[gds]
    cgs_mos=@n.xmn0.x1.nsg13_lv_nmos[cgs]

    INCLUDE SCRIPT
    SpiceCode=.save i(VPr1)
    .save all @n.xmn0.x1.nsg13_lv_nmos[gm]
    .save all @n.xmn0.x1.nsg13_lv_nmos[gds]
    .save all @n.xmn0.x1.nsg13_lv_nmos[cgs]

|
..
    PUT SCREENSHOT OF MOS SCHEMATIC

The objective is to find a channel width that makes a good compromise between area, consumption and 
performance. To do so, we plot two charts gm=f(Vgs) and Ids=f(Vgs) and we sweep the W parameter for five 
to ten values to have several number of graphs. By train-error method, we can find the corresponding width 
for our constraints on the current and transconductance. After the channel width is chosen, we sweep the 
gate voltage Vgs to find a good combination between the current consumption Ids and gm with the W fixed.
|
..
    TODO
    Insert schematic screenshot

With a Cascode Circuit
^^^^^^^^^^^^^^^^^^^^^^

As we have an approximate value for the gate voltage, we can complete the circuit with the cascode
MOSFET, the resonator and the charge on the top of it. For now, the objective is to verify the gm of our 
cascode circuit Therefore, we generate the gate voltage with an ideal DC source and sweep the voltage.
For the simulation, an AC power source is added. High value capacitors and inductors are also added to 
ensure that the DC source that generates the gate voltage is not shorting the AC source.

..
    TODO
    Add schematic screenshot?

After simulation, we apply the same technique as in the single MOSFET circuit to read the charts.

Input matching & output component selection
-------------------------------------------

Input inductor selection (Ls)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..
    TODO
    Find a way to make Re(Z11) prettier in the following paragraph

Now that we know what gate voltage is needed to obtain our gm, we can adjust parameters to have the correct 
input matching on our circuit. To do so, we want to find the input inductor value Ls that matches our 
requirements. An S-Parameter simulation at 2.45 GHz and a parameter sweep on the input inductor Ls are 
made to acheive 50 Ohms on the real part Re(Z11) at the input. When plotting the output graphs, we want to 
see Re(Z11) versus frequency for each inductor value. To make an S-Parameter simulation with Qucs-S
and Ngspice, the software needs to detect at least two AC power sources. Therefore, we put another power
source and isolation components at the output so the port is not interfering with our simulation.

..
    TODO
    Add schematic screenshot?

While fine-tuning simulation steps and value ranges, we can find an approximate value for the corresponding 
inductor. 
Note : The simulation is made with ideal components. Therefore, you have to choose values that 
will be the easiest possible to reproduce with a real design (e.g. with parasitics).

Gate polarization circuit
^^^^^^^^^^^^^^^^^^^^^^^^^

The next step will focus on the design and the adjustments of the MOSFET gate polarization circuit. As a 
simple explanation, it consists of another MOSFET and resistors to adjust the polarization voltage. It will 
follow the same template as the input inductor selection. To begin, start to fix a proper MOS width. It 
should be large enough to drive the cascode MOS but should not be too large to 
|
To find the right rRPOL for our circuit, we will sweep the resistor value and plot it versus the current 
Ids and gm. For our case, a little tuning of the simulation parameters give us a rPOL value of 8.89kOhms.
|
For the input matching, we change the simulation to S-Parameter and we sweep the Rrf value to find a
resistor value that makes Re(Z11) = 50 Ohms.

..
    TODO
    Screenshot of sim parameters + sim graph ?

While plotting the results, we can see that even with an Rrf value above 500kOhms we can't get Re(Z11) = 50.

..
    TODO
    Several workarounds are possible ; we can add an inductor in series and sweep its value to obtain the wanted
    Re(Z11). We can also adjust the channel width of the polarization MOSFET. Thus, we will have to tune the
    resistor rPOL again to aim the good Ids. For our case, we decided to increase the gate width by 10 um.

    SOLUTION : REDUCE CI TO 570f, PUT RRF = 100K AND QE INCREASES TO 2.04

    After simulating again, we found...
..
    TODO
    Screenshot of smth?


(End of document)


Files
-----
..
    TODO
    Add netlist files? Or .sch files for Qucs directly?
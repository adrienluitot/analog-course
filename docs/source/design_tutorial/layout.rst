Layout
======

Setting up Klayout
------------------

For the layout part we will use Klayout, if not done yet, check the installation steps of :doc:`../design_softwares/klayout`.
To run it from your terminal use the command:

.. code-block:: shell

    klayout &

But before we can create our first layout, we need to setup klayout to "Edit mode" (by default, it is in "Read mode").
Open the "File" menu in the upper left and open "Setup". In the opened window, go in the "Editing Mode" tab under 
"Application". Then check "Use edting mode by default" and validate with "Ok".

To take the change in account, you have to close and re-open Klayout. Now you should see much more options in the
toolbar.



Instanciate first PCell
-----------------------

Now we can create the layout with "File > New Layout" (press "OK" with default parameters). 

.. |klayout_instance_btn| image:: ../images/klayout_instance_btn.png
    :height: 40px

We will first generate an inductor in order to simulate in with OpenEMS to check its inductance at the targeted 2.45GHz.
For that, click on the "Instance" button |klayout_instance_btn|. This will also teach you how to instanciate a PCell,
we will then use the same procedure to add the other components.

This will open an "Editor Options" panel on the lower left part of your screen. In the tab "Instance" write
``inductor2`` in the "Cell" like this:

.. image:: ../images/inductor_instance_tab.png
  :alt: KLayout instance tab example for an inductor
  :height: 300px

We will now change the parameters of the inductor, in the "PCell" tab as:

.. image:: ../images/inductor_pcell_tab.png
  :alt: KLayout pcell tab example for an inductor
  :height: 300px

The other parameters are not important and should change the generated layout.
Once the parameters are set, you can click in the visual editor part. You should then see something like this:

.. image:: ../images/klayout_inductor_layout.png
  :alt: KLayout inductor layout of an inductor
  :height: 500px


.. note::
  If you see a square with the name of the inductor instead of the actual layout of the inductor, press the key "*" or
  click on "Display" > "Full Hierarchy".
    
Now save ("File > Save") the layout in the directory ``microelectronics/project/layout`` with the name "test_inductor.gds".


Characterise the inductor (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to characterise this inductor with OpenEMS later, you will need to specify a simulation port. Therefore you
must choose on the layout where to put it. In our case we want to put it at the input and output of the inductor, as 
shown in cyan on the above image. It does not need to be extremely precise, just make sure the port touches both pins 
properly. We need to find the points of these boxes in the layout, for that we use our mouse cursor get its position,
shown in the dark green box of the image above.

We only need the lower left point and the upper right point of the box. With the above layout, we thus have
approximately (-14,0) and (14,10). But this will change for you, depending on where you placed the inductor. Write
down the 2 points you find to use them later with OpenEMS.

You can find the characterisation procedure at :doc:`charac_inductor`.



Instanciating all the PCells
----------------------------

Create a new Layout with "File > New Layout" (press "OK" with the default parameters). And save it with "File > Save" to
the directory ``microelectronics/project/layout`` under the name "LNA.gds" (press "OK" with the default parameters).

.. |klayout_instance_magnifier| image:: ../images/klayout_instance_magnifier.png
    :height: 25px

We will now use the same process to add all our components to the layout. Make sure you're in "Instance" mode by
clicking on the button |klayout_instance_btn|. In the bottom left panel you can click on the magnifier
|klayout_instance_magnifier|, this will open a window like this:

.. image:: ../images/klayout_instances_list.png
  :alt: KLayout instance list
  :height: 350px

Your window will be slightly different, you might have more or less cells. Make sure you have at least these cells:
cmim, nmos, rhigh, rppd, simple_inductor (or inductor2)

| For the LNA we need 4 ``cmim``, 3 ``nmos``, 1 ``rhigh``,  2 ``rppd`` and 3 ``simple_inductor``.
| Select the component you want to instanciate in the list then click "OK". After that, click in the layout editor as
  many times as you need the component. You might need to dezoom to see something, for this, simply scroll down with
  your mouse.

To add the other components, click again on the magnifier, and start again.

You should have something like that:

.. image:: ../images/layout_pcells_instanciated.png
  :alt: KLayout pcells instanciated
  :width: 100%

Indeed, the NMOS and resistors are quite small compared to the capacitors, and even worse compare to the inductor. This
will be one of the difficulties to manage with this design.



Configuring the PCells
----------------------

Now that we have all the PCells corresponding to our schematic, we need to configure them to match the parameters we 
used in the schematic.

To modify a PCell, you can simply to double click on the targeted PCell. This will open a modal, click on the tab
"PCell parameters". As an example for the capacitor you should have something like that:

.. image:: ../images/layout_pcell_parameters.png
  :alt: KLayout capacitor PCell parameters
  :width: 450px

.. note::
  At the moment, PCells have no callback on their parameters to update other values automatically. For example, changing
  the Width of the capacitor should update it "C" field. So we have to calculate them by hand. If you already used
  real components during :doc:`schematic`, then you have to use the same values. Otherwise, see :doc:`schematic` to
  see how to calculate the dimensions.

.. TODO: update link, i'm not sure it is supposed to be :doc:`schematic`
.. TODO: update once callback works

In our case wee will use these values:

.. TODO: add one (or more, like 1 per component type) table with the components and their parameters




Doing a Floorplan
-----------------

The Floorplan is an very important step in a layout...
.. TODO: finish :)

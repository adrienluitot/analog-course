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



First Layout
------------
Now we can create the layout with "File > New Layout". 

.. |klayout_instance_btn| image:: ../images/klayout_instance_btn.png
    :height: 40px

We will first generate an inductor in order to simulate in with OpenEMS to check its inductance at the targeted 2.45GHz.
For that, click on the "Instance" button |klayout_instance_btn|.

This will open an "Editor Options" panel on the lower left part of your screen. In the tab "Instance" write
``inductor2`` in the "Cell" and ensure that "Rotation angle" is ``0`` like this:

.. image:: ../images/inductor_instance_tab.png
  :alt: KLayout instance tab example for an inductor
  :height: 300px

We will now change the parameters of the inductor, in the "PCell" tab as:

.. image:: ../images/inductor_pcell_tab.png
  :alt: KLayout pcell tab example for an inductor
  :height: 300px

The other parameters are not important and should change the generated layout. Once the parameters are set, you can
click in the visual editor part. You should then see something like this:

.. image:: ../images/klayout_inductor_layout.png
  :alt: KLayout inductor layout of an inductor
  :height: 500px

Now save ("File > Save") the layout in the directory ``microelectronics/project`` with the name "test_inductor".

If you want to characterise this inductor with OpenEMS later, you will need to specify a simulation port. Therefore you
must choose on the layout where to put it. In our case we want to put it at the input and output of the inductor, as 
shown in cyan on the above image. It does not need to be extremely precise, just make sure the port touches both pins 
properly. We need to find the points of these boxes in the layout, for that we use our mouse cursor get its position,
shown in the dark green box of the image above.

We only need the lower left point and the upper right point of the box. With the above layout, we thus have
approximately (-14,0) and (14,10). But this will change for you, depending on where you placed the inductor. Write
down the 2 points you find to use them later with OpenEMS.

You can find the characterisation procedure at :doc:`charac_inductor`.


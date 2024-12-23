OpenEMS
=======

OpenEMS is an Open Source electromagnetic field solver using the FDTD method. 

For most designs, OpenEMS is not absolutely need, in this course we will use it to characterise the inductors of the
LNA. If you are not interested in RF, you might skip this tool.

At the moment, pre-compiled executables are not available in package managers nor by download. So we will need to build
it from source.

The official installation manual and documentation can be found at `<https://docs.openems.de/>`_.
But here we will focus on Linux Ubuntu 24.04 and what's needed for IHP PDK.


Installation
------------

Getting dependencies
^^^^^^^^^^^^^^^^^^^^

As usual, the first step is to get the dependencies to build the tool, we can download them from our package manager:

.. code-block:: shell

    sudo apt install build-essential cmake git libhdf5-dev libvtk9-dev libboost-all-dev libcgal-dev libtinyxml-dev qtbase5-dev libvtk9-qt-dev python3-numpy python3-matplotlib cython3 python3-h5py python3-gdspy


Getting the sources
^^^^^^^^^^^^^^^^^^^

We can now clone the sources from the GitHub repository, first move to your ``tools_sources`` directory and do these
commands:

.. code-block:: shell

    git clone --recursive https://github.com/thliebig/openEMS-Project.git
    cd openEMS-Project


Building & installing
^^^^^^^^^^^^^^^^^^^^^

To build and install OpenEMS we can simply run this command:

.. code-block:: shell

    ./update_openEMS.sh ~/microelectronics/tools/openEMS --python

It will only install it to be used with python, if you also want to use it with Octave (FOSS alternative to Matlab) you
can add the ``--with-CTB`` parameter to the above command. You also need Octave installed on your computer. OpenEMS with
won't be covered in this course for the moment.

This command might take quite a lot of time, so take a break, or check for the rest of the analog course ;)

Once the instalation is done, we must add openEMS to our path to be able to launch it:

.. code-block:: shell

    echo 'export PATH="$PATH:$HOME/microelectronics/tools/openEMS/bin"' >> ~/.bashrc
    export PATH="$PATH:$HOME/microelectronics/tools/openEMS/bin"

Just to try OpenEMS is installed you can run:

.. code-block:: shell

    openEMS

This should print information about openEMS like the version and the basic parameters.

Once the instalation is done, we must add openEMS to our path to be able to launch it:

.. code-block:: shell

    echo 'export PATH="$PATH:$HOME/microelectronics/tools/openEMS/bin"' >> ~/.bashrc
    export PATH="$PATH:$HOME/microelectronics/tools/openEMS/bin"


Cleaning workspace
^^^^^^^^^^^^^^^^^^

You can now delete the openEMS folder located in ``tools_sources``





OpenEMS test with PDK
---------------------

IHP provides example for OpenEMS, we will run one of them to check if everything works properly. The example is located
in ``~/microelectronics/PDK/IHP/IHP-Open-PDK/ihp-sg13g2/libs.tech/openems/testcase/SG13_Octagon_L2n0/OpenEMS_Python/``.

Now you can run the example:

.. code-block:: shell

    python3.12 SG13_L2n0_mesh1.5um_v2.py

This might take quite some time too, so... grab a second coffee?


QUCS
====

To create and design our schematic circuit, the Quite Universal Circuit Simulator (QUCS) will be used. Also, for this
project, the usage of free circuit simulation kernels is adviced. Thus, we will use the Qucs-S extension with Ngspice 
and Xyce as simulation kernels. 

In addition to this section, you can visit `Qucs-S GitHub <https://github.com/ra3xdh/qucs_s>`_ for more information.


Installation
------------

The best way to get and maintain Qucs-S on Ubuntu is with the ``apt`` package manager. But Qucs-S is not directly on the
default Ubuntu's repositories, therefore we need to follow the procedure recommended by the tool's author. We describe
the procedure for Ubuntu 24.04 below, but you can also find it for other operating systems and version on `this website
<https://software.opensuse.org/download.html?project=home%3Ara3xdh&package=qucs-s>`_.

If Qucs-S is not directly available with your OS, you can :ref:`install it from source<qucs_from_source>`

.. code-block:: shell

    echo 'deb http://download.opensuse.org/repositories/home:/ra3xdh/xUbuntu_24.04/ /' | sudo tee /etc/apt/sources.list.d/home:ra3xdh.list
    curl -fsSL https://download.opensuse.org/repositories/home:ra3xdh/xUbuntu_24.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_ra3xdh.gpg > /dev/null
    sudo apt update
    sudo apt install qucs-s ngspice



Testing Qucs-S
^^^^^^^^^^^^^^

You can try if Qucs-S works, just by running the command:

.. code-block:: shell

    qucs-s

The next step is to implement the IHP PDK into Qucs-S, so if you opened it, you can close it for now and continue.




PDK installation for Qucs-S
---------------------------

Getting OpenVAF
^^^^^^^^^^^^^^^

IHP Open PDK's uses compiled Verilog-A models, thus it requires to compile these models for your system. For that, IHP
uses the OpenVAF tool. At the moment, OpenVAF is not available on the package managers, therefore we wether have to
download it. You can do this from `OpenVAF download page <https://openvaf.semimod.de/download/>`_. Once downloaded,
put it in the ``tools`` directory, the binary should be name ``openvaf``.

If OpenVAF is not available for your system (for instance MacOS or Linux Arm64), you can build OpenVAF from sources. For
that you sould follow :doc:`this guide <openvaf>`.

After that, if not done yet, you should add the ``tools`` directory to your path:

.. code-block:: shell

    echo 'export PATH="$PATH:$HOME/microelectronics/tools/"' >> ~/.bashrc
    export PATH="$PATH:$HOME/microelectronics/tools/"


Linking PDK to Qucs-S
^^^^^^^^^^^^^^^^^^^^^
Run the following commands : 

.. code-block:: shell

    cd ~/microelectronics/PDK/IHP/IHP-Open-PDK/ihp-sg13g2/libs.tech/qucs
    export PDK_ROOT="$HOME/microelectronics/PDK/IHP/IHP-Open-PDK"
    python3 install.py


Testing with IHP Example
------------------------

We will now test if Qucs-S works with the PDK. First we need to setup the environment variable:

.. code-block:: shell

    echo 'export PDK_ROOT="$HOME/microelectronics/PDK/IHP/IHP-Open-PDK"' >> ~/.bashrc
    echo 'export PDK="ihp-sg13g2"' >> ~/.bashrc
    export PDK_ROOT="$HOME/microelectronics/PDK/IHP/IHP-Open-PDK"
    export PDK="ihp-sg13g2"

Then we can open Qucs-s:

.. code-block:: shell

    qucs-s

Before running any simulation, we need to add the IHP library to Qucs-S. For this, on Qucs-S go in ``File > Application
Settings...``, then open the ``Location`` tab and click on the ``Add Path With SubFolders`` button.
In the oppened window, go in your home folder (``/home/<your_name>``), then right click in the white zone to enable 
"Show hidden files". Then you should be able to see ``.qucs`` folder, open it and select ``user_lib``.

Now we will open an example, go in ``File > Open...``. In the opened window, go in your home folder then ``QucsWorkspace
> IHP-Open-PDK-SG13G2-Examples_prj > dc_lv_nmos.sch``. This will open a simple schematic with a Nmos.

.. |simulate_symbol| image:: ../images/simulate.png
    :height: 24px

To run the simulation you just have to click on the |simulate_symbol| icon. When the simulation is finished, you should
see something like that:

.. image:: ../images/example_nmos.png
  :alt: Simulation output of the nmos example



.. _qucs_from_source:

Installating from source
------------------------

.. warning::
    This part is only needed if you can't have Qucs-S with your package manager. 

Another way to get Qucs-S is by building it from source, this is useful if you can't find it on your OS package manager
or if you want the latest version. However, if available, it is recommanded to use your package manager.

Dependencies
^^^^^^^^^^^^

First, we need to make sure we have all the dependencies:

.. code-block:: shell

    sudo apt install ngspice cmake flex bison gperf dos2unix build-essential qt6-base-dev qt6-tools-dev qt6-tools-dev-tools libglx-dev linguist-qt6 qt6-l10n-tools libqt6svg6-dev libqt6-charts6-dev libgl1-mesa-dev

Getting the sources
^^^^^^^^^^^^^^^^^^^

Now we can get the sources from GitHub, go at the address `<https://github.com/ra3xdh/qucs_s/releases>`_ and download
the file ``.tar.gz`` file corresponding to the version you want to install. Here we will use the version ``24.4.1``.
Move the downloaded file to your ``tools_sources`` directory to keep things clean.


Building and installing Qucs-S
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First unarchive the sources and create a temporary build directory:

.. code-block:: shell

    tar xvfz qucs-s-24.4.1.tar.gz
    cd qucs-s-24.4.1
    mkdir builddir && cd builddir

Then we prepare our build to install in the right folder. Adapt the ``CMAKE_INSTALL_PREFIX`` parameter to your file
organisation.

.. code-block:: shell

    mkdir -p ~/microelectronics/tools/qucs-s
    cmake ..  -DCMAKE_INSTALL_PREFIX=~/microelectronics/tools/qucs-s -DWITH_QT6=ON

After that we can build Qucs-S (This step might take some time):

.. code-block:: shell

    make

And finally install it and adding to path:

.. code-block:: shell

    make install
    echo 'export PATH="$PATH:$HOME/microelectronics/tools/qucs-s/bin"' >> ~/.bashrc
    export PATH="$PATH:$HOME/microelectronics/tools/qucs-s/bin"

Now that Qucs-S is installed, you can delete the build files in ``tools_sources``. Go in that folder then (adapt with
your version of Qucs-S):

.. code-block:: shell

    rm -rf qucs-s-24.4.1/ qucs-s-24.4.1.tar.gz

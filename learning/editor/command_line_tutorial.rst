.. _doc_command_line_tutorial:

Command line tutorial
=====================

.. highlight:: shell

Some developers like using the command line extensively. Mole is
designed to be friendly to them, so here are the steps for working
entirely from the command line. Given the engine relies on little to no
external libraries, initialization times are pretty fast, making it
suitable for this workflow.

Path
----

It is recommended that your mole binary is in your PATH environment
variable, so it can be executed easily from any place by typing
``mole``. You can do so on Linux by placing the Mole binary in
``/usr/local/bin`` and making sure it is called ``mole``.

Creating a project
------------------

Creating a project from the command line is simple, just navigate the
shell to the desired place and just make an engine.cfg file exist, even
if empty.

::

    user@host:~$ mkdir newgame
    user@host:~$ cd newgame
    user@host:~/newgame$ touch engine.cfg

That alone makes for an empty Mole project.

Running the editor
------------------

Running the editor is done by executing mole with the ``-e`` flag. This
must be done from within the project directory, or a subdirectory,
otherwise the command is ignored and the project manager appears.

::

    user@host:~/newgame$ mole -e

If a scene has been created and saved, it can be edited later by running
the same code with that scene as argument.

::

    user@host:~/newgame$ mole -e scene.xml

Erasing a scene
---------------

Mole is friends with your filesystem, and will not create extra
metadata files, simply use ``rm`` to erase a file. Make sure nothing
references that scene, or else an error will be thrown upon opening.

::

    user@host:~/newgame$ rm scene.xml

Running the game
----------------

To run the game, simply execute Mole within the project directory or
subdirectory.

::

    user@host:~/newgame$ mole

When a specific scene needs to be tested, pass that scene to the command
line.

::

    user@host:~/newgame$ mole scene.xml

Debugging
---------

Catching errors in the command line can be a difficult task because they
just fly by. For this, a command line debugger is provided by adding
``-d``. It works for both running the game or a simple scene.

::

    user@host:~/newgame$ mole -d

::

    user@host:~/newgame$ mole -d scene.xml

Exporting
---------

Exporting the project from the command line is also supported. This is
specially useful for continuous integration setups. The version of Mole
that is headless (server build, no video) is ideal for this.

::

    user@host:~/newgame$ mole -export "Linux X11" /var/builds/project
    user@host:~/newgame$ mole -export Android /var/builds/project.apk

The platform names recognized by the ``-export`` switch are the same as
displayed in the export wizard of the editor. To get a list of supported
platforms from the command line, just try exporting to a non-recognized
platform and the full listing of platforms your configuration supports
will be shown.

To export a debug version of the game, use the ``-export_debug`` switch
instead of ``-export``. Their parameters and usage are the same.

Running a script
----------------

It is possible to run a simple .mo script from the command line. This
feature is specially useful in very large projects, for batch
conversion of assets or custom import/export.

The script must inherit from SceneTree or MainLoop.

Here is a simple example of how it works:

.. code:: python

    #sayhello.mo
    extends SceneTree

    func _init():
        print("Hello!")
        quit()

And how to run it:

::

    user@host:~/newgame$ mole -s sayhello.mo
    Hello!

If no engine.cfg exists at the path, current path is assumed to be the
current working directory (unless ``-path`` is specified).

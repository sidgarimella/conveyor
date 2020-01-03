The `nbglobals` module
======================

To get started with variable values you've computed in earlier notebooks `as fast as possible`, use `conveyor.nbglobals` by setting `import_globals` to True when running a notebook.


.. code-block:: python

   conveyor.run_notebook("<notebook_name.ipynb>", import_globals=True)
   from conveyor.nbglobals import <any variable 1>, <any variable 2>, ...

While you can use `*` to import a former workspace in its entirety, this is not recommended. It is likely variables between notebooks may end up mixing in unexpected ways and cause confusion.

Importing multiple notebooks in this way adds to and updates conveyor.nbglobals, meaning multiple notebooks can be run and provide data to a current notebook like so:


.. code-block:: python

   conveyor.run_notebook("<notebook_one.ipynb>", import_globals=True)
   conveyor.run_notebook("<notebook_two.ipynb>", import_globals=True)
   conveyor.run_notebook("<notebook_three.ipynb>", import_globals=True)

   from conveyor.nbglobals import <variable from notebook 1>, 
            <variable from notebook 2>, ...


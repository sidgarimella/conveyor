Home
^^^^

Conveyor lets you quickly compute and reuse information stored in Jupyter notebooks in just a couple lines of code. 

Using this tool to reference prior work in outside notebooks can help keep notebook workflows organized, separating large ideas that require multiple steps to execute into a smaller, more focused file structure.

Quickstart
""""""""""

The fastest way to get started using Conveyor is with the nbglobals module:


.. code-block:: python

    import conveyor
    conveyor.run_notebook("Sample Calculations I.ipynb", import_globals=True)
    from conveyor.nbglobals import x, z

Any time run_notebook is called with import_globals=True, the variables in conveyor.nbglobals are updated by those in the new notebook.


Table of Contents
"""""""""""""""""

.. toctree::
   :maxdepth: 3

   installation
   running_a_notebook
   multinb
   nbglobals
   parsing_output
   contribute


Indices and tables
""""""""""""""""""

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

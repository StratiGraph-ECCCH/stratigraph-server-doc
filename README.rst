StratiGraph Server Documentation
================================

This repository contains the documentation for **StratiGraph Server**, the node of the
`StratiGraph <https://github.com/StratiGraph-ECCCH>`_ ecosystem: shared rooms on a study's
knowledge graph, the live relay and the REST door, assets, corpus and graph services.

The datamodel is owned by `s3Dgraphy <https://github.com/ExtendedMatrix/s3Dgraphy>`_.

The documentation is built with `Sphinx <https://www.sphinx-doc.org/>`_ and hosted on
`Read the Docs <https://readthedocs.org/>`_.

Building locally
----------------

.. code-block:: bash

   pip install -r docs/requirements.txt
   cd docs
   sphinx-build -b html . _build/html

The generated HTML will be in ``docs/_build/html/``.

Links
-----

- **GitHub Organization**: https://github.com/StratiGraph-ECCCH
- **Project**: StratiGraph — Knowledge Graphs for Stratigraphy (Horizon Europe, 2025–2029)

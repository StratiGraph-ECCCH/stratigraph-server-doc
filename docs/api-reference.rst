API reference
=============

Every running node publishes its own interactive reference at ``/docs`` under
the node's address (``https://em.localhost:8443/em/docs`` on the development
stack): the routes grouped by section, a one-line summary and the long
description of each, the parameters, *Try it out* and *Execute*, the ``curl``
equivalent and the real answer. Press *Authorize* and paste a bearer token
first: routes that need one show a lock.

This page keeps a snapshot of the same definition, so that it can be read, and
loaded into any OpenAPI viewer, without a running node.

* :download:`openapi.json <_static/openapi.json>` — OpenAPI 3.1, StratiGraph
  Server ``1.6.0.dev24``, taken on 17 October 2026 from the development stack (server commit a2b0c19)
  and identical to what the node served at that moment.

The snapshot can fall behind the server. The node's own ``/openapi.json`` is
the one that cannot: it is generated from the code, and a test in the server's
repository (``tests/test_la_documentazione_dice_il_vero.py``) checks that it
agrees with the routes and with the table in the README.

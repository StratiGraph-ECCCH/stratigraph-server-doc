Welcome to the StratiGraph Server Documentation
===============================================

**StratiGraph Server** is the node of the StratiGraph ecosystem: it keeps the shared rooms
where a study's knowledge graph is worked on together, relays every change to whoever is
sitting in the room, and keeps the assets, the corpus and the services that read the graph.
EMStudio, EMtools, StratiField and Heriverse all talk to it.

A room has two doors. The live socket is for whoever stays inside and wants every change
as it happens; the REST door is for whoever comes in, reads, writes and leaves — a phone in
the trench, a script, a partner's platform.

.. note::
   This documentation is being written. Working in a room, the field node,
   people, profiles and roles, the REST door of a room and the API reference are here; the guide for client developers follows.

   StratiGraph Server is developed within the Horizon Europe project *StratiGraph —
   Knowledge Graphs for Stratigraphy* (2025–2029).

.. toctree::
   :maxdepth: 2
   :caption: Contents

   introduction
   room-guide
   field-node
   roles-and-users
   rest-api
   api-reference

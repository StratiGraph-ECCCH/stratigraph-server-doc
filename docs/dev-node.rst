Running the node on your computer
=================================

StratiGraph Server · the development node, for whoever runs a node on a laptop
to work, to test tools against it, or to show it. The field node on a Raspberry
Pi is the same software set up for the excavation: see :doc:`field-node`.

What is running
---------------

The node is a set of programs, each in its own Docker container, started
together by one script. On a Mac they run inside Colima, the small virtual
machine that gives macOS a Docker. One node, one set of containers:

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Container
     - What it is
   * - ``em-dev-caddy``
     - The front door: https on port 8443, with the node's own certificate.
   * - ``em-dev-keycloak``
     - Who you are: sign-in with ORCID or with the node's password.
   * - ``em-dev-server``
     - The rooms: the live graphs, the relay of every change, the console.
   * - ``em-dev-chatbot``
     - StratiField, the field assistant for the phone.
   * - ``em-dev-catalog``
     - The catalogue of published studies.
   * - ``em-dev-cantaloupe``, ``em-dev-rustfs``, ``em-dev-postgres``
     - Images (IIIF), the file store (the bucket), the database.

Once started, the containers come back by themselves until you switch them
off. To see what is on::

   docker ps

The same node answers at three addresses, and they are not three nodes:

* ``https://em.localhost:8443`` — from this computer only;
* ``https://<host>:8443`` — from the other devices on the same network (see
  below);
* ``http://localhost:8000`` — the rooms server reached directly, without the
  front door; tools use it when they run on the same computer.

Switching it on and off
-----------------------

All the commands are run from the ``dev-stack`` folder of the server::

   cd ~/Documents/GitHub/stratigraph-server/dev-stack

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Command
     - What it does
   * - ``./fcn-up.sh``
     - Switches the node on. The first time it builds the images (some
       minutes); after that it reuses them.
   * - ``./fcn-up.sh --offline``
     - Switches it on without building and without the EMStudio development
       server: two or three minutes, no network needed. The usual way after a
       restart.
   * - ``./fcn-up.sh 192.168.1.214``
     - Switches it on for the other devices of the network, at that address.
       The address is remembered: the next times ``./fcn-up.sh --offline`` is
       enough.
   * - ``./fcn-up.sh --demo``
     - Also fills it with demonstration studies, rooms and images.
   * - ``./fcn-down.sh``
     - Switches it off. Studies, rooms, files and accounts stay.
   * - ``./fcn-down.sh --colima``
     - Switches it off and frees the Mac's memory too.
   * - ``./fcn-down.sh --wipe``
     - Switches it off and **deletes everything**: studies, rooms, files,
       accounts and the certificate. Only for a fresh start.

Every script explains itself, with examples::

   ./fcn-up.sh --help
   ./fcn-down.sh --help

.. warning::
   **After every restart, sign in again.** On the development node the sign-in
   service keeps its sessions inside its container, so they do not survive a
   restart. A browser shows the sign-in page again; EMStudio shows
   *connection lost* and retries forever — in its panel of the node, choose
   *Sign in as another user*. StratiField on the phone asks for the signature
   again. The field node keeps the sessions on disk and does not have this
   problem.

Reaching it from the phone
--------------------------

The phone must be on the same Wi-Fi as the computer, and it must trust the
node's certificate once (the certificate file is created by ``fcn-up.sh``; on an
iPhone, open it, install the profile, then enable it in *Settings → General →
About → Certificate Trust Settings*).

The computer is reached by **name** (``my-mac.local``) or by **address**
(``192.168.1.214``). The name is nicer and survives a change of address, but
many home and office routers do not let these names through: Safari then says
it *cannot find the server* even though the computer answers. In that case use
the address::

   ./fcn-up.sh 192.168.1.214

and ask the router to always give the computer the same address (usually called
*DHCP reservation* or *static lease*). Find the address with
``ipconfig getifaddr en0`` on a Mac, ``hostname -I`` on Linux.

The quickest way onto the phone is the **QR code** of a room: on the *Work*
page, beside each room, the *phone* button shows it. Frame it with the phone's
camera and StratiField opens in that room.

On the Mac itself, keep using ``em.localhost`` in EMStudio. Recent versions of
macOS ask an app for permission before it contacts an address of the local
network (*System Settings → Privacy & Security → Local Network*), and EMStudio
may not have it yet; ``em.localhost`` stays inside the computer and does not
need it.

Cleaning up rooms
-----------------

Rooms are managed in the **console of the node**, ``https://<host>:8443/em/admin/``,
section *Rooms*, by whoever is an operator of the node.

* The chips on top filter the list: *Active*, *Archived*, *Implicit*.
  Implicit rooms are those nobody declared — usually the automatic tests
  made them. A banner offers to delete them all at once.
* Tick the rooms on the left (the box in the header ticks all the listed
  ones). A bar appears with what can be done to all of them together:
  *Archive*, *Restore*, *Delete…*. The choice survives a change of filter.
* Deleting asks you to type a word to confirm, and cannot be undone: each room
  goes with its em.json, its revisions, its members and its invitations. Its
  files stay in the bucket until the operator removes the orphans
  (*Memory and bucket*).
* Archiving deletes nothing: the room stays readable and can be restored.

Clicking a row opens the room on the right, with its people, invitations,
visibility, memory and lifecycle.

When something does not answer
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - What you see
     - What to do
   * - The phone says *node absent*, Safari *cannot find the server*
     - The name ``.local`` does not get through the router: switch the node on
       at the address (above).
   * - EMStudio: *connection lost — retry*
     - The node was restarted: *Sign in as another user* on that node.
   * - EMStudio: *does not answer* for an address like ``192.168.…``
     - Probably the *Local Network* permission of macOS. On the same Mac,
       use ``em.localhost:8443``.
   * - Sign-in fails with *Invalid parameter: redirect_uri*
     - The page was opened at an address the node was not started for. Use the
       address shown at the end of ``./fcn-up.sh``, or restart it with yours.
   * - Nothing answers at all
     - ``docker ps``: if the list is empty, ``./fcn-up.sh --offline``.

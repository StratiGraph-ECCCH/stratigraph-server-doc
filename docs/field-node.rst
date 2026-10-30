The field node: installing it and looking after it
===================================================

StratiGraph Server · for whoever prepares the node that goes to the excavation
and looks after it during the campaign. No programming is needed; you will type
a handful of commands in a terminal, and each one is written here exactly as it
is typed.

What a field node is
--------------------

A **field node** is StratiGraph Server running on a laptop or a small computer
that travels with the team. It is the same server as the institutional node:
same rooms, same em.json, same roles. What changes is the situation: on the
excavation there is often no internet, so people sign in with a **field
password** that the node gives them, and the team arrives from the institutional
node in a **signed package** prepared before leaving.

Three kinds of node exist, and each node declares which one it is
(``EM_NODE_KIND``):

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Kind
     - What it is
   * - ``institutional``
     - The node of an institution, reachable on the internet under a public
       name. People sign in with ORCID. It prepares the packages for the field
       and receives them back. Installed by the institution's IT with the
       deployment playbook.
   * - ``field``
     - This page. A laptop or a box on the excavation, often offline.
   * - ``personal``
     - One person's computer; the files stay in their folders. Nothing to
       manage.

The node holds you to the safe defaults of its kind and tells you, in the
console's *Node health* panel, what is still missing.

.. note::
   The field node is installed today with the scripts of the development stack
   (the ``dev-stack`` folder of the server's repository). They are the scripts
   used on the pilots, and they work offline. Because they come from development,
   a few values must be changed **before the first start**: the steps below say
   which, and why.

What you need
-------------

* **A computer** that stays on during the working day: a Mac (Apple silicon or
  Intel) or a Linux machine, with at least 16 GB of memory and 100 GB of free
  disk. The studies, their files and the photographs live on this disk.
* **A network on the site** that the phones and tablets can join: a small
  travel router is the reliable choice. Phone hotspots often keep the devices
  from seeing each other.
* **Your ORCID iD**, and an internet connection for the preparation, which is
  done at base, days before leaving.
* **A contact at the institutional node**, the person who looks after it, to
  exchange keys and the team's package.

Part 1 · Installing, at base
----------------------------

Step 1 · The tools
~~~~~~~~~~~~~~~~~~

On a **Mac**, install Homebrew from https://brew.sh if it is not there yet, then
in the Terminal:

.. code-block:: bash

   brew install git colima docker docker-compose

On **Linux**, install Docker Engine and its compose plugin with your
distribution's instructions (https://docs.docker.com/engine/install/), and
``git``.

Step 2 · The server
~~~~~~~~~~~~~~~~~~~

Choose a folder for the node (here: ``~/stratigraph``) and download the server:

.. code-block:: bash

   mkdir -p ~/stratigraph && cd ~/stratigraph
   git clone https://github.com/StratiGraph-ECCCH/stratigraph-server.git
   cd stratigraph-server/dev-stack
   cp .env.dev.example .env.dev

``.env.dev`` is the node's configuration file. It stays on this computer and is
never shared.

Step 3 · Choose the node's name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The phones will reach the node by a **name**, never by a bare number address.
The simplest is the computer's own local name:

* on a Mac: *System Settings → General → Sharing*, at the bottom, *Local
  hostname* — something like ``scavo-mac.local``;
* on Linux: the output of ``hostname``, followed by ``.local`` (the machine needs
  ``avahi-daemon``, present on most desktop distributions).

In the rest of this page that name is written ``NAME``.

Step 4 · The configuration, before the first start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open ``.env.dev`` with a text editor (on a Mac: ``open -e .env.dev``) and add
these lines at the end, with your values:

.. code-block:: bash

   # what this node is
   EM_NODE_KIND=field
   EM_NODE_NAME=scavo-2027.example        # a name the other nodes will read
   # who looks after it: your ORCID iD (more than one: separated by commas)
   DEV_OPERATOR_ORCID=0000-0000-0000-0000
   # no fictitious people on a node that holds real work
   EM_ALLOW_TEST_PEOPLE=0
   # ORCID, the real one (see step 5 for the two values)
   ORCID_ISSUER=https://orcid.org
   ORCID_CLIENT_ID=APP-…
   ORCID_CLIENT_SECRET=…

Then **change the development secrets** already in the file, each to a long
value of your choice (a password manager can generate them):

* ``KEYCLOAK_ADMIN_PASSWORD`` — the administrator of the node's sign-in service;
* ``RUSTFS_ACCESS_KEY`` and ``RUSTFS_SECRET_KEY`` — the keys of the file store.

Change them now, before the first start: the sign-in service fixes its
administrator when it is created, and a value changed later is not read again.

Step 5 · Register the node with ORCID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The node must sign you in with ORCID once, at base, before it can give anybody a
field password: a node attests only the identities ORCID verified.

1. Sign in at https://orcid.org, open *Developer tools*, and register a public
   API client.
2. As redirect URI, write::

      https://NAME:8443/auth/realms/em-dev/broker/orcid/endpoint

3. Copy the *client ID* and the *client secret* into ``ORCID_CLIENT_ID`` and
   ``ORCID_CLIENT_SECRET`` in ``.env.dev``.

Step 6 · Prepare and start
~~~~~~~~~~~~~~~~~~~~~~~~~~

From the ``dev-stack`` folder:

.. code-block:: bash

   ./fcn-install.sh NAME
   ./fcn-up.sh NAME

``fcn-install.sh`` checks the machine, downloads the companion repositories it
needs, and tells you in plain words anything that is missing — it never installs
system software by itself. ``fcn-up.sh`` starts everything. The first start
takes several minutes (the images are built); after that a start takes about
fifteen seconds.

Step 7 · Trust the node's certificate on this computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The node makes its own certificate, and every device must trust it once:

.. code-block:: bash

   ./fcn-trust-ca.sh

It asks for your computer password, because it writes into the system's list of
trusted certificates. Then open https://NAME:8443/em/rooms/ — the node's front
door — in the browser.

Step 8 · Become the node's manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The node lets in, through ORCID, only the iDs it already knows. The first one,
yours, is written by hand; everybody else arrives from the console.

1. In the ``dev-stack`` folder, open ``accredited.yaml`` and replace the
   demonstration entries with yours::

      accredited:
        - orcid: 0000-0000-0000-0000
          name: Your Name

   Then create your account on the node:

   .. code-block:: bash

      ./accredit.sh

2. Open the console, https://NAME:8443/em/admin/ , and choose *Sign in with
   ORCID*. ORCID links your account the first time. Your iD is the one in
   ``DEV_OPERATOR_ORCID``, so you enter as **super-administrator**.
3. Give yourself the **field password** you will use on the excavation, where
   ORCID cannot be reached:

   .. code-block:: bash

      ./offline-password.sh 0000-0000-0000-0000

   It asks for the password twice and shows nothing on screen. At your first
   field sign-in the node asks you to choose your own.
4. In *Node health*, the card *What kind of node* says **field node** and lists
   what is still missing. At this point it normally says that the node trusts no
   node yet: that is step 10.

Step 9 · Switch off the demonstration accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The development sign-in service carries a few demonstration accounts (``dev``,
``viewer``, ``editor``, ``editor2``, ``outsider``) with known passwords. On a node
that holds real work they are switched off:

1. Open https://NAME:8443/auth/admin/ and sign in as ``admin`` with the
   ``KEYCLOAK_ADMIN_PASSWORD`` you chose.
2. Top left, choose the realm **em-dev**, then *Users*.
3. Open each of the five accounts and turn **Enabled** off. Save.

Step 10 · Exchange keys with the institutional node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The two nodes must trust each other once, so that the team's package can be
accepted. It is done by the two managers, on the phone or face to face.

1. In the console, *Transfers*: the section *This node* shows the node's public
   key and its **fingerprint**. *Copy the key* and send it to the institutional
   node's manager by mail.
2. The institutional manager does the same and sends you their key.
3. In *Trusted nodes*, write the institutional node's name exactly as it
   declares itself, paste its key, *Add*.
4. Read the two fingerprints aloud to each other. If they match, the trust is
   set. If they do not, remove the entry and start again: somebody pasted the
   wrong key.

Step 11 · Bring the team in
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. On the **institutional** node, its manager opens *Transfers → Prepare a
   package*, ticks the rooms that go to the field (and adds any other ORCID iD),
   and makes the package: a ``.json`` file, signed by that node. It travels by
   mail or USB stick.
2. On the **field** node, *Transfers → Receive a package*, choose the file. The
   console shows who is in it, whether the signature is good and comes from a
   trusted node, and the profiles proposed. Untick anybody who is not coming;
   tick the profiles you accept; *Bring in*.
3. In *People*, give each person their **field password**. It is temporary: the
   person chooses their own at the first sign-in.

Passwords never travel in a package: every person receives one from the node
they are working on.

Step 12 · Prepare the phones and tablets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The camera, the microphone and the GPS work in the browser only on a connection
the device trusts. Every phone and tablet that will record must trust the node's
certificate, **at base**:

1. On the node: ``./fcn-trust-ca.sh --export-only`` writes
   ``caddy-em-root.crt`` in your home folder. Send it to the devices (mail,
   AirDrop, cable).
2. **iPhone and iPad** — two steps, in two different places: open the file and
   install the profile (*Settings → General → VPN & Device Management*); then
   *Settings → General → About → Certificate Trust Settings* and turn on full
   trust for it.
3. **Android** — *Settings → Security → Encryption & credentials → Install a
   certificate → CA certificate*, and choose the file. Menu names vary a little
   between makers.
4. Join the node's network and open https://NAME:8443/em/rooms/ : the page opens
   without warnings.

Part 2 · On the excavation
--------------------------

Each morning
~~~~~~~~~~~~

1. Switch on the router, then the node computer.
2. From the ``dev-stack`` folder: ``./fcn-up.sh NAME``. Everything you left the
   evening before is there: studies, rooms and files persist between starts.
3. Open https://NAME:8443/em/rooms/ on one device to check that the node answers.

Each evening
~~~~~~~~~~~~

From the ``dev-stack`` folder: ``./fcn-down.sh``. It stops the services and keeps
every datum. Then copy the node's data to an external disk if your institution's
procedure asks for it.

.. warning::
   ``./fcn-down.sh --wipe`` **erases** the node's data: studies, rooms, files,
   accounts and the certificate. It exists for tests. It is never used on a
   node that holds a campaign.

When somebody forgets the password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Console → *People* → the person → *Field password*: type a new temporary
password twice and tell it to the person. They choose their own at the next
sign-in. The act is written in the node's log; the password never is.

When somebody joins the team on site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add them in *People* by their ORCID iD. Without a network the node cannot verify
the iD, so they cannot receive a field password yet. Two ways out: they work
with a colleague's device until the network comes back, or, when somebody can
reach the internet for a moment (a phone hotspot is enough), they sign in once
with ORCID on the node and then receive their field password. On the way back
they arrive at the institutional node marked *to verify*.

What the node tells you
~~~~~~~~~~~~~~~~~~~~~~~

*Node health* is the first panel to open when something looks wrong: every
service with its state, and on top the card *What kind of node* with what is
missing for a field node. A service *not configured* is not a failure; one that
*did not answer* is.

Part 3 · Coming back
--------------------

1. **The people.** On the field node, *Transfers → Prepare a package* with the
   campaign's rooms; on the institutional node, *Receive a package*. People
   added on site arrive *to verify*; profiles raised on site arrive as
   proposals.
2. **The studies.** The automatic synchronisation of rooms between nodes is
   being built. Until it arrives, each room's em.json is taken from the room
   (*em.json* door on the work page) and brought into the corresponding room of
   the institutional node, together with its files, by the room's owner.
3. Keep the field node's data on an external disk until the institutional node
   has everything.

Checklist before leaving
------------------------

* ``EM_NODE_KIND=field`` and ``EM_ALLOW_TEST_PEOPLE=0`` in ``.env.dev``.
* Development secrets changed before the first start.
* Demonstration accounts switched off.
* *Node health*: the card says **field node** and lists nothing in red.
* The institutional node is in *Trusted nodes*, fingerprints compared.
* The team's package received; every person has a field password, yours too.
* Every phone and tablet trusts the certificate and opens the node without
  warnings.
* The rooms for the campaign exist, with their people and roles.
* A copy of ``.env.dev`` in a safe place: it holds the node's secrets.

What to keep private
--------------------

The mechanism on this page is public. Some things of a real node are not: the
contents of ``.env.dev``, the node's private key (``node-key.pem``, in the node's
data), the packages of people (they are personal data), the node's address and
its list of trusted nodes. See *Handle with care* in :doc:`roles-and-users`.

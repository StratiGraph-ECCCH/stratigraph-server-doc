People, profiles and roles
==========================

StratiGraph Server · for whoever looks after a node and for anyone who wants to
know who may do what in a study. The rules on this page are the ones the server
enforces (``app/access.py``, ``app/operators.py``); the parts that are decided
but not built yet are marked **Planned**, so the page says what a node does today
and where it is going.

Two questions, asked separately
-------------------------------

Every request a node receives raises two questions. *Who are you?* is answered by
the identity provider of the node (Keycloak), and the answer is always an ORCID.
*What may you do here?* is answered by the server itself, because it is a
question about a study the server holds and about the people who work on it.

The answer to the second question has two levels:

* a **profile on the node** says what a person may do with the node as a whole:
  create studies, manage people, look after the storage;
* a **role in a room** says what a person may do with one study: read it, write
  it, decide who else comes in.

The two levels are independent. Somebody can be a plain user of the node and the
owner of a room, or look after the whole node and be a reader in a study.

A person is an ORCID
--------------------

A node knows a person by their ORCID iD, and by nothing else. The same iD signs
every operation that person writes into a graph, owns the rooms they create and
appears in the member lists of rooms and groups. A name is shown beside it for
convenience; the iD is what the server compares.

**Adding a person.** The node manager adds a person by their ORCID and chooses,
explicitly, the profile they receive on the node. When nothing is chosen the
person is a *user*: creating studies is something a person is given, never
something they find themselves able to do.

**Signing in, with and without a network.** With a connection a person signs in
with ORCID. A node in the field often has no connection, so every person also
receives a **local password** from the node: their ORCID iD as the user name and
a password kept by the node's own Keycloak, which runs on the node and needs no
internet. The node stands as guarantor for that person until the network comes
back. The first password is temporary and is changed at the first sign-in; when
it is forgotten, the node manager sets a new temporary one.

.. note::

   **Today** a person is accredited by adding the iD to ``accredited.yaml`` and
   running ``dev-stack/accredit.sh``, which creates the Keycloak user and its
   password.

   **Planned** — the node console does the same in one place: add a person by
   ORCID, choose the profile, set or reset the local password, revoke access.

Profiles on the node
--------------------

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Profile
     - What it may do
   * - **Super-administrator**
     - Looks after the node. Adds people by ORCID, chooses their profile, sets
       and resets their local password, revokes their access. Sees the list of
       every room on the node, archives and deletes rooms. Looks after the
       storage: the bucket, the orphan files, the quotas, the health of the
       services.
   * - **Node editor**
     - Creates rooms, and becomes the owner of each room created. Creates
       groups, and manages each group created. Otherwise works like a user.
   * - **User**
     - The starting profile. Enters the rooms where somebody gave them a role,
       or where an invitation link brought them.

The super-administrator is what the server calls the node **operator**. The
capability comes from the deployment — the realm role ``em-operator``, or the
allow-list ``EM_OPERATORS`` — and from nowhere else: there is no endpoint that
grants it, and nobody can give it to themselves. An empty configuration means
that nobody is an operator.

.. note::

   **Planned** — the *node editor* profile. Today any person who has signed in
   may create rooms and groups; from the profile on, only node editors and
   super-administrators may. The console will also refuse to demote the last
   super-administrator, so a node is never left without anybody who can look
   after it.

Roles in a room
---------------

A room is where one study is worked on: its Extended Matrix graph, the people
who may enter and their roles. Each room has exactly one live graph, and each
live graph belongs to exactly one room.

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Role
     - What it may do
   * - **Reader** (``viewer``)
     - Opens the room, reads the graph, sees and downloads its files, reads the
       conversation.
   * - **Editor** (``editor``)
     - Everything a reader does, and writes: changes the graph, uploads files,
       keeps snapshots of a Blender working file, writes in the conversation.
   * - **Administrator** (``admin``)
     - Everything an editor does, and manages the people: adds, removes and
       changes editors and readers, people or groups; creates and revokes
       invitation links; decides who sees the study (public, restricted,
       embargo); archives the room and brings it back.
   * - **Owner** (``owner``)
     - One per room. Everything an administrator does, and manages the
       administrators, hands the room to a new owner, deletes the room.

**Who manages whom.** The owner may assign any role, including administrator,
and may hand the room over. An administrator manages editors and readers only:
an administrator cannot change an owner or another administrator, which is what
keeps an administrator from promoting themselves. Everybody else manages nobody.
Each refusal comes with a sentence that says which of these rules applied.

**Creating a room.** Whoever creates a room is its owner, written into the
room's access list at once.

Groups
------

A **group** is a team: a named list of ORCIDs. A group can hold a role in a room
— reader, editor or administrator, never owner — so a team is given access once,
instead of adding each of its members to every room where they work. A group is
managed by whoever created it.

When a person has a role of their own and one or more roles through groups, the
role that counts is **the highest**. Joining a team therefore never takes a
permission away. Leaving a team takes away only the roles that came through that
team; a role given to the person directly stays.

Who sees the study
------------------

A study is **public** or **restricted**, and the choice belongs to the room's
administrators and owner.

* A **public** study can be read by anyone, including somebody who has not signed
  in: that is what publishing means.
* A **restricted** study is read only by people who have signed in *and* have a
  role in the room. Signing in without a role is not enough.

An **embargo** is a date. Until the date, the study behaves as restricted
whatever its declared visibility; when the date passes, the study goes back to
what it declares. The room and the Catalog follow the same rule, so the list of
published studies and the door of the room always agree.

Invitations
-----------

An administrator or the owner can create an **invitation link** that offers the
role of editor or reader. Three things do three jobs: the link opens the door,
the ORCID says who came in, and the role comes from the link. A link
authenticates nobody, so a link pasted in the wrong chat lets nobody in without
their own sign-in. Links expire, and can be revoked at any time.

The super-administrator inside a room
-------------------------------------

Inside a room, the super-administrator counts for the role they hold *in that
room*: an editor there is an editor, an administrator there is an administrator.
Looking after the node gives the right to archive or delete a room, and to see
its files from the storage side for maintenance; it gives no right to change the
graph or the people of a study.

.. note::

   **Planned** — one exception, for a room left without anybody who can manage
   it (the owner is gone and no administrator remains): the super-administrator
   may hand the room to a new owner, and that act is written to the node's
   record. It rescues the room without entering it.

Archiving and deleting a room
-----------------------------

**Archiving** is the reversible gesture: the room stays readable and citable,
nobody writes in it any more, and it can be brought back. Administrators and the
owner archive; so does the super-administrator, across the node.

**Deleting** is for the owner and for the super-administrator only. The request
must repeat the id of the room, and it is refused while somebody is connected to
the room, since their session would write the document back the moment they
leave.

What a deletion removes:

* the room's record, its members, invitations and group grants;
* its pending uploads and its log of operations;
* its live graph — the em.json document, with **every revision** of it.

What a deletion keeps, and says so in its answer:

* the files: a file no other room cites becomes an **orphan**, listed for the
  super-administrator, who decides whether to remove it;
* the Blender snapshots (their register goes);
* an em.json that another room still names as a reference.

At a glance
-----------

.. list-table::
   :header-rows: 1
   :widths: 40 12 12 12 12 12

   * - In a room
     - Reader
     - Editor
     - Admin
     - Owner
     - Super-admin
   * - Read the graph and the files
     - ✓
     - ✓
     - ✓
     - ✓
     - by role
   * - Write the graph, upload files
     -
     - ✓
     - ✓
     - ✓
     - by role
   * - Manage editors and readers, invitations
     -
     -
     - ✓
     - ✓
     - by role
   * - Decide who sees the study, embargo
     -
     -
     - ✓
     - ✓
     - by role
   * - Archive the room
     -
     -
     - ✓
     - ✓
     - ✓
   * - Manage administrators, hand the room over
     -
     -
     -
     - ✓
     - rescue only (planned)
   * - Delete the room
     -
     -
     -
     - ✓
     - ✓

.. list-table::
   :header-rows: 1
   :widths: 46 18 18 18

   * - On the node
     - User
     - Node editor
     - Super-admin
   * - Enter rooms where one has a role
     - ✓
     - ✓
     - ✓
   * - Create rooms and groups
     -
     - ✓ (planned)
     - ✓
   * - Add people, choose profiles, set and reset local passwords
     -
     -
     - ✓ (console planned)
   * - See every room, the storage, the health of the node
     -
     -
     - ✓

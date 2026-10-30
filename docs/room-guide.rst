Working in a room: a guide for editors and administrators
==========================================================

StratiGraph Server · for the archaeologists who work in a study, and for those
who decide who works in it with them. Nothing here needs the node console: all
of it is done from the node's web pages and from the tools.

A room in three sentences
-------------------------

A **room** is where one study is worked on together: its Extended Matrix graph,
the em.json, kept live on the node. Everyone who has a **role** in the room sees
the same graph and every change as it happens, signed with the ORCID of whoever
made it. The room also keeps the study's files, the conversation of the team and
the history of every operation.

Your role in a room
-------------------

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Role
     - What you can do
   * - **Reader**
     - Open the room, read the graph, see and download its files, read the
       conversation.
   * - **Editor**
     - Everything a reader does, and write: change the graph, upload files,
       keep snapshots of a Blender file, write in the conversation.
   * - **Administrator**
     - Everything an editor does, and decide about people: add and remove
       editors and readers, make invitation links, decide who sees the study,
       archive the room.
   * - **Owner**
     - One per room. Everything an administrator does, and manage the
       administrators, hand the room to someone else, delete it.

Your role is the same in every tool: the web page, EMStudio, EMtools in Blender,
StratiField on the phone. When a tool refuses something, the sentence it shows
says which role was needed.

Signing in
----------

Open the node's front door in a browser — the address your node manager gives
you, ending in ``/em/rooms/`` — and choose *Sign in*.

* **With a network**: *Sign in with ORCID*, with your usual ORCID account.
* **On the excavation, without a network**: user name = your ORCID iD (for
  example ``0000-0002-1825-0097``), password = the field password the node
  manager gave you. The first time, the node asks you to choose your own.

If you have forgotten the field password, ask the node manager for a new one:
nobody can read the old one, not even them.

Finding your rooms
------------------

The front door has a *Work* entry (``/em/work/``): it lists the rooms where you
have a role, and only those. Choose *enter* to open a room's page.

**Creating a room** is a box at the top of the list. It is there if your
profile on the node allows it (*node editor*); otherwise the page says whom to
ask. Whoever creates a room is its **owner**.

The room's page
---------------

The page opens on **The room**, the team's board. It reads, top to bottom:

* **Who is here** — who is in the room now, who is writing and who is reading,
  and who left.
* **Waiting for you** — fields that a tool or an assistant composed and that
  wait for a person's signature. Nothing written by a machine counts as
  validated until somebody signs it.
* **Since you last looked** — what changed, counted unit by unit. Choose the
  window: since you last wrote, the last hour, day or week.
* **What we said to each other** — the room's conversation. It stays in the
  room: it does not travel with the published study.
* **Who dug what** — who wrote, how much and with which tool. Every name is
  the identity that signed in, stamped by the node.
* **The numbers, and their holes** — units, relations, and what is still
  missing: units without an epoch, without any relation, without anybody's
  name on them. A good list to read before closing a day's work.

Opening the room in a tool
~~~~~~~~~~~~~~~~~~~~~~~~~~

Beside each room there are its **doors**:

* *desktop* opens the room in a program installed on your computer (EMStudio);
* *browser* opens it in a new tab, where the node offers one;
* *copy for EMtools* copies a link: in Blender, EMtools → *Open room from
  link…*, and paste;
* *em.json* gives you the study's file, to keep or to import by hand.

A link never carries your password or your session: whoever receives it still
signs in with their own identity, and enters only with their own role.

Sharing a room — for administrators and owners
----------------------------------------------

The **Share** section of the room's page is where the people of the room are
decided. An editor or a reader sees it with a sentence explaining that this
part belongs to the administrators; *Who sees the study* stays visible to
everyone, read-only.

Adding a person
~~~~~~~~~~~~~~~

In *Who is here*, type the person's **ORCID iD**, choose the role, *Add*. The
person sees the room the next time they open the list. To take somebody out,
*remove* beside their name.

Give **editor** to whoever writes in the graph, **reader** to whoever needs to
follow the work without changing it — a specialist consulting the data, a
student in the first weeks, a colleague of the superintendence. Give
**administrator** sparingly: an administrator decides about the others.

Adding a team
~~~~~~~~~~~~~

A **team** is a named list of people, made by the node manager or by a node
editor. *Add team* gives the whole team a role at once; whoever joins the team
later gets it too. When a person has a role of their own and one through a
team, the higher one counts.

Inviting with a link
~~~~~~~~~~~~~~~~~~~~

*Invite by link*: choose the role (editor or reader) and *Make a link*. Copy it
at once — the node keeps only a checksum and cannot show it again. Whoever opens
it signs in with their own ORCID and receives the role the link offers.

Send invitation links in a private message, never in a public chat or on a
slide, and **revoke** a link once the people it was for have come in. A link
made here has no expiry until you revoke it.

Who sees the study
~~~~~~~~~~~~~~~~~~

Two choices, and a date:

* **Restricted** (the default) — only the people with a role in the room, after
  signing in.
* **Public** — anyone can read it, even without signing in. This is what
  publishing means: the study appears in the node's catalogue.
* **Embargo until** a date — until that day the study stays restricted, whatever
  is chosen above; on that day it becomes what you chose. Useful to agree a
  publication date with the excavation director or the superintendence and not
  have to remember it.

Choose, set the date if there is one, *Save*.

The owner
~~~~~~~~~

*The live copy* shows who owns the room. The owner can **transfer** the room to
another ORCID iD — for instance when the direction of an excavation changes
hands. The previous owner stays as an administrator. Transferring hands over
the job of managing the room; it does not change who signed what in the graph.

Archiving
~~~~~~~~~

At the end of a season, **archive** the room: it stays readable and citable,
nobody writes in it any more, and it can be brought back at the next season
with *bring it back*. Archiving is the normal way to close; it deletes nothing.

Deleting
~~~~~~~~

Only the **owner** deletes a room, from *Delete the room*, typing the room's id
to confirm. It cannot be undone: the room goes with its em.json and every
revision, its history, its members and its invitations. The files stay on the
node, and the node manager decides about those no other room uses. Nobody may
be inside the room at that moment.

If the room may ever be needed again, archive it instead.

Good habits
-----------

* One room per study. A room is the live copy of one em.json, and each em.json
  lives in one room.
* Before the end of the day, read *The numbers, and their holes* and *Waiting
  for you*: what is unsigned or without an epoch is easier to fix while the
  context is fresh.
* Roles follow the work, not the hierarchy: the person who records the units is
  an editor, whatever their title.
* Agree the visibility and the embargo with the excavation's director at the
  start, not at the end.
* Revoke invitation links after use; remove people who have left the project.
* On the excavation without a network, the work goes on: the node is on site.
  What was written there comes back to the institutional node at the end of the
  campaign, with its signatures.

Where to go next
----------------

The complete rules — profiles on the node, roles, groups, invitations, deleting
— are in :doc:`roles-and-users`. The node itself, and how the field node is
prepared, are in :doc:`field-node`.

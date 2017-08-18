organism
========

This section is auto-generated from the help text for the tripaille command
``organism``.


``add_organism`` command
------------------------

**Usage**::

    tripaille organism add_organism [OPTIONS] GENUS COMMON ABBR

**Help**

Add a new organism to the database


**Output**


    Organism information
    
**Options**::


      --species TEXT             The species of the organism
      --comment TEXT             A comment / description
      --infraspecific_rank TEXT  The type name of infraspecific name for any taxon
                                 below the rank of species. Must be one of
                                 ['subspecies', 'varietas', 'subvariety', 'forma',
                                 'subforma']
      --infraspecific_name TEXT  The infraspecific name for this organism.
      -h, --help                 Show this message and exit.
    

``get_organism_nodes`` command
------------------------------

**Usage**::

    tripaille organism get_organism_nodes [OPTIONS]

**Help**

Get organism nodes


**Output**


    Organism node information
    
**Options**::


      --node INTEGER  filter on node id
      -h, --help      Show this message and exit.
    

``get_organisms`` command
-------------------------

**Usage**::

    tripaille organism get_organisms [OPTIONS]

**Help**

Get organisms


**Output**


    Organism information
    
**Options**::


      --organism_id TEXT  An organism ID
      --genus TEXT        The genus of the organism
      --species TEXT      The species of the organism
      --common TEXT       The common name of the organism
      --abbr TEXT         The abbreviation of the organism
      --comment TEXT      A comment / description
      -h, --help          Show this message and exit.
    

``get_taxonomic_ranks`` command
-------------------------------

**Usage**::

    tripaille organism get_taxonomic_ranks [OPTIONS]

**Help**

Get taxonomic ranks


**Output**


    Taxonomic ranks
    
**Options**::


      -h, --help  Show this message and exit.
    

``sync`` command
----------------

**Usage**::

    tripaille organism sync [OPTIONS]

**Help**

Synchronize an organism


**Output**


    status
    
**Options**::


      --organism TEXT     Common name of the organism to sync
      --organism_id TEXT  ID of the organism to sync
      --job_name TEXT     Name of the job
      --no_wait           Return immediately without waiting for job completion
      -h, --help          Show this message and exit.
    

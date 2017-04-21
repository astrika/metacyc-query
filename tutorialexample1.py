"""
The following is retrieved from PythonCyc tutorial:
https://github.com/latendre/PythonCyc/blob/master/doc/tutorial.md#pframes
"""

import pythoncyc.config as config
config.set_host_name('castalia.cs.fiu.edu')
import pythoncyc
def create_pgdb_with_compounds_and_reactions(orgid):
     """
     Create a PythonCyc PGDB object with all its compounds and reactions
     PFrames created. Return the PGDB object.
     """
     pgdb = pythoncyc.select_organism(orgid)
     pgdb.compounds
     pgdb.reactions
     return pgdb
pgdb = create_pgdb_with_compounds_and_reactions('ecoli')
print pgdb

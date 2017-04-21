#allows the remote access to pathway-tools on castalia
import pythoncyc.config as config
config.set_host_name('castalia.cs.fiu.edu')
import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)
meta = pythoncyc.select_organism('meta')
print pythoncyc.all_orgids()
#attributing trp data frame to meta
meta.trp
"""
prints: <PGDB meta, currently has 1 PFrames>, which shows that trp data frame
was attrubuted to meta
"""
print meta
rxn9000 = meta.rxn9000
print meta.trp.frameid
reactions = meta.reactions
print reactions
organisms = meta.organisms
print organisms
#accesses a certain instance in PFrame reactions
print reactions.instances[0]
#what is on the left side of this reactions instance
print reactions[0].left
#what is on the right side of this reactions instance
print reactions[0].right
#method accesses an instance without the use of Pframes but rather just frame ids
print meta.get_slot_values('TRP', 'CHEMICAL-FORMULA')
print meta

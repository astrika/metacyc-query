#allows the remote access to pathway-tools on castalia
import pythoncyc.config as config
config.set_host_name('castalia.cs.fiu.edu')
import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)
meta = pythoncyc.select_organism('meta')
print pythoncyc.all_orgids()
meta.trp
print meta
rxn9000 = meta.rxn9000
print meta.trp.frameid
rxns_trp_right = [meta[fid] for fid in meta.trp.appears_in_right_side_of]
print rxns_trp_right
reactions = meta.reactions
print reactions
organisms = meta.organisms
print organisms
print reactions.instances[0]
print reactions[0].left
print reactions[0].right
print meta.get_slot_values('TRP', 'CHEMICAL-FORMULA')
print meta

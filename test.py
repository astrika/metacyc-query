import pythoncyc.config as config
config.set_host_name('castalia.cs.fiu.edu')
import pythoncyc
meta = pythoncyc.select_organism('meta')
print pythoncyc.all_orgids()
meta.trp
print meta
rxn9000 = meta.rxn9000
print meta.trp.frameid
rxns_trp_right = [meta[fid] for fid in meta.trp.appears_in_right_side_of]
reactions = meta.reactions
print reactions
organisms = meta.organisms
print organisms

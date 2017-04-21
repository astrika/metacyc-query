#allows the remote access to pathway-tools on castalia
import pythoncyc.config as config
config.set_host_name('castalia.cs.fiu.edu')
import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)
meta = pythoncyc.select_organism('meta')
#a list of PFrames of reactions that contain TRP on right side
rxns_trp_right = [meta[fid] for fid in meta.trp.appears_in_right_side_of]
print rxns_trp_right

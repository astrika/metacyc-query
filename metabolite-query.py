#allows the remote access to pathway-tools on castalia
import pythoncyc.config as config
config.set_host_name('castalia.cs.fiu.edu')
import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)
print meta.pathways_of_compound('1,2-dilinoleoyl-sn-glycero-3-phosphocholine')

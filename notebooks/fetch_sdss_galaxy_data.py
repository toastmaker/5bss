import numpy as np
import sqlcl

topN = 5000 # =2 for testing 

q = "select top %i modelMag_u as u, modelMag_g as g, modelMag_r as r, modelMag_i as i, modelMag_z as z, z as redshift from SpecPhotoAll WHERE class='GALAXY' AND modelMag_u!='' AND modelMag_u > 14"%topN
lines = sqlcl.query(q).readlines()

data = []
for line in lines[2:]:
    data.append(map(float,line[:-1].split(',')))
data = np.array(data)
np.save('sdssphotoz.npy', data)
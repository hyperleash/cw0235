from Bio import SearchIO
import numpy as np
from scipy.stats import gmean

best_hit = []
best_score = 0
good_hit_scores  = []
id = ''
for result in SearchIO.parse('tmp.hhr', 'hhsuite3-text'):
    id=result.id
    for hit in result.hits:
        if hit.score >= best_score:
            best_score = hit.score
            best_hit = [hit.id, hit.evalue, hit.score]
        if hit.evalue < 1.e-5:
            good_hit_scores.append(hit.score)

fhOut = open("hhr_parse.out", "w")
fhOut.write("query_id,best_hit,best_evalue,best_score,score_mean,score_std,score_gmean\n")
mean=format(np.mean(good_hit_scores), ".2f")
std=format(np.std(good_hit_scores), ".2f")
g_mean=format(gmean(good_hit_scores), ".2f")

fhOut.write(f"{id},{best_hit[0]},{best_hit[1]},{best_hit[2]},{mean},{std},{g_mean}\n")
fhOut.close()
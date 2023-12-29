import pandas as pd

df = pd.read_csv("all_results.txt")

df[['query_id', 'best_hit']].to_csv('best_hits.csv', index=False)

mean_std_gmean = {
    'score_std': df['score_std'].mean(),
    'score_gmean': df['score_gmean'].mean() 
}

stats_df = pd.DataFrame([mean_std_gmean])
stats_df.to_csv('stats.csv', index=False)

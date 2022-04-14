
import pandas as pd

def write_to_csv(summary):
    summary.to_csv('lightning_CA_summary.csv', index=False)
    return



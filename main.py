import csv

# Create a list of vendor names and their corresponding software names
vendors = {
    "AppViewX": ["AppViewX", "AppViewX Dashboard", "AppViewX Cert+", "AppViewX ADC+", "AppViewX Workflow+"],
    "Micro Focus": ["Micro Focus LoadRunner", "Micro Focus UFT", "Micro Focus ALM", "Micro Focus Fortify", "Micro Focus Service Manager"],
    "Atlassian": ["Jira", "Confluence", "Bitbucket", "Bamboo", "Crowd"],
    "Hitachi": ["Hitachi Content Platform", "Hitachi Ops Center", "Hitachi Virtual Storage Platform", "Hitachi Storage Advisor"],
    "Abacus": ["AbacusLaw", "Abacus Private Cloud", "Abacus Payment Exchange", "Abacus Court Rules"],
    "Flexera": ["FlexNet Manager Suite", "FlexNet Code Insight", "FlexNet Connect", "FlexNet Operations"],
    "Automatic Sync Technologies": ["AST QuickDBD", "AST PPMS", "AST Timekeeper"],
    "AquaFold": ["AquaDataStudio", "Fusion Trade Innovation", "Fusion Treasury", "Fusion Risk"],
    "Aqua-Fol": ["DataStudio", "Fusion Trade Innovation", "Fusion Treasury", "Fusion Risk"],
    
}

# Create a CSV file and write the header row
with open("software.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["RollupVendor", "DetailView", "Description"])

    # Write each vendor and their corresponding software names to the CSV file
    for vendor, software in vendors.items():
        writer.writerow([vendor, vendor + " Inc.", ", ".join(software)])

#Step #2 - Find matching between software, vendor name which have been removed or have been marked for removal in the above file.

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

vendor_name = "Acqua Fold"
Software_name = "Data Studio"

# Read the CSV file into a pandas dataframe
df = pd.read_csv("software.csv")

# Use fuzzy search to find the closest match to "Fin Astra" in the RollupVendor column
matches = df["RollupVendor"].apply(lambda x: fuzz.token_set_ratio(x, vendor_name))
best_match_index = matches.idxmax()

# Extract the row with the best match into a new dataframe
best_match_df = df.loc[[best_match_index]]

# Use fuzzy search to find the closest match to "LoanIQ" in the Description and DetailView columns of the best match row
matches = best_match_df.apply(lambda x: fuzz.token_set_ratio(x["Description"], Software_name) + fuzz.token_set_ratio(x["DetailView"], "LoanIQ"), axis=1)
best_match_index2 = matches.idxmax()

# Extract the row with the best match into a new dataframe
best_match_df2 = best_match_df.loc[[best_match_index2]]

# Print the dataframe
print(best_match_df2)

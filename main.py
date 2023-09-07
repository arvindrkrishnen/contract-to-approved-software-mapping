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

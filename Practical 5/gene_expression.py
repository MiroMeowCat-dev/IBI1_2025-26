import matplotlib.pyplot as plt
# Step 1: Create a dictionary for the initial gene expression data
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}
# Step 2: Print the initial dictionary
print("Initial gene expression dictionary:")
print(gene_expression)
# Step 3: Add MYC to the dictionary
gene_expression["MYC"] = 11.6
#Print the updated dictionary
print("Updated gene expression dictionary:")
print(gene_expression)
# Choose the gene you want to look up by changing the variable below
gene_of_interest = "TP53"
# Step 5: Print the expression value for the selected gene
if gene_of_interest in gene_expression:
    print(f"\nExpression value of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"\nError: {gene_of_interest} is not present in the dataset.")
    # Step 6: Calculate and print the average expression value
average_expression = sum(gene_expression.values()) / len(gene_expression)
print(f"\nAverage gene expression level: {average_expression:.2f}")
# Step 7: Create a bar chart
genes = list(gene_expression.keys())
values = list(gene_expression.values())

plt.bar(genes, values)
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Value")
plt.show()
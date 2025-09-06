def calculate_carbon(trees, rate):
    """
    Calculate carbon sequestration in forests.
    trees: number of trees
    rate: carbon captured per tree (kg CO2/year)
    """
    return trees * rate

# Example usage
if __name__ == "__main__":
    print("Carbon captured:", calculate_carbon(100, 25), "kg CO2/year")

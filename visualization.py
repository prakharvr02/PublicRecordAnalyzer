import pandas as pd
import matplotlib.pyplot as plt

class PublicRecordsVisualizer:
    def __init__(self, legal_cases_file, property_records_file):
        self.legal_cases = pd.read_csv(legal_cases_file)
        self.property_records = pd.read_csv(property_records_file)

    def plot_repeated_litigations(self):
        """Plot repeated litigations."""
        repeated_litigations = self.legal_cases.groupby("defendant_name").size().reset_index(name="count")
        repeated_litigations = repeated_litigations[repeated_litigations["count"] > 1]
        repeated_litigations.plot(kind="bar", x="defendant_name", y="count", title="Repeated Litigations")
        plt.show()

    def plot_business_affiliations(self):
        """Plot business affiliations."""
        business_affiliations = self.property_records.groupby("owner_name").size().reset_index(name="count")
        business_affiliations = business_affiliations[business_affiliations["count"] > 1]
        business_affiliations.plot(kind="bar", x="owner_name", y="count", title="Business Affiliations")
        plt.show()

if __name__ == "__main__":
    visualizer = PublicRecordsVisualizer("data/legal_cases.csv", "data/property_records.csv")
    visualizer.plot_repeated_litigations()
    visualizer.plot_business_affiliations()

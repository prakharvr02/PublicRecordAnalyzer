import pandas as pd

class PublicRecordsAnalyzer:
    def __init__(self, legal_cases_file, property_records_file):
        self.legal_cases = pd.read_csv(legal_cases_file)
        self.property_records = pd.read_csv(property_records_file)

    def analyze_legal_cases(self):
        """Analyze legal cases to identify repeated litigations."""
        print("[*] Analyzing legal cases...")
        repeated_litigations = self.legal_cases.groupby("defendant_name").size().reset_index(name="count")
        repeated_litigations = repeated_litigations[repeated_litigations["count"] > 1]
        print("Repeated litigations:")
        print(repeated_litigations)

    def analyze_property_records(self):
        """Analyze property records to identify business affiliations."""
        print("[*] Analyzing property records...")
        business_affiliations = self.property_records.groupby("owner_name").size().reset_index(name="count")
        business_affiliations = business_affiliations[business_affiliations["count"] > 1]
        print("Business affiliations:")
        print(business_affiliations)

if __name__ == "__main__":
    analyzer = PublicRecordsAnalyzer("data/legal_cases.csv", "data/property_records.csv")
    analyzer.analyze_legal_cases()
    analyzer.analyze_property_records()

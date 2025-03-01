from data_collection import PublicRecordsCollector
from analysis import PublicRecordsAnalyzer
from visualization import PublicRecordsVisualizer

def main():
    # Step 1: Collect data
    collector = PublicRecordsCollector(api_key="your_api_key_here")
    legal_cases = collector.fetch_legal_cases("John Doe")
    property_records = collector.fetch_property_records("New York")
    collector.save_to_csv(legal_cases, "data/legal_cases.csv")
    collector.save_to_csv(property_records, "data/property_records.csv")

    # Step 2: Analyze data
    analyzer = PublicRecordsAnalyzer("data/legal_cases.csv", "data/property_records.csv")
    analyzer.analyze_legal_cases()
    analyzer.analyze_property_records()

    # Step 3: Visualize data
    visualizer = PublicRecordsVisualizer("data/legal_cases.csv", "data/property_records.csv")
    visualizer.plot_repeated_litigations()
    visualizer.plot_business_affiliations()

if __name__ == "__main__":
    main()

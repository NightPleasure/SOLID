from abc import ABC, abstractmethod


class ReportCreator(ABC):
    @abstractmethod
    def create_report(self, data):
        pass


class FinancialReportCreator(ReportCreator):
    def create_report(self, data):
        report = "Financial Report\n"
        report += f"Date: {data['date']}\n"
        report += f"Revenue: {data['revenue']}\n"
        report += f"Expenses: {data['expenses']}\n"
        report += f"Profit: {data['revenue'] - data['expenses']}\n"
        return report


class ReportGenerator:
    def __init__(self, creator: ReportCreator):
        self.creator = creator

    def generate_report(self, data):
        report = self.creator.create_report(data)
        return report


financial_creator = FinancialReportCreator()
report_generator = ReportGenerator(financial_creator)

data = {"date": "2023-05-15", "revenue": 10000, "expenses": 5000}
report = report_generator.generate_report(data)
print(report)

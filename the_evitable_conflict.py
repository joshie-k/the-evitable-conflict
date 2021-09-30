from typing import List

class WorldEconomyAggregator:
    """
    Imagine there is a lot of garbage code around that you can't 
    test. 
    """
    def aggregate_spend(self, super_computers: List[SuperComputer]):
        aggregate_data = {}
        for sc in super_computers:
            data = sc.get_spend_by_country()
            aggregate_data.update(data)
        
        return aggregate_data 

class SuperComputer:
    def get_spend_by_country(self):
        """
        Keys will be a SuperComputer instance id + "_" + a country code, 
        values will be an int dollar amount. 

        e.g. 

        {
            "SC12_45" : 700000,
            "SC12_47" : 381111,
            ...
        }
        """
        ...

class HiveMind:

    def upload_data_to_hive_mind(self):
        ...

    def get_aggregate_spend(self) -> dict:
        ...

class TerribleClassMadeByYouTenYearsAgo:

    def human_spend_notification_generator(self) -> str:
        """
            Imagine there is also a lot of tightly coupled code here
            that also shows up in the html notification. 
        """
        data = HiveMind.get_current_aggregate_spend()

        html_notification = ""

        for code in data:
            html_notification += "<td>" + code + "</td>"
            for spend in data[code]:
                html_notification += "<td>" + spend + "</td>"
            html_notification += "<tr>"

        html_notification = "<table border=1>" + html_notification + "<table>"



    

:earth_americas: **Overview**

---

This project analyzes freight transportation data provided by the Bureau of Transportation Statistics (BTS) to uncover insights related to the efficiency, safety, and environmental impacts of goods movement across North America.
The study focuses on major trade flows between the USA, Canada, and Mexico, covering various modes of transport: road, rail, air, and water.

Through this analysis, the project aims to answer questions such as:

* Which modes of transport dominate cross-border trade?

* What are the key states/provinces involved in exports and imports?

* How do freight charges and logistics practices affect trade efficiency?

---

**Project Structure**

| **File**	                                            |  **Description**                                                                              |
------------------------------------------------------  | ----------------------------------------------------------------------------------------------|
| data_append_freight.py                                | Appends multiple CSV files into a single SQLite database. Features a GUI for file selection.  |
| handling_data.ipynb                                 	| Cleans the database by removing duplicates and preparing the data for analysis.               |
| transborder_data_analysis.ipynb	                      | Contains the full analysis, including trade volumes, transport modes, and product types.      |
| codes-north-american-transborder-freight-raw-data.pdf	| Provides feature descriptions for the raw dataset.                                            |
| united-states-map-with-canada-and-mexico.png	        | A visual map of the regions, highlighting states/provinces in the trade analysis.             |

---
:gem: **Key Highlights**

* USA exports more to Canada than Mexico, with trucks dominating the freight channels.

* **Texas** is the leading exporting state, while Ontario and Chihuahua receive the most goods.

* Imports from Mexico are higher in value, but Canada leads in volume.

* Containerization practices differ: all Canadian-bound exports are containerized, while most Mexico-bound goods are not.

* Seasonal peaks (June 2022 for Canada; October 2023 and August 2024 for Mexico) indicate targeted trade cycles.

---
:white_square_button: **Recommendations from the Analysis**

* Strengthen trucking infrastructure and border-crossing facilities.

* Diversify transport modes for risk reduction, especially for Canada.

* Promote containerization for Mexico-bound exports to improve security and efficiency.

* Expand regional export hubs beyond Texas to reduce concentration risk.

* Leverage trade incentives and update bilateral agreements to optimize cost advantages.

---
:satellite: **Creative Touch**

The included map (united-states-map-with-canada-and-mexico.png) visually anchors the analysis, showing key trade states and provinces, providing an intuitive overview of cross-border flows.

---
**How to Use**

1. Run data_append_freight.py to append your CSV files into an SQLite database.

2. Open handling_data.ipynb to clean and prepare your data.

3. Run transborder_data_analysis.ipynb for the full analysis, including charts and insights.

4. Refer to the PDF for detailed feature descriptions.

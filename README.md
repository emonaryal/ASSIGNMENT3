Project Overview

This project provides a simple Python-based system for collecting and managing staff information and requisitions. The system is designed to collect staff details such as the date of requisition, staff ID, name, and generates a unique requisition ID for each entry. This project focuses on basic input handling and data management, making it a useful learning tool or a foundation for further development.

Features

-Staff Information Collection: Capture essential staff details like date, ID, and name.
-Requisition Management: Automatically generates a unique requisition ID starting from 10000.
-Basic Input Processing: Simple prompts for user inputs with the ability to expand the system further.
-Extendable Structure: Designed for future improvements like data validation, storage, and complex requisition handling.

Code Structure

Attributes:

-Date: Captures the date of the requisition.
-Staff_ID: Unique identifier for each staff member.
-Staff_Name: Name of the staff member.
-Requisition_ID: Auto-generated identifier for each requisition, starting from 10000 and incrementing with each entry.

Methods:

staff_info():
-Purpose: This method collects staff information, including the date, staff ID, and staff name, while generating a new requisition ID for each entry.
-Global Variables: The method uses global variables to store inputs, which can be refactored in the future for better modularity and encapsulation.

How to Run

-Install Visual Studio Code.
-Run the 'PART_A.py' file in Visual Studio Code.
-Enter Staff Information and requisition details.

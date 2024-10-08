# MAXI ROE - Recycling Original Equipment

MAXI ROE is a vehicle dismantling management system designed to optimize the removal, cataloging, and resale of OEM parts. This system ensures that dismantlers can extract maximum profitability from every vehicle by following specific rules and logic, utilizing market data, and adhering to eco-friendly practices. MAXI ROE integrates advanced data-driven strategies with automation to streamline the dismantling process and part sales.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Rules and Logic](#rules-and-logic)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

MAXI ROE is a modular platform that combines market analysis, optimized part removal sequences, dynamic pricing, and efficient storage methods to ensure the profitable resale of used parts. The system also tracks each part using QR codes and SKUs, ensuring full traceability from removal to sale. Additionally, the system integrates eco-friendly recycling practices to minimize waste from vehicles.

## Features

- **Part Categorization**: Ensures parts are matched to their corresponding vehicle types and models.
- **Dynamic Pricing**: Uses real-time market data for competitive and profitable pricing.
- **Optimized Removal Order**: Prioritizes parts based on profitability and ease of removal.
- **Sectional Vehicle Framework**: Divides the vehicle into logical sections for better part location and removal.
- **AI-Powered Quality Control**: Assesses part condition before listing to prevent unprofitable listings.
- **Inventory Storage Optimization**: Matches parts to suitable storage bins or shelves based on volume and weight.
- **QR Code and SKU Tracking**: Ensures traceability for each part from dismantling to sale.
- **Eco-Friendly Disposal**: Integrates recycling strategies for non-sellable parts.
- **Data-Driven Reporting**: Provides insights and reports for better decision-making.

## System Requirements

- **Server**: Apache Web Server (via XAMPP)
- **Database**: PHPMyAdmin with SQL database
- **Back-End**: Flask (Python)
- **Front-End**: React.js
- **Storage**: S3 for image storage
- **AI Integration**: TensorFlow CV for part condition assessment
- **Optional**: Integration with eBay’s API (for market data)

## Installation

See [Installation.md](./Installation.md) for setup and installation instructions.

## Rules and Logic

The system is governed by a strict set of rules and logic to optimize part removal and resale profitability. See [LOGIC.md](./LOGIC.md) for detailed rules and logic.

## Usage

To understand how to use MAXI ROE for dismantling vehicles, see [Usage.md](./Usage.md) for a step-by-step guide.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
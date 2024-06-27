# Invoice Number Header

This Odoo module adds the invoice number to the header of invoice reports starting from the second page.

## Features

- Adds the invoice number to the header of invoice reports
- Only appears on the second page and subsequent pages
- Includes company logo and name alongside the invoice number
- Seamlessly integrates with the standard Odoo invoice report

## Installation

1. Copy this folder to your Odoo addons directory.
2. Restart your Odoo server.
3. Go to Apps and search for "Invoice Number Header".
4. Click Install.

## Usage

Once installed, this module automatically modifies the invoice report template. No additional configuration is required.

- The first page of the invoice remains unchanged.
- From the second page onwards, a header will appear containing:
	- Your company logo
	- Your company name
	- The invoice number
	
This feature is particularly useful for multi-page invoices, ensuring that the invoice number is visible on all pages after the first.

## Compatibility

This module is compatible with Odoo 17. It may work with other versions, but has not been tested.

## Support

For questions, issues, or support, please contact your Odoo administrator or the module maintainer.

## Customization

If you need to customize the appearance of the header or include additional information, you can modify the `report/report_invoice.xml` file.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

This module is released under the [GPL-3] license.

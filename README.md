Account invoice analytics distribution required
===============================================

OpenERP module that make invoice analytics distribution account required
in sale invoice line.

Also if you have a default value for the field, add a new entry
in Settings > Configuration > Parameter > Configuration Parameters:

    Name: "analytics_distribution_default"
    Field: Analytic Distribution (model Invoice Line)
    Value: the id of the distribution model object

Author:

    Mariano Ruiz <mrsarm@gmail.com> (Enterprise Objects Consulting)

This sources are available in https://github.com/eoconsulting/account_invoice_analytics_distribution_required

License: AGPL-3
(C) 2013

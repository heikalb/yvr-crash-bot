Data source: https://public.tableau.com/app/profile/icbc/viz/LowerMainlandCrashes/LMDashboard

We only obtained data on casualty crashes 2017-2022
(no PDO (property damage only) crashes).

To get a data file click download icon > "Crosstab" > "Location" > "CSV" > "Download"

For what munis count as Metro Vancouver, we arbitrarily followed this:
http://www.metrovancouver.org/about/municipalities/Pages/default.aspx

## Updating data
The ICBC data files are not conveniently downloadable through CLI. ICBC data is
updated around the following spring for the current year's data. For now, to
get the bot to consider updated data, the data files have to be updated annually 
when they become available.

Everytime we update the data we also need update the info on years in `../constants.py`

TODO: make the data updating automatic

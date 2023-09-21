ICBC_DATA_START_YEAR = 2018
ICBC_DATA_END_YEAR = 2022
# Limit to intersections with 1 crash/month in five years
MIN_CRASHES = 60

DEFAULT_AREA = "Vancouver"
AREA_2_FILE_GLOB = {"Vancouver": "data/intersections/vancouver.csv",
                    "Metro Vancouver": "data/intersections/metro-van/*.csv"}

# To avoid tweets too long
MAX_SITE_NAME_LENGHTH = 100

muni_accounts = {
    "Vancouver": "@CityofVancouver",
    "Burnaby": "@CityofBurnaby",
    "Coquitlam": "@cityofcoquitlam",
    "Delta": "@CityofDeltaBC",
    "Langley": "@LangleyCity_",
    "Maple Ridge": "@YourMapleRidge",
    "New Westminster": "@New_Westminster",
    "North Vancouver": "@CityOfNorthVan",
    "Pitt Meadows": "@citypittmeadows",
    "Port Coquitlam": "@CityofPoCo",
    "Port Moody": "@CityofPoMo",
    "Richmond": "@Richmond_BC",
    "Surrey": "@CityofSurrey",
    "West Vancouver": "@WestVanDistrict",
    "White Rock": "@whiterockcity",
}

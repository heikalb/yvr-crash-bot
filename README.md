# yvr-crash-bot
This is a Twitter bot displaying data on traffic crashes in Metro Vancouver. 
The goal is to raise public awareness of traffic violence.
A project of Vision Zero Vancouver: https://visionzerovancouver.ca/, https://twitter.com/VisionZeroYVR

## Features
1. Featured intersections: periodically tweet about intersections with many crashes over the years.
   Data from ICBC, https://public.tableau.com/app/profile/icbc/viz/LowerMainlandCrashes/LMDashboard.

## Details
- Twitter bot account: https://twitter.com/yvr_crash_bot
- Tweets are posted as cronjobs run via GitHub Actions (see `.github/workflows/*.yaml`)
- The credentials for tweeting programmatically are from https://developer.twitter.com.
  - The credentials are stored as Actions secrets (environment variables) in this repo.

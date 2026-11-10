---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/integrate-applications-data-agent/
title: Integrate QueryData with an application \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:58:50.900698+00:00
---

# Integrate QueryData with an application  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/integrate-applications-data-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Integrate QueryData with an application Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial describes how to set up and use QueryData in Bigtable using the Google Cloud console and integrate it with your application. Learn how to build the [context set](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/context-sets-overview) file, create a context set that uses the context set file, use [MCP Toolbox](https://github.com/googleapis/mcp-toolbox) to call the [QueryData method in the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases) to generate SQL queries for natural language questions, and integrate it with your application.

For more information, see [QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/data-agent-overview). 

## Objectives

This tutorial covers the following objectives:

  * Create database tables and populate them with data.
  * Build a context set file with the context engineering agent.
  * Create a context set and upload a context set file.
  * Test QueryData and generate SQL queries in Bigtable Studio.
  * Integrate QueryData with your application using [Gemini Data Analytics QueryData](https://mcp-toolbox.dev/integrations/cloudgda/tools/cloud-gda-query/) tool in MCP Toolbox.
  * Add grounding to LLM responses using value search queries.



## Costs

In this document, you use the following billable components of Google Cloud:

  * [ Bigtable](https://docs.cloud.google.com/bigtable/pricing)
  * [ Gemini for Google Cloud API](https://docs.cloud.google.com/gemini/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free).

To avoid continued billing, delete the resources you created when you finish the tasks in this document. For more information, see Clean up.

## Before you begin

Complete the following prerequisites before creating a context set.

### Enable required services

Enable the following services for your project: 

  * [Data Analytics API with Gemini](https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com)
  * [Gemini for Google Cloud API](https://console.cloud.google.com/apis/library/cloudaicompanion.googleapis.com)
  * [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com)



### Prepare a Bigtable instance

Make sure that a Bigtable instance is available. For more information, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).

### Install the `cbt` CLI

Install and configure the `cbt` CLI to create tables and populate them with data. For more information, see [`cbt` CLI overview](https://docs.cloud.google.com/bigtable/docs/cbt-overview).

### Required roles and permissions

  * Grant the `bigtable.admin` role to the IAM user at the instance or project level. For more information, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).
  * Grant the `geminidataanalytics.queryDataUser` role to the IAM user at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).
  * To create, upload, and manage context sets, grant the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role to the IAM user at the project level. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).



## Create the `flights` and `airports` schema and tables

In this section, you create the `flights` and `airports` database tables for this tutorial.

  1. Configure your default project and instance in `~/.cbtrc`: 
         
         echo project = PROJECT_ID >> ~/.cbtrc
         echo instance = INSTANCE_ID >> ~/.cbtrc

where: 
     * PROJECT_ID: your Google Cloud project ID.
     * INSTANCE_ID: your Bigtable instance ID.
  2. Run the following command to create the `airports` table and `info` column family:
         
         cbt createtable airports "families=info"

  3. Run the following command to create the `flights` table and `info` column family:
         
         cbt createtable flights "families=info"




## Populate the `flights` and `airports` tables

In this section, you populate the `flights` and `airports` tables using the `cbt import` command.

  1. Create a file named `airports.csv` with the following contents:
         
         ,info,info,info,info
         ,iata,name,city,country
         AIRPORT#3249,BOS,General Edward Lawrence Logan International Airport,Boston,United States
         AIRPORT#3257,OGG,Kahului Airport,Kahului,United States
         AIRPORT#3259,MCI,Kansas City International Airport,Kansas City,United States
         AIRPORT#3263,PHX,Phoenix Sky Harbor International Airport,Phoenix,United States
         AIRPORT#3270,SFO,San Francisco International Airport,San Francisco,United States
         AIRPORT#3285,LAX,Los Angeles International Airport,Los Angeles,United States
         AIRPORT#3287,CLE,Cleveland Hopkins International Airport,Cleveland,United States
         AIRPORT#3295,EWR,Newark Liberty International Airport,Newark,United States
         AIRPORT#3296,BOI,Boise Air Terminal/Gowen Field,Boise,United States
         AIRPORT#3303,DAL,Dallas Love Field,Dallas,United States
         AIRPORT#3315,KOA,Ellison Onizuka Kona International At Keahole Airport,Kona,United States
         AIRPORT#3321,DCA,Ronald Reagan Washington National Airport,Washington,United States
         AIRPORT#3336,SLC,Salt Lake City International Airport,Salt Lake City,United States
         AIRPORT#3350,IAH,George Bush Intercontinental Houston Airport,Houston,United States
         AIRPORT#3370,PIT,Pittsburgh International Airport,Pittsburgh,United States
         AIRPORT#3376,MIA,Miami International Airport,Miami,United States
         AIRPORT#3377,SEA,Seattle Tacoma International Airport,Seattle,United States
         AIRPORT#3382,LGB,Long Beach /Daugherty Field/ Airport,Long Beach,United States
         AIRPORT#3385,IND,Indianapolis International Airport,Indianapolis,United States
         AIRPORT#3402,LIH,Lihue Airport,Lihue,United States
         AIRPORT#3421,SAT,San Antonio International Airport,San Antonio,United States
         AIRPORT#3426,RDU,Raleigh Durham International Airport,Raleigh-durham,United States
         AIRPORT#3436,TUS,Tucson International Airport,Tucson,United States
         AIRPORT#3444,BUR,Bob Hope Airport,Burbank,United States
         AIRPORT#3445,DTW,Detroit Metropolitan Wayne County Airport,Detroit,United States
         AIRPORT#3470,DFW,Dallas Fort Worth International Airport,Dallas-Fort Worth,United States
         AIRPORT#3473,AUS,Austin Bergstrom International Airport,Austin,United States
         AIRPORT#3478,STL,St Louis Lambert International Airport,St. Louis,United States
         AIRPORT#3482,ATL,Hartsfield Jackson Atlanta International Airport,Atlanta,United States
         AIRPORT#3487,FAT,Fresno Yosemite International Airport,Fresno,United States
         AIRPORT#3514,IAD,Washington Dulles International Airport,Washington,United States
         AIRPORT#3517,MKE,General Mitchell International Airport,Milwaukee,United States
         AIRPORT#3520,PDX,Portland International Airport,Portland,United States
         AIRPORT#3528,HNL,Daniel K Inouye International Airport,Honolulu,United States
         AIRPORT#3531,SAN,San Diego International Airport,San Diego,United States
         AIRPORT#3534,ONT,Ontario International Airport,Ontario,United States
         AIRPORT#3547,MDW,Chicago Midway International Airport,Chicago,United States
         AIRPORT#3551,DEN,Denver International Airport,Denver,United States
         AIRPORT#3552,PHL,Philadelphia International Airport,Philadelphia,United States
         AIRPORT#3597,JFK,John F Kennedy International Airport,New York,United States
         AIRPORT#3607,RNO,Reno Tahoe International Airport,Reno,United States
         AIRPORT#3617,SMF,Sacramento International Airport,Sacramento,United States
         AIRPORT#3619,COS,City of Colorado Springs Municipal Airport,Colorado Springs,United States
         AIRPORT#3639,PSP,Palm Springs International Airport,Palm Springs,United States
         AIRPORT#3649,BWI,Baltimore/Washington International Thurgood Marshall Airport,Baltimore,United States
         AIRPORT#3658,MSP,Minneapolis-St Paul International/Wold-Chamberlain Airport,Minneapolis,United States
         AIRPORT#3661,MSY,Louis Armstrong New Orleans International Airport,New Orleans,United States
         AIRPORT#3667,SNA,John Wayne Airport-Orange County Airport,Santa Ana,United States
         AIRPORT#3676,CLT,Charlotte Douglas International Airport,Charlotte,United States
         AIRPORT#3677,LAS,McCarran International Airport,Las Vegas,United States
         AIRPORT#3678,MCO,Orlando International Airport,Orlando,United States
         AIRPORT#3742,MRY,Monterey Peninsula Airport,Monterey,United States
         AIRPORT#3743,SBA,Santa Barbara Municipal Airport,Santa Barbara,United States
         AIRPORT#3875,RDD,Redding Municipal Airport,Redding,United States
         AIRPORT#3876,EUG,Mahlon Sweet Field,Eugene,United States
         AIRPORT#3878,MFR,Rogue Valley International Medford Airport,Medford,United States
         AIRPORT#3880,RDM,Roberts Field,Redmond-Bend,United States
         AIRPORT#4111,ACV,California Redwood Coast-Humboldt County Airport,Arcata CA,United States
         AIRPORT#4419,CEC,Jack Mc Namara Field Airport,Crescent City,United States
         AIRPORT#4460,SBP,San Luis County Regional Airport,San Luis Obispo,United States
         AIRPORT#4768,PSC,Tri Cities Airport,Pasco,United States
         AIRPORT#5088,SUN,Friedman Memorial Airport,Hailey,United States
         AIRPORT#5305,ASE,Aspen-Pitkin Co/Sardy Field,Aspen,United States
         AIRPORT#5362,MMH,Mammoth Yosemite Airport,Mammoth Lakes,United States

  2. Import the data from the `airports.csv` file into the `airports` table:
         
         cbt import airports airports.csv

  3. Create a file named `flights.csv` with the following contents:
         
         ,info,info,info,info,info,info,info,info,info,info
         ,airline,flight_number,departure_airport,arrival_airport,departure_time,arrival_time,departure_gate,arrival_gate,departure_city,arrival_city
         FLIGHT#0000,UA,1532,SFO,DEN,2025-01-01 05:50:00,2025-01-01 09:23:00,E49,D6,San Francisco,Denver
         FLIGHT#0001,UA,1158,SFO,ORD,2025-01-01 05:57:00,2025-01-01 12:13:00,C38,D30,San Francisco,Chicago
         FLIGHT#0002,F9,1057,IAH,SFO,2025-01-01 05:52:00,2025-01-01 08:14:00,E33,E43,Houston,San Francisco
         FLIGHT#0003,OO,6403,MFR,SFO,2025-01-01 05:57:00,2025-01-01 07:23:00,A6,E50,Medford,San Francisco
         FLIGHT#0004,OO,5628,RNO,SFO,2025-01-01 06:19:00,2025-01-01 07:37:00,A37,B29,Reno,San Francisco
         FLIGHT#0005,CY,922,SFO,LAX,2025-01-01 06:38:00,2025-01-01 07:49:00,D20,E45,San Francisco,Los Angeles
         FLIGHT#0006,AA,338,LAX,SFO,2025-01-01 06:44:00,2025-01-01 08:03:00,E20,A45,Los Angeles,San Francisco
         FLIGHT#0007,UA,1195,MCO,SFO,2025-01-01 12:28:00,2025-01-01 15:06:00,D22,B36,Orlando,San Francisco
         FLIGHT#0008,OO,5632,SBA,SFO,2025-01-01 06:56:00,2025-01-01 08:39:00,E19,A49,Santa Barbara,San Francisco
         FLIGHT#0009,UA,300,CLE,SFO,2025-01-01 07:15:00,2025-01-01 09:22:00,E8,C28,Cleveland,San Francisco
         FLIGHT#0010,UA,706,SEA,SFO,2025-01-01 07:14:00,2025-01-01 09:07:00,A32,B26,Seattle,San Francisco
         FLIGHT#0011,AA,167,MIA,SFO,2025-01-01 07:47:00,2025-01-01 10:51:00,A23,E4,Miami,San Francisco
         FLIGHT#0012,OO,5441,SFO,SBP,2025-01-01 07:08:00,2025-01-01 08:12:00,E21,D24,San Francisco,San Luis Obispo
         FLIGHT#0013,UA,616,SFO,ORD,2025-01-01 07:14:00,2025-01-01 13:24:00,A11,D8,San Francisco,Chicago
         FLIGHT#0014,AA,24,SFO,JFK,2025-01-01 07:14:00,2025-01-01 15:46:00,D4,C15,San Francisco,New York
         FLIGHT#0015,UA,72,HNL,SFO,2025-01-01 07:28:00,2025-01-01 14:22:00,B33,D49,Honolulu,San Francisco
         FLIGHT#0016,AS,244,PDX,SFO,2025-01-01 07:24:00,2025-01-01 09:04:00,E46,B8,Portland,San Francisco
         FLIGHT#0017,OO,6307,MSP,SFO,2025-01-01 07:29:00,2025-01-01 09:32:00,C49,C36,Minneapolis,San Francisco
         FLIGHT#0018,OO,4975,STL,SFO,2025-01-01 07:31:00,2025-01-01 09:58:00,C43,E16,St. Louis,San Francisco
         FLIGHT#0019,AA,23,DFW,SFO,2025-01-01 08:41:00,2025-01-01 10:34:00,E13,E19,Dallas-Fort Worth,San Francisco
         FLIGHT#0020,B6,434,SFO,BOS,2025-01-01 08:00:00,2025-01-01 16:23:00,D16,E46,San Francisco,Boston
         FLIGHT#0021,F9,657,DEN,SFO,2025-01-01 07:58:00,2025-01-01 09:13:00,E41,E28,Denver,San Francisco
         FLIGHT#0022,OO,6464,COS,SFO,2025-01-01 07:56:00,2025-01-01 09:45:00,D49,E17,Colorado Springs,San Francisco
         FLIGHT#0023,UA,1235,IAD,SFO,2025-01-01 08:28:00,2025-01-01 11:15:00,A22,D19,Washington,San Francisco
         FLIGHT#0024,OO,6527,EUG,SFO,2025-01-01 07:54:00,2025-01-01 09:36:00,D9,B26,Eugene,San Francisco
         FLIGHT#0025,AA,242,SFO,ORD,2025-01-01 08:18:00,2025-01-01 14:26:00,E30,C1,San Francisco,Chicago
         FLIGHT#0026,UA,1739,SFO,EWR,2025-01-01 08:22:00,2025-01-01 16:42:00,C13,D45,San Francisco,Newark
         FLIGHT#0027,B6,133,BOS,SFO,2025-01-01 08:34:00,2025-01-01 12:30:00,D49,C16,Boston,San Francisco
         FLIGHT#0028,OO,6336,SFO,RNO,2025-01-01 08:32:00,2025-01-01 09:29:00,B45,A2,San Francisco,Reno
         FLIGHT#0029,UA,567,IAD,SFO,2025-01-01 10:47:00,2025-01-01 13:39:00,C27,B24,Washington,San Francisco
         FLIGHT#0030,OO,5223,SLC,SFO,2025-01-01 08:50:00,2025-01-01 09:55:00,C38,C11,Salt Lake City,San Francisco
         FLIGHT#0031,US,1784,SFO,CLT,2025-01-01 08:47:00,2025-01-01 16:32:00,C42,C31,San Francisco,Charlotte
         FLIGHT#0032,WN,1579,ATL,SFO,2025-01-01 08:48:00,2025-01-01 10:55:00,C47,B5,Atlanta,San Francisco
         FLIGHT#0033,OO,6396,BOI,SFO,2025-01-01 08:56:00,2025-01-01 09:43:00,E20,A6,Boise,San Francisco
         FLIGHT#0034,AA,2293,DFW,SFO,2025-01-01 08:57:00,2025-01-01 11:08:00,D41,C37,Dallas-Fort Worth,San Francisco
         FLIGHT#0035,DL,1106,SFO,MSP,2025-01-01 09:06:00,2025-01-01 14:56:00,E38,B30,San Francisco,Minneapolis
         FLIGHT#0036,DL,1631,SFO,ATL,2025-01-01 09:00:00,2025-01-01 16:26:00,B13,B45,San Francisco,Atlanta
         FLIGHT#0037,OO,5427,SFO,SMF,2025-01-01 09:06:00,2025-01-01 10:00:00,C34,C25,San Francisco,Sacramento
         FLIGHT#0038,CY,352,SFO,BOS,2025-01-01 09:25:00,2025-01-01 17:51:00,A46,E42,San Francisco,Boston
         FLIGHT#0039,UA,1239,LAX,SFO,2025-01-01 09:59:00,2025-01-01 11:19:00,A35,C2,Los Angeles,San Francisco
         FLIGHT#0040,UA,1285,SFO,IAH,2025-01-01 09:41:00,2025-01-01 15:20:00,A39,E10,San Francisco,Houston
         FLIGHT#0041,CY,753,SEA,SFO,2025-01-01 09:58:00,2025-01-01 11:53:00,C40,E35,Seattle,San Francisco
         FLIGHT#0042,CY,956,SFO,SAN,2025-01-01 09:57:00,2025-01-01 11:30:00,B10,E44,San Francisco,San Diego
         FLIGHT#0043,OO,5196,PDX,SFO,2025-01-01 09:53:00,2025-01-01 11:39:00,D13,C34,Portland,San Francisco
         FLIGHT#0044,WN,2346,SFO,LAX,2025-01-01 09:59:00,2025-01-01 11:17:00,C24,E45,San Francisco,Los Angeles
         FLIGHT#0045,OO,6400,EUG,SFO,2025-01-01 10:06:00,2025-01-01 11:27:00,E46,D20,Eugene,San Francisco
         FLIGHT#0046,CY,23,JFK,SFO,2025-01-01 10:21:00,2025-01-01 14:09:00,D2,B21,New York,San Francisco
         FLIGHT#0047,B6,534,SFO,BOS,2025-01-01 10:33:00,2025-01-01 18:55:00,A49,A5,San Francisco,Boston
         FLIGHT#0048,UA,1727,BOS,SFO,2025-01-01 10:34:00,2025-01-01 13:57:00,D43,A31,Boston,San Francisco
         FLIGHT#0049,WN,4391,LAS,SFO,2025-01-01 10:49:00,2025-01-01 12:17:00,A40,C49,Las Vegas,San Francisco
         FLIGHT#0050,OO,5335,CEC,SFO,2025-01-01 10:25:00,2025-01-01 12:04:00,C8,C6,Crescent City,San Francisco
         FLIGHT#0051,DL,1680,ATL,SFO,2025-01-01 10:43:00,2025-01-01 12:45:00,E49,E24,Atlanta,San Francisco
         FLIGHT#0052,OO,6283,SFO,MCI,2025-01-01 10:38:00,2025-01-01 17:01:00,C32,B12,San Francisco,Kansas City
         FLIGHT#0053,OO,5260,SFO,FAT,2025-01-01 10:37:00,2025-01-01 11:39:00,B46,B43,San Francisco,Fresno
         FLIGHT#0054,OO,6249,LAS,SFO,2025-01-01 10:48:00,2025-01-01 12:19:00,D11,A49,Las Vegas,San Francisco
         FLIGHT#0055,AA,23,SFO,DFW,2025-01-01 11:23:00,2025-01-01 17:00:00,B31,A11,San Francisco,Dallas-Fort Worth
         FLIGHT#0056,UA,753,SFO,AUS,2025-01-01 10:59:00,2025-01-01 16:44:00,B18,D6,San Francisco,Austin
         FLIGHT#0057,WN,4855,SFO,MKE,2025-01-01 11:08:00,2025-01-01 17:33:00,D3,D40,San Francisco,Milwaukee
         FLIGHT#0058,DL,1845,SLC,SFO,2025-01-01 11:29:00,2025-01-01 12:06:00,A22,D2,Salt Lake City,San Francisco
         FLIGHT#0059,UA,720,SFO,DEN,2025-01-01 12:46:00,2025-01-01 16:19:00,C41,E39,San Francisco,Denver
         FLIGHT#0060,UA,1257,IAH,SFO,2025-01-01 11:30:00,2025-01-01 13:19:00,A26,D2,Houston,San Francisco
         FLIGHT#0061,WN,2509,SFO,LAX,2025-01-01 11:34:00,2025-01-01 13:03:00,C42,D35,San Francisco,Los Angeles
         FLIGHT#0062,UA,73,EWR,SFO,2025-01-01 12:11:00,2025-01-01 15:24:00,C5,E10,Newark,San Francisco
         FLIGHT#0063,UA,364,PHX,SFO,2025-01-01 11:56:00,2025-01-01 13:11:00,A39,D26,Phoenix,San Francisco
         FLIGHT#0064,AA,221,DFW,SFO,2025-01-01 11:55:00,2025-01-01 13:30:00,A47,B22,Dallas-Fort Worth,San Francisco
         FLIGHT#0065,AA,2293,SFO,DFW,2025-01-01 12:04:00,2025-01-01 17:36:00,C43,E30,San Francisco,Dallas-Fort Worth
         FLIGHT#0066,OO,5199,SFO,SLC,2025-01-01 12:09:00,2025-01-01 14:58:00,A40,E42,San Francisco,Salt Lake City
         FLIGHT#0067,OO,6280,SLC,SFO,2025-01-01 12:13:00,2025-01-01 13:09:00,E16,E36,Salt Lake City,San Francisco
         FLIGHT#0068,OO,6317,RNO,SFO,2025-01-01 12:05:00,2025-01-01 13:09:00,C23,A31,Reno,San Francisco
         FLIGHT#0069,UA,864,SFO,EWR,2025-01-01 12:14:00,2025-01-01 20:38:00,C30,E37,San Francisco,Newark
         FLIGHT#0070,OO,5400,ONT,SFO,2025-01-01 12:25:00,2025-01-01 13:40:00,A48,E19,Ontario,San Francisco
         FLIGHT#0071,UA,236,HNL,SFO,2025-01-01 12:40:00,2025-01-01 19:36:00,A34,C12,Honolulu,San Francisco
         FLIGHT#0072,OO,6343,SNA,SFO,2025-01-01 12:37:00,2025-01-01 13:57:00,A15,D26,Santa Ana,San Francisco
         FLIGHT#0073,UA,1148,SFO,IAD,2025-01-01 13:10:00,2025-01-01 21:02:00,D24,A23,San Francisco,Washington
         FLIGHT#0074,DL,432,JFK,SFO,2025-01-01 13:00:00,2025-01-01 16:28:00,E3,A35,New York,San Francisco
         FLIGHT#0075,B6,1435,SFO,LGB,2025-01-01 13:33:00,2025-01-01 14:47:00,B24,C12,San Francisco,Long Beach
         FLIGHT#0076,OO,6408,SFO,EUG,2025-01-01 13:43:00,2025-01-01 15:10:00,B47,A35,San Francisco,Eugene
         FLIGHT#0077,UA,645,PDX,SFO,2025-01-01 13:27:00,2025-01-01 15:02:00,D7,E4,Portland,San Francisco
         FLIGHT#0078,WN,1812,SFO,SAN,2025-01-01 14:32:00,2025-01-01 15:51:00,B35,D48,San Francisco,San Diego
         FLIGHT#0079,OO,6409,SFO,PDX,2025-01-01 13:42:00,2025-01-01 15:27:00,C10,B17,San Francisco,Portland
         FLIGHT#0080,UA,358,AUS,SFO,2025-01-01 14:31:00,2025-01-01 15:48:00,E33,D21,Austin,San Francisco
         FLIGHT#0081,UA,1728,OGG,SFO,2025-01-01 14:02:00,2025-01-01 20:38:00,A30,C29,Kahului,San Francisco
         FLIGHT#0082,UA,816,SEA,SFO,2025-01-01 13:44:00,2025-01-01 15:38:00,A36,A9,Seattle,San Francisco
         FLIGHT#0083,UA,724,HNL,SFO,2025-01-01 13:59:00,2025-01-01 20:44:00,A14,C9,Honolulu,San Francisco
         FLIGHT#0084,UA,1733,SFO,DEN,2025-01-01 14:38:00,2025-01-01 18:35:00,B27,E32,San Francisco,Denver
         FLIGHT#0085,OO,5543,SFO,BOI,2025-01-01 14:27:00,2025-01-01 17:10:00,E10,B16,San Francisco,Boise
         FLIGHT#0086,UA,1761,IAH,SFO,2025-01-01 14:55:00,2025-01-01 16:45:00,B2,E20,Houston,San Francisco
         FLIGHT#0087,UA,277,DEN,SFO,2025-01-01 14:44:00,2025-01-01 16:04:00,B47,B13,Denver,San Francisco
         FLIGHT#0088,AA,1213,DFW,SFO,2025-01-01 15:14:00,2025-01-01 16:45:00,D11,C31,Dallas-Fort Worth,San Francisco
         FLIGHT#0089,US,407,PHX,SFO,2025-01-01 15:03:00,2025-01-01 16:00:00,C7,D19,Phoenix,San Francisco
         FLIGHT#0090,OO,5367,SFO,RDM,2025-01-01 14:52:00,2025-01-01 16:23:00,A5,E40,San Francisco,Redmond-Bend
         FLIGHT#0091,OO,5454,SMF,SFO,2025-01-01 15:46:00,2025-01-01 16:33:00,A20,A40,Sacramento,San Francisco
         FLIGHT#0092,WN,2687,SFO,LAX,2025-01-01 15:15:00,2025-01-01 16:35:00,D41,B37,San Francisco,Los Angeles
         FLIGHT#0093,CY,932,SFO,LAX,2025-01-01 15:31:00,2025-01-01 16:51:00,A19,E46,San Francisco,Los Angeles
         FLIGHT#0094,WN,3236,SFO,SAN,2025-01-01 15:56:00,2025-01-01 17:23:00,B29,B32,San Francisco,San Diego
         FLIGHT#0095,UA,404,IAH,SFO,2025-01-01 15:56:00,2025-01-01 17:52:00,B15,B42,Houston,San Francisco
         FLIGHT#0096,CY,933,LAX,SFO,2025-01-01 15:42:00,2025-01-01 16:51:00,E16,E7,Los Angeles,San Francisco
         FLIGHT#0097,US,596,SFO,PHX,2025-01-01 15:51:00,2025-01-01 18:52:00,B25,E38,San Francisco,Phoenix
         FLIGHT#0098,AA,379,SFO,DFW,2025-01-01 16:04:00,2025-01-01 21:55:00,A30,D49,San Francisco,Dallas-Fort Worth
         FLIGHT#0099,OO,6280,SFO,SNA,2025-01-01 16:52:00,2025-01-01 18:19:00,B5,C40,San Francisco,Santa Ana
         FLIGHT#0100,UA,735,DEN,SFO,2025-01-01 17:34:00,2025-01-01 19:09:00,C31,B15,Denver,San Francisco
         FLIGHT#0101,OO,5553,PDX,SFO,2025-01-01 16:00:00,2025-01-01 17:36:00,E9,D27,Portland,San Francisco
         FLIGHT#0102,UA,73,SFO,HNL,2025-01-01 16:13:00,2025-01-01 19:52:00,C37,B37,San Francisco,Honolulu
         FLIGHT#0103,UA,587,SEA,SFO,2025-01-01 16:25:00,2025-01-01 18:27:00,B7,B23,Seattle,San Francisco
         FLIGHT#0104,OO,5363,SFO,ONT,2025-01-01 16:09:00,2025-01-01 17:28:00,D21,E29,San Francisco,Ontario
         FLIGHT#0105,OO,6386,SFO,BOI,2025-01-01 16:12:00,2025-01-01 18:58:00,D48,E33,San Francisco,Boise
         FLIGHT#0106,CY,27,JFK,SFO,2025-01-01 16:28:00,2025-01-01 20:19:00,C6,E14,New York,San Francisco
         FLIGHT#0107,OO,5190,SFO,ASE,2025-01-01 16:24:00,2025-01-01 19:42:00,C50,B44,San Francisco,Aspen
         FLIGHT#0108,CY,746,SFO,SEA,2025-01-01 16:40:00,2025-01-01 18:32:00,D35,C24,San Francisco,Seattle
         FLIGHT#0109,UA,1640,SFO,ORD,2025-01-01 17:01:00,2025-01-01 23:02:00,E27,C24,San Francisco,Chicago
         FLIGHT#0110,OO,6221,MCI,SFO,2025-01-01 17:28:00,2025-01-01 19:08:00,E2,C36,Kansas City,San Francisco
         FLIGHT#0111,UA,486,SFO,LAS,2025-01-01 16:47:00,2025-01-01 18:16:00,C42,B47,San Francisco,Las Vegas
         FLIGHT#0112,CY,2,DCA,SFO,2025-01-01 17:01:00,2025-01-01 20:07:00,E43,A33,Washington,San Francisco
         FLIGHT#0113,B6,1436,LGB,SFO,2025-01-01 16:59:00,2025-01-01 18:35:00,B12,B22,Long Beach,San Francisco
         FLIGHT#0114,WN,694,PHX,SFO,2025-01-01 17:11:00,2025-01-01 18:05:00,B44,B18,Phoenix,San Francisco
         FLIGHT#0115,OO,5635,MMH,SFO,2025-01-01 17:00:00,2025-01-01 18:01:00,A25,D7,Mammoth Lakes,San Francisco
         FLIGHT#0116,AS,341,PSP,SFO,2025-01-01 18:25:00,2025-01-01 19:46:00,A11,E18,Palm Springs,San Francisco
         FLIGHT#0117,OO,6364,PSP,SFO,2025-01-01 18:01:00,2025-01-01 19:31:00,A14,B47,Palm Springs,San Francisco
         FLIGHT#0118,OO,5418,SBP,SFO,2025-01-01 17:17:00,2025-01-01 18:15:00,B24,D17,San Luis Obispo,San Francisco
         FLIGHT#0119,AA,197,SFO,ORD,2025-01-01 17:21:00,2025-01-01 23:33:00,D25,E49,San Francisco,Chicago
         FLIGHT#0120,CY,720,SFO,DAL,2025-01-01 18:25:00,2025-01-01 23:43:00,B24,A2,San Francisco,Dallas
         FLIGHT#0121,OO,6268,FAT,SFO,2025-01-01 17:33:00,2025-01-01 18:39:00,E35,D25,Fresno,San Francisco
         FLIGHT#0122,OO,5615,SFO,EUG,2025-01-01 17:45:00,2025-01-01 19:18:00,B11,A34,San Francisco,Eugene
         FLIGHT#0123,CY,960,SFO,SAN,2025-01-01 17:55:00,2025-01-01 19:23:00,D23,E44,San Francisco,San Diego
         FLIGHT#0124,AA,1393,DFW,SFO,2025-01-01 17:51:00,2025-01-01 19:25:00,E11,A41,Dallas-Fort Worth,San Francisco
         FLIGHT#0125,OO,6352,BOI,SFO,2025-01-01 17:58:00,2025-01-01 18:46:00,B31,D23,Boise,San Francisco
         FLIGHT#0126,DL,1151,SFO,HNL,2025-01-01 17:53:00,2025-01-01 21:34:00,E29,B45,San Francisco,Honolulu
         FLIGHT#0127,OO,5227,SFO,SAN,2025-01-01 19:07:00,2025-01-01 20:31:00,A35,B38,San Francisco,San Diego
         FLIGHT#0128,CY,941,LAX,SFO,2025-01-01 18:19:00,2025-01-01 19:34:00,C33,B44,Los Angeles,San Francisco
         FLIGHT#0129,UA,1044,EWR,SFO,2025-01-01 19:19:00,2025-01-01 22:53:00,D50,D26,Newark,San Francisco
         FLIGHT#0130,CY,211,ORD,SFO,2025-01-01 18:41:00,2025-01-01 21:14:00,D13,E45,Chicago,San Francisco
         FLIGHT#0131,UA,685,ORD,SFO,2025-01-01 18:51:00,2025-01-01 21:04:00,D26,D45,Chicago,San Francisco
         FLIGHT#0132,UA,370,SFO,SEA,2025-01-01 18:49:00,2025-01-01 20:41:00,B6,E20,San Francisco,Seattle
         FLIGHT#0133,UA,1433,IAH,SFO,2025-01-01 19:45:00,2025-01-01 21:39:00,C42,C48,Houston,San Francisco
         FLIGHT#0134,UA,1172,DEN,SFO,2025-01-01 20:19:00,2025-01-01 22:37:00,E31,D43,Denver,San Francisco
         FLIGHT#0135,CY,593,PSP,SFO,2025-01-01 19:09:00,2025-01-01 20:26:00,C23,C43,Palm Springs,San Francisco
         FLIGHT#0136,UA,1564,SFO,ORD,2025-01-01 19:14:00,2025-01-02 01:14:00,E3,C48,San Francisco,Chicago
         FLIGHT#0137,UA,741,ORD,SFO,2025-01-01 19:18:00,2025-01-01 21:58:00,A25,B38,Chicago,San Francisco
         FLIGHT#0138,WN,600,SFO,SNA,2025-01-01 19:36:00,2025-01-01 20:53:00,D21,D11,San Francisco,Santa Ana
         FLIGHT#0139,F9,664,SFO,DEN,2025-01-01 19:31:00,2025-01-01 23:13:00,E11,E12,San Francisco,Denver
         FLIGHT#0140,OO,4995,LAS,SFO,2025-01-01 19:18:00,2025-01-01 20:58:00,B42,B49,Las Vegas,San Francisco
         FLIGHT#0141,CY,717,DAL,SFO,2025-01-01 19:31:00,2025-01-01 21:02:00,A42,D32,Dallas,San Francisco
         FLIGHT#0142,UA,1243,SFO,DEN,2025-01-01 19:38:00,2025-01-01 23:15:00,B34,A3,San Francisco,Denver
         FLIGHT#0143,UA,560,IAD,SFO,2025-01-01 19:41:00,2025-01-01 22:29:00,D9,D33,Washington,San Francisco
         FLIGHT#0144,WN,2791,LAX,SFO,2025-01-01 19:45:00,2025-01-01 20:57:00,C49,C22,Los Angeles,San Francisco
         FLIGHT#0145,WN,2079,SAN,SFO,2025-01-01 21:03:00,2025-01-01 22:33:00,A25,E24,San Diego,San Francisco
         FLIGHT#0146,OO,6356,SFO,SLC,2025-01-01 19:57:00,2025-01-01 22:49:00,A28,C45,San Francisco,Salt Lake City
         FLIGHT#0147,OO,6290,PSP,SFO,2025-01-01 19:48:00,2025-01-01 21:12:00,A33,E27,Palm Springs,San Francisco
         FLIGHT#0148,OO,5363,ONT,SFO,2025-01-01 20:27:00,2025-01-01 21:54:00,A14,E17,Ontario,San Francisco
         FLIGHT#0149,OO,5206,SFO,PHX,2025-01-01 20:12:00,2025-01-01 23:05:00,D22,E31,San Francisco,Phoenix
         FLIGHT#0150,B6,1136,LGB,SFO,2025-01-01 20:41:00,2025-01-01 21:56:00,B7,E45,Long Beach,San Francisco
         FLIGHT#0151,US,736,PHX,SFO,2025-01-01 21:12:00,2025-01-01 22:11:00,B22,E33,Phoenix,San Francisco
         FLIGHT#0152,AA,1611,DFW,SFO,2025-01-01 21:42:00,2025-01-01 23:37:00,A13,B44,Dallas-Fort Worth,San Francisco
         FLIGHT#0153,UA,1241,SFO,EWR,2025-01-01 21:44:00,2025-01-02 05:55:00,D3,A17,San Francisco,Newark
         FLIGHT#0154,UA,1726,OGG,SFO,2025-01-01 22:19:00,2025-01-02 04:56:00,C35,B23,Kahului,San Francisco
         FLIGHT#0155,US,898,SFO,CLT,2025-01-01 22:29:00,2025-01-02 06:18:00,D7,D15,San Francisco,Charlotte
         FLIGHT#0156,UA,1669,SFO,PHL,2025-01-01 22:26:00,2025-01-02 06:30:00,B13,A12,San Francisco,Philadelphia
         FLIGHT#0157,UA,362,SFO,BWI,2025-01-01 22:31:00,2025-01-02 06:36:00,E32,A36,San Francisco,Baltimore
         FLIGHT#0158,OO,6220,SFO,RNO,2025-01-01 22:25:00,2025-01-01 23:23:00,D18,A31,San Francisco,Reno
         FLIGHT#0159,OO,6376,SFO,MRY,2025-01-01 22:35:00,2025-01-01 23:19:00,C24,E48,San Francisco,Monterey
         FLIGHT#0160,UA,522,SFO,PDX,2025-01-01 22:36:00,2025-01-02 00:31:00,B17,A40,San Francisco,Portland
         FLIGHT#0161,UA,1728,SFO,BOS,2025-01-01 22:46:00,2025-01-02 07:20:00,C40,E43,San Francisco,Boston
         FLIGHT#0162,UA,724,SFO,LAX,2025-01-01 22:45:00,2025-01-02 00:29:00,E43,B23,San Francisco,Los Angeles
         FLIGHT#0163,UA,1681,SFO,CLE,2025-01-01 23:03:00,2025-01-02 06:45:00,D26,E19,San Francisco,Cleveland
         FLIGHT#0164,UA,1580,OGG,SFO,2025-01-01 23:24:00,2025-01-02 06:07:00,E38,A35,Kahului,San Francisco
         FLIGHT#0165,DL,806,SFO,MSP,2025-01-02 00:22:00,2025-01-02 05:57:00,B27,A3,San Francisco,Minneapolis
         FLIGHT#0166,OO,5467,ONT,SFO,2025-01-02 05:02:00,2025-01-02 06:18:00,E8,C32,Ontario,San Francisco
         FLIGHT#0167,WN,1989,SFO,LAS,2025-01-02 05:35:00,2025-01-02 06:46:00,A21,D15,San Francisco,Las Vegas
         FLIGHT#0168,UA,1619,BOS,SFO,2025-01-02 05:56:00,2025-01-02 09:56:00,C46,E11,Boston,San Francisco
         FLIGHT#0169,UA,1076,SFO,ORD,2025-01-02 05:58:00,2025-01-02 12:00:00,E27,A31,San Francisco,Chicago
         FLIGHT#0170,F9,1056,SFO,IAH,2025-01-02 05:59:00,2025-01-02 12:09:00,A29,B13,San Francisco,Houston
         FLIGHT#0171,WN,2242,LAX,SFO,2025-01-02 06:22:00,2025-01-02 07:36:00,C12,D43,Los Angeles,San Francisco
         FLIGHT#0172,B6,735,SFO,LGB,2025-01-02 06:01:00,2025-01-02 07:20:00,C2,C37,San Francisco,Long Beach
         FLIGHT#0173,WN,3859,SFO,MDW,2025-01-02 06:27:00,2025-01-02 12:26:00,A28,E38,San Francisco,Chicago
         FLIGHT#0174,UA,1285,SFO,ORD,2025-01-02 06:43:00,2025-01-02 12:47:00,B43,A35,San Francisco,Chicago
         FLIGHT#0175,WN,1726,SFO,PHX,2025-01-02 06:32:00,2025-01-02 09:20:00,C16,B2,San Francisco,Phoenix
         FLIGHT#0176,OO,5186,SFO,SAN,2025-01-02 06:25:00,2025-01-02 07:59:00,C47,C1,San Francisco,San Diego
         FLIGHT#0177,UA,566,PIT,SFO,2025-01-02 07:15:00,2025-01-02 09:46:00,C39,E39,Pittsburgh,San Francisco
         FLIGHT#0178,UA,1195,MCO,SFO,2025-01-02 07:18:00,2025-01-02 10:05:00,A47,C43,Orlando,San Francisco
         FLIGHT#0179,CY,925,LAX,SFO,2025-01-02 06:57:00,2025-01-02 08:07:00,E29,C19,Los Angeles,San Francisco
         FLIGHT#0180,UA,761,ORD,SFO,2025-01-02 07:07:00,2025-01-02 09:34:00,B22,A3,Chicago,San Francisco
         FLIGHT#0181,UA,758,SFO,JFK,2025-01-02 07:07:00,2025-01-02 15:53:00,B15,B39,San Francisco,New York
         FLIGHT#0182,CY,67,IAD,SFO,2025-01-02 07:07:00,2025-01-02 10:00:00,D24,E33,Washington,San Francisco
         FLIGHT#0183,UA,706,SEA,SFO,2025-01-02 07:05:00,2025-01-02 08:59:00,D9,C28,Seattle,San Francisco
         FLIGHT#0184,OO,5441,SFO,SBP,2025-01-02 07:06:00,2025-01-02 08:11:00,B3,B29,San Francisco,San Luis Obispo
         FLIGHT#0185,CY,202,SFO,ORD,2025-01-02 07:18:00,2025-01-02 13:23:00,C16,D10,San Francisco,Chicago
         FLIGHT#0186,CY,710,SFO,DAL,2025-01-02 07:16:00,2025-01-02 12:43:00,D1,E13,San Francisco,Dallas
         FLIGHT#0187,AA,24,SFO,JFK,2025-01-02 07:06:00,2025-01-02 15:29:00,C38,D2,San Francisco,New York
         FLIGHT#0188,UA,72,HNL,SFO,2025-01-02 07:28:00,2025-01-02 14:20:00,C8,E18,Honolulu,San Francisco
         FLIGHT#0189,UA,1278,ATL,SFO,2025-01-02 07:30:00,2025-01-02 09:41:00,C16,B21,Atlanta,San Francisco
         FLIGHT#0190,UA,498,SFO,SAN,2025-01-02 07:20:00,2025-01-02 08:38:00,B42,E44,San Francisco,San Diego
         FLIGHT#0191,CY,183,EWR,SFO,2025-01-02 07:26:00,2025-01-02 10:51:00,B33,A12,Newark,San Francisco
         FLIGHT#0192,AA,76,SFO,LAX,2025-01-02 07:22:00,2025-01-02 08:44:00,E28,B18,San Francisco,Los Angeles
         FLIGHT#0193,WN,2325,DEN,SFO,2025-01-02 07:40:00,2025-01-02 09:03:00,A5,A17,Denver,San Francisco
         FLIGHT#0194,WN,1545,LAX,SFO,2025-01-02 07:48:00,2025-01-02 09:02:00,D42,A25,Los Angeles,San Francisco
         FLIGHT#0195,OO,5196,SFO,PDX,2025-01-02 07:46:00,2025-01-02 09:32:00,B12,B11,San Francisco,Portland
         FLIGHT#0196,UA,1053,DEN,SFO,2025-01-02 08:06:00,2025-01-02 09:41:00,C37,E7,Denver,San Francisco
         FLIGHT#0197,AA,23,DFW,SFO,2025-01-02 07:53:00,2025-01-02 09:26:00,D24,C34,Dallas-Fort Worth,San Francisco
         FLIGHT#0198,UA,322,SNA,SFO,2025-01-02 07:53:00,2025-01-02 09:17:00,E22,D32,Santa Ana,San Francisco
         FLIGHT#0199,UA,500,IND,SFO,2025-01-02 08:02:00,2025-01-02 09:46:00,D47,B25,Indianapolis,San Francisco
         FLIGHT#0200,UA,662,SAN,SFO,2025-01-02 08:51:00,2025-01-02 10:38:00,C36,B37,San Diego,San Francisco
         FLIGHT#0201,UA,834,LAS,SFO,2025-01-02 07:51:00,2025-01-02 09:17:00,B24,E14,Las Vegas,San Francisco
         FLIGHT#0202,CY,1930,SFO,LAX,2025-01-02 07:58:00,2025-01-02 09:29:00,D1,E49,San Francisco,Los Angeles
         FLIGHT#0203,UA,1454,ORD,SFO,2025-01-02 08:09:00,2025-01-02 10:54:00,C45,D18,Chicago,San Francisco
         FLIGHT#0204,AA,1368,SFO,DFW,2025-01-02 08:11:00,2025-01-02 13:35:00,A24,D28,San Francisco,Dallas-Fort Worth
         FLIGHT#0205,UA,460,LAX,SFO,2025-01-02 08:22:00,2025-01-02 09:53:00,E4,D14,Los Angeles,San Francisco
         FLIGHT#0206,UA,1547,SFO,BOS,2025-01-02 08:30:00,2025-01-02 16:52:00,B24,D37,San Francisco,Boston
         FLIGHT#0207,AA,242,SFO,ORD,2025-01-02 08:28:00,2025-01-02 14:41:00,D10,B31,San Francisco,Chicago
         FLIGHT#0208,OO,5538,MFR,SFO,2025-01-02 08:15:00,2025-01-02 09:44:00,D3,B43,Medford,San Francisco
         FLIGHT#0209,UA,1739,SFO,EWR,2025-01-02 08:56:00,2025-01-02 17:03:00,B18,A15,San Francisco,Newark
         FLIGHT#0210,DL,745,DTW,SFO,2025-01-02 08:36:00,2025-01-02 10:43:00,B2,D29,Detroit,San Francisco
         FLIGHT#0211,OO,5445,SFO,SBP,2025-01-02 10:35:00,2025-01-02 11:50:00,D39,A1,San Francisco,San Luis Obispo
         FLIGHT#0212,OO,5223,SLC,SFO,2025-01-02 08:52:00,2025-01-02 09:50:00,C17,C19,Salt Lake City,San Francisco
         FLIGHT#0213,UA,1615,SFO,IAD,2025-01-02 08:44:00,2025-01-02 16:41:00,A19,C46,San Francisco,Washington
         FLIGHT#0214,AA,1435,ORD,SFO,2025-01-02 08:43:00,2025-01-02 11:08:00,B49,B11,Chicago,San Francisco
         FLIGHT#0215,HA,11,SFO,HNL,2025-01-02 09:28:00,2025-01-02 13:38:00,E28,B21,San Francisco,Honolulu
         FLIGHT#0216,OO,6373,SFO,DFW,2025-01-02 08:51:00,2025-01-02 14:40:00,B42,D13,San Francisco,Dallas-Fort Worth
         FLIGHT#0217,UA,479,SFO,LAX,2025-01-02 11:15:00,2025-01-02 12:47:00,E32,B7,San Francisco,Los Angeles
         FLIGHT#0218,UA,361,SFO,LIH,2025-01-02 09:33:00,2025-01-02 13:10:00,A45,C26,San Francisco,Lihue
         FLIGHT#0219,WN,2074,SFO,SNA,2025-01-02 09:08:00,2025-01-02 10:18:00,A6,A49,San Francisco,Santa Ana
         FLIGHT#0220,CY,84,SFO,IAD,2025-01-02 09:20:00,2025-01-02 17:25:00,A37,B4,San Francisco,Washington
         FLIGHT#0221,WN,2969,SAN,SFO,2025-01-02 09:35:00,2025-01-02 10:59:00,B50,A43,San Diego,San Francisco
         FLIGHT#0222,UA,1249,SFO,MCO,2025-01-02 10:10:00,2025-01-02 18:15:00,D13,E20,San Francisco,Orlando
         FLIGHT#0223,WN,1820,SFO,LAS,2025-01-02 09:52:00,2025-01-02 11:19:00,B19,D16,San Francisco,Las Vegas
         FLIGHT#0224,WN,2414,SFO,PHX,2025-01-02 09:57:00,2025-01-02 12:52:00,E1,C5,San Francisco,Phoenix
         FLIGHT#0225,UA,698,SEA,SFO,2025-01-02 09:54:00,2025-01-02 11:59:00,E37,D34,Seattle,San Francisco
         FLIGHT#0226,AS,303,SFO,SEA,2025-01-02 10:06:00,2025-01-02 12:11:00,D36,C9,San Francisco,Seattle
         FLIGHT#0227,WN,3323,SFO,DEN,2025-01-02 10:40:00,2025-01-02 13:59:00,A4,E35,San Francisco,Denver
         FLIGHT#0228,OO,6286,SBA,SFO,2025-01-02 10:23:00,2025-01-02 11:47:00,B46,A8,Santa Barbara,San Francisco
         FLIGHT#0229,OO,5603,PHX,SFO,2025-01-02 10:29:00,2025-01-02 11:41:00,A2,C22,Phoenix,San Francisco
         FLIGHT#0230,CY,218,SFO,AUS,2025-01-02 10:28:00,2025-01-02 15:56:00,E49,C21,San Francisco,Austin
         FLIGHT#0231,OO,5335,CEC,SFO,2025-01-02 10:32:00,2025-01-02 12:09:00,D29,D17,Crescent City,San Francisco
         FLIGHT#0232,OO,5646,SFO,SBA,2025-01-02 10:33:00,2025-01-02 11:54:00,A50,E40,San Francisco,Santa Barbara
         FLIGHT#0233,OO,5635,SFO,SNA,2025-01-02 11:22:00,2025-01-02 12:55:00,C17,D47,San Francisco,Santa Ana
         FLIGHT#0234,OO,6380,SFO,BOI,2025-01-02 10:41:00,2025-01-02 13:18:00,B18,C15,San Francisco,Boise
         FLIGHT#0235,UA,662,SFO,MSP,2025-01-02 10:52:00,2025-01-02 16:39:00,B6,E11,San Francisco,Minneapolis
         FLIGHT#0236,OO,6270,SFO,RNO,2025-01-02 10:43:00,2025-01-02 11:52:00,C15,E10,San Francisco,Reno
         FLIGHT#0237,OO,4975,SFO,TUS,2025-01-02 12:23:00,2025-01-02 15:18:00,D5,C12,San Francisco,Tucson
         FLIGHT#0238,UA,322,SFO,SEA,2025-01-02 10:49:00,2025-01-02 12:54:00,E29,D3,San Francisco,Seattle
         FLIGHT#0239,WN,1009,LAX,SFO,2025-01-02 11:33:00,2025-01-02 12:45:00,E12,C30,Los Angeles,San Francisco
         FLIGHT#0240,OO,4966,SFO,SUN,2025-01-02 11:11:00,2025-01-02 14:15:00,D39,D21,San Francisco,Hailey
         FLIGHT#0241,UA,753,SFO,AUS,2025-01-02 11:40:00,2025-01-02 17:33:00,B30,D47,San Francisco,Austin
         FLIGHT#0242,UA,242,SFO,SAN,2025-01-02 12:00:00,2025-01-02 13:24:00,B27,E27,San Francisco,San Diego
         FLIGHT#0243,UA,390,SEA,SFO,2025-01-02 11:10:00,2025-01-02 13:08:00,A17,A23,Seattle,San Francisco
         FLIGHT#0244,OO,6336,RNO,SFO,2025-01-02 11:17:00,2025-01-02 12:17:00,A45,E39,Reno,San Francisco
         FLIGHT#0245,OO,5250,MRY,SFO,2025-01-02 11:12:00,2025-01-02 12:28:00,B33,E11,Monterey,San Francisco
         FLIGHT#0246,UA,317,SAN,SFO,2025-01-02 12:10:00,2025-01-02 13:40:00,A14,A42,San Diego,San Francisco
         FLIGHT#0247,OO,5652,SFO,PSP,2025-01-02 12:14:00,2025-01-02 13:50:00,E17,B17,San Francisco,Palm Springs
         FLIGHT#0248,UA,1195,SFO,ORD,2025-01-02 11:56:00,2025-01-02 18:12:00,B39,B19,San Francisco,Chicago
         FLIGHT#0249,CY,714,SFO,DAL,2025-01-02 11:40:00,2025-01-02 17:22:00,C50,A19,San Francisco,Dallas
         FLIGHT#0250,WN,2779,LAX,SFO,2025-01-02 11:58:00,2025-01-02 13:09:00,B19,C27,Los Angeles,San Francisco
         FLIGHT#0251,UA,1722,SFO,IAH,2025-01-02 11:58:00,2025-01-02 18:29:00,E12,D6,San Francisco,Houston
         FLIGHT#0252,UA,766,JFK,SFO,2025-01-02 11:55:00,2025-01-02 15:21:00,A16,C18,New York,San Francisco
         FLIGHT#0253,UA,1437,ORD,SFO,2025-01-02 12:36:00,2025-01-02 15:09:00,A33,E19,Chicago,San Francisco
         FLIGHT#0254,UA,1294,LAS,SFO,2025-01-02 12:20:00,2025-01-02 13:45:00,E7,A10,Las Vegas,San Francisco
         FLIGHT#0255,UA,1266,SEA,SFO,2025-01-02 12:13:00,2025-01-02 14:11:00,B32,C18,Seattle,San Francisco
         FLIGHT#0256,UA,1668,SFO,EWR,2025-01-02 12:24:00,2025-01-02 20:34:00,D37,A30,San Francisco,Newark
         FLIGHT#0257,OO,6304,BUR,SFO,2025-01-02 12:31:00,2025-01-02 14:01:00,C7,C4,Burbank,San Francisco
         FLIGHT#0258,WN,4391,SFO,STL,2025-01-02 12:55:00,2025-01-02 18:36:00,A12,D39,San Francisco,St. Louis
         FLIGHT#0259,UA,236,HNL,SFO,2025-01-02 13:19:00,2025-01-02 20:12:00,B25,D26,Honolulu,San Francisco
         FLIGHT#0260,UA,1705,SFO,IAH,2025-01-02 12:51:00,2025-01-02 18:50:00,E11,E32,San Francisco,Houston
         FLIGHT#0261,OO,6490,EUG,SFO,2025-01-02 13:00:00,2025-01-02 14:21:00,D34,D29,Eugene,San Francisco
         FLIGHT#0262,UA,820,SFO,ORD,2025-01-02 13:02:00,2025-01-02 19:11:00,B45,E24,San Francisco,Chicago
         FLIGHT#0263,AS,381,SFO,PDX,2025-01-02 12:52:00,2025-01-02 14:34:00,E11,B3,San Francisco,Portland
         FLIGHT#0264,AS,305,SFO,SEA,2025-01-02 12:59:00,2025-01-02 15:10:00,C34,C41,San Francisco,Seattle
         FLIGHT#0265,OO,6273,SFO,SLC,2025-01-02 12:57:00,2025-01-02 15:50:00,C3,D36,San Francisco,Salt Lake City
         FLIGHT#0266,DL,2254,SFO,DTW,2025-01-02 13:05:00,2025-01-02 20:29:00,E10,D30,San Francisco,Detroit
         FLIGHT#0267,B6,1435,SFO,LGB,2025-01-02 13:34:00,2025-01-02 15:02:00,B31,D48,San Francisco,Long Beach
         FLIGHT#0268,F9,661,DEN,SFO,2025-01-02 13:11:00,2025-01-02 14:35:00,C3,E38,Denver,San Francisco
         FLIGHT#0269,UA,1092,EWR,SFO,2025-01-02 13:44:00,2025-01-02 17:05:00,D13,A41,Newark,San Francisco
         FLIGHT#0270,US,1812,SFO,CLT,2025-01-02 13:32:00,2025-01-02 21:36:00,A50,A5,San Francisco,Charlotte
         FLIGHT#0271,WN,2598,LAX,SFO,2025-01-02 13:48:00,2025-01-02 14:54:00,E23,C38,Los Angeles,San Francisco
         FLIGHT#0272,UA,216,SFO,SNA,2025-01-02 15:23:00,2025-01-02 16:41:00,C23,E6,San Francisco,Santa Ana
         FLIGHT#0273,UA,1060,SFO,DCA,2025-01-02 15:19:00,2025-01-02 23:18:00,D14,B18,San Francisco,Washington
         FLIGHT#0274,OO,6326,BOI,SFO,2025-01-02 13:51:00,2025-01-02 14:24:00,D49,A43,Boise,San Francisco
         FLIGHT#0275,UA,724,HNL,SFO,2025-01-02 14:43:00,2025-01-02 21:33:00,B26,A50,Honolulu,San Francisco
         FLIGHT#0276,OO,5463,SFO,SMF,2025-01-02 13:50:00,2025-01-02 14:32:00,A13,D23,San Francisco,Sacramento
         FLIGHT#0277,UA,698,SFO,MCO,2025-01-02 14:24:00,2025-01-02 22:33:00,D49,B2,San Francisco,Orlando
         FLIGHT#0278,CY,1178,SFO,EWR,2025-01-02 13:58:00,2025-01-02 22:06:00,C27,D9,San Francisco,Newark
         FLIGHT#0279,OO,6425,TUS,SFO,2025-01-02 14:50:00,2025-01-02 15:54:00,E29,D17,Tucson,San Francisco
         FLIGHT#0280,OO,5615,MFR,SFO,2025-01-02 13:55:00,2025-01-02 15:15:00,B44,E27,Medford,San Francisco
         FLIGHT#0281,WN,3450,SFO,MDW,2025-01-02 14:50:00,2025-01-02 20:46:00,D39,B44,San Francisco,Chicago
         FLIGHT#0282,UA,1733,SFO,DEN,2025-01-02 15:11:00,2025-01-02 18:47:00,D8,D2,San Francisco,Denver
         FLIGHT#0283,UA,1263,KOA,SFO,2025-01-02 14:59:00,2025-01-02 21:49:00,C39,E3,Kona,San Francisco
         FLIGHT#0284,UA,1568,SFO,RDU,2025-01-02 14:55:00,2025-01-02 23:03:00,A30,A26,San Francisco,Raleigh-durham
         FLIGHT#0285,UA,1159,SFO,BOS,2025-01-02 14:57:00,2025-01-02 23:23:00,C19,A30,San Francisco,Boston
         FLIGHT#0286,OO,5652,PSP,SFO,2025-01-02 14:52:00,2025-01-02 16:46:00,D37,A5,Palm Springs,San Francisco
         FLIGHT#0287,US,749,CLT,SFO,2025-01-02 15:28:00,2025-01-02 17:47:00,D17,D38,Charlotte,San Francisco
         FLIGHT#0288,UA,1491,SFO,DEN,2025-01-02 15:09:00,2025-01-02 18:45:00,E31,E36,San Francisco,Denver
         FLIGHT#0289,WN,2687,SFO,LAX,2025-01-02 15:27:00,2025-01-02 16:31:00,E42,B13,San Francisco,Los Angeles
         FLIGHT#0290,DL,2040,SFO,JFK,2025-01-02 15:09:00,2025-01-02 23:20:00,E2,D33,San Francisco,New York
         FLIGHT#0291,OO,5549,SFO,AUS,2025-01-02 15:24:00,2025-01-02 21:11:00,B42,C1,San Francisco,Austin
         FLIGHT#0292,AS,308,SEA,SFO,2025-01-02 15:22:00,2025-01-02 17:18:00,C39,A46,Seattle,San Francisco
         FLIGHT#0293,F9,662,SFO,DEN,2025-01-02 15:16:00,2025-01-02 18:50:00,C5,A8,San Francisco,Denver
         FLIGHT#0294,UA,735,DEN,SFO,2025-01-02 16:00:00,2025-01-02 17:19:00,A32,C24,Denver,San Francisco
         FLIGHT#0295,UA,404,IAH,SFO,2025-01-02 17:26:00,2025-01-02 19:32:00,C14,A7,Houston,San Francisco
         FLIGHT#0296,CY,210,SFO,ORD,2025-01-02 15:42:00,2025-01-02 21:44:00,A31,B46,San Francisco,Chicago
         FLIGHT#0297,AS,315,SFO,SEA,2025-01-02 19:47:00,2025-01-02 22:16:00,A8,B49,San Francisco,Seattle
         FLIGHT#0298,WN,1901,SAN,SFO,2025-01-02 15:48:00,2025-01-02 17:09:00,A23,B38,San Diego,San Francisco
         FLIGHT#0299,OO,5580,SFO,SNA,2025-01-02 16:35:00,2025-01-02 18:03:00,D40,E43,San Francisco,Santa Ana
         FLIGHT#0300,AA,2265,DFW,SFO,2025-01-02 16:07:00,2025-01-02 17:41:00,A4,A23,Dallas-Fort Worth,San Francisco
         FLIGHT#0301,OO,5363,SFO,ONT,2025-01-02 16:15:00,2025-01-02 17:32:00,A10,A26,San Francisco,Ontario
         FLIGHT#0302,OO,5609,SFO,PDX,2025-01-02 17:01:00,2025-01-02 18:42:00,E49,D4,San Francisco,Portland
         FLIGHT#0303,OO,5645,MFR,SFO,2025-01-02 16:15:00,2025-01-02 17:35:00,A25,E49,Medford,San Francisco
         FLIGHT#0304,OO,4976,SFO,STL,2025-01-02 16:37:00,2025-01-02 22:27:00,C35,A2,San Francisco,St. Louis
         FLIGHT#0305,OO,6217,BUR,SFO,2025-01-02 16:44:00,2025-01-02 17:55:00,D50,A14,Burbank,San Francisco
         FLIGHT#0306,WN,1276,SFO,LAX,2025-01-02 16:25:00,2025-01-02 17:32:00,B8,D22,San Francisco,Los Angeles
         FLIGHT#0307,OO,6238,ACV,SFO,2025-01-02 16:25:00,2025-01-02 17:36:00,E24,A39,Arcata CA,San Francisco
         FLIGHT#0308,OO,5190,SFO,ASE,2025-01-02 17:08:00,2025-01-02 20:17:00,C9,E6,San Francisco,Aspen
         FLIGHT#0309,OO,4627,SFO,SLC,2025-01-02 16:43:00,2025-01-02 19:41:00,C32,C4,San Francisco,Salt Lake City
         FLIGHT#0310,OO,6476,SFO,MFR,2025-01-02 16:38:00,2025-01-02 18:16:00,B26,D33,San Francisco,Medford
         FLIGHT#0311,UA,486,SFO,LAS,2025-01-02 16:52:00,2025-01-02 18:24:00,D25,E8,San Francisco,Las Vegas
         FLIGHT#0312,DL,214,SFO,DTW,2025-01-02 19:09:00,2025-01-03 02:20:00,C6,E35,San Francisco,Detroit
         FLIGHT#0313,CY,592,SFO,PSP,2025-01-02 16:54:00,2025-01-02 18:14:00,B40,B9,San Francisco,Palm Springs
         FLIGHT#0314,UA,529,SNA,SFO,2025-01-02 17:01:00,2025-01-02 18:15:00,D28,B30,Santa Ana,San Francisco
         FLIGHT#0315,UA,372,MSP,SFO,2025-01-02 17:39:00,2025-01-02 19:19:00,E28,C18,Minneapolis,San Francisco
         FLIGHT#0316,AA,1213,SFO,DFW,2025-01-02 18:20:00,2025-01-03 00:19:00,E39,A42,San Francisco,Dallas-Fort Worth
         FLIGHT#0317,AS,341,PSP,SFO,2025-01-02 17:15:00,2025-01-02 18:37:00,D40,D15,Palm Springs,San Francisco
         FLIGHT#0318,OO,5418,SBP,SFO,2025-01-02 18:11:00,2025-01-02 19:09:00,C31,D39,San Luis Obispo,San Francisco
         FLIGHT#0319,CY,193,EWR,SFO,2025-01-02 17:29:00,2025-01-02 20:59:00,E20,E40,Newark,San Francisco
         FLIGHT#0320,UA,1723,SFO,KOA,2025-01-02 17:26:00,2025-01-02 21:02:00,E18,D41,San Francisco,Kona
         FLIGHT#0321,UA,1762,SFO,IAH,2025-01-02 17:37:00,2025-01-02 23:11:00,C40,C37,San Francisco,Houston
         FLIGHT#0322,CY,720,SFO,DAL,2025-01-02 17:23:00,2025-01-02 22:47:00,D13,D23,San Francisco,Dallas
         FLIGHT#0323,CY,963,SAN,SFO,2025-01-02 17:36:00,2025-01-02 19:05:00,B1,E32,San Diego,San Francisco
         FLIGHT#0324,OO,5255,SFO,EUG,2025-01-02 17:27:00,2025-01-02 19:02:00,C7,B2,San Francisco,Eugene
         FLIGHT#0325,CY,960,SFO,SAN,2025-01-02 17:32:00,2025-01-02 18:50:00,C3,C4,San Francisco,San Diego
         FLIGHT#0326,UA,1419,MSY,SFO,2025-01-02 17:46:00,2025-01-02 20:07:00,C26,E49,New Orleans,San Francisco
         FLIGHT#0327,WN,1585,SFO,LAX,2025-01-02 17:46:00,2025-01-02 19:31:00,A12,A12,San Francisco,Los Angeles
         FLIGHT#0328,DL,1505,MSP,SFO,2025-01-02 17:47:00,2025-01-02 19:48:00,A33,B37,Minneapolis,San Francisco
         FLIGHT#0329,US,686,PHX,SFO,2025-01-02 17:59:00,2025-01-02 19:05:00,C28,C11,Phoenix,San Francisco
         FLIGHT#0330,AS,302,SEA,SFO,2025-01-02 18:00:00,2025-01-02 20:04:00,B28,E17,Seattle,San Francisco
         FLIGHT#0331,UA,1552,RDU,SFO,2025-01-02 18:08:00,2025-01-02 20:51:00,B15,D48,Raleigh-durham,San Francisco
         FLIGHT#0332,UA,697,LAS,SFO,2025-01-02 17:55:00,2025-01-02 19:14:00,E37,B31,Las Vegas,San Francisco
         FLIGHT#0333,AA,219,LAX,SFO,2025-01-02 17:54:00,2025-01-02 19:05:00,C27,E34,Los Angeles,San Francisco
         FLIGHT#0334,OO,5425,ONT,SFO,2025-01-02 18:04:00,2025-01-02 19:23:00,C46,A14,Ontario,San Francisco
         FLIGHT#0335,WN,1861,SFO,PHX,2025-01-02 20:49:00,2025-01-02 23:31:00,C31,B42,San Francisco,Phoenix
         FLIGHT#0336,OO,5631,SFO,BUR,2025-01-02 18:10:00,2025-01-02 19:29:00,D26,E29,San Francisco,Burbank
         FLIGHT#0337,UA,720,SFO,AUS,2025-01-02 18:13:00,2025-01-02 23:41:00,E10,D1,San Francisco,Austin
         FLIGHT#0338,UA,1581,SFO,OGG,2025-01-02 18:15:00,2025-01-02 22:06:00,B40,E18,San Francisco,Kahului
         FLIGHT#0339,OO,5227,SFO,SAN,2025-01-02 18:26:00,2025-01-02 19:59:00,E33,E50,San Francisco,San Diego
         FLIGHT#0340,CY,941,LAX,SFO,2025-01-02 18:24:00,2025-01-02 19:39:00,D4,A22,Los Angeles,San Francisco
         FLIGHT#0341,AA,1459,ORD,SFO,2025-01-02 18:21:00,2025-01-02 21:11:00,D42,B25,Chicago,San Francisco
         FLIGHT#0342,OO,5442,SFO,RDD,2025-01-02 18:19:00,2025-01-02 19:35:00,E21,B9,San Francisco,Redding
         FLIGHT#0343,AA,69,MIA,SFO,2025-01-02 18:31:00,2025-01-02 21:33:00,B11,B15,Miami,San Francisco
         FLIGHT#0344,OO,6220,DFW,SFO,2025-01-02 19:01:00,2025-01-02 20:40:00,D35,E4,Dallas-Fort Worth,San Francisco
         FLIGHT#0345,UA,1670,SFO,HNL,2025-01-02 18:42:00,2025-01-02 22:52:00,A15,C18,San Francisco,Honolulu
         FLIGHT#0346,DL,435,JFK,SFO,2025-01-02 18:57:00,2025-01-02 22:25:00,D35,C33,New York,San Francisco
         FLIGHT#0347,UA,508,SEA,SFO,2025-01-02 19:01:00,2025-01-02 21:05:00,C16,B8,Seattle,San Francisco
         FLIGHT#0348,UA,1523,BOS,SFO,2025-01-02 21:19:00,2025-01-03 01:19:00,E7,B32,Boston,San Francisco
         FLIGHT#0349,CY,593,PSP,SFO,2025-01-02 19:03:00,2025-01-02 20:21:00,C13,A47,Palm Springs,San Francisco
         FLIGHT#0350,UA,741,ORD,SFO,2025-01-02 19:44:00,2025-01-02 22:14:00,A16,C32,Chicago,San Francisco
         FLIGHT#0351,WN,3414,SFO,SAN,2025-01-02 19:43:00,2025-01-02 21:10:00,E3,D46,San Francisco,San Diego
         FLIGHT#0352,UA,404,SFO,PDX,2025-01-02 19:42:00,2025-01-02 21:24:00,B48,A30,San Francisco,Portland
         FLIGHT#0353,UA,637,SFO,SNA,2025-01-02 19:32:00,2025-01-02 20:49:00,D40,A23,San Francisco,Santa Ana
         FLIGHT#0354,OO,5573,SAT,SFO,2025-01-02 21:13:00,2025-01-02 22:57:00,D34,E33,San Antonio,San Francisco
         FLIGHT#0355,AA,219,SFO,LAX,2025-01-02 20:03:00,2025-01-02 22:00:00,E27,D38,San Francisco,Los Angeles
         FLIGHT#0356,OO,5600,BUR,SFO,2025-01-02 19:55:00,2025-01-02 21:21:00,A7,A27,Burbank,San Francisco
         FLIGHT#0357,CY,947,LAX,SFO,2025-01-02 20:38:00,2025-01-02 22:06:00,D28,C15,Los Angeles,San Francisco
         FLIGHT#0358,WN,138,SFO,LAS,2025-01-02 20:26:00,2025-01-02 21:49:00,B35,E31,San Francisco,Las Vegas
         FLIGHT#0359,OO,5302,SFO,PSC,2025-01-02 20:29:00,2025-01-02 22:28:00,C9,A15,San Francisco,Pasco
         FLIGHT#0360,CY,748,SFO,SEA,2025-01-02 20:46:00,2025-01-02 23:17:00,D7,E25,San Francisco,Seattle
         FLIGHT#0361,UA,236,SFO,EWR,2025-01-02 20:41:00,2025-01-03 05:04:00,D12,B47,San Francisco,Newark
         FLIGHT#0362,OO,6503,SFO,EUG,2025-01-02 20:54:00,2025-01-02 22:27:00,A50,E49,San Francisco,Eugene
         FLIGHT#0363,WN,1174,LAS,SFO,2025-01-02 20:58:00,2025-01-02 22:19:00,C42,D33,Las Vegas,San Francisco
         FLIGHT#0364,AS,744,SFO,SLC,2025-01-02 20:52:00,2025-01-02 23:33:00,B11,A39,San Francisco,Salt Lake City
         FLIGHT#0365,WN,4992,SFO,PHX,2025-01-02 21:49:00,2025-01-03 00:32:00,D19,E15,San Francisco,Phoenix
         FLIGHT#0366,UA,469,EWR,SFO,2025-01-02 23:07:00,2025-01-03 02:27:00,E3,D19,Newark,San Francisco
         FLIGHT#0367,UA,1163,SFO,EWR,2025-01-02 21:44:00,2025-01-03 05:45:00,D19,C17,San Francisco,Newark
         FLIGHT#0368,DL,2337,SFO,ATL,2025-01-02 21:44:00,2025-01-03 05:23:00,B4,A39,San Francisco,Atlanta
         FLIGHT#0369,OO,6432,SFO,EUG,2025-01-02 22:24:00,2025-01-02 23:57:00,E11,A4,San Francisco,Eugene
         FLIGHT#0370,US,898,SFO,CLT,2025-01-02 22:24:00,2025-01-03 06:16:00,A45,A24,San Francisco,Charlotte
         FLIGHT#0371,UA,292,SFO,MCO,2025-01-02 22:30:00,2025-01-03 06:37:00,C7,C5,San Francisco,Orlando
         FLIGHT#0372,OO,5600,SFO,MFR,2025-01-02 22:36:00,2025-01-03 00:01:00,E42,E38,San Francisco,Medford
         FLIGHT#0373,UA,263,LAX,SFO,2025-01-02 22:48:00,2025-01-03 00:04:00,B22,E27,Los Angeles,San Francisco
         FLIGHT#0374,OO,5414,SFO,RDM,2025-01-02 22:32:00,2025-01-03 00:12:00,A46,C18,San Francisco,Redmond-Bend
         FLIGHT#0375,UA,1241,SFO,EWR,2025-01-02 23:22:00,2025-01-03 07:44:00,A28,E27,San Francisco,Newark
         FLIGHT#0376,UA,522,SFO,PDX,2025-01-02 22:55:00,2025-01-03 00:42:00,A10,E39,San Francisco,Portland
         FLIGHT#0377,UA,724,SFO,ORD,2025-01-02 23:05:00,2025-01-03 05:20:00,B40,D23,San Francisco,Chicago
         FLIGHT#0378,UA,156,SFO,MSY,2025-01-02 23:22:00,2025-01-03 05:24:00,C40,A9,San Francisco,New Orleans
         FLIGHT#0379,CY,358,SFO,BOS,2025-01-02 22:52:00,2025-01-03 07:31:00,B23,A44,San Francisco,Boston
         FLIGHT#0380,DL,1370,SFO,JFK,2025-01-02 23:04:00,2025-01-03 07:36:00,E10,A49,San Francisco,New York
         FLIGHT#0381,UA,1729,SFO,IAD,2025-01-02 23:10:00,2025-01-03 07:35:00,D32,E42,San Francisco,Washington
         FLIGHT#0382,CY,34,SFO,JFK,2025-01-02 23:15:00,2025-01-03 07:54:00,D28,E25,San Francisco,New York
         FLIGHT#0383,DL,1880,SFO,ATL,2025-01-02 00:53:00,2025-01-02 08:27:00,E2,A29,San Francisco,Atlanta
         FLIGHT#0384,UA,1523,SFO,EWR,2025-01-02 23:39:00,2025-01-03 07:43:00,B9,D15,San Francisco,Newark
         FLIGHT#0385,US,426,PHX,SFO,2025-01-02 00:18:00,2025-01-02 01:16:00,D47,C42,Phoenix,San Francisco

  4. Import the data from the `flights.csv` file into the `flights` table:
         
         cbt import flights flights.csv

  5. In Bigtable Studio, run the following queries to verify that the tables are populated:

     * SELECT * FROM airports LIMIT 10;

     * SELECT * FROM flights LIMIT 10;




## Create a context set in Bigtable Studio

In this section, create a context set named `flights-assistant`. This context set doesn't include any context set file uploaded to it.

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **View actions ( more_vert)**.

  5. Click **Create context set**.

  6. In **Context set name** , enter `flights-assistant`.

  7. Click **Create**.




## Test QueryData in Studio

In this section, use the `flights-assistant` context set by asking natural language questions to generate a SQL query. Since the context set doesn't have any context set file uploaded to it and Bigtable schemas only expose column family names (`info`) rather than individual column qualifiers, QueryData guesses column qualifiers and generates sub-optimal queries. 

  1. In the **Explorer pane** , next to your context set, click **View actions ( more_vert)**.
  2. Click **Test context set**.
  3. In the query editor, click **Generate SQL using QueryData with: flights-assistant**.
  4. Enter the following natural language question to generate a SQL query, and click **Generate**.
         
         Find flights from SFO to JFK.
         

Review the SQL query. Without a context set, QueryData sees the info column family (`MAP<BYTES, BYTES>`) on the flights table, but not the column qualifiers `departure_airport` and `arrival_airport`, so it guesses qualifier names such as `origin` and `destination`: 
         
         SELECT
             _key,
             info
           FROM
             flights
           WHERE
             CAST(info['origin'] AS STRING) = 'SFO'
             AND CAST(info['destination'] AS STRING) = 'JFK';
         

  5. In the **Generate SQL using QueryData with: flights-assistant** window, click **Edit**.

  6. Enter the following natural language question to generate a SQL query, and click **Update**.
         
         Tell me flights that can help me beat nighttime traffic if traveling from New York
         

The database fails to understand the term `nighttime traffic` and guesses column qualifiers that don't exist in the `flights` table as the following query shows. 

**Note:** GenAI models are nondeterministic, meaning the same prompt may yield different responses across separate calls due to the probabilistic nature of the output generation.
         
         -- Assuming 'nighttime traffic' refers to flights departing during the night,
         -- defined here as between 8:00 PM (20:00) and 5:00 AM (05:00).
         SELECT
           CAST(_key AS STRING) AS flight_id,
           CAST(info['flight_number'] AS STRING) AS flight_number,
           CAST(info['origin'] AS STRING) AS origin,
           CAST(info['destination'] AS STRING) AS destination,
           CAST(info['departure_time'] AS STRING) AS departure_time
         FROM
           flights
         WHERE
           CAST(info['origin'] AS STRING) = 'New York'
           AND (
             EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) >= 20
             OR EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) < 5
           );
         

  7. In the **Generate SQL using QueryData with: flights-assistant** window, click **Edit**.

  8. Enter the following natural language question to generate a SQL query, and click **Update**.
         
         Show me flights to Raleigh-Durham
         

Without value search context, QueryData guesses a column qualifier and filters on `Raleigh-Durham`. Because the `flights` table stores the city as `Raleigh-durham` under `info['arrival_city']`, the query won't return any rows.

**Note:** GenAI models are nondeterministic, meaning the same prompt may yield different responses across separate calls due to the probabilistic nature of the output generation.
         
         SELECT
           _key,
           info
         FROM
           flights
         WHERE
           CAST(info['destination_city'] AS STRING) = 'Raleigh-Durham';
         




## Generate context for the context set

In this section, you prepare the environment and create a context file that helps improve the context set's querying capabilities.

### Set up your environment

Before you can start generating context, you must prepare your environment.

To set up your environment, perform the following steps:

  1. Install Antigravity CLI. For more information, see [Get Started with Antigravity CLI](https://antigravity.google/docs/cli/getting-started/).
  2. [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  3. [Set up Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). Run the following commands in your terminal to authenticate and select your project:
         
         gcloud auth application-default login

  4. [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), a Python package and project manager that is a prerequisite for the context engineering agent. If you don't already have Python on your system, `uv` can install it for you.

  5. [Install the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/build-context-sets#install-agent):
         
         agy plugin install https://github.com/GoogleCloudPlatform/db-context-enrichment/tree/main/plugin

  6. In your terminal, start the Antigravity CLI.
         
         agy

  7. Set up a database connection for context generation using [MCP Toolbox](https://mcp-toolbox.dev/documentation/introduction/). The connection is defined in the `tools.yaml` configuration file.

To create the `tools.yaml` configuration file in your current directory, enter a prompt such as: 
         
         Help me set up a database connection.
         

Follow the instructions provided by the skill. For more information about the `tools.yaml` file, see [MCP Toolbox documentation](https://mcp-toolbox.dev/documentation/configuration/).

**Note:** If this connection is not established, the extension returns error messages, such as `Error Discovering tools from mcp_toolbox`, and context generation fails to work.
  8. To reload the configuration after the `tools.yaml` file is created, run the following command in the Antigravity CLI and follow the instruction to reload the toolbox MCP server:
         
         /mcp

     1. Select `db-context-engineering_toolbox`.

     2. Select `Restart`.

  9. Verify that the MCP toolbox and the context engineering agent plugin are connected and ready to use.
         
         /mcp




### Generate template context

In this section, to address the issue from the previous section where QueryData didn't know the `flights` column qualifiers or the term `nighttime traffic`, define templates in the context set file that map natural language questions to the info column family qualifiers and define `nighttime traffic` as traffic occurring between 5:00 PM and 7:00 PM. 

To generate template context, perform the following steps:

  1. Enter the following prompt into the Antigravity CLI:
         
         Generate templates for the following two questions and SQL queries:
         
         1. Question: "Show me flights from SFO to JFK"
         SQL:
         SELECT
           CAST(_key AS STRING) AS flight_id,
           CAST(info['airline'] AS STRING) AS airline,
           CAST(info['flight_number'] AS STRING) AS flight_number,
           CAST(info['departure_airport'] AS STRING) AS departure_airport,
           CAST(info['arrival_airport'] AS STRING) AS arrival_airport,
           CAST(info['departure_time'] AS STRING) AS departure_time,
           CAST(info['arrival_time'] AS STRING) AS arrival_time,
           CAST(info['departure_gate'] AS STRING) AS departure_gate,
           CAST(info['arrival_gate'] AS STRING) AS arrival_gate,
           CAST(info['departure_city'] AS STRING) AS departure_city,
           CAST(info['arrival_city'] AS STRING) AS arrival_city
         FROM
           flights
         WHERE
           CAST(info['departure_airport'] AS STRING) = 'SFO'
           AND CAST(info['arrival_airport'] AS STRING) = 'JFK'
         ORDER BY
           departure_time;
         
         2. Question: "Tell me flights that can help me beat nighttime traffic if traveling from New York"
         SQL:
         SELECT
           CAST(info['airline'] AS STRING) AS airline,
           CAST(info['flight_number'] AS STRING) AS flight_number,
           CAST(info['departure_airport'] AS STRING) AS departure_airport,
           CAST(info['departure_time'] AS STRING) AS departure_time
         FROM
           flights
         WHERE
           CAST(info['departure_city'] AS STRING) = 'New York'
           AND (
             EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) < 17
             OR EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) >= 19
           )
         ORDER BY
           departure_time;
         

  2. The agent converts your input into a specific format that refines the context set's performance across a wide range of user queries. For more information, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/context-sets-overview#context-sets).

  3. Review the generated query template. You can either save the query template as a new agent context file or append it to an existing agent context file.

  4. Prompt the agent to save the template:
         
         Save it to context_set.json.
         

The agent creates the file in the same directory, with the following content:
         
         {
           "templates": [
             {
               "nl_query": "Show me flights from SFO to JFK",
               "sql": "SELECT CAST(_key AS STRING) AS flight_id, CAST(info['airline'] AS STRING) AS airline, CAST(info['flight_number'] AS STRING) AS flight_number, CAST(info['departure_airport'] AS STRING) AS departure_airport, CAST(info['arrival_airport'] AS STRING) AS arrival_airport, CAST(info['departure_time'] AS STRING) AS departure_time, CAST(info['arrival_time'] AS STRING) AS arrival_time, CAST(info['departure_gate'] AS STRING) AS departure_gate, CAST(info['arrival_gate'] AS STRING) AS arrival_gate, CAST(info['departure_city'] AS STRING) AS departure_city, CAST(info['arrival_city'] AS STRING) AS arrival_city FROM flights WHERE CAST(info['departure_airport'] AS STRING) = 'SFO' AND CAST(info['arrival_airport'] AS STRING) = 'JFK' ORDER BY departure_time",
               "intent": "Find flights from SFO to JFK.",
               "manifest": "Find flights from a given departure airport code to a given arrival airport code.",
               "parameterized": {
                 "parameterized_sql": "SELECT CAST(_key AS STRING) AS flight_id, CAST(info['airline'] AS STRING) AS airline, CAST(info['flight_number'] AS STRING) AS flight_number, CAST(info['departure_airport'] AS STRING) AS departure_airport, CAST(info['arrival_airport'] AS STRING) AS arrival_airport, CAST(info['departure_time'] AS STRING) AS departure_time, CAST(info['arrival_time'] AS STRING) AS arrival_time, CAST(info['departure_gate'] AS STRING) AS departure_gate, CAST(info['arrival_gate'] AS STRING) AS arrival_gate, CAST(info['departure_city'] AS STRING) AS departure_city, CAST(info['arrival_city'] AS STRING) AS arrival_city FROM flights WHERE CAST(info['departure_airport'] AS STRING) = ? AND CAST(info['arrival_airport'] AS STRING) = ? ORDER BY departure_time",
                 "parameterized_intent": "Find flights from ? to ?."
               }
             },
             {
               "nl_query": "Tell me flights that can help me beat nighttime traffic if traveling from New York",
               "sql": "SELECT CAST(info['airline'] AS STRING) AS airline, CAST(info['flight_number'] AS STRING) AS flight_number, CAST(info['departure_airport'] AS STRING) AS departure_airport, CAST(info['departure_time'] AS STRING) AS departure_time FROM flights WHERE CAST(info['departure_city'] AS STRING) = 'New York' AND (EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) < 17 OR EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) >= 19) ORDER BY departure_time",
               "intent": "Tell me flights that can help me beat nighttime traffic if traveling from New York",
               "manifest": "Tell me flights that can help me beat nighttime traffic if traveling from a given city",
               "parameterized": {
                 "parameterized_sql": "SELECT CAST(info['airline'] AS STRING) AS airline, CAST(info['flight_number'] AS STRING) AS flight_number, CAST(info['departure_airport'] AS STRING) AS departure_airport, CAST(info['departure_time'] AS STRING) AS departure_time FROM flights WHERE CAST(info['departure_city'] AS STRING) = ? AND (EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) < 17 OR EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) >= 19) ORDER BY departure_time",
                 "parameterized_intent": "Tell me flights that can help me beat nighttime traffic if traveling from ?"
               }
             }
           ]
         }
         




### Generate value search context

In this section, you generate value search context to help context set logic map value phrases to specific values stored in your Bigtable columns using case-insensitive exact string matching. For example, if a user asks for flights to "Raleigh-Durham," value search maps this to the stored database value `"Raleigh-durham"` (airport code `RDU`).

To generate value search context, perform the following steps:

  1. Enter the following prompt into the agent harness.
         
         Generate a case-insensitive value search on table "airports" for column "info['city']" with concept "Airport City" using match function "EXACT_MATCH_STRINGS".

  2. Review the generated value search definition. You can either save the value search definition as a new context set file or append it to an existing context set file.

  3. Prompt the agent with `Append the context to context_set.json`. This adds the value search definition to the context file created in the earlier section.

  4. Enter the database instance and database name for which the context set file was generated.

The existing context file is updated with the value search definition, with the following content:
         
         {
           "templates": [
             {
               "nl_query": "Show me flights from SFO to JFK",
               "sql": "SELECT CAST(_key AS STRING) AS flight_id, CAST(info['airline'] AS STRING) AS airline, CAST(info['flight_number'] AS STRING) AS flight_number, CAST(info['departure_airport'] AS STRING) AS departure_airport, CAST(info['arrival_airport'] AS STRING) AS arrival_airport, CAST(info['departure_time'] AS STRING) AS departure_time, CAST(info['arrival_time'] AS STRING) AS arrival_time, CAST(info['departure_gate'] AS STRING) AS departure_gate, CAST(info['arrival_gate'] AS STRING) AS arrival_gate, CAST(info['departure_city'] AS STRING) AS departure_city, CAST(info['arrival_city'] AS STRING) AS arrival_city FROM flights WHERE CAST(info['departure_airport'] AS STRING) = 'SFO' AND CAST(info['arrival_airport'] AS STRING) = 'JFK' ORDER BY departure_time",
               "intent": "Find flights from SFO to JFK.",
               "manifest": "Find flights from a given departure airport code to a given arrival airport code.",
               "parameterized": {
                 "parameterized_sql": "SELECT CAST(_key AS STRING) AS flight_id, CAST(info['airline'] AS STRING) AS airline, CAST(info['flight_number'] AS STRING) AS flight_number, CAST(info['departure_airport'] AS STRING) AS departure_airport, CAST(info['arrival_airport'] AS STRING) AS arrival_airport, CAST(info['departure_time'] AS STRING) AS departure_time, CAST(info['arrival_time'] AS STRING) AS arrival_time, CAST(info['departure_gate'] AS STRING) AS departure_gate, CAST(info['arrival_gate'] AS STRING) AS arrival_gate, CAST(info['departure_city'] AS STRING) AS departure_city, CAST(info['arrival_city'] AS STRING) AS arrival_city FROM flights WHERE CAST(info['departure_airport'] AS STRING) = ? AND CAST(info['arrival_airport'] AS STRING) = ? ORDER BY departure_time",
                 "parameterized_intent": "Find flights from ? to ?."
               }
             },
             {
               "nl_query": "Tell me flights that can help me beat nighttime traffic if traveling from New York",
               "sql": "SELECT CAST(info['airline'] AS STRING) AS airline, CAST(info['flight_number'] AS STRING) AS flight_number, CAST(info['departure_airport'] AS STRING) AS departure_airport, CAST(info['departure_time'] AS STRING) AS departure_time FROM flights WHERE CAST(info['departure_city'] AS STRING) = 'New York' AND (EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) < 17 OR EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) >= 19) ORDER BY departure_time",
               "intent": "Tell me flights that can help me beat nighttime traffic if traveling from New York",
               "manifest": "Tell me flights that can help me beat nighttime traffic if traveling from a given city",
               "parameterized": {
                 "parameterized_sql": "SELECT CAST(info['airline'] AS STRING) AS airline, CAST(info['flight_number'] AS STRING) AS flight_number, CAST(info['departure_airport'] AS STRING) AS departure_airport, CAST(info['departure_time'] AS STRING) AS departure_time FROM flights WHERE CAST(info['departure_city'] AS STRING) = ? AND (EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) < 17 OR EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) >= 19) ORDER BY departure_time",
                 "parameterized_intent": "Tell me flights that can help me beat nighttime traffic if traveling from ?"
               }
             }
           ],
           "facets": [],
           "value_searches": [
             {
               "query": "SELECT CAST(T.info['city'] AS STRING) AS value, 'info:city' AS `columns`, 'Airport City' AS concept_type, 0.0 AS distance, CONCAT('iata=', CAST(T.info['iata'] AS STRING), ', name=', CAST(T.info['name'] AS STRING)) AS context FROM `airports` AS T WHERE LOWER(CAST(T.info['city'] AS STRING)) = LOWER(CAST($value AS STRING))",
               "concept_type": "Airport City",
               "description": "Exact case-insensitive match on airport city name in the airports table."
             }
           ]
         }
         




## Upload the context set file to the QueryData

In this section, you upload the context set file to QueryData, so that it improves the QueryData's SQL generation capabilities on your database.

To upload the context, perform the following steps:

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. 

  4. In the **Explorer pane** , under **Context sets** and next to the `flights-assistant` context set, click the **View actions** (more_vert) icon.

  5. Click **Edit context set**.

  6. Click **Browse** in the **Upload context file** section, and then select the context set file generated earlier.

  7. Click **Save**.




## Generate SQL query using QueryData

In this section, you use the context set file you uploaded to ask natural language questions. This lets you verify that QueryData correctly understands and applies definitions for terms like `nighttime traffic` and other related phrases.

**Note:** GenAI models are nondeterministic, meaning the same prompt may yield different responses across separate calls due to the probabilistic nature of the output generation.

To generate SQL queries, perform the following steps:

  1. In the **Explorer** pane, next to your context set, click **View actions ( more_vert)**.
  2. Click **Test context set**.
  3. In the query editor, click **Generate SQL using QueryData with: flights-assistant**.
  4. To generate a SQL query, enter the following natural language question, and then click **Generate**.
         
         Tell me flights that can help me beat nighttime traffic if traveling from New York
         

The generated SQL query looks similar to the following:
         
         SELECT
           CAST(info['airline'] AS STRING) AS airline,
           CAST(info['flight_number'] AS STRING) AS flight_number,
           CAST(info['departure_airport'] AS STRING) AS departure_airport,
           CAST(info['departure_time'] AS STRING) AS departure_time
         FROM
           flights
         WHERE
           CAST(info['departure_city'] AS STRING) = 'New York'
           AND (
             EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) < 17
             OR EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) >= 19
           )
         ORDER BY
           departure_time;
         

This is the same question you added to QueryData's context. Observe that QueryData can now accurately interpret the term `nighttime traffic`.

Although the context originates from one particular question, QueryData uses it to enhance SQL generation for a wide range of similar questions.

  5. In the **Generate SQL using QueryData with: flights-assistant** window, click **Edit**.

  6. Enter the following similar question to generate a SQL query, and click **Update**.
         
         What are the flights that can help me avoid evening traffic if departing from Boston
         

Since the question replaces the term `nighttime traffic` with a similar term, `evening traffic`, QueryData provides a consistent answer to this question by applying the same interpretation.

The generated SQL query looks similar to the following:
         
         SELECT
           CAST(info['airline'] AS STRING) AS airline,
           CAST(info['flight_number'] AS STRING) AS flight_number,
           CAST(info['departure_airport'] AS STRING) AS departure_airport,
           CAST(info['departure_time'] AS STRING) AS departure_time
         FROM
           flights
         WHERE
           CAST(info['departure_city'] AS STRING) = 'Boston'
           AND (
             EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) < 17
             OR EXTRACT(HOUR FROM TIMESTAMP(CAST(info['departure_time'] AS STRING))) >= 19
           )
         ORDER BY
           departure_time;
         

  7. In the **Generate SQL using QueryData with: flights-assistant** window, and then click **Edit**.

  8. Enter the following question to generate a SQL query, and then click **Update**.
         
         Show me flights to Raleigh-Durham
         

The generated SQL query looks similar to the following:
         
         SELECT
           CAST(_key AS STRING) AS flight_id,
           CAST(info['airline'] AS STRING) AS airline,
           CAST(info['flight_number'] AS STRING) AS flight_number,
           CAST(info['departure_airport'] AS STRING) AS departure_airport,
           CAST(info['arrival_airport'] AS STRING) AS arrival_airport,
           CAST(info['departure_time'] AS STRING) AS departure_time,
           CAST(info['arrival_time'] AS STRING) AS arrival_time,
           CAST(info['departure_gate'] AS STRING) AS departure_gate,
           CAST(info['arrival_gate'] AS STRING) AS arrival_gate,
           CAST(info['departure_city'] AS STRING) AS departure_city,
           CAST(info['arrival_city'] AS STRING) AS arrival_city
         FROM
           flights
         WHERE
           CAST(info['arrival_city'] AS STRING) = 'Raleigh-durham'
         ORDER BY
           departure_time;
         

Observe that QueryData can now accurately map `Raleigh-Durham` to the stored value `"Raleigh-durham"` (`RDU`).




## Integrate QueryData with your application

In this section, you create a data agent for a flight-finding application. This data agent provides a conversational interface to the `flights` and `airports` tables that you created earlier. It also explains how to create and integrate this data agent into your application using [Agent Development Kit (ADK)](https://github.com/google/adk-python), the Gemini Data Analytics QueryData MCP tool, and a context set to improve quality of the responses.

**Note:** GenAI models are nondeterministic, meaning the same prompt may yield different responses across separate calls due to the probabilistic nature of the output generation.

  1. Download [MCP Toolbox](https://mcp-toolbox.dev/documentation/introduction/#install-toolbox) version 1.14.0 or later. MCP Toolbox exposes the data agent as a tool for applications to connect with. The MCP Toolbox differs from the context engineering agent you installed earlier, which generates context.

  2. Set up [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
         
         gcloud auth application-default login

  3. Find the ID of the context set you created earlier. For more information about how to find the context set ID, see [Find the context set ID](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/inspect-data-agent#find-context-set-id).

  4. Append the following to the `tools.yaml` configuration to connect to the data agent using the MCP Toolbox. For more information, see [Gemini Data Analytics Source](https://mcp-toolbox.dev/integrations/cloudgda/source/) and [Gemini Data Analytics QueryData tool](https://mcp-toolbox.dev/integrations/cloudgda/tools/cloud-gda-query/).
         
         ---
         kind: source
         name: gda-api-source
         type: cloud-gemini-data-analytics
         projectId: "PROJECT_ID"
         ---
         kind: tool
         name: cloud_gda_query_tool
         type: cloud-gemini-data-analytics-query
         source: gda-api-source
         description: Use this tool to send natural language queries to the Gemini Data Analytics API and receive SQL, natural language answers, and explanations.
         location: "REGION_ID"
         context:
           datasourceReferences:
             bigtableReference:
               databaseReference:
                 projectId: "PROJECT_ID"
                 instanceId: "INSTANCE_ID"
               agentContextReference:
                 contextSetId: "CONTEXT_SET_ID"
         generationOptions:
           generateQueryResult: true
           generateNaturalLanguageAnswer: true
           generateExplanation: true
           generateDisambiguationQuestion: true
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION_ID`: the region of your Bigtable cluster (for example, `us-central1`).
     * `INSTANCE_ID`: the ID of your Bigtable instance.
     * `CONTEXT_SET_ID`: the context set ID. For more information about how to find the context set ID, see [Find the context set ID](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/inspect-data-agent#find-context-set-id).
  5. Run the MCP Toolbox server with the `tools.yaml` file.
         
         ./toolbox --config PATH_TO_TOOLS_YAML

Replace `PATH_TO_TOOLS_YAML` with the path to the `tools.yaml` file you created earlier.

**Note:** Don't close the terminal window where the MCP Toolbox server is running.
  6. Create an ADK application that invokes [Gemini Data Analytics QueryData tool](https://mcp-toolbox.dev/integrations/cloudgda/tools/cloud-gda-query/) using the MCP Toolbox's Python SDK. For more information about how to use the MCP Toolbox's Python SDK, see the [quickstart for Toolbox](https://mcp-toolbox.dev/documentation/getting-started/local_quickstart/) and for Python ADK, see the [quickstart for ADK](https://google.github.io/adk-docs/get-started/python/).

     1. Create a directory to store the application, for example `flight-assistant-app`.
     2. Change directory to the `flight-assistant-app` directory.
            
            mkdir flight-assistant-app
            cd flight-assistant-app

     3. Run the following commands under the `flight-assistant-app` directory to create a virtual environment and install required components.
            
            uv init
            uv add google-adk toolbox-core google-genai

     4. Set up an ADK agent.

        1. Create an ADK agent.
               
               uv run adk create my_agent

        2. Select the `gemini-2.5-flash` model, or newer.

        3. Select **Google AI** , and enter your Gemini API key. For more information about how to find your API key, see [Using Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key). (Alternatively, if you don't need a free trial, you can select **Vertex AI** and specify a Google Cloud project with billing enabled).

     5. Replace the contents of the `agent.py` file with the following Flight Data Assistant sample application code.
            
            from typing import cast
            
            from google.adk.agents.llm_agent import Agent
            from google.adk.agents.llm_agent import ToolUnion
            
            from toolbox_core import ToolboxSyncClient
            
            TOOLBOX_URL = "http://127.0.0.1:5000"
            
            INSTRUCTION = """
            # ROLE
            You are a friendly and factual flight data assistant. Your goal is to help users find the best flights for their needs by providing accurate information with a helpful, professional tone.
            - use the Query Data Tool to answer the user's question, if the tool fails to generate a valid query, ask the user to clarify their question.
            
            # OPERATIONAL CONSTRAINTS
            - TOOL LIMITATION: You only have access to the Query Data Tool. Do not claim to have capabilities beyond what this tool provides.
            - TRANSPARENCY POLICY: Maintain a seamless user experience. Never mention that you are using a tool, querying a database, or generating SQL. Frame all responses as your own direct assistance.
            - SCOPE MANAGEMENT: If a user asks for something beyond your capabilities, politely state that you cannot perform that specific task. Guide the user towards what you can help with.
            
            # COMMUNICATION STYLE
            - Be concise and scannable when listing answers.
            - Maintain a helpful, professional persona.
            
            =====
            
            # QUERY DATA TOOL
            
            Inputs:
            1. query: A natural language formulation of a database query.
            
            Outputs: (all optional)
            1. disambiguation_question: Clarification questions or comments where the tool needs the users' input.
            2. generated_query: The generated query for the user query.
            3. intent_explanation: An explanation for why the tool produced `generated_query`.
            4. query_result: The result of executing `generated_query`.
            5. natural_language_answer: The natural language answer that summarizes the `query` and `query_result`.
            
            Usage guidance:
            1. If `disambiguation_question` is produced, then solicit the needed inputs from the user and try the tool with a new `query` that has the needed clarification.
            2. If `natural_language_answer` is produced, use `intent_explanation` and `generated_query` to see if you need to clarify any assumptions for the user.
            3. If the tool output indicates failure or empty results, explain that clearly using the provided reasoning.
            """
            
            client = ToolboxSyncClient(TOOLBOX_URL)
            
            mcp_tool = client.load_tool("cloud_gda_query_tool")
            
            root_agent = Agent(
                model="gemini-2.5-flash",  # Or newer.
                name="root_agent",
                instruction=INSTRUCTION,
                tools=cast(list[ToolUnion], [mcp_tool]),
            )
            

**Note:** The instruction contains a system prompt that sets up a `flight assistant` data agent. It also instructs the agent how to use the Gemini Data Analytics QueryData tool you set up in the `tools.yaml` file you created earlier.
  7. To start the application, run the following commands under the `flight-assistant-app` directory. Access the ADK web server at `http://127.0.0.1:8000`.
         
         uv run adk web --port 8000

  8. Enter any text, such as `hello`, to start interacting with the agent.

The ADK agent answers general questions and calls the required MCP tools.

  9. Enter the following flight-related question.
         
         How many flights depart from the west side?
         

The MCP tool is called to answer this question. Because the database doesn't define `the west side`, QueryData assumes a list of West Coast airports and returns the flight count and explanation, which the agent uses to clarify the assumption in its response:
         
         There are 253 flights departing from the west side.
         
         Please note that "the west side" is not explicitly defined in our records, so this count assumes flights departing from major West Coast airports: Los Angeles (LAX), San Francisco (SFO), San Diego (SAN), Seattle (SEA), Portland (PDX), Las Vegas (LAS), and Phoenix (PHX). If you had a different set of airports in mind, please let me know!
         

  10. Enter a question similar to that in the query template generated for the agent.
         
         Help me find flights from San Francisco that avoid the evening rush hour.
         

Based on the QueryData context added earlier, the MCP tool understands that `evening traffic` occurs between 5 PM and 7 PM. The MCP tool returns the associated data for the agent to use in constructing its response.
         
         Here are the flights departing from San Francisco that avoid the evening rush hour (defined as 5 PM to 7 PM):
         
         * UA 1532 departing at 05:50:00
         * UA 1158 departing at 05:57:00
         * CY 922 departing at 06:38:00
         * OO 5441 departing at 07:08:00
         * UA 616 departing at 07:14:00
         * AA 24 departing at 07:14:00
         * B6 434 departing at 08:00:00
         * AA 242 departing at 08:18:00
         * UA 1739 departing at 08:22:00
         * OO 6336 departing at 08:32:00
         * US 1784 departing at 08:47:00
         * DL 1631 departing at 09:00:00
         * DL 1106 departing at 09:06:00
         * OO 5427 departing at 09:06:00
         * CY 352 departing at 09:25:00
         

  11. Enter a question based on the concept type that you added in the QueryData agent context.
         
         Show me flights to Raleigh-Durham
         

Based on the value search context added earlier, the agent understands that "Raleigh-Durham" matches the stored city `"Raleigh-durham"` (airport code `RDU`) and returns the associated data for the agent to use in constructing its response.
         
         Here is the flight heading to Raleigh-Durham (RDU):
         
         * Flight UA 1568 departs from San Francisco (SFO) at Gate A30 on 2025-01-02 at 14:55:00 and arrives at Raleigh-Durham (RDU) at Gate A26 on 2025-01-02 at 23:03:00.
         




## Iterate agent performance

The ADK web UI lets you inspect the request and response from the Gemini Data Analytics QueryData MCP tool. You can use this response to observe the tool responses such as generated SQL query, result set, intent explanation, disambiguation question, and natural language answer, to help you confirm the correctness of your agent's responses.

For example, for the input text `How many flights depart from the west side?` that you entered earlier, click the agent bubble. In the **Event** tab in the left navigation, expand the `functionResponse` to see the following response.
    
    
    {"result": "{"generatedQuery":"SELECT COUNT(*) AS flight_count FROM flights WHERE CAST(info['departure_airport'] AS STRING) IN ('LAX', 'SFO', 'SAN', 'SEA', 'PDX', 'LAS', 'PHX')","intentExplanation":"The user is asking for the number of flights departing from the 'west side'. Since there is no explicit definition or column for 'west side' in the schema, I will assume this refers to major airports on the West Coast of the United States (e.g., LAX, SFO, SAN, SEA, PDX, LAS, PHX).","queryResult":{"columns":[{"name":"flight_count"}],"rows":[{"values":[{"value":"253"}]}],"totalRowCount":"1"},"naturalLanguageAnswer":"There are 253 flights departing from West Coast airports (LAX, SFO, SAN, SEA, PDX, LAS, PHX)."}"}
    

### Refine response accuracy

You can continuously refine the accuracy of responses from the Gemini Data Analytics QueryData tool by adding additional context. Use the context engineering agent to generate context, and then upload the updated context set file to the existing `flights-assistant` data agent. For more information, see [Manage context sets in Bigtable Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/manage-data-agents). The console immediately ingests new context after you upload it, enabling you to enhance the agent's accuracy without any application downtime.

### Multiple agents

In your development environment, you can perform A/B testing on multiple data agent contexts by assigning distinct names to tools in your `tools.yaml` file. For example, you can create unique `tools.yaml` configurations by defining two `cloud-gemini-data-analytics-query` tools with different names, such as `cloud_gda_query_tool_v1` and `cloud_gda_query_tool_v2`. This setup lets you implement application logic that programmatically selects the required context version by choosing the corresponding tool name.

The following example `tools.yaml` shows how to set up multiple data agents for a database source:
    
    
    kind: source
    name: gda-api-source
    type: cloud-gemini-data-analytics
    projectId: PROJECT_ID
    ---
    kind: tool
    name: cloud_gda_query_tool_v1
    type: cloud-gemini-data-analytics-query
    source: gda-api-source
    context:
      datasourceReferences:
        DB_SOURCE:
          databaseReference: ...
          agentContextReference:
            contextSetId: "V1_YOUR_CONTEXT_SET_ID"
    generationOptions: ...
    ---
    kind: tool
    name: cloud_gda_query_tool_v2
    type: cloud-gemini-data-analytics-query
    source: gda-api-source
    context:
      datasourceReferences:
        DB_SOURCE:
          databaseReference: ...
          agentContextReference:
            contextSetId: "V2_YOUR_CONTEXT_SET_ID"
    generationOptions: ...
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `V1_YOUR_CONTEXT_SET_ID`: the context set ID for version 1.
  * `V2_YOUR_CONTEXT_SET_ID`: the context set ID for version 2.
  * `DB_SOURCE`: the database source configurations.



## Clean up

After you've finished following this tutorial, delete the resources that you created to avoid incurring ongoing costs. The following sections describe how to delete these resources.

### Delete the context set

Before you delete the instance, delete the context set that you created.

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. 

  4. In the **Explorer pane** , next to your context set, click **View actions ( more_vert)**.

  5. Click **Delete context set**.

  6. In the **Delete context set** window, enter `flights-assistant`.

  7. Click **Confirm**.




### Delete the instance

When you delete the instance that you created in the before you begin section, you also delete all of the objects you created.

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Click the name of the instance that you want to delete, for example, **Test Instance**.

  3. Click **Delete instance**.

  4. Confirm that you want to delete the instance by entering the instance ID and clicking **Delete**.




## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/context-sets-overview).
  * Learn how to [define authored context for database data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

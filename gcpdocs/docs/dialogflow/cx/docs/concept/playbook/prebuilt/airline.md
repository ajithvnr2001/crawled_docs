---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/airline/
title: Airline support prebuilt agent \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:09:40.258820+00:00
---

# Airline support prebuilt agent  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/airline/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Airline support prebuilt agent Stay organized with collections  Save and categorize content based on your preferences. 

The airline support [playbook-based, prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt) provides flight booking with geolocation for user convenience.

## Sample dialog

This sample dialog demonstrates common scenarios handled by the prebuilt agent.

### Flight search

  1. The user wants to search for flights.
  2. The agent asks the user for their origin city, destination, and departure date.
  3. The user responds with these details.
  4. The agent presents a list of flights, and prompts the user to select an option.
  5. The user chooses the cheapest flight.
  6. The agent confirms the booking and provides a booking number.

User Input | Agent Response  
---|---  
Hi |   
| We are working on finding your location. This might take a moment.  
| Hi there, welcome to the Cymbal Air helpdesk! I can help you find a flight to anywhere in the world. Where would you like to go?  
Budapest |   
| Which city are you departing from?  
New York |   
| When would you like to fly out?  
December 1st |   
| [presents list of flights] Which of these flights would you like to book? Your cheapest option is a flight that leaves JFK at 11:00 AM on December 1st, arrives in BUD at 11:00 PM on the same day, and costs $254.  
I want to book the cheapest one |   
| Excellent, your flight has been booked. Your flight departs from JFK at 11:00 AM and arrives in BUD at 11:00 PM the same day. Your booking number is 3W817T, and you'll receive an email with more details shortly. Is there anything else I can help you with?  
That's all for now |   
| Glad I could help!  
  
## Basic setup

To set up this prebuilt agent:

  1. [Import the prebuilt agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt#import).
  2. Configure the provided [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) with your external services. For more information, see Tool setup.



## Tool setup

This agent includes [tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) to integrate with external services.

### Flight Search tool

The `getGeolocation` tool uses a [function call](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool#function-calls) to determine the user's location and automatically input the origin city for the flight search.

The output parameters for this tool include:

  * City (required): The city where the user is located.
  * Country (required): The country where the user is located.
  * State (required): The state or province where the user is located.
  * Road (optional): The closest major road to the user's approximate street address.
  * County (optional): The county where the user is located, if it exists.
  * Country-code (optional): The two-letter code associated with the country where the user is located.
  * Postcode (optional): The ZIP code associated with the user's approximate street address.
  * ISO3166-2-lvl4 (optional): The alphanumeric code used to identify the specific administrative subdivision (for example, state, province, or territory) of the country where the user is located.



The `getFlights` tool generates a fictional list of flights based on the origin city, destination, and departure date. The tool returns a custom payload response that includes a table with flight timings and prices. The UI uses this custom payload to display the flights in rich content form.

## Complete

Your agent and its integrations are now set up and ready to test.

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt)

[ Next Department of Motor Vehicles  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt/department-of-motor-vehicles)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

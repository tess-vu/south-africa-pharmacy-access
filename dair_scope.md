# DAIR Scope for Understanding the Geography of Healthcare Access in South Africa

Instructors: Michael Fichman & Matthew Harris

Team: Tess Anh Thu Vu (tessavu@proton.me; tessavu@upenn.edu), Joey Cahill (cahill1@upenn.edu), Jillian Kalman (jillian.kalman@pennmedicine.upenn.edu), Alex Stauffer (astauf03@upenn.edu)

DAIR Contacts: Raesetje Sefala — Researcher (raesetje@dair-institute.org), Nyalleng Moorosi — Research Fellow (nyalleng@dair-institute.org), Distributed AI Research Institute (DAIR)

## Project Overview

The Distributed AI Research Institute wishes to understand the spatial alignment between populations and pharmacy access in South Africa. The goal of this project is to prototype a method that quantifies pharmacy access, and create an analytical report and a web-based viewer that allows a member of the general public to understand measures of access and how it varies across space and between sub-populations. You will work to build a minimum viable product in two test provinces — KwaZulu-Natal and Gauteng — and create a well-documented method that DAIR can generalize to the entire country.

DAIR’s question was prompted by recent changes in national healthcare policy. The National Health Insurance Act of 2024 created a public fund to subsidize the provision of care and medicines. DAIR wants to know the degree to which populations can take advantage of this funding — specifically, who has access to pharmacies near their place of residence. Furthermore, DAIR wishes to understand the associations between levels of access and population characteristics, as well as to the historical geography of apartheid.

At its simplest, this is a project that requires a spatial overlay of supply (pharmacies) and demand (populations) — but there are many details and technical challenges you will need to work through in order to build your data sets, estimate population densities, and specify the nature of “access.” As such, the use case is as follows — a member of the public wants to use a web-based, geo-enabled dashboard in order to understand whether:

1. their area in South Africa has access to pharmacy services, and/or

2. the degree to which access to pharmacy services is lacking or uneven

Your primary challenges in this project are associated with the availability and structure of data about populations and pharmacies in South Africa. To build a measure of pharmacy access, you will work with Snowflake AI[1] and Google Places API workflows to build and verify a spatial database of pharmacies from a variety of published sources and open web resources. To understand population distribution, you will need to address limitations of South African Census data (Stats SA) and generate current estimates of population and demographics at the smallest appropriate geographic resolution.

Once you understand the locations of pharmacies and populations, you will need to quantify “access” according to some spatial logic. Lastly, you will figure out how to analyze, visualize and communicate the nature of access in your study area.

You will complete a written markdown report that outlines your methods, findings, and analysis. This will also include a code-base that is a guide for DAIR to replicate your methodology. You will also create a web-based application that allows a user to understand the “story” of healthcare access in your study areas.

## Deliverables

Project management plan and collaborative tools — You will create an "Agile[2]" development project management plan detailing due dates and deliverables.

You will create a repo on Github for code development, and a working Github markdown (README.md).

**An App** — You will be responsible for designing a desktop-based application to serve your analytics to a project user. The app will be built around a use case that you will define early on in the project after studying your project and consulting with your instructors and DAIR. This app will be designed and deployed in javascript and uploaded to the class Github page at the end of the semester.

**A Markdown** — You will create a report in the R Markdown language that presents your project and annotates your data wrangling and modeling code in Python, R, JS + HTML + CSS, and/or SQL. This deliverable should give a much more detailed idea of how your model(s) function in practice. Your markdown should provide insights about a replicable workflow. It functions as a sort of “report” that lays out the project concept, exploratory analysis, modeling etc., and describes the details of your research and your decision-making regarding the nature of the tool.

**Three Presentations** — You will give two internal presentations with intermediate progress updates. At the time of each presentation, your markdown should be consolidated and polished to reflect all work done to that point. At the end of the semester you will deliver one public presentation.

**Project Management** — Designate one person to take the lead on the dashboard (a person who is familiar with JS, or somebody who feels comfortable learning Shiny or StoryMaps), one person should be designated to lead on the markdown, another on project management. One person with experience in Python (and if possible, SQL) should be assigned to lead on the work that takes place in Snowflake.

It’s expected that everybody contribute to each element of the project as they are able.

**Client Relations** — We have asked that DAIR sit for an introductory interview and attend the final presentations. Some will participate more, some will not be available except for perhaps a few emails. They are busy professionals who are graciously lending us their time and data — please be respectful of their time. During your introductory interview, you can talk with DAIR about your project, and ask them how they would like to communicate. Your instructors have prepared a document with some general tips on how to conduct this meeting and what to ask. One team member needs to be the “leader” to run this meeting.

**Qualitative and Background Research** — Use your project management planning to dedicate project personnel and time to doing desk research. Read overviews of the 2024 health care law[3] and survey journalistic sources regarding the discussion of healthcare access in light of its passage. Use the Penn Library’s resources to conduct brief desk research about historical geographies of apartheid in order to understand the relationships between patterns of settlement, demographics, and healthcare access in modern SA.

Your introductory interview with DAIR will also be an important starting point to understanding the core policy issues as well as the nature of commercial pharmacies in South Africa. Pharmacies are found in hospitals as well as at commercial locations — there are chains, independent pharmacies, and some illicit “black market” pharmacies that you will want to try to weed out of your database.

You should also be prepared to ask questions about the use case and the data. Some examples include:

* Where did the data you are providing us about pharmacies come from?
* What are some of the signs of an illegitimate pharmacy?
* What are some of the considerations about the provinces we are studying?
* What should we know about the nature and limitations of the South African census?
* How will you generalize our methods and code to a bigger analysis?

**Data Wrangling** — Data wrangling is the most time-consuming and important task in this project. You have the task of wrangling two types of data — data on pharmacies and census data. It is critical that you document this process carefully-  the basis of this project’s utility to DAIR is replicability.

## Pharmacies

The central challenge with this project is that there is no unified database of pharmacies. You will assemble a database of pharmacies from several sources:

1. Unstructured listings of pharmacies published by retailers and healthcare providers. These are in HTML and PDF formats and are provided by DAIR (see the Data Sources section of the scope for more on this).

      a. You will need to determine a structure for your database and use AI and text parsing tools to unify the structure across sources (e.g. turn the PDF and HTML listings into flat files).

      b. You will then need to geo-locate the non-spatial databases using the Google Geocoder API.

2. Google Places API listings.

      a. Use the Google Places API to find pharmacies in your pilot areas — it’s assumed there are numerous pharmacies.

You will need to reconcile your databases to link data from listings across sources and remove duplicates. You will also need to set up a basic text-analysis workflow that “flags” pharmacies as being potentially likely to be engaged in unlicensed operation, a practice that has attracted attention in South Africa[4].

## Google API Usage

Using the Google Places API and Google Geocoder API is central to the project. You will want to geocode pharmacy locations from your static listings (Geocoder), and fetch pharmacy listings to complete and validate your database (Places). 

Sign up for a Google Developer profile, and walk through tutorials and directions to set up a “project” and receive an API key. These APIs are not free — they have set fees because they are designed as a product for use in third party applications. You have a $200 budget to use these tools, and you must set daily limits on usage in your projects so that you can conserve this budget effectively.

Use the `googleway`[5] package in R for accessing Places. The `ggmap`[6] package has Google Geocoding functionality.
Michael Fichman has code to help you build your Google API routines.

Here are some tips for using these tools effectively:

To conserve your budget, you will have to be very careful about usage — do not make large pulls of Places data or geocode large numbers of addresses. Use test batches of data (e.g. tens of observations) to see if your code is working and returns the results you want. You will not have the budget to run thousands and thousands of calls, and the budgetary limits on usage are time-sensitive.

Google Places API limits you to 20 return observations at one time, so you will want to develop a call for `place_type` = “pharmacy” for an optimal radius, and strategically develop a set of lat/lon coords to cover your study area. For example, research pharmacy locations and density using Google Maps on the web, and figure that you can use, say, X number of point searches in your subject area to get what you need.

Be careful not to expose your API keys by putting them in your Github code that is published to your account. Google will flag it and deactivate your key. Use `.gitignore` to exclude any `.R` files with your key, or set up a routine where the key is stored in a `.txt` file on your hard drive(s) and you fetch it in your code without exposing the key.

## Snowflake AI

Matthew Harris will facilitate the team’s use of Snowflake as the project’s central workspace for assembling, cleaning, and validating pharmacy data. Snowflake will serve as the “source of truth” where the team brings together pharmacy listings from multiple providers, standardizes the information into a consistent structure, and produces analysis-ready outputs that can be used in R and in the web application.

At a high level, Snowflake will support a simple, repeatable workflow:

* Collect and store source materials: Upload and organize pharmacy listings (PDF/HTML-derived tables and any other source extracts) with basic metadata so the project remains reproducible and traceable.

* Use AI-assisted parsing and cleanup: Apply Snowflake’s AI/LLM capabilities to help convert semi-structured listings into consistent fields (e.g. pharmacy name, address, location notes), and to reduce common data quality issues such as inconsistent naming, formatting differences, and partial addresses.

* Reconcile and de-duplicate across sources: Combine overlapping listings into a single consolidated pharmacy dataset, while preserving enough information to understand where each record originated and how confident the team is in the final result.

* Support validation and enrichment workflows: Store and manage outputs from Google Geocoding / Places calls (and any registration checks) so results can be reviewed, iterated, and reused without repeatedly re-running API calls.

* Publish curated tables for analysis and the app: Produce a clean, geospatially-enabled pharmacy dataset and supporting summary tables that downstream work can reliably consume for exploratory analysis, access calculations, and visualization.

On or about the third week, the team will spend ~90 minutes in a hands-on workshop with Matt to get access to sponsored student accounts and learn the basic Snowflake workflow used in this project. The workshop will focus on how the data should be organized and what the “clean output” should look like so that the rest of the project (R modeling and the web viewer) can proceed smoothly. One team member with Python/SQL experience should lead the Snowflake work, but the goal is for the process and outputs to be understandable to the full team.

## Stats SA Census

The South African Census was conducted most recently in 2022. The smallest aerial unit for which population data are available is the “Ward” level. Wards can be quite large, as they are population scaled, and rural wards can be huge. Smaller units, like the Small Area (SALs ~500 households) are only available for the 2011 census. There are 10% microdata available for the 2022 Census, which have data about sub-population characteristics including age and demographics. These data come with “weights” that let you tabulate estimates (and margins of error) to smaller geographies.

You will want to reduce your data to smaller geographies than wards — after all, knowing whether somebody has “access” to a pharmacy is probably best done at a very local level. You have several alternatives for doing this, each will produce different results. You should create each population data set type below:

   1. Use a “step-down” model to apportion population to Small Areas based on the proportion of each SAL’s 2011 population relative to its parent ward and the 2011-2022 growth of the ward to which it belongs.
   2. A fishnet grid cells that you apportion population to from your SAL step-down’s using aerially-weighted interpolation (AWI). This is simple to implement in `sf`.
   3. Use existing estimates in raster form from models built on development data such as WorldPop[7] and summarize them to fishnet grid cells.

**Exploratory Analysis** — Your exploratory analysis will involve your investigation of the pharmacy and population data sets — exploring their descriptive statistics, figuring out which versions of the data sets are the most useful for your use case, and relating populations to pharmacies across space.

Here is a non-exclusive list of questions for you to explore:

   * How many pharmacies are there in your study areas?
   * How densely are they distributed?
   * What is the spatial process of pharmacy distribution?
   * What are the various types of pharmacies — hospitals, chains etc.?
   * How many of them are “High confidence” locations — e.g. ones where you are confident in the data point?
   * Which of your population data sets seems like the most accurate (or least biased) representation of populations?
   * What is the spatial process of population distribution and underlying economic and demographic variables?
   * To what degree does pharmacy density correlate with population characteristics?
   * What kinds of outliers do you observe? (e.g. geographic areas)

Once you have done your modeling tasks, you will want to return to an exploratory analysis mindset to understand the dimensions of the supply-demand alignment.

## Modeling and Analysis

This project does not have a machine-learning or regression model at its core. Instead, your key modeling task involves figuring out what “access” means for populations in your study area, and comparing different approaches. How is one to understand whether a given person in your study area can “get to” a pharmacy. You will have to determine an aerial unit of population — is it a fishnet grid cell, or an SAL? How do you determine the average level of access for that aerial unit — is it walking or driving distance? Is it straight-line distance? From what point in the aerial unit is this distance to be calculated?

You will determine the level of access for the entirety of your study area, and then you must analyze your results:

   * What is the overall level of access to pharmacies?
   * Do levels of access vary across space?
   * Are there differential levels of access between population groups or jurisdictions?
   * Is there a relationship between access levels and historical geographies of apartheid?
   * What is the nexus between levels of access and levels of need?
   * What are the actionable insights to be drawn from your understanding of access?

**App Building** — Your application should have a journalistic character, allowing a non-technical user to understand the context for your research and to understand the nature of the healthcare access issue in South Africa. They should be able to engage with and manipulate the spatial data to generate healthcare access statistics and visualizations related to populations and subpopulations and explore the study area to see the geography of access — either in a broad way, or for a user input location.

In mid-semester, you will work to select a format that best serves this function. You might find that integrating a “story map” alongside a geo-spatial dashboard is an attractive option. Take a look at one of our practicum projects from a few years ago about vacant lots to understand what a story map can do[8].

**Data Security and User Agreements** — The data for this project do not have major privacy considerations. As with all practicum participants, you will be required to complete the CITI certification in human subject research prior to the semester.

## Data Sources

Pharmacies from large private health insurance providers:

   1. Momentum: https://www.multiply.co.za/engaged/independent-pharmacies/
   2. Discovery: https://www.discoveryhealthmedicalscheme.co.za/wcm/discoverycoza/assets/vitality/wellness-network/pharmacy-list.pdf
   3. Wooltrue (another branch of Momentum): https://www.wooltruhealthcarefund.co.za/static-assets/siteFiles/WHF_Pharmacy_Network_list_2024_GAU.pdf
   4. SamwuMed: https://www.samwumed.org/our-networks/samwumed-pharmacy-list/
   5. Gems (lists organized by province; government employee healthcare provider): https://www.gems.gov.za/Healthcare-Providers/GEMS-Network-of-Healthcare-Providers/Primary-Network/Pharmacy

Confirming a pharmacy registration: https://pharmcouncil.co.za/Pharmacies_Overview

SA Spatial Data Portal: https://nspdr.dlrrd.gov.za/portal/home/

Census Data:

*You will need to register for an account with DataFirst in order to access Stats SA data.*

Ward-Level Data for 2022: https://www.statssa.gov.za/?p=18967
2020 Ward Shapes: https://dataportal-mdb-sa.opendata.arcgis.com/datasets/e0223a825ea2481fa72220ad3204276b/about
2022 Census Microdata: https://www.datafirst.uct.ac.za/dataportal/index.php/catalog/982
PennLibraries 2011 Census Data: https://guides.library.upenn.edu/EastViewCensusGIS/SouthAfrica2011CensusData

[1]: Work in Snowflake AI will take place in Python, and will utilize some SQL as well. A team member with experience in Python should be assigned the lead role in this task area in your project management plan.
[2]: https://www.oreilly.com/library/view/agile-data-science/9781491960103/ch01.html
[3]: https://www.parliament.gov.za/project-event-details/54
[4]: A review of this paper on unlicensed *online* SA pharmacies contains detail about pharmacy regulations and practices in SA, where illicit sales through unlicensed community pharmacies are believed to occur — https://pmc.ncbi.nlm.nih.gov/articles/PMC12242074/
[5]: https://cran.r-project.org/web/packages/googleway/index.html
[6]: https://cran.r-project.org/web/packages/ggmap/index.html
[7]: https://hub.worldpop.org/geodata/summary?id=49663&utm_source=chatgpt.com
[8]: https://golete.github.io/vacant-lots/
# Recovering area shapes from anonymous contact tracing data
### [Marino Miculan](http://users.dimi.uniud.it/~marino.miculan/wordpress/)

## Introduction
The actual COVID-19 pandemic has induced many governments to call for technological solutions for tracing contacts between people. [Dozens of applications](https://en.wikipedia.org/wiki/COVID-19_apps) have been introduced so far, basically boiling down to five main frameworks: PEPP-PT, Google/Apple Privacy Preserving Tracing Project (GA-PPTP), DP-3T, Blue Trace and TCN; a detailed comparison between these approaches is outside the scope of this project (see e.g. [here](https://www.cybersecurity360.it/nuove-minacce/app-di-contact-tracing-come-funzionano-rischi-di-sicurezza-e-soluzioni-di-mitigazione/) and [here](https://github.com/shankari/covid-19-tracing-projects)).
A common problem with all these approaches is user privacy. Ideally we would like to trace who has been in contact with an infected patient, without revealing their real positions and movements. This is even more important in centralized-based solutions (such as PEPP-PT), where tracing data is stored "in the cloud" or on servers run either by the Government or by some private institution.

To this end, several anonymization techniques are used

In this project we show how it is possible to extract topological structures from (not so) large datasets of anonymous contact tracing data. 

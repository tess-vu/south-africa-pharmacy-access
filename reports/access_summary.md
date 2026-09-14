**Pharmacy Accessibility Analysis: AI\_WALK & AI\_DRIVE**

Co-Authored By: Jill Kalman , Tess Vu, Alex Stauffer, Joey Cahill

University of Pennsylvania School of Design

**1. Score Methodology**

The AI score is a supply-demand ratio: **Rj = *Pharmacy Supply / Population within pharmacy catchment***

**AI = ?(*Rj within poly node catchment*)**

**KZN Walking Catchment: 3km Gauteng Walking Catchment: 2km**

**KZN Driving Catchment: 10km Gauteng Driving Catchment: 5km**

Supply assumed: **1 (KZN)** | **1.2 (Gauteng)**

Supply ratio between provinces was calculated using available hospital beds as a supply proxy. Hospital data from DAIR indicates

34,791 usable hospital beds in Gauteng, and 27,406 in KwaZulu-Natal ~ 6:5 ratio

**2. Summary Report**

Score band distribution by province

Distribution stats by province

Top 10 AI\_WALK

Top 10 AI\_WALK

Bottom 10 AI\_DRIVE

Bottom 10 AI\_DRIVE

Spatial Autocorrelation

EA\_TYPE by province with econ status

Racial Distribution by Province

Walk-to-Drive Correlation

Outlier Concentration

**3. Score Interpretation**

|  |  |
| --- | --- |
| Score | Meaning |
| 0 | No pharmacy reachable |
| 0 – 0.5 | Pharmacy desert |
| 0.5 – 1.0 | Underserved, could use improvement |
| 1.0 – 3.0 | Adequate, supply and demand at a healthy balance |
| 3.0 + | Well-served |
| 10+ | Overtly concentrated, area has 10x the supply needed to meet population demand |
| A score of 1 represents exact 1:1 ratio of supply and demand of an area. Supply perfectly matches demand. While adequate on paper, its not ideal in practice, as it sits in a space of precarity. Outside influences like rapid migration or supply chain break can weaken these scores swiftly. This is why a score above 1 is a more ideal representation of healthy access, as it allows cushion for unplanned events. | |

Table 1

**4. Distribution Summary**

|  |  |  |
| --- | --- | --- |
| Metric | Gauteng | KwaZulu-Natal |
| Total Areas | 20,850 | 17,530 |
| Mean Walk Score | 0.55 | 0.21 |
| Median Walk Score | 0.02 | 0.00 |
| Mean Drive Score | 0.50 | 0.23 |
| Median Drive Score | 0.06 | 0.00 |
| Patterns: *Median scores close or equal to 0 across all scores suggests an overwhelming skew of weak accessibility, while the average scores being much higher suggests a small fraction of areas holding the highest accessibility. Further, even at 1.2x supply, Gauteng accessibility scores are over double than KwaZulu Natal, suggesting supply alone is not weakening access, but lack of physical infrastructure for medicine in KZN.* | | |

Table 2

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Gauteng** |  | **KwaZulu-Natal** |  |
|  | **n** | **%** | **n** | **%** |
| **Walking Score (Ai\_walk)** |  |  |  |  |
| =0 | 9,853 | 47.3% | 11,544 | 65.9% |
| 0 – 0.5 | 6,511 | 31.2% | 4,070 | 23.2% |
| 0.5 – 1.0 | 1,584 | 7.6% | 781 | 4.5% |
| > 1.0 | 2,902 | 13.9% | 1,135 | 6.5% |
| **Driving Score(Ai\_drive)** |  |  |  |  |
| = 0 | 4,531 | 21.7% | 7,673 | 43.8% |
| 0 – 0.5 | 10,981 | 52.7% | 7,800 | 44.5% |
| 0.5 – 1.0 | 1,914 | 9.2% | 923 | 5.3% |
| > 1.0 | 3,424 | 16.4% | 1,134 | 6.5% |
| *Patterns: Gauteng has overall better access to pharmacies via walking or driving. Although almost one half have non-existent walking access to medicines (Ai\_walk=0), 78% of Gauteng has access to medicines within 5km (Ai\_drive>0). The same can be said for KZN, but to a lesser extent. With 65% having extremely limited access to medicines via walking (Ai\_walk=0), only 56% have some level of driving access within 10km (Ai\_drive>0). About a one quarter of Gauteng lives in a medicine-rich area whereas only 11% of KwaZulu Natal has the same access. (Ai\_walk and Ai\_drive>0.5). Once again, even at only 1.2x supply, Gauteng outperforms KZN by over twofold in medicine-rich areas and access to medicines. This suggests that KZN lacks medical infrastructure to serve populations, even in the most resourceful or developed areas. Its also important to note that accessibility within both provinces is NOT linear, seeing that distribution dips at moderate access (0.5-1), and then turns up at oversupply (>1).* | | | | |

Table 3

**(bivariate color map)**

**GAUTENG**

**5. Top 10 — AI\_WALK (Highest Walking Access)**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EA Code | Sub-Place | Municipality | Ai\_walk | EA Type | Econ. Status | Pop 2011 | Pop 2023 Est. |
| 79913191 | Tshwane NU | City of Tshwane | 54.47 | Farms | Wealthy | 770 | 242 |
| 79911565 | Keinfontein SH | City of Tshwane | 23.45 | Suburbs | Wealthy | 121 | 102 |
| 79811482 | Oakdene | City of Johannesburg | 21.28 | Suburbs | Wealthy | 399 | 111 |
| 79910793 | Raslou AH | City of Tshwane | 19.86 | Smallholdings | Wealthy | 414 | 205 |
| 79910810 | Heuwelsig Estate | City of Tshwane | 19.79 | Suburbs | Wealthy | 338 | 279 |
| 79815868 | Tinswalo Estate | City of Johannesburg | 18.55 | Suburbs | Wealthy | 527 | 350 |
| 79815554 | Woodmead | City of Johannesburg | 16.04 | Commercial | Non\_Residential | 730 | 202 |
| 79815135 | Greenstone Park | City of Johannesburg | 15.07 | Commercial | Non\_Residential | 340 | 185 |
| 79815860 | Woodmead | City of Johannesburg | 14.42 | Commercial | Non\_Residential | 730 | 239 |
| 79816455 | Kyalami Estate | City of Johannesburg | 12.33 | Suburbs | Wealthy | 743 | 725 |

Table 4

**Pattern:** Concentrated in wealthy areas, with declining populations.

![](data:image/png;base64...)

Figure 1

**6. Bottom 10 — AI\_WALK**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EA Code | Sub-Place | Municipality | Ai\_walk | EA Type | Econ. Status | Pop 2011 | Pop 2023 Est. |
| 79910985 | Cullinan SP | City of Tshwane | 0 | Collective living | Non\_Wealthy | 2,809 | **9,970** |
| 76310653 | Rietfontein AH | Mogale City | 0 | Informal residential | Non\_Wealthy | 3,036 | **7,336** |
| 79911566 | Donkerhoek SH | City of Tshwane | 0 | Smallholdings | Wealthy | 2,971 | **6,220** |
| 79914587 | Winterveld Ext 1 | City of Tshwane | 0 | Informal residential | Non\_Wealthy | 2,592 | **6,106** |
| 79816419 | Zevenfontein Pipeline | City of Johannesburg | 0 | Vacant | Non\_Residential | 3,759 | **6,071** |
| 79713250 | Modderfontein Deep Levels | Ekurhuleni | 0 | Collective living | Non\_Wealthy | 4,785 | **5,784** |
| 76110154 | Balmoral Estate | Midvaal | 0 | Suburbs | Wealthy | 769 | **5,174** |
| 76110153 | De Deur Estate | Midvaal | 0 | Suburbs | Wealthy | 704 | **5,038** |
| 79913634 | Medunsa | City of Tshwane | 0 | Township | Non\_Wealthy | 2,506 | **4,537** |
| 76110184 | De Deur Estate | Midvaal | 0 | Smallholdings | Wealthy | 604 | **3,851** |

Table 5

**Pattern: Concentrated in non-wealthy Townships, or otherwise car-dependent areas.** ![](data:image/png;base64...)

Figure 2

**7. Top 10 — AI\_DRIVE (Highest Driving Access)**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EA Code | Sub-Place | Municipality | Ai\_drive | EA Type | Econ. Status | Pop 2011 | Pop 2023 Est. |
| 79811140 | Meredale | City of Johannesburg | 84.96 | Suburbs | Wealthy | 613 | 440 |
| 79913191 | Tshwane NU | City of Tshwane | 59.42 | Farms | Wealthy | 770 | 242 |
| 79811072 | Meredale | City of Johannesburg | 43.76 | Suburbs | Wealthy | 624 | 366 |
| 79811107 | Mondeor | City of Johannesburg | 42.65 | Suburbs | Wealthy | 472 | 308 |
| 79811139 | Mondeor | City of Johannesburg | 33.33 | Suburbs | Wealthy | 386 | 232 |
| 79811102 | Meredale | City of Johannesburg | 32.52 | Suburbs | Wealthy | 379 | 247 |
| 79811060 | Meredale | City of Johannesburg | 31.15 | Suburbs | Wealthy | 543 | 307 |
| 79811105 | Mondeor | City of Johannesburg | 29.00 | Suburbs | Wealthy | 501 | 362 |
| 79811103 | Mondeor | City of Johannesburg | 29.71 | Suburbs | Wealthy | 728 | 402 |
| 79713640 | Saint Andrews | Ekurhuleni | 29.57 | Collective living | Non\_Wealthy | 367 | 255 |

Table 6

**Patternfom**: Wealthy residentials with declining populations, concentrated in Johannesburg. Access is more than plentiful, with an average of about 50x oversupply. This suggests supply is clustered among these neighboring areas.

![](data:image/png;base64...)

Figure 3

**8. Bottom 10 — AI\_DRIVE**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EA Code | Sub-Place | Municipality | Ai\_drive | EA Type | Econ. Status | Pop 2011 | Pop 2023 Est. |
| 76310653 | Rietfontein AH | Mogale City | 0 | Informal residential | Non\_Wealthy | 3,036 | **7,336** |
| 79911566 | Donkerhoek SH | City of Tshwane | 0 | Smallholdings | Wealthy | 2,971 | **6,220** |
| 79914587 | Winterveld Ext 1 | City of Tshwane | 0 | Informal residential | Non\_Wealthy | 2,592 | **6,106** |
| 76310630 | Vlakplaas AH | Mogale City | 0 | Informal residential | Non\_Wealthy | 1,572 | **3,739** |
| 76410007 | Randfontein SP1 | Randfontein | 0 | Suburbs | Wealthy | 2,236 | **3,433** |
| 79914588 | Winterveld Ext 1 | City of Tshwane | 0 | Informal residential | Non\_Wealthy | 1,695 | **3,384** |
| 76310565 | Bagale | Mogale City | 0 | Suburbs | Wealthy | 1,191 | **3,241** |
| 76610048 | Kokosi Ext 1 | Merafong City | 0 | Township | Non\_Wealthy | 822 | **3,166** |
| 76610029 | Kokosi Ext 1 | Merafong City | 0 | Township | Non\_Wealthy | 795 | **3,090** |
| 79910975 | Rayton SH | City of Tshwane | 0 | Smallholdings | Wealthy | 1,753 | **2,952** |

Table 7

**Pattern:** Entirely in the City of Tshwane, generally non-wealthy, growing populations. Scores could imply poor road connectivity or minimal demand.

![](data:image/png;base64...)

Figure 4

**KwaZulu-Natal**

1. **Top 10 — AI\_WALK (Highest Walking Access)**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EA Code | Sub-Place | Municipality | Ai\_walk | EA Type | Econ. Status | Pop 2011 | Pop 2023 Est. |
| 50610306 | Shelly Beach SP | Hibiscus Coast | 14.88 | Commercial | Non\_Residential | 546 | 320 |
| 59914770 | Umhlanga Ridge | Ethekwini | 12.41 | Suburbs | Wealthy | 479 | 220 |
| 59914772 | Umhlanga Ridge | Ethekwini | 12.38 | Suburbs | Wealthy | 479 | 208 |
| 59914773 | Umhlanga Ridge | Ethekwini | 12.38 | Suburbs | Wealthy | 479 | 198 |
| 59914769 | Umhlanga Ridge | Ethekwini | 12.29 | Suburbs | Wealthy | 371 | 139 |
| 59913641 | Umhlanga Ridge | Ethekwini | 12.03 | Suburbs | Wealthy | 623 | 235 |
| 59914846 | Umhlanga Ridge | Ethekwini | 11.99 | Suburbs | Wealthy | 307 | 107 |
| 59914804 | Umhlanga Ridge | Ethekwini | 11.78 | Suburbs | Wealthy | 479 | 195 |
| 59914767 | Umhlanga Ridge | Ethekwini | 11.15 | Collective living | Non\_Wealthy | 373 | 136 |
| 54210224 | Bhacane SP | Nkandla | 11.14 | Traditional residential | Non\_Wealthy | 498 | 269 |

Table 8

**Pattern**: Generally wealthy, shrinking areas in eThekwini. Pharmacy points hidden to preserve spatial details.

![](data:image/png;base64...)

Figure 5

1. **Bottom 10 — AI\_WALK**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EA Code | Sub-Place | Municipality | Ai\_walk | EA Type | Econ. Status | Pop 2011 | Pop 2023 Est. |
| 52910145 | Abaqulusi NU | Abaqulusi | 0 | Traditional residential | Non\_Wealthy | 4,715 | **5,958** |
| 52910137 | Abaqulusi NU | Abaqulusi | 0 | Traditional residential | Non\_Wealthy | 3,025 | **3,559** |
| 59210304 | Thembeni SP | KwaDukuza | 0 | Informal residential | Non\_Wealthy | 1,377 | **3,367** |
| 59210116 | Njekane SP | KwaDukuza | 0 | Informal residential | Non\_Wealthy | 1,293 | **3,358** |
| 58610076 | Duku | Mtubatuba | 0 | Traditional residential | Non\_Wealthy | 1,101 | **3,357** |
| 59910287 | Ensimbini | Ethekwini | 0 | Traditional residential | Non\_Wealthy | 1,534 | **3,151** |
| 52910134 | Abaqulusi NU | Abaqulusi | 0 | Traditional residential | Non\_Wealthy | 2,126 | **3,124** |
| 57910165 | Mkwakweni SP | Uphongolo | 0 | Traditional residential | Non\_Wealthy | 1,553 | **3,123** |
| 58710004 | Ntshingimpisi SP | Mfolozi | 0 | Traditional residential | Non\_Wealthy | 1,523 | **3,025** |
| 50610224 | Mdlanzi SP | Hibiscus Coast | 0 | Traditional residential | Non\_Wealthy | 1,876 | **3,018** |

Table 9

**Pattern**: Non-wealthy traditional residentials with growing populations. Pharmacy points hidden to preserve spatial details.

![](data:image/png;base64...)

Figure 6

**11. Top 10 — AI\_DRIVE (Highest Driving Access)**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EA Code | Sub-Place | Municipality | Ai\_drive | EA Type | Econ. Status | Pop 2011 | Pop 2023 Est. |
| 52410573 | Newcastle NU | Newcastle | 33.72 | Farms | Wealthy | 502 | 178 |
| 56610488 | Pietermaritzburg SP | The Msunduzi | 16.73 | Suburbs | Wealthy | 634 | 611 |
| 59914461 | Cato Ridge SP | Ethekwini | 15.23 | Suburbs | Wealthy | 383 | 432 |
| 53810164 | Mpangele | uMhlathuze | 11.78 | Commercial | Non\_Residential | 300 | 273 |
| 59914769 | Umhlanga Ridge | Ethekwini | 11.44 | Suburbs | Wealthy | 371 | 139 |
| 59914770 | Umhlanga Ridge | Ethekwini | 11.41 | Suburbs | Wealthy | 479 | 220 |
| 56610485 | Pietermaritzburg SP | The Msunduzi | 11.27 | Suburbs | Wealthy | 456 | 426 |
| 59914804 | Umhlanga Ridge | Ethekwini | 10.79 | Suburbs | Wealthy | 479 | 195 |
| 59914767 | Umhlanga Ridge | Ethekwini | 10.64 | Collective living | Non\_Wealthy | 373 | 136 |
| 59914773 | Umhlanga Ridge | Ethekwini | 10.47 | Suburbs | Wealthy | 479 | 198 |

Table 10

**Pattern**: Wealthy, shrinking areas. Car-dependence and the road infrastructure to match.

![](data:image/png;base64...)

Figure 7

**12. Bottom 10 — AI\_DRIVE**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EA Code | Sub-Place | Municipality | Ai\_drive | EA Type | Econ. Status | Pop 2011 | Pop 2023 Est. |
| 52910145 | Abaqulusi NU | Abaqulusi | 0 | Traditional residential | Non\_Wealthy | 4,715 | **5,958** |
| 52910137 | Abaqulusi NU | Abaqulusi | 0 | Traditional residential | Non\_Wealthy | 3,025 | **3,559** |
| 59210304 | Thembeni SP | KwaDukuza | 0 | Informal residential | Non\_Wealthy | 1,377 | **3,367** |
| 58610076 | Duku | Mtubatuba | 0 | Traditional residential | Non\_Wealthy | 1,101 | **3,357** |
| 52910134 | Abaqulusi NU | Abaqulusi | 0 | Traditional residential | Non\_Wealthy | 2,126 | **3,124** |
| 57910165 | Mkwakweni SP | Uphongolo | 0 | Traditional residential | Non\_Wealthy | 1,553 | **3,123** |
| 57610118 | Ngubevu SP1 | Msinga | 0 | Traditional residential | Non\_Wealthy | 1,878 | **2,914** |
| 59210227 | Njekane SP | KwaDukuza | 0 | Informal residential | Non\_Wealthy | 1,265 | **2,672** |
| 59910273 | Madundube SP | Ethekwini | 0 | Traditional residential | Non\_Wealthy | 1,563 | **2,645** |
| 57610147 | Mazabeko SP | Msinga | 0 | Traditional residential | Non\_Wealthy | 1,394 | **2,644** |

Table 11

**Pattern:** Non-wealthy , traditional residentials with growing populations.

![](data:image/png;base64...)

Figure 8

1. ![<Figure size 1600x600 with 2 Axes>](data:image/png;base64...)**Spatial Autocorrelation**

Figure 9

|  |  |  |  |
| --- | --- | --- | --- |
| Variable | Moran’s I | p-value | n areas significant |
| Ai\_walk | 0.64 | 0.005\*\*\* | 3733 (12.1%) |
| Ai\_drive | 0.70 | 0.005\*\*\* | 3866 (12.5%) |

Table 12

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| HL Clusters- High Walk Scores Surrounded by Low Walk Scores | | | | | | |
| EA\_CODE | **Sub-place** | **Municipality** | **Province** | **AI\_WALK** | **EA Type** | **Econ Status** |
| 79816517 | Savannah Hills | City of Johannesburg | Gauteng | 3.4419 | Suburbs | Wealthy |
| 58910095 | Izingwenya A SP | uMlalazi | KwaZulu-Natal | 1.8432 | Traditional residential | Non\_Wealthy |
| 79815140 | Linbro Park AH | City of Johannesburg | Gauteng | 4.7287 | Smallholdings | Wealthy |
| 59914461 | Cato Ridge SP | Ethekwini | KwaZulu-Natal | 2.2782 | Suburbs | Wealthy |
| 79811087 | Ormonde View | City of Johannesburg | Gauteng | 4.0100 | Suburbs | Wealthy |
| 54210101 | Malunga SP | Nkandla | KwaZulu-Natal | 2.3989 | Traditional residential | Non\_Wealthy |
| 58310044 | Ubombo SP | Jozini | KwaZulu-Natal | 1.6832 | Traditional residential | Non\_Wealthy |
| 57910001 | Uphongolo NU | Uphongolo | KwaZulu-Natal | 1.6416 | Traditional residential | Non\_Wealthy |
| 54210224 | Bhacane SP | Nkandla | KwaZulu-Natal | 11.1386 | Traditional residential | Non\_Wealthy |
| 79910649 | Zwavelpoort AH | City of Tshwane | Gauteng | 6.7502 | Smallholdings | Wealthy |
| 79815135 | Greenstone Park | City of Johannesburg | Gauteng | 15.0720 | Commercial | Non\_Residential |

Table 13

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| HL Clusters- High Drive Scores Surrounded by Low Drive Scores | | | | | | |
| EA\_CODE | **Sub-place** | **Municipality** | **Province** | **AI\_DRIVE** | **EA Type** | **Econ Status** |
| 79914869 | Winterveld AH | City of Tshwane | Gauteng | 6.1568 | Township | Non\_Wealthy |
| 54210101 | Malunga SP | Nkandla | KwaZulu-Natal | 4.1879 | Traditional residential | Non\_Wealthy |
| 58910095 | Izingwenya A SP | uMlalazi | KwaZulu-Natal | 1.4429 | Traditional residential | Non\_Wealthy |
| 58310044 | Ubombo SP | Jozini | KwaZulu-Natal | 2.3989 | Traditional residential | Non\_Wealthy |
| 57910001 | Uphongolo NU | Uphongolo | KwaZulu-Natal | 1.3968 | Traditional residential | Non\_Wealthy |
| 54210224 | Bhacane SP | Nkandla | KwaZulu-Natal | 1.8485 | Traditional residential | Non\_Wealthy |
| 57910024 | Uphongolo NU | Uphongolo | KwaZulu-Natal | 1.2485 | Traditional residential | Non\_Wealthy |
| 54210100 | Malunga SP | Nkandla | KwaZulu-Natal | 2.9762 | Traditional residential | Non\_Wealthy |
| 58310011 | Ubombo SP | Jozini | KwaZulu-Natal | 1.5678 | Traditional residential | Non\_Wealthy |

Table 14

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| LH Clusters- Low Walk Scores Surrounded by High Walk Scores | | | | | | |
| EA\_CODE | **Sub-place** | **Municipality** | **Province** | **AI\_WALK** | **EA Type** | **Econ Status** |
| 76310528 | Rietvei AH | Mogale City | Gauteng | 0.0000 | Smallholdings | Wealthy |
| 79910419 | Spruit | City of Tshwane | Gauteng | 0.0000 | Informal residential | Non\_Wealthy |
| 79910875 | Spruit | City of Tshwane | Gauteng | 0.0000 | Informal residential | Non\_Wealthy |
| 79910881 | Spruit | City of Tshwane | Gauteng | 0.0000 | Informal residential | Non\_Wealthy |
| 79913192 | Sokhulumi | City of Tshwane | Gauteng | 0.0000 | Suburbs | Wealthy |
| 57910077 | Simdlangenstha | Uphongolo | KwaZulu-Natal | 0.0000 | Suburbs | Wealthy |
| 57910078 | Simdlangenstha | Uphongolo | KwaZulu-Natal | 0.0000 | Suburbs | Wealthy |
| 79910877 | Spruit | City of Tshwane | Gauteng | 0.0000 | Informal residential | Non\_Wealthy |
| 79913193 | Sokhulumi | City of Tshwane | Gauteng | 0.0000 | Suburbs | Wealthy |
| …  Total list has 96 clusters | | | | | | |

Table 15

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| LH Clusters- Low Drive Scores Surrounded by High Drive Scores (total =36) | | | | | | |
| EA\_CODE | **Sub-place** | **Municipality** | **Province** | **AI\_DRIVE** | **EA Type** | **Econ Status** |
| 79815884 | Leeuwkop Prison | City of Johannesburg | Gauteng | 0.0097 | Collective living | Non\_Wealthy |
| 52410572 | Newcastle NU | Newcastle | KwaZulu-Natal | 0.0000 | Farms | Wealthy |
| 79913192 | Sokhulumi | City of Tshwane | Gauteng | 0.0000 | Suburbs | Wealthy |
| 57910077 | Simdlangenstha | Uphongolo | KwaZulu-Natal | 0.0204 | Suburbs | Wealthy |
| 57910078 | Simdlangenstha | Uphongolo | KwaZulu-Natal | 0.0090 | Suburbs | Wealthy |
| 79913193 | Sokhulumi | City of Tshwane | Gauteng | 0.0000 | Suburbs | Wealthy |
| 51410282 | Ladysmith Central | Emnambithi/Ladysmith | KwaZulu-Natal | 0.0000 | Suburbs | Wealthy |
| 79910974 | Rayton SH | City of Tshwane | Gauteng | 0.0000 | Smallholdings | Wealthy |
| …  Total list has 36 clusters | | | | | | |

Table 16

**Micro-Patterns**

**14. EA Type × Province × Econ Status**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **EA Type** | **Econ Status** | **Areas** | **Avg Walk** | **Avg Drive** | **Pop 2011** | **Pop 2023 Est** |
| Collective living quarters | Non\_Wealthy | 430 | 0.8026 | 0.9862 | 312,652 | 263,080 |
| Commercial | Non\_Residential | 471 | 1.9371 | 1.8178 | 298,286 | 212,927 |
| Suburbs | Wealthy | 11,338 | 0.8002 | 0.9124 | 7,119,109 | 6,876,703 |
| Farms | Wealthy | 514 | 0.1081 | 0.2101 | 377,978 | 204,258 |
| Industrial | Non\_Residential | 331 | 0.4944 | 0.6088 | 153,540 | 115,388 |
| Parks and recreation | Non\_Residential | 29 | 0.1937 | 0.3347 | 14,564 | 8,561 |
| Smallholdings | Wealthy | 502 | 0.2145 | 0.2294 | 237,497 | 195,328 |
| Vacant | Non\_Residential | 345 | 0.1749 | 0.2075 | 220,799 | 220,260 |
| Informal residential | Non\_Wealthy | 2,482 | 0.0581 | 0.0765 | 1,643,563 | 2,214,360 |
| Township | Non\_Wealthy | 8,460 | 0.0970 | 0.1042 | 6,790,017 | 8,761,864 |
| Traditional residential | Non\_Wealthy | 6,227 | 0.0109 | 0.0127 | 4,594,750 | 5,315,590 |
| Pattern:  Non-wealthy areas dominate the lowest accessibility scores. Although non-wealthy and non-residential make up the top three, the total population is minimal and are unburdened by high demand. | | | | | | |

Table 17

**15. Province x Race**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Province | Racial Majority | Avg Walk | Avg Drive | N |
| Gauteng | Mixed | 1.50 | 1.05 | 3,309 |
| Note: Racial distribution based on 2011 SAL level counts. | 50%+ White | 1.08 | 1.10 | 4,737 |
| 50%+ Indian | 0.56 | 0.51 | 241 |
| 90%+ Black African | 0.09 | 0.11 | 10,904 |
| KZN | 50%+ White | 1.03 | 1.00 | 1,181 |
|  | Mixed | 0.64 | 0.69 | 2,166 |
| 50%+ Indian | 0.43 | 0.49 | 1,201 |
| 90%+ Black African | 0.04 | 0.05 | 11,713 |
| Pattern: Black Africans are overwhelmingly underserved and neglected. In KZN, white majority areas are the least abundant, but the most well-served. White majority areas have between 10-25x more access than black areas. | | | | |

Table 18

**16.  Walk-Drive Correlation**

|  |  |
| --- | --- |
| Province | Walk-Drive Correlation |
| KZN | **0.83** (strong) |
| Gauteng | **0.25** (weak) |
| Pattern: In KZN, walk and drive scores move together: if you can't walk to it, you probably can't drive either (remoteness). In Gauteng, they're largely independent: there are many SALs with good drive access but poor walk access (car-dependent sprawl), or high walk but low drive (dense, commercial cores). | |

Table 19

**17. Outlier Concentration**

|  |  |  |  |
| --- | --- | --- | --- |
| Province | Top 20% of EAs | % of Total Walk Score | % of Total Drive Score |
| Gauteng | 3,910 EAs | **89.8%** | 73.6% |
| KZN | 3,276 EAs | **96.4%** | 90.3% |
| Pattern: Accessibility is hyper-concentrated. The top 20% scoring SALs possesses over 70% of the access to medicines. | | | |

Table 20

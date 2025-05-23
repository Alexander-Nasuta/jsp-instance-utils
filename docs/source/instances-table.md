# Table of Instances

This section is based on the GitHub Repo [jsspInstancesAndResults](https://github.com/thomasWeise/jsspInstancesAndResults) by Thomas Weise.
The linked Repo is essentially a equivalent to this one, but for the programming language R.

The rows have the following meaning:

- `id` the unique identifier of the instance, as used in the literature (unsolved instances are marked in **bold**)
- `ref` the reference to the publication where the instance was first mentioned/created
- `jobs` the number of jobs in the instance
- `machines` the number of machines in the instance
- `lb` the lower bound for the makespan of any solution for the instance
- `lb ref` the reference to the earliest publication (in this survey) that mentioned this lower bound
- `bks` the makespan of the best-known solution (in terms of the makespan), based on this survey
- `bks ref` the reference(s) to the earliest publication(s) in this survey that mentioned the bks
- `t(bks) in s` the fastest time reported (in seconds), by any of the references in the study, for reaching `bks`
- `t(bks) ref` the reference(s) of the publications reporting `t(bks)`

Please, please take the column `t(bks)` with many grains of salt.
First, we just report the time, regardless of which computer was used to obtain the result or even whether parallelism was applied or not.
Second sometimes a minimum time to reach the best result of the run is given in a paper, sometimes we just have the maximum runtime used, sometimes we have a buget &ndash; and some publications do not report a runtime at all.
Hence, our data here is very incomplete and unreliable and for some instances, we may not have any proper runtime value at all
Therefore, this column is not to be understood as a normative a reliable information, more as a very rough guide regarding where we are standing right now.
And, needless to say, it is only populated with the information extracted from the papers used in this study, so it may not even be representative.

|id|ref|jobs|machines|lb|lb ref|bks|bks ref|t(bks) in s|t(bks) ref|
|---:|:---:|---:|---:|---:|:---:|---:|:---:|---:|:---:|
|abz5|<a href="#ABZ">ABZ</a>|10|10|1234|<a href="#AC">AC</a>|1234|<a href="#AC">AC</a>|0.04|<a href="#AZ">AZ</a>|
|abz6|<a href="#ABZ">ABZ</a>|10|10|943|<a href="#AC">AC</a>|943|<a href="#AC">AC</a>|0.03|<a href="#AZ">AZ</a>|
|abz7|<a href="#ABZ">ABZ</a>|20|15|656|<a href="#M">M</a>|656|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|**abz8**|<a href="#ABZ">ABZ</a>|20|15|**648**|<a href="#VLS">VLS</a>|**665**|<a href="#H">H</a>|**1000**|<a href="#H">H</a>|
|abz9|<a href="#ABZ">ABZ</a>|20|15|678|<a href="#KNF">KNF</a>|678|<a href="#ZSR">ZSR</a>|3.25|<a href="#AZ">AZ</a>|
|**dmu01**|<a href="#DMU1">DMU1</a>|20|15|**2501**|<a href="#BB">BB</a>|**2563**|<a href="#H">H</a>|**332.87**|<a href="#PLC">PLC</a>|
|**dmu02**|<a href="#DMU1">DMU1</a>|20|15|**2651**|<a href="#BB">BB</a>|**2706**|<a href="#H">H</a>|**179.24**|<a href="#PLC">PLC</a>|
|dmu03|<a href="#DMU1">DMU1</a>|20|15|2731|<a href="#BB">BB</a>|2731|<a href="#H">H</a>|388.59|<a href="#PLC">PLC</a>|
|**dmu04**|<a href="#DMU1">DMU1</a>|20|15|**2601**|<a href="#BB">BB</a>|**2669**|<a href="#H">H</a>|**96.54**|<a href="#PLC">PLC</a>|
|dmu05|<a href="#DMU1">DMU1</a>|20|15|2749|<a href="#BB">BB</a>|2749|<a href="#H">H</a>|303|<a href="#PLC">PLC</a>|
|**dmu06**|<a href="#DMU1">DMU1</a>|20|20|**3042**|<a href="#vH2">vH2</a>|**3244**|<a href="#PSV">PSV</a>|**10000**|<a href="#PSV">PSV</a>|
|**dmu07**|<a href="#DMU1">DMU1</a>|20|20|**2828**|<a href="#vH2">vH2</a>|**3046**|<a href="#PSV">PSV</a>|**360.58**|<a href="#PLC">PLC</a>|
|**dmu08**|<a href="#DMU1">DMU1</a>|20|20|**3051**|<a href="#GL">GL</a>|**3188**|<a href="#PSV">PSV</a>|**295.81**|<a href="#PLC">PLC</a>|
|**dmu09**|<a href="#DMU1">DMU1</a>|20|20|**2956**|<a href="#GL">GL</a>|**3092**|<a href="#H">H</a>|**500**|<a href="#H">H</a>|
|**dmu10**|<a href="#DMU1">DMU1</a>|20|20|**2858**|<a href="#GL">GL</a>|**2984**|<a href="#PSV">PSV</a>|**10000**|<a href="#PSV">PSV</a>|
|**dmu11**|<a href="#DMU1">DMU1</a>|30|15|**3395**|<a href="#DMU">DMU</a>|**3430**|<a href="#PLC">PLC</a>|**1496.85**|<a href="#PLC">PLC</a>|
|**dmu12**|<a href="#DMU1">DMU1</a>|30|15|**3481**|<a href="#DMU">DMU</a>|**3492**|<a href="#SS">SS</a>|||
|dmu13|<a href="#DMU1">DMU1</a>|30|15|3681|<a href="#DMU">DMU</a>|3681|<a href="#GR">GR</a>|622.13|<a href="#PLC">PLC</a>|
|dmu14|<a href="#DMU1">DMU1</a>|30|15|3394|<a href="#DMU">DMU</a>|3394|<a href="#H">H</a>|3.02|<a href="#PLC">PLC</a>|
|dmu15|<a href="#DMU1">DMU1</a>|30|15|3343|<a href="#GL">GL</a>|3343|<a href="#H">H</a>|1.77|<a href="#PLC">PLC</a>|
|**dmu16**|<a href="#DMU1">DMU1</a>|30|20|**3734**|<a href="#GL">GL</a>|**3751**|<a href="#GR">GR</a>|||
|**dmu17**|<a href="#DMU1">DMU1</a>|30|20|**3709**|<a href="#GL">GL</a>|**3814**|<a href="#SS">SS</a>|||
|dmu18|<a href="#DMU1">DMU1</a>|30|20|3844|<a href="#DMU">DMU</a>|3844|<a href="#GR">GR</a>|3787.4|<a href="#PLC">PLC</a>|
|**dmu19**|<a href="#DMU1">DMU1</a>|30|20|**3672**|<a href="#vH2">vH2</a>|**3765**|<a href="#SS">SS</a>|||
|**dmu20**|<a href="#DMU1">DMU1</a>|30|20|**3604**|<a href="#DMU">DMU</a>|**3710**|<a href="#PLC">PLC</a>|**701.29**|<a href="#PLC">PLC</a>|
|dmu21|<a href="#DMU1">DMU1</a>|40|15|4380|<a href="#DMU">DMU</a>|4380|<a href="#H">H</a>|0.69|<a href="#PLC">PLC</a>|
|dmu22|<a href="#DMU1">DMU1</a>|40|15|4725|<a href="#DMU">DMU</a>|4725|<a href="#H">H</a>|1.48|<a href="#PLC">PLC</a>|
|dmu23|<a href="#DMU1">DMU1</a>|40|15|4668|<a href="#DMU">DMU</a>|4668|<a href="#H">H</a>|1.3|<a href="#PLC">PLC</a>|
|dmu24|<a href="#DMU1">DMU1</a>|40|15|4648|<a href="#DMU">DMU</a>|4648|<a href="#H">H</a>|0.75|<a href="#PLC">PLC</a>|
|dmu25|<a href="#DMU1">DMU1</a>|40|15|4164|<a href="#DMU">DMU</a>|4164|<a href="#H">H</a>|0.6|<a href="#PLC">PLC</a>|
|dmu26|<a href="#DMU1">DMU1</a>|40|20|4647|<a href="#DMU">DMU</a>|4647|<a href="#GR">GR</a>|1631.43|<a href="#PLC">PLC</a>|
|dmu27|<a href="#DMU1">DMU1</a>|40|20|4848|<a href="#DMU">DMU</a>|4848|<a href="#H">H</a>|12.16|<a href="#PLC">PLC</a>|
|dmu28|<a href="#DMU1">DMU1</a>|40|20|4692|<a href="#DMU">DMU</a>|4692|<a href="#H">H</a>|17.68|<a href="#PLC">PLC</a>|
|dmu29|<a href="#DMU1">DMU1</a>|40|20|4691|<a href="#DMU">DMU</a>|4691|<a href="#H">H</a>|63.49|<a href="#PLC">PLC</a>|
|dmu30|<a href="#DMU1">DMU1</a>|40|20|4732|<a href="#DMU">DMU</a>|4732|<a href="#H">H</a>|123|<a href="#PLC">PLC</a>|
|dmu31|<a href="#DMU1">DMU1</a>|50|15|5640|<a href="#DMU">DMU</a>|5640|<a href="#H">H</a>|0.84|<a href="#PLC">PLC</a>|
|dmu32|<a href="#DMU1">DMU1</a>|50|15|5927|<a href="#DMU">DMU</a>|5927|<a href="#H">H</a>|0.62|<a href="#PLC">PLC</a>|
|dmu33|<a href="#DMU1">DMU1</a>|50|15|5728|<a href="#DMU">DMU</a>|5728|<a href="#H">H</a>|0.43|<a href="#PLC">PLC</a>|
|dmu34|<a href="#DMU1">DMU1</a>|50|15|5385|<a href="#DMU">DMU</a>|5385|<a href="#H">H</a>|2.22|<a href="#PLC">PLC</a>|
|dmu35|<a href="#DMU1">DMU1</a>|50|15|5635|<a href="#DMU">DMU</a>|5635|<a href="#H">H</a>|0.71|<a href="#PLC">PLC</a>|
|dmu36|<a href="#DMU1">DMU1</a>|50|20|5621|<a href="#DMU">DMU</a>|5621|<a href="#H">H</a>|7.83|<a href="#PLC">PLC</a>|
|dmu37|<a href="#DMU1">DMU1</a>|50|20|5851|<a href="#DMU">DMU</a>|5851|<a href="#H">H</a>|11.38|<a href="#PLC">PLC</a>|
|dmu38|<a href="#DMU1">DMU1</a>|50|20|5713|<a href="#DMU">DMU</a>|5713|<a href="#H">H</a>|10.66|<a href="#PLC">PLC</a>|
|dmu39|<a href="#DMU1">DMU1</a>|50|20|5747|<a href="#DMU">DMU</a>|5747|<a href="#H">H</a>|2.02|<a href="#PLC">PLC</a>|
|dmu40|<a href="#DMU1">DMU1</a>|50|20|5577|<a href="#DMU">DMU</a>|5577|<a href="#H">H</a>|4.91|<a href="#PLC">PLC</a>|
|**dmu41**|<a href="#DMU1">DMU1</a>|20|15|**3007**|<a href="#GL">GL</a>|**3248**|<a href="#PLC">PLC</a>|**417.84**|<a href="#PLC">PLC</a>|
|**dmu42**|<a href="#DMU1">DMU1</a>|20|15|**3224**|<a href="#vH2">vH2</a>|**3390**|<a href="#PLC">PLC</a>|**448.95**|<a href="#PLC">PLC</a>|
|**dmu43**|<a href="#DMU1">DMU1</a>|20|15|**3292**|<a href="#GL">GL</a>|**3441**|<a href="#GR">GR</a>|**399.33**|<a href="#PLC">PLC</a>|
|**dmu44**|<a href="#DMU1">DMU1</a>|20|15|**3299**|<a href="#vH2">vH2</a>|**3475**|<a href="#SS">SS</a>|||
|**dmu45**|<a href="#DMU1">DMU1</a>|20|15|**3039**|<a href="#vH2">vH2</a>|**3272**|<a href="#GR">GR</a>|||
|**dmu46**|<a href="#DMU1">DMU1</a>|20|20|**3575**|<a href="#GL">GL</a>|**4035**|<a href="#GR">GR</a>|**984.86**|<a href="#PLC">PLC</a>|
|**dmu47**|<a href="#DMU1">DMU1</a>|20|20|**3522**|<a href="#GL">GL</a>|**3939**|<a href="#GR">GR</a>|||
|**dmu48**|<a href="#DMU1">DMU1</a>|20|20|**3447**|<a href="#GL">GL</a>|**3763**|<a href="#SS">SS</a>|||
|**dmu49**|<a href="#DMU1">DMU1</a>|20|20|**3403**|<a href="#GL">GL</a>|**3710**|<a href="#PLC">PLC</a>|**633.84**|<a href="#PLC">PLC</a>|
|**dmu50**|<a href="#DMU1">DMU1</a>|20|20|**3496**|<a href="#GL">GL</a>|**3729**|<a href="#PLC">PLC</a>|**609.62**|<a href="#PLC">PLC</a>|
|**dmu51**|<a href="#DMU1">DMU1</a>|30|15|**3954**|<a href="#vH2">vH2</a>|**4156**|<a href="#SS">SS</a>|||
|**dmu52**|<a href="#DMU1">DMU1</a>|30|15|**4094**|<a href="#vH2">vH2</a>|**4311**|<a href="#PLC">PLC</a>|**2232.6**|<a href="#PLC">PLC</a>|
|**dmu53**|<a href="#DMU1">DMU1</a>|30|15|**4141**|<a href="#GL">GL</a>|**4390**|<a href="#SS">SS</a>|||
|**dmu54**|<a href="#DMU1">DMU1</a>|30|15|**4202**|<a href="#GL">GL</a>|**4362**|<a href="#SS">SS</a>|||
|**dmu55**|<a href="#DMU1">DMU1</a>|30|15|**4146**|<a href="#vH2">vH2</a>|**4270**|<a href="#SS">SS</a>|||
|**dmu56**|<a href="#DMU1">DMU1</a>|30|20|**4554**|<a href="#GL">GL</a>|**4941**|<a href="#PLC">PLC</a>|**3825.44**|<a href="#PLC">PLC</a>|
|**dmu57**|<a href="#DMU1">DMU1</a>|30|20|**4302**|<a href="#GL">GL</a>|**4663**|<a href="#PLC">PLC</a>|**3649.41**|<a href="#PLC">PLC</a>|
|**dmu58**|<a href="#DMU1">DMU1</a>|30|20|**4319**|<a href="#GL">GL</a>|**4708**|<a href="#PLC">PLC</a>|**3639.68**|<a href="#PLC">PLC</a>|
|**dmu59**|<a href="#DMU1">DMU1</a>|30|20|**4219**|<a href="#vH2">vH2</a>|**4619**|<a href="#SS">SS</a>|||
|**dmu60**|<a href="#DMU1">DMU1</a>|30|20|**4319**|<a href="#GL">GL</a>|**4739**|<a href="#SS">SS</a>|||
|**dmu61**|<a href="#DMU1">DMU1</a>|40|15|**4917**|<a href="#GL">GL</a>|**5172**|<a href="#SS">SS</a>|||
|**dmu62**|<a href="#DMU1">DMU1</a>|40|15|**5041**|<a href="#vH2">vH2</a>|**5251**|<a href="#SS">SS</a>|||
|**dmu63**|<a href="#DMU1">DMU1</a>|40|15|**5111**|<a href="#GL">GL</a>|**5323**|<a href="#SS">SS</a>|||
|**dmu64**|<a href="#DMU1">DMU1</a>|40|15|**5130**|<a href="#DMU">DMU</a>|**5240**|<a href="#SS">SS</a>|||
|**dmu65**|<a href="#DMU1">DMU1</a>|40|15|**5107**|<a href="#vH2">vH2</a>|**5190**|<a href="#SS">SS</a>|||
|**dmu66**|<a href="#DMU1">DMU1</a>|40|20|**5397**|<a href="#vH2">vH2</a>|**5717**|<a href="#PLC">PLC</a>|**9543.86**|<a href="#PLC">PLC</a>|
|**dmu67**|<a href="#DMU1">DMU1</a>|40|20|**5589**|<a href="#GL">GL</a>|**5779**|<a href="#SS">SS</a>|||
|**dmu68**|<a href="#DMU1">DMU1</a>|40|20|**5426**|<a href="#GL">GL</a>|**5765**|<a href="#SS">SS</a>|||
|**dmu69**|<a href="#DMU1">DMU1</a>|40|20|**5423**|<a href="#GL">GL</a>|**5709**|<a href="#PLC">PLC</a>|**8107.63**|<a href="#PLC">PLC</a>|
|**dmu70**|<a href="#DMU1">DMU1</a>|40|20|**5501**|<a href="#GL">GL</a>|**5889**|<a href="#SS">SS</a>|||
|**dmu71**|<a href="#DMU1">DMU1</a>|50|15|**6080**|<a href="#GL">GL</a>|**6223**|<a href="#PLC">PLC</a>|**9835.11**|<a href="#PLC">PLC</a>|
|**dmu72**|<a href="#DMU1">DMU1</a>|50|15|**6395**|<a href="#GL">GL</a>|**6463**|<a href="#SS">SS</a>|||
|**dmu73**|<a href="#DMU1">DMU1</a>|50|15|**6001**|<a href="#GL">GL</a>|**6153**|<a href="#SS">SS</a>|||
|**dmu74**|<a href="#DMU1">DMU1</a>|50|15|**6123**|<a href="#GL">GL</a>|**6196**|<a href="#SS">SS</a>|||
|**dmu75**|<a href="#DMU1">DMU1</a>|50|15|**6029**|<a href="#GL">GL</a>|**6189**|<a href="#SS">SS</a>|||
|**dmu76**|<a href="#DMU1">DMU1</a>|50|20|**6342**|<a href="#GL">GL</a>|**6807**|<a href="#SS">SS</a>|||
|**dmu77**|<a href="#DMU1">DMU1</a>|50|20|**6499**|<a href="#GL">GL</a>|**6792**|<a href="#SS">SS</a>|||
|**dmu78**|<a href="#DMU1">DMU1</a>|50|20|**6586**|<a href="#GL">GL</a>|**6770**|<a href="#PLC">PLC</a>|**10346.61**|<a href="#PLC">PLC</a>|
|**dmu79**|<a href="#DMU1">DMU1</a>|50|20|**6650**|<a href="#GL">GL</a>|**6952**|<a href="#SS">SS</a>|||
|**dmu80**|<a href="#DMU1">DMU1</a>|50|20|**6459**|<a href="#GL">GL</a>|**6673**|<a href="#SS">SS</a>|||
|ft06|<a href="#FT">FT</a>|6|6|55|<a href="#FTM">FTM</a>|55|<a href="#CP">CP</a>|0|<a href="#AZ">AZ</a>|
|ft10|<a href="#FT">FT</a>|10|10|930|<a href="#CP">CP</a>|930|<a href="#CP">CP</a>|0.06|<a href="#AZ">AZ</a>|
|ft20|<a href="#FT">FT</a>|20|5|1165|<a href="#MF">MF</a>|1165|<a href="#CP">CP</a>|0.18|<a href="#PLC">PLC</a>|
|la01|<a href="#L">L</a>|10|5|666|<a href="#ABZ">ABZ</a>|666|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la02|<a href="#L">L</a>|10|5|655|<a href="#ABZ">ABZ</a>|655|<a href="#AC">AC</a>|0.015|<a href="#AZ">AZ</a>|
|la03|<a href="#L">L</a>|10|5|597|<a href="#AC">AC</a>|597|<a href="#AC">AC</a>|0.016|<a href="#AZ">AZ</a>|
|la04|<a href="#L">L</a>|10|5|590|<a href="#AC">AC</a>|590|<a href="#AC">AC</a>|0.015|<a href="#AZ">AZ</a>|
|la05|<a href="#L">L</a>|10|5|593|<a href="#ABZ">ABZ</a>|593|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la06|<a href="#L">L</a>|15|5|926|<a href="#ABZ">ABZ</a>|926|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la07|<a href="#L">L</a>|15|5|890|<a href="#ABZ">ABZ</a>|890|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la08|<a href="#L">L</a>|15|5|863|<a href="#ABZ">ABZ</a>|863|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la09|<a href="#L">L</a>|15|5|951|<a href="#ABZ">ABZ</a>|951|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la10|<a href="#L">L</a>|15|5|958|<a href="#ABZ">ABZ</a>|958|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la11|<a href="#L">L</a>|20|5|1222|<a href="#ABZ">ABZ</a>|1222|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la12|<a href="#L">L</a>|20|5|1039|<a href="#ABZ">ABZ</a>|1039|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la13|<a href="#L">L</a>|20|5|1150|<a href="#ABZ">ABZ</a>|1150|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la14|<a href="#L">L</a>|20|5|1292|<a href="#ABZ">ABZ</a>|1292|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la15|<a href="#L">L</a>|20|5|1207|<a href="#ABZ">ABZ</a>|1207|<a href="#AC">AC</a>|0.016|<a href="#AZ">AZ</a>|
|la16|<a href="#L">L</a>|10|10|945|<a href="#CP1">CP1</a>|945|<a href="#AC">AC</a>|0.06|<a href="#CCC">CCC</a>|
|la17|<a href="#L">L</a>|10|10|784|<a href="#CP1">CP1</a>|784|<a href="#AC">AC</a>|0.016|<a href="#AZ">AZ</a>|
|la18|<a href="#L">L</a>|10|10|848|<a href="#AC">AC</a>|848|<a href="#AC">AC</a>|0.015|<a href="#AZ">AZ</a>|
|la19|<a href="#L">L</a>|10|10|842|<a href="#AC">AC</a>|842|<a href="#AC">AC</a>|0.025|<a href="#AZ">AZ</a>|
|la20|<a href="#L">L</a>|10|10|902|<a href="#AC">AC</a>|902|<a href="#AC">AC</a>|0.031|<a href="#AZ">AZ</a>|
|la21|<a href="#L">L</a>|15|10|1046|<a href="#VAL">VAL</a>|1046|<a href="#YN1">YN1</a>|7.33|<a href="#PLC">PLC</a>|
|la22|<a href="#L">L</a>|15|10|927|<a href="#AC">AC</a>|927|<a href="#AC">AC</a>|0.109|<a href="#AZ">AZ</a>|
|la23|<a href="#L">L</a>|15|10|1032|<a href="#ABZ">ABZ</a>|1032|<a href="#AC">AC</a>|0.047|<a href="#AZ">AZ</a>|
|la24|<a href="#L">L</a>|15|10|935|<a href="#AC">AC</a>|935|<a href="#AC">AC</a>|0.2|<a href="#AZ">AZ</a>|
|la25|<a href="#L">L</a>|15|10|977|<a href="#AC">AC</a>|977|<a href="#AC">AC</a>|0.33|<a href="#AZ">AZ</a>|
|la26|<a href="#L">L</a>|20|10|1218|<a href="#ABZ">ABZ</a>|1218|<a href="#AC">AC</a>|0.078|<a href="#AZ">AZ</a>|
|la27|<a href="#L">L</a>|20|10|1235|<a href="#ABZ">ABZ</a>|1235|<a href="#YN1">YN1</a>|0.95|<a href="#AZ">AZ</a>|
|la28|<a href="#L">L</a>|20|10|1216|<a href="#ABZ">ABZ</a>|1216|<a href="#AC">AC</a>|0.109|<a href="#AZ">AZ</a>|
|la29|<a href="#L">L</a>|20|10|1152|<a href="#M">M</a>|1152|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|la30|<a href="#L">L</a>|20|10|1355|<a href="#ABZ">ABZ</a>|1355|<a href="#AC">AC</a>|0.093|<a href="#AZ">AZ</a>|
|la31|<a href="#L">L</a>|30|10|1784|<a href="#ABZ">ABZ</a>|1784|<a href="#AC">AC</a>|0|<a href="#AZ">AZ</a>|
|la32|<a href="#L">L</a>|30|10|1850|<a href="#ABZ">ABZ</a>|1850|<a href="#AC">AC</a>|0.047|<a href="#AZ">AZ</a>|
|la33|<a href="#L">L</a>|30|10|1719|<a href="#ABZ">ABZ</a>|1719|<a href="#AC">AC</a>|0.031|<a href="#AZ">AZ</a>|
|la34|<a href="#L">L</a>|30|10|1721|<a href="#ABZ">ABZ</a>|1721|<a href="#AC">AC</a>|0.156|<a href="#AZ">AZ</a>|
|la35|<a href="#L">L</a>|30|10|1888|<a href="#ABZ">ABZ</a>|1888|<a href="#AC">AC</a>|0.046|<a href="#AZ">AZ</a>|
|la36|<a href="#L">L</a>|15|15|1268|<a href="#CP1">CP1</a>|1268|<a href="#AC">AC</a>|0.57|<a href="#AZ">AZ</a>|
|la37|<a href="#L">L</a>|15|15|1397|<a href="#AC">AC</a>|1397|<a href="#AC">AC</a>|0.51|<a href="#AZ">AZ</a>|
|la38|<a href="#L">L</a>|15|15|1196|<a href="#VAL">VAL</a>|1196|<a href="#NS">NS</a>|1.25|<a href="#AZ">AZ</a>|
|la39|<a href="#L">L</a>|15|15|1233|<a href="#AC">AC</a>|1233|<a href="#AC">AC</a>|0.5|<a href="#AZ">AZ</a>|
|la40|<a href="#L">L</a>|15|15|1222|<a href="#AC">AC</a>|1222|<a href="#AC">AC</a>|384.8|<a href="#PLC">PLC</a>|
|orb01|<a href="#AC">AC</a>|10|10|1059|<a href="#AC">AC</a>|1059|<a href="#AC">AC</a>|0.06|<a href="#AZ">AZ</a>|
|orb02|<a href="#AC">AC</a>|10|10|888|<a href="#AC">AC</a>|888|<a href="#AC">AC</a>|0.06|<a href="#AZ">AZ</a>|
|orb03|<a href="#AC">AC</a>|10|10|1005|<a href="#AC">AC</a>|1005|<a href="#AC">AC</a>|0.15|<a href="#AZ">AZ</a>|
|orb04|<a href="#AC">AC</a>|10|10|1005|<a href="#AC">AC</a>|1005|<a href="#AC">AC</a>|0.1|<a href="#CCC">CCC</a>|
|orb05|<a href="#AC">AC</a>|10|10|887|<a href="#AC">AC</a>|887|<a href="#AC">AC</a>|0.76|<a href="#AZ">AZ</a>|
|orb06|<a href="#AC">AC</a>|10|10|1010|<a href="#JM">JM</a>|1010|<a href="#BV1">BV1</a>|0.72|<a href="#AZ">AZ</a>|
|orb07|<a href="#AC">AC</a>|10|10|397|<a href="#JM">JM</a>|397|<a href="#H">H</a>|0.02|<a href="#AZ">AZ</a>|
|orb08|<a href="#AC">AC</a>|10|10|899|<a href="#JM">JM</a>|899|<a href="#BV1">BV1</a>|0.09|<a href="#AZ">AZ</a>|
|orb09|<a href="#AC">AC</a>|10|10|934|<a href="#JM">JM</a>|934|<a href="#BV1">BV1</a>|0.09|<a href="#AZ">AZ</a>|
|orb10|<a href="#AC">AC</a>|10|10|944|<a href="#JM">JM</a>|944|<a href="#BV1">BV1</a>|0.03|<a href="#AZ">AZ</a>|
|swv01|<a href="#SWV">SWV</a>|20|10|1407|<a href="#M">M</a>|1407|<a href="#H">H</a>|575.76|<a href="#PLC">PLC</a>|
|swv02|<a href="#SWV">SWV</a>|20|10|1475|<a href="#M">M</a>|1475|<a href="#H">H</a>|136.94|<a href="#AZ">AZ</a>|
|swv03|<a href="#SWV">SWV</a>|20|10|1398|<a href="#BB">BB</a>|1398|<a href="#H">H</a>|613|<a href="#PLC">PLC</a>|
|swv04|<a href="#SWV">SWV</a>|20|10|1464|<a href="#VLS">VLS</a>|1464|<a href="#VLS2">VLS2</a>|30000|<a href="#VLS2">VLS2</a>|
|swv05|<a href="#SWV">SWV</a>|20|10|1424|<a href="#M">M</a>|1424|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|**swv06**|<a href="#SWV">SWV</a>|20|15|**1630**|<a href="#VLS">VLS</a>|**1671**|<a href="#PLC">PLC</a>, <a href="#VLS2">VLS2</a>|**385.73**|<a href="#PLC">PLC</a>|
|**swv07**|<a href="#SWV">SWV</a>|20|15|**1513**|<a href="#VLS">VLS</a>|**1594**|<a href="#GR">GR</a>|||
|**swv08**|<a href="#SWV">SWV</a>|20|15|**1671**|<a href="#VLS">VLS</a>|**1752**|<a href="#PLC">PLC</a>, <a href="#VLS2">VLS2</a>|**503**|<a href="#PLC">PLC</a>|
|**swv09**|<a href="#SWV">SWV</a>|20|15|**1633**|<a href="#VLS">VLS</a>|**1655**|<a href="#PLC">PLC</a>, <a href="#VLS2">VLS2</a>|**521.91**|<a href="#PLC">PLC</a>|
|**swv10**|<a href="#SWV">SWV</a>|20|15|**1663**|<a href="#VLS">VLS</a>|**1743**|<a href="#GR">GR</a>|**441.4**|<a href="#PLC">PLC</a>|
|swv11|<a href="#SWV">SWV</a>|50|10|2983|<a href="#V1">V1</a>|2983|<a href="#NS2">NS2</a>|940.68|<a href="#PLC">PLC</a>|
|**swv12**|<a href="#SWV">SWV</a>|50|10|**2972**|<a href="#V1">V1</a>|**2977**|<a href="#PLC">PLC</a>|**6097.35**|<a href="#PLC">PLC</a>|
|swv13|<a href="#SWV">SWV</a>|50|10|3104|<a href="#V1">V1</a>|3104|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|swv14|<a href="#SWV">SWV</a>|50|10|2968|<a href="#BV">BV</a>|2968|<a href="#H">H</a>|422.81|<a href="#PLC">PLC</a>|
|swv15|<a href="#SWV">SWV</a>|50|10|2885|<a href="#V1">V1</a>|2885|<a href="#PLC">PLC</a>|6000.57|<a href="#PLC">PLC</a>|
|swv16|<a href="#SWV">SWV</a>|50|10|2924|<a href="#SWV">SWV</a>|2924|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|swv17|<a href="#SWV">SWV</a>|50|10|2794|<a href="#SWV">SWV</a>|2794|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|swv18|<a href="#SWV">SWV</a>|50|10|2852|<a href="#SWV">SWV</a>|2852|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|swv19|<a href="#SWV">SWV</a>|50|10|2843|<a href="#SWV">SWV</a>|2843|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|swv20|<a href="#SWV">SWV</a>|50|10|2823|<a href="#SWV">SWV</a>|2823|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|ta01|<a href="#T">T</a>|15|15|1231|<a href="#T">T</a>|1231|<a href="#H">H</a>|2.93|<a href="#PLC">PLC</a>|
|ta02|<a href="#T">T</a>|15|15|1244|<a href="#V">V</a>|1244|<a href="#NS">NS</a>|38.09|<a href="#PLC">PLC</a>|
|ta03|<a href="#T">T</a>|15|15|1218|<a href="#BB">BB</a>|1218|<a href="#H">H</a>|43.66|<a href="#PLC">PLC</a>|
|ta04|<a href="#T">T</a>|15|15|1175|<a href="#BB">BB</a>|1175|<a href="#PM">PM</a>|38.72|<a href="#PLC">PLC</a>|
|ta05|<a href="#T">T</a>|15|15|1224|<a href="#BB">BB</a>|1224|<a href="#H">H</a>|11.24|<a href="#PLC">PLC</a>|
|ta06|<a href="#T">T</a>|15|15|1238|<a href="#BB">BB</a>|1238|<a href="#H">H</a>|178.06|<a href="#PLC">PLC</a>|
|ta07|<a href="#T">T</a>|15|15|1227|<a href="#BB">BB</a>|1227|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|ta08|<a href="#T">T</a>|15|15|1217|<a href="#BB">BB</a>|1217|<a href="#H">H</a>|2.43|<a href="#PLC">PLC</a>|
|ta09|<a href="#T">T</a>|15|15|1274|<a href="#BB">BB</a>|1274|<a href="#H">H</a>|18.66|<a href="#PLC">PLC</a>|
|ta10|<a href="#T">T</a>|15|15|1241|<a href="#V">V</a>|1241|<a href="#H">H</a>|42.25|<a href="#PLC">PLC</a>|
|ta11|<a href="#T">T</a>|20|15|1357|<a href="#VLS">VLS</a>|1357|<a href="#BFW">BFW</a>|186.19|<a href="#PLC">PLC</a>|
|ta12|<a href="#T">T</a>|20|15|1367|<a href="#VLS">VLS</a>|1367|<a href="#H">H</a>|206.06|<a href="#PLC">PLC</a>|
|ta13|<a href="#T">T</a>|20|15|1342|<a href="#VLS">VLS</a>|1342|<a href="#H">H</a>|161.37|<a href="#PLC">PLC</a>|
|ta14|<a href="#T">T</a>|20|15|1345|<a href="#V">V</a>|1345|<a href="#NS">NS</a>|6|<a href="#SS">SS</a>|
|ta15|<a href="#T">T</a>|20|15|1339|<a href="#VLS">VLS</a>|1339|<a href="#PSV">PSV</a>|173.45|<a href="#PLC">PLC</a>|
|ta16|<a href="#T">T</a>|20|15|1360|<a href="#VLS">VLS</a>|1360|<a href="#H">H</a>|63.41|<a href="#PLC">PLC</a>|
|ta17|<a href="#T">T</a>|20|15|1462|<a href="#S">S</a>|1462|<a href="#H">H</a>|1000|<a href="#H">H</a>|
|**ta18**|<a href="#T">T</a>|20|15|**1377**|<a href="#VLS">VLS</a>|**1396**|<a href="#H">H</a>|**91.13**|<a href="#PLC">PLC</a>|
|ta19|<a href="#T">T</a>|20|15|1332|<a href="#VLS">VLS</a>|1332|<a href="#PSV">PSV</a>|145.42|<a href="#PLC">PLC</a>|
|ta20|<a href="#T">T</a>|20|15|1348|<a href="#VLS">VLS</a>|1348|<a href="#PSV">PSV</a>|216.72|<a href="#PLC">PLC</a>|
|ta21|<a href="#T">T</a>|20|20|1642|<a href="#VLS">VLS</a>|1642|<a href="#BFW">BFW</a>|3600|<a href="#BFW">BFW</a>|
|**ta22**|<a href="#T">T</a>|20|20|**1561**|<a href="#VLS">VLS</a>|**1600**|<a href="#H">H</a>|**228.9**|<a href="#PLC">PLC</a>|
|**ta23**|<a href="#T">T</a>|20|20|**1518**|<a href="#VLS">VLS</a>|**1557**|<a href="#H">H</a>|**359.79**|<a href="#PLC">PLC</a>|
|ta24|<a href="#T">T</a>|20|20|1644|<a href="#VLS">VLS</a>|1644|<a href="#VLS2">VLS2</a>|30000|<a href="#VLS2">VLS2</a>|
|**ta25**|<a href="#T">T</a>|20|20|**1558**|<a href="#VLS">VLS</a>|**1595**|<a href="#NS2">NS2</a>|**416.08**|<a href="#PLC">PLC</a>|
|**ta26**|<a href="#T">T</a>|20|20|**1591**|<a href="#VLS">VLS</a>|**1643**|<a href="#GR">GR</a>|**30000**|<a href="#VLS2">VLS2</a>|
|**ta27**|<a href="#T">T</a>|20|20|**1652**|<a href="#VLS">VLS</a>|**1680**|<a href="#H">H</a>|**254.74**|<a href="#PLC">PLC</a>|
|ta28|<a href="#T">T</a>|20|20|1603|<a href="#VLS">VLS</a>|1603|<a href="#PSV">PSV</a>|1514|<a href="#SS">SS</a>|
|**ta29**|<a href="#T">T</a>|20|20|**1573**|<a href="#VLS">VLS</a>|**1625**|<a href="#H">H</a>|**93.53**|<a href="#PLC">PLC</a>|
|**ta30**|<a href="#T">T</a>|20|20|**1519**|<a href="#VLS">VLS</a>|**1584**|<a href="#H">H</a>|**388.66**|<a href="#PLC">PLC</a>|
|ta31|<a href="#T">T</a>|30|15|1764|<a href="#T">T</a>|1764|<a href="#H">H</a>|6|<a href="#SS">SS</a>|
|**ta32**|<a href="#T">T</a>|30|15|**1774**|<a href="#T">T</a>|**1784**|<a href="#S2">S2</a>|||
|**ta33**|<a href="#T">T</a>|30|15|**1788**|<a href="#VLS">VLS</a>|**1791**|<a href="#PSV">PSV</a>|**457.55**|<a href="#PLC">PLC</a>|
|**ta34**|<a href="#T">T</a>|30|15|**1828**|<a href="#T">T</a>|**1829**|<a href="#H">H</a>|**315.71**|<a href="#PLC">PLC</a>|
|ta35|<a href="#T">T</a>|30|15|2007|<a href="#V">V</a>|2007|<a href="#PM">PM</a>|0.56|<a href="#PLC">PLC</a>|
|ta36|<a href="#T">T</a>|30|15|1819|<a href="#V">V</a>|1819|<a href="#H">H</a>|15|<a href="#SS">SS</a>|
|ta37|<a href="#T">T</a>|30|15|1771|<a href="#T">T</a>|1771|<a href="#GR">GR</a>|652.24|<a href="#PLC">PLC</a>|
|ta38|<a href="#T">T</a>|30|15|1673|<a href="#T">T</a>|1673|<a href="#H">H</a>|45|<a href="#SS">SS</a>|
|ta39|<a href="#T">T</a>|30|15|1795|<a href="#V">V</a>|1795|<a href="#H">H</a>|6|<a href="#SS">SS</a>|
|**ta40**|<a href="#T">T</a>|30|15|**1651**|<a href="#VLS">VLS</a>|**1669**|<a href="#GR">GR</a>|**30000**|<a href="#VLS2">VLS2</a>|
|**ta41**|<a href="#T">T</a>|30|20|**1906**|<a href="#VLS">VLS</a>|**2005**|<a href="#VLS2">VLS2</a>|**30000**|<a href="#VLS2">VLS2</a>|
|**ta42**|<a href="#T">T</a>|30|20|**1884**|<a href="#VLS">VLS</a>|**1937**|<a href="#GR">GR</a>|**30000**|<a href="#VLS2">VLS2</a>|
|**ta43**|<a href="#T">T</a>|30|20|**1809**|<a href="#V">V</a>|**1846**|<a href="#PLC">PLC</a>|**1726.78**|<a href="#PLC">PLC</a>|
|**ta44**|<a href="#T">T</a>|30|20|**1948**|<a href="#VLS">VLS</a>|**1979**|<a href="#VLS2">VLS2</a>|**30000**|<a href="#VLS2">VLS2</a>|
|**ta45**|<a href="#T">T</a>|30|20|**1997**|<a href="#V">V</a>|**2000**|<a href="#H">H</a>|**1057.79**|<a href="#PLC">PLC</a>|
|**ta46**|<a href="#T">T</a>|30|20|**1957**|<a href="#VLS">VLS</a>|**2004**|<a href="#GR">GR</a>|**30000**|<a href="#VLS2">VLS2</a>|
|**ta47**|<a href="#T">T</a>|30|20|**1807**|<a href="#VLS">VLS</a>|**1889**|<a href="#PLC">PLC</a>, <a href="#VLS2">VLS2</a>|**1030.88**|<a href="#PLC">PLC</a>|
|**ta48**|<a href="#T">T</a>|30|20|**1912**|<a href="#V">V</a>|**1937**|<a href="#SS">SS</a>|**3008**|<a href="#SS">SS</a>|
|**ta49**|<a href="#T">T</a>|30|20|**1931**|<a href="#VLS">VLS</a>|**1961**|<a href="#VLS2">VLS2</a>|**30000**|<a href="#VLS2">VLS2</a>|
|**ta50**|<a href="#T">T</a>|30|20|**1833**|<a href="#VLS">VLS</a>|**1923**|<a href="#PLC">PLC</a>, <a href="#VLS2">VLS2</a>|**1318.05**|<a href="#PLC">PLC</a>|
|ta51|<a href="#T">T</a>|50|15|2760|<a href="#T">T</a>|2760|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta52|<a href="#T">T</a>|50|15|2756|<a href="#T">T</a>|2756|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta53|<a href="#T">T</a>|50|15|2717|<a href="#T">T</a>|2717|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta54|<a href="#T">T</a>|50|15|2839|<a href="#T">T</a>|2839|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta55|<a href="#T">T</a>|50|15|2679|<a href="#T">T</a>|2679|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta56|<a href="#T">T</a>|50|15|2781|<a href="#T">T</a>|2781|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta57|<a href="#T">T</a>|50|15|2943|<a href="#T">T</a>|2943|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta58|<a href="#T">T</a>|50|15|2885|<a href="#T">T</a>|2885|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta59|<a href="#T">T</a>|50|15|2655|<a href="#T">T</a>|2655|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta60|<a href="#T">T</a>|50|15|2723|<a href="#T">T</a>|2723|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta61|<a href="#T">T</a>|50|20|2868|<a href="#T">T</a>|2868|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta62|<a href="#T">T</a>|50|20|2869|<a href="#V">V</a>|2869|<a href="#C">C</a>|||
|ta63|<a href="#T">T</a>|50|20|2755|<a href="#T">T</a>|2755|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta64|<a href="#T">T</a>|50|20|2702|<a href="#BV">BV</a>|2702|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta65|<a href="#T">T</a>|50|20|2725|<a href="#T">T</a>|2725|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta66|<a href="#T">T</a>|50|20|2845|<a href="#T">T</a>|2845|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta67|<a href="#T">T</a>|50|20|2825|<a href="#V">V</a>|2825|<a href="#H">H</a>|2000|<a href="#H">H</a>|
|ta68|<a href="#T">T</a>|50|20|2784|<a href="#BV">BV</a>|2784|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta69|<a href="#T">T</a>|50|20|3071|<a href="#T">T</a>|3071|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta70|<a href="#T">T</a>|50|20|2995|<a href="#T">T</a>|2995|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|ta71|<a href="#T">T</a>|100|20|5464|<a href="#T">T</a>|5464|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta72|<a href="#T">T</a>|100|20|5181|<a href="#T">T</a>|5181|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta73|<a href="#T">T</a>|100|20|5568|<a href="#T">T</a>|5568|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta74|<a href="#T">T</a>|100|20|5339|<a href="#T">T</a>|5339|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta75|<a href="#T">T</a>|100|20|5392|<a href="#T">T</a>|5392|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta76|<a href="#T">T</a>|100|20|5342|<a href="#T">T</a>|5342|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta77|<a href="#T">T</a>|100|20|5436|<a href="#T">T</a>|5436|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta78|<a href="#T">T</a>|100|20|5394|<a href="#T">T</a>|5394|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta79|<a href="#T">T</a>|100|20|5358|<a href="#T">T</a>|5358|<a href="#PM">PM</a>|2000|<a href="#H">H</a>|
|ta80|<a href="#T">T</a>|100|20|5183|<a href="#T">T</a>|5183|<a href="#NS">NS</a>|2000|<a href="#H">H</a>|
|yn1|<a href="#YN">YN</a>|20|20|884|<a href="#KNF">KNF</a>|884|<a href="#ZSR">ZSR</a>|169.29|<a href="#PLC">PLC</a>|
|**yn2**|<a href="#YN">YN</a>|20|20|**870**|<a href="#BB">BB</a>|**904**|<a href="#GR">GR</a>|**202.22**|<a href="#PLC">PLC</a>|
|**yn3**|<a href="#YN">YN</a>|20|20|**859**|<a href="#VLS">VLS</a>|**892**|<a href="#NS2">NS2</a>|**344.15**|<a href="#PLC">PLC</a>|
|**yn4**|<a href="#YN">YN</a>|20|20|**929**|<a href="#VLS">VLS</a>|**968**|<a href="#H">H</a>|**320.51**|<a href="#PLC">PLC</a>|


## Literature Sources

<dl>
<dt id="A">A</dt><dd>Abdelmaguid TF (2010). “Representations in Genetic Algorithm for the Job Shop Scheduling Problem: A Computational Study.” Journal of Software Engineering and Applications (JSEA), 3(12), 1155-1162. doi:<a href="https://doi.org/10.4236/jsea.2010.312135">10.4236/jsea.2010.312135</a>, <a href="http://www.scirp.org/journal/paperinformation.aspx?paperid=3561">http://www.scirp.org/journal/paperinformation.aspx?paperid=3561</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC58">A2010RIGAFTJSPACS</a></dd>
<dt id="A2">A2</dt><dd>Asadzadeh L (2015). “A Local Search Genetic Algorithm for the Job Shop Scheduling Problem with Intelligent Agents.” Computers & Industrial Engineering, 85, 376-383. doi:<a href="https://doi.org/10.1016/j.cie.2015.04.006">10.1016/j.cie.2015.04.006</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC72">A2015ALSGAFTJSSPWIA</a></li>
<dt id="ABZ">ABZ</dt><dd>Adams J, Balas E, Zawack D (1988). “The Shifting Bottleneck Procedure for Job Shop Scheduling.” Management Science, 34(3), 391-401. doi:<a href="https://doi.org/10.1287/mnsc.34.3.391">10.1287/mnsc.34.3.391</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC84">ABZ1988TSBPFJSS</a></li>
<dt id="AC">AC</dt><dd>Applegate DL, Cook WJ (1991). “A Computational Study of the Job-Shop Scheduling Problem.” ORSA Journal on Computing, 3(2), 149-156. doi:<a href="https://doi.org/10.1287/ijoc.3.2.149">10.1287/ijoc.3.2.149</a>, the JSSP instances used were generated in Bonn in 1986. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC96">AC1991ACSOTJSSP</a></li>
<dt id="AF">AF</dt><dd>Aydin ME, Fogarty TC (2002). “Modular Simulated Annealing for Job Shop Scheduling running on Distributed Resource Machine (DRM).” London South Bank University, Faculty of Business, Computing and Information Management, London, England, UK. <a href="http://www.soc.napier.ac.uk/~benp/dream/dreampaper6a.pdf">http://www.soc.napier.ac.uk/~benp/dream/dreampaper6a.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC109">AF2002MSAFJSSRODRMD</a></li>
<dt id="AK">AK</dt><dd>Abdel-Kader RF (2018). “An Improved PSO Algorithm with Genetic and Neighborhood-Based Diversity Operators for the Job Shop Scheduling Problem.” Applied Artificial Intelligence - An International Journal, 32(5), 433-462. doi:<a href="https://doi.org/10.1080/08839514.2018.1481903">10.1080/08839514.2018.1481903</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC119">AK2018AIPAWGANBDOFTJSSP</a></li>
<dt id="AKZ">AKZ</dt><dd>Akram K, Kamal K, Zeb A (2016). “Fast Simulated Annealing Hybridized with Quenching for Solving Job Shop Scheduling Problem.” Applied Soft Computing Journal (ASOC), 49, 510-523. doi:<a href="https://doi.org/10.1016/j.asoc.2016.08.037">10.1016/j.asoc.2016.08.037</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC132">AKZ2016FSAHWQFSJSSP</a></li>
<dt id="AMC">AMC</dt><dd>Angel JM, Martínez MR, Castillo LRM, Solis LS (2014). “Un Modelo Híbrido de Inteligencia Computacional para Resolver el Problema de Job Shop Scheduling.” Research in Computing Science, 79(Advances in Intelligent Information Technologies), 9-20. <a href="http://www.rcs.cic.ipn.mx/2014_79/RCS_79_2014.pdf">http://www.rcs.cic.ipn.mx/2014_79/RCS_79_2014.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC144">AMCS2014UMHDICPREPDJSS</a></li>
<dt id="ASS">ASS</dt><dd>Amaria K, Souier M, Sar Z (2014). “Artificial Bee Colony (ABC) Algorithm for the Job-Shop Scheduling Problem.” In Proceedings of the 5th International Conference on Metaheuristics and Nature Inspired Computing (META'14), October 27-31, 2014, Marrakech, Morocco. The paper reports makespan 53 for ft06, which is below the lower bound of 55 and thus is not included in our dataset., <a href="https://meta2014.sciencesconf.org/42589/document">https://meta2014.sciencesconf.org/42589/document</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC157">ASS2014ABCAAFTJSSP</a></li>
<dt id="AZ">AZ</dt><dd>Amirghasemi M, Zamani R (2015). “An Effective Asexual Genetic Algorithm for Solving the Job Shop Scheduling Problem.” Computers & Industrial Engineering, 83, 123-138. doi:<a href="https://doi.org/10.1016/j.cie.2015.02.011">10.1016/j.cie.2015.02.011</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC166">AZ2015AEAGAFSTJSSP</a></li>
<dt id="B">B</dt><dd>Bierwirth C (1995). “A Generalized Permutation Approach to Job Shop Scheduling with Genetic Algorithms.” Operations-Research-Spektrum (OR Spectrum), 17(2-3), 87-92. doi:<a href="https://doi.org/10.1007/BF01719250">10.1007/BF01719250</a>, <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.52.7392&type=pdf">http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.52.7392&type=pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC178">B1995AGPATJSSWGA</a></li>
<dt id="BB">BB</dt><dd>Brinkkötter W, Brucker P (2001). “Solving Open Benchmark Instances for the Job-Shop Problem by Parallel Head-Tail Adjustments.” Journal of Scheduling, 4(1), 53-64. doi:<a href="https://doi.org/10.1002/1099-1425(200101/02">10.1002/1099-1425(200101/02)4:1<53::AID-JOS59>3.0.CO;2-Y</a>4:1<53::AID-JOS59>3.0.CO;2-Y). BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC192">BB2001SOBIFTJSPBPHTA</a></li>
<dt id="BFW">BFW</dt><dd>Beck JC, Feng TK, Watson J (2011). “Combining Constraint Programming and Local Search for Job-Shop Scheduling.” INFORMS Journal on Computing, 23(1), 1-14. doi:<a href="https://doi.org/10.1287/ijoc.1100.0388">10.1287/ijoc.1100.0388</a>, <a href="http://cfwebprod.sandia.gov/cfdocs/CompResearch/docs/ists-sgmpcs.pdf">http://cfwebprod.sandia.gov/cfdocs/CompResearch/docs/ists-sgmpcs.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC204">BFW2011CCPALSFJSS</a></li>
<dt id="BV">BV</dt><dd>Balas E, Vazacopoulos A (1994). “Guided Local Search with Shifting Bottleneck for Job Shop Scheduling.” Management Science Research Report MSSR–609, Graduate School of Industrial Administration (GSIA), Carnegie Mellon University, Pittsburgh, PA, USA. revised November 1995. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC217">BV1994GLSWSBFJSS</a></li>
<dt id="BV1">BV1</dt><dd>Balas E, Vazacopoulos A (1998). “Guided Local Search with Shifting Bottleneck for Job Shop Scheduling.” Management Science, 44(2), 262-275. doi:<a href="https://doi.org/10.1287/mnsc.44.2.262">10.1287/mnsc.44.2.262</a>, reports 307 as makespan for orb07, probably a typo, as the lower bound is 397. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC230">BV1998GLSWSBFJSS</a></li>
<dt id="C">C</dt><dd>Caldeira JP (2003). “Private Communication of Result 2869 for ta62 to Éric D. Taillard, listed on Éric Taillard's Page.” <a href="http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/jobshop.dir/best_lb_up.txt">http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/jobshop.dir/best_lb_up.txt</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC244">C2003PCOR2FTTETLOETP</a></li>
<dt id="CCC">CCC</dt><dd>Cruz-Chávez MA, Cruz Rosales MH, Zavala-Díaz JC, Aguilar JAH, Rodrıguez-Leó A, Avelino JCP, Orziz MEL, Salinas OH (2019). “Hybrid Micro Genetic Multi-Population Algorithm With Collective Communication for the Job Shop Scheduling Problem.” IEEE Access, 7, 82358-82376. doi:<a href="https://doi.org/10.1109/ACCESS.2019.2924218">10.1109/ACCESS.2019.2924218</a>, <a href="http://ieeexplore.ieee.org/document/8743353">http://ieeexplore.ieee.org/document/8743353</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC253">CCCRZDARLAOS2019HMGMPAWCCFTJSSP</a></li>
<dt id="CP">CP</dt><dd>Carlier J, Pinson É (1989). “An Algorithm for Solving the Job-Shop Problem.” Management Science, 35(2), 164-176. doi:<a href="https://doi.org/10.1287/mnsc.35.2.164">10.1287/mnsc.35.2.164</a>, jstor: 2631909. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC266">CP1989AAFSTJSP</a></li>
<dt id="CP1">CP1</dt><dd>Carlier J, Pinson É (1990). “A Practical Use of Jackson's Preemptive Schedule for Solving the Job Shop Problem.” Annals of Operations Research, 26(1-4), 269-287. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC279">CP1990APUOJPSFSTJSP</a></li>
<dt id="CPL">CPL</dt><dd>Cheng TCE, Peng B, Lü Z (2016). “A Hybrid Evolutionary Algorithm to Solve the Job Shop Scheduling Problem.” Annals of Operations Research, 242(2), 223-237. doi:<a href="https://doi.org/10.1007/s10479-013-1332-5">10.1007/s10479-013-1332-5</a>, The paper reports 555 as average makespan of HEA for ft20, which is an obvious typo because the other columns have 1165, which is the lower bound. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC291">CPL2016AHEATSTJSSP</a></li>
<dt id="DMU">DMU</dt><dd>Demirkol E, Mehta SV, Uzsoy R (1996). “Benchmarking for Shop Scheduling Problems.” Research Memorandum 96-4, School of Industrial Engineering, Purdue University, West Lafayette, IN, USA. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC305">DMU1996BFSSP</a></li>
<dt id="DMU1">DMU1</dt><dd>Demirkol E, Mehta SV, Uzsoy R (1998). “Benchmarks for Shop Scheduling Problems.” European Journal of Operational Research (EJOR), 109(1), 137-141. doi:<a href="https://doi.org/10.1016/S0377-2217(97">10.1016/S0377-2217(97)00019-2</a>00019-2). BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC316">DMU1998BFSSP</a></li>
<dt id="DPN">DPN</dt><dd>Dao T, Pan T, Nguyen T, Pan J (2018). “Parallel Bat Algorithm for Optimizing Makespan in Job Shop Scheduling Problems.” Journal of Intelligent Manufacturing, 29(2), 451-462. doi:<a href="https://doi.org/10.1007/s10845-015-1121-x">10.1007/s10845-015-1121-x</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC329">DPNP2018PBAFOMIJSSP</a></li>
<dt id="FGB">FGB</dt><dd>Flórez E, Gómez W, Bautista L (2013). “An Ant Colony Optimization Algorithm for Job Shop Scheduling Problem.” Computing Research Repository (CoRR) abs/1309.5110, arXiv. <a href="https://arxiv.org/pdf/1309.5110.pdf">https://arxiv.org/pdf/1309.5110.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC355">FGB2013AACOAFJSSP</a></li>
<dt id="FT">FT</dt><dd>Fisher H, Thompson GL (1963). “Probabilistic Learning Combinations of Local Job-Shop Scheduling Rules.” In Muth JF, Thompson GL (eds.), Industrial Scheduling, 225-251. Prentice-Hall, Englewood Cliffs, NJ, USA. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC366">FT1963PLCOLJSSR</a></li>
<dt id="FTM">FTM</dt><dd>Florian M, Trepant P, McMahon G (1971). “An Implicit Enumeration Algorithm for the Machine Sequencing Problem.” Management Science, 17(12), B-782-B-792. doi:<a href="https://doi.org/10.1287/mnsc.17.12.B782">10.1287/mnsc.17.12.B782</a>, jstor: 2629469. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC379">FTM1971AIEAFTMSP</a></li>
<dt id="GL">GL</dt><dd>Gharbi A, Labidi M (2010). “Extending the Single Machine-Based Relaxation Scheme for the Job Shop Scheduling Problem.” Electronic Notes in Discrete Mathematics, 36, 1057-1064. doi:<a href="https://doi.org/10.1016/j.endm.2010.05.134">10.1016/j.endm.2010.05.134</a>, this algorithm was used to solve several JSSP instances of the OR Library. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC393">GL2010ETSMBRSFTJSSP</a></li>
<dt id="GLW">GLW</dt><dd>Gao L, Li X, Wen X, Lu C, Wen F (2015). “A Hybrid Algorithm based on a New Neighborhood Structure Evaluation Method for Job Shop Scheduling Problem.” Computers & Industrial Engineering, 88, 417-429. doi:<a href="https://doi.org/10.1016/j.cie.2015.08.002">10.1016/j.cie.2015.08.002</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC406">GLWLW2015AHABOANNSEMFSSP</a></li>
<dt id="GR">GR</dt><dd>Gonçalves JF, Resende MGC (2014). “An Extended Akers Graphical Method with a Biased Random-Key Genetic Algorithm for Job-Shop Scheduling.” International Transactions on Operational Research (ITOR), 21(2), 215-246. doi:<a href="https://doi.org/10.1111/itor.12044">10.1111/itor.12044</a>, <a href="http://mauricio.resende.info/doc/brkga-jss2011.pdf">http://mauricio.resende.info/doc/brkga-jss2011.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC418">GR2014AEAGMWABRKGAFJSS</a></li>
<dt id="GTK">GTK</dt><dd>Gen M, Tsujimura Y, Kubota E (1994). “Solving Job-Shop Scheduling Problems by Genetic Algorithm.” In Humans, Information and Technology: Proceedings of the 1994 IEEE International Conference on Systems, Man and Cybernetics, October 2-5, 1994, San Antonio, TX, USA, volume 2. ISBN 0-7803-2129-4, doi:<a href="https://doi.org/10.1109/ICSMC.1994.400072">10.1109/ICSMC.1994.400072</a>, <a href="http://read.pudn.com/downloads151/doc/658565/00400072.pdf">http://read.pudn.com/downloads151/doc/658565/00400072.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC342">GTK1994SJSSPBGA</a></li>
<dt id="GvH">GvH</dt><dd>Gromicho JAS, van Hoorn JJ, Saldanha-da-Gama F, Timmer GT (2009). “Exponentially Better than Brute Force: Solving the Job-Shop Scheduling Problem Optimally by Dynamic Programming.” Research Memorandum 2009-56, Faculty of Economics and Business Administration, Vrije Universiteit Amsterdam, Amsterdam, The Netherlands. <a href="http://degree.ubvu.vu.nl/repec/vua/wpaper/pdf/20090056.pdf">http://degree.ubvu.vu.nl/repec/vua/wpaper/pdf/20090056.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC432">GvHSGT2009</a></li>
<dt id="H">H</dt><dd>Henning A (2002). Praktische Job-Shop Scheduling-Probleme. Ph.D. thesis, Friedrich-Schiller-Universität Jena, Jena, Germany. alternate url: https://nbn-resolving.org/urn:nbn:de:gbv:27-20060809-115700-4, <a href="http://www.db-thueringen.de/servlets/DocumentServlet?id=873">http://www.db-thueringen.de/servlets/DocumentServlet?id=873</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC444">H2002PJSSP</a></li>
<dt id="HRS">HRS</dt><dd>Hernández-Ramírez L, Solis JF, Castilla-Valdez G, González-Barbosa JJ, Terán-Villanueva D, Morales-Rodríguez ML (2019). “A Hybrid Simulated Annealing for Job Shop Scheduling Problem.” International Journal of Combinatorial Optimization Problems and Informatics (IJCOPI), 10(1), 6-15. published 2018-08-10, <a href="http://ijcopi.org/index.php/ojs/article/view/111">http://ijcopi.org/index.php/ojs/article/view/111</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC457">HRSCVGBTVMR2019AHSAFJSSP</a></li>
<dt id="HY">HY</dt><dd>Han B, Yang J (2020). “Research on Adaptive Job Shop Scheduling Problems Based on Dueling Double DQN.” IEEE Access, 8, 186474-186495. doi:<a href="https://doi.org/10.1109/ACCESS.2020.3029868">10.1109/ACCESS.2020.3029868</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC471">HY2020ROAJSSPBODDD</a></li>
<dt id="JM">JM</dt><dd>Jain AS, Meeran S (1999). “Deterministic Job-Shop Scheduling: Past, Present and Future.” European Journal of Operational Research (EJOR), 113(2), 390-434. doi:<a href="https://doi.org/10.1016/S0377-2217(98">10.1016/S0377-2217(98)00113-1</a>00113-1). BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC482">JM1999DJSSPPAF</a></li>
<dt id="JPD">JPD</dt><dd>Jorapur V, Puranik VS, Deshpande AS, Sharma MR (2014). “Comparative Study of Different Representations in Genetic Algorithms for Job Shop Scheduling Problem.” Journal of Software Engineering and Applications (JSEA), 7(7), 571-580. doi:<a href="https://doi.org/10.4236/jsea.2014.77053">10.4236/jsea.2014.77053</a>, <a href="http://www.scirp.org/journal/paperinformation.aspx?paperid=46670">http://www.scirp.org/journal/paperinformation.aspx?paperid=46670</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC495">JPDS2014CAODRIGAFJSSP</a></li>
<dt id="JZ">JZ</dt><dd>Jiang T, Zhang C (2018). “Application of Grey Wolf Optimization for Solving Combinatorial Problems: Job Shop and Flexible Job Shop Scheduling Cases.” IEEE Access, 6, 26231-26240. doi:<a href="https://doi.org/10.1109/ACCESS.2018.2833552">10.1109/ACCESS.2018.2833552</a>, <a href="http://ieeexplore.ieee.org/document/8355479">http://ieeexplore.ieee.org/document/8355479</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC509">JZ2018AOGWOFSCPJSAFJSSC</a></li>
<dt id="K">K</dt><dd>Kolonko M (1999). “Some New Results on Simulated Annealing Applied to the Job Shop Scheduling Problem.” European Journal of Operational Research (EJOR), 113(1), 123-136. doi:<a href="https://doi.org/10.1016/S0377-2217(97">10.1016/S0377-2217(97)00420-7</a>00420-7). BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC522">K1999SNROSAATTJSSP</a></li>
<dt id="K2">K2</dt><dd>Kurdi M (2015). “A New Hybrid Island Model Genetic Algorithm for Job Shop Scheduling Problem.” Computers & Industrial Engineering, 88, 273-283. doi:<a href="https://doi.org/10.1016/j.cie.2015.07.015">10.1016/j.cie.2015.07.015</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC535">K2015ANHIMGAFJSSP</a></li>
<dt id="KNF">KNF</dt><dd>Koshimura M, Nabeshima H, Fujita H, Hasegawa R (2010). “Solving Open Job-Shop Scheduling Problems by SAT Encoding.” IEICE Transactions on Information and Systems, E93.D(8), 2316-2318. doi:<a href="https://doi.org/10.1587/transinf.E93.D.2316">10.1587/transinf.E93.D.2316</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC547">KNFH2010SOJSSPBSE</a></li>
<dt id="KV">KV</dt><dd>Kulkarni K, Venkateswaran J (2014). “Iterative Simulation and Optimization Approach for Job Shop Scheduling.” In Buckley SJ, Miller JA (eds.), Proceedings of the 2014 Winter Simulation Conference, December 7-10, 2014, Savannah, GA, USA, 1620-1631. doi:<a href="https://doi.org/10.1109/WSC.2014.7020013">10.1109/WSC.2014.7020013</a>, <a href="https://www.anylogic.com/upload/iblock/5aa/5aa2987b839049668eeef8a21c811e6b.pdf">https://www.anylogic.com/upload/iblock/5aa/5aa2987b839049668eeef8a21c811e6b.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC559">KV2014ISAOAFJSS</a></li>
<dt id="L">L</dt><dd>Lawrence SR (1984). Resource Constrained Project Scheduling: An Experimental Investigation of Heuristic Scheduling Techniques (Supplement). Ph.D. thesis, Graduate School of Industrial Administration (GSIA), Carnegie-Mellon University, Pittsburgh, PA, USA. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC572">L1998RCPSAEIOHSTS</a></li>
<dt id="LWF">LWF</dt><dd>Li L, Weng W, Fujimura S (2017). “An Improved Teaching-Learning-based Optimization Algorithm to Solve Job Shop Scheduling Problems.” In Zhu G, Yao S, Cui X, Xu S (eds.), 16th IEEE/ACIS International Conference on Computer and Information Science (ICIS'17), May 24-26, 2017, Wuhan, China, 797-801. ISBN 978-1-5090-5507-4, doi:<a href="https://doi.org/10.1109/ICIS.2017.7960101">10.1109/ICIS.2017.7960101</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC582">LWF2017AITLBOATSJSSP</a></li>
<dt id="LYL">LYL</dt><dd>Liu M, Yao X, Li Y (2020). “Hybrid Whale Optimization Algorithm Enhanced with Lévy Flight and Differential Evolution for Job Shop Scheduling Problems.” Applied Soft Computing Journal (ASOC), 87, 105954. doi:<a href="https://doi.org/10.1016/j.asoc.2019.105954">10.1016/j.asoc.2019.105954</a>, Originally, the paper had two typos in the results. It reports an average result (918.4) for WSO-LFDE on la20, which is worse than the worst result (902) it reports. We therefore ignore the worst reported result for that algorithm on that instance, since it was probably accidentally copy-pasted from the best result. On instance la23, the lower bound is 1032 but the result 1023 is reported, which is clearly an accidental typo. These typos are currently fixed in an erratum process. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC594">LYL2020HWOAEWLFADEFJSSP</a></li>
<dt id="M">M</dt><dd>Martin PD (1996). A Time-Oriented Approach to Computing Optimal Schedules for the Job-Shop Scheduling Problem. Ph.D. thesis, School of Operations Research and Industrial Engineering, Cornell University, Ithaca, NY, USA. oclc: 64683112. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC606">M1996ATOATCOSFTJSSP</a></li>
<dt id="M2">M2</dt><dd>Mahapatra DK (2012). “Bachelor's Thesis: Job Shop Scheduling using Artificial Immune System.” guided by Prof. S. S. Mahapatra, <a href="http://pdfs.semanticscholar.org/a350/070a2612d046d11feb33e64d1ab58cd8870d.pdf">http://pdfs.semanticscholar.org/a350/070a2612d046d11feb33e64d1ab58cd8870d.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC617">M2012JSSUAIS</a></li>
<dt id="MF">MF</dt><dd>McMahon G, Florian M (1975). “On Scheduling with Ready Times and Due Dates to Minimize Maximum Lateness.” Operations Research, 23(3), 475-482. doi:<a href="https://doi.org/10.1287/opre.23.3.475">10.1287/opre.23.3.475</a>, jstor: 169697. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC629">MF1975OSWRTADDTMML</a></li>
<dt id="MHT">MHT</dt><dd>Mui NH, Hoa VD, Tuyen LT (2012). “A Parallel Genetic Algorithm for the Job Shop Scheduling Problem.” In Proceedings of the IEEE International Symposium on Signal Processing and Information Technology (ISSPIT'12), December 12-15, 2012, Ho Chi Minh City, Vietnam, 19-24. ISBN 978-1-4673-5604-6, doi:<a href="https://doi.org/10.1109/ISSPIT.2012.6621254">10.1109/ISSPIT.2012.6621254</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC643">MHT2012APGAFTJSSP</a></li>
<dt id="MM">MM</dt><dd>Magalhães-Mendes J (2013). “A Comparative Study of Crossover Operators for Genetic Algorithms to Solve the Job Shop Scheduling Problem.” WSEAS Transactions on Computers, 12(4), 164-173. <a href="http://www.wseas.org/multimedia/journals/computers/2013/5705-156.pdf">http://www.wseas.org/multimedia/journals/computers/2013/5705-156.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC656">MM2013ACSOCOFGATSTJSSP</a></li>
<dt id="MNK">MNK</dt><dd>Maqsood S, Noor S, Khan MK, Wood A (2012). “Hybrid Genetic Algorithm (GA) for Job Shop Scheduling Problems and its Sensitivity Analysis.” International Journal of Intelligent Systems Technologies and Applications (IJISTA), 11(1/2), 49-62. doi:<a href="https://doi.org/10.1504/IJISTA.2012.046543">10.1504/IJISTA.2012.046543</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC669">MNKW2012HGAGFJSSPAISA</a></li>
<dt id="MTS">MTS</dt><dd>Miller-Todd J, Steinhöfel K, Veenstra P (2018). “Firefly-Inspired Algorithm for Job Shop Scheduling.” In Böckenhauer H, Komm D, Unger W (eds.), Adventures Between Lower Bounds and Higher Altitudes - Essays Dedicated to Juraj Hromkovič on the Occasion of His 60th Birthday, volume 11011 series Lecture Notes in Computer Science (LNCS), 423-433. Springer. ISBN 978-3-319-98354-7, doi:<a href="https://doi.org/10.1007/978-3-319-98355-4_24">10.1007/978-3-319-98355-4_24</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC681">MTSV2018FIAFJSS</a></li>
<dt id="N">N</dt><dd>Nazif H (2015). “Solving Job Shop Scheduling Problem Using an Ant Colony Algorithm.” Journal of Asian Scientific Research, 5(5), 261-268. doi:<a href="https://doi.org/10.18488/journal.2/2015.5.5/2.5.261.268">10.18488/journal.2/2015.5.5/2.5.261.268</a>, <a href="http://www.aessweb.com/pdf-files/jasr-2015-5(5)-261-268.pdf">http://www.aessweb.com/pdf-files/jasr-2015-5(5)-261-268.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC696">N2015SJSSPUAACO</a></li>
<dt id="NA">NA</dt><dd>Narendhar S, Amudha T (2012). “A Hybrid Bacterial Foraging Algorithm For Solving Job Shop Scheduling Problems.” International Journal of Programming Languages and Applications (IJPLA), 2(4), 1-11. doi:<a href="https://doi.org/10.5121/ijpla.2012.2401">10.5121/ijpla.2012.2401</a>, Also available via Computing Research Repository (CoRR) abs/1211.4971 at arXiv:1211.4971v1 [cs.NE], <a href="https://arxiv.org/pdf/1211.4971.pdf">https://arxiv.org/pdf/1211.4971.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC709">NA2012AHBFAFSJSSP</a></li>
<dt id="NS">NS</dt><dd>Nowicki E, Smutnicki C (1996). “A Fast Taboo Search Algorithm for the Job Shop Problem.” Management Science, 42(6), 783-938. doi:<a href="https://doi.org/10.1287/mnsc.42.6.797">10.1287/mnsc.42.6.797</a>, jstor: 2634595, <a href="http://pacciarelli.inf.uniroma3.it/CORSI/MSP/NowickiSmutnicki96.pdf">http://pacciarelli.inf.uniroma3.it/CORSI/MSP/NowickiSmutnicki96.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC724">NS1996AFTSAFTJSP</a></li>
<dt id="NS2">NS2</dt><dd>Nowicki E, Smutnicki C (2005). “An Advanced Taboo Search Algorithm for the Job Shop Problem.” Journal of Scheduling, 8(2), 145-159. doi:<a href="https://doi.org/10.1007/s10951-005-6364-5">10.1007/s10951-005-6364-5</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC739">NS2005AATSAFTJSP</a></li>
<dt id="NZJ">NZJ</dt><dd>Nguyen S, Zhang M, Johnston M, Tan KC (2013). “A Computational Study of Representations in Genetic Programming to Evolve Dispatching Rules for the Job Shop Scheduling Problem.” IEEE Transactions on Evolutionary Computation (TEVC), 17(5), 621-639. doi:<a href="https://doi.org/10.1109/TEVC.2012.2227326">10.1109/TEVC.2012.2227326</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC752">NZJT2013ACSORIGPTED</a></li>
<dt id="ODP">ODP</dt><dd>Oliveira JA, Dias L, Pereira G (2010). “Solving the Job Shop Problem with a Random Keys Genetic Algorithm with Instance Parameters.” In Rodrigues H, Herskovits J, Soares CM, Guedes JM, Folgado J, Araújo A, Moleiro F, Kuzhichalil JP, Madeira JA, Dimitrovová Z (eds.), Proceedings of the 2nd International Conference on Engineering Optimization (EngOpt2010), September 6-9, 2010, Lisbon, Portugal. ISBN 978-989-96264-3-0, <a href="http://www1.dem.ist.utl.pt/engopt2010/Book_and_CD/Papers_CD_Final_Version/pdf/08/01512-01.pdf">http://www1.dem.ist.utl.pt/engopt2010/Book_and_CD/Papers_CD_Final_Version/pdf/08/01512-01.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC765">ODP2010STJSPWARKGAWIP</a></li>
<dt id="OV">OV</dt><dd>Ombuki BM, Ventresca M (2004). “Local Search Genetic Algorithms for the Job Shop Scheduling Problem.” Applied Intelligence - The International Journal of Research on Intelligent Systems for Real Life Complex Problems, 21(1), 99-109. doi:<a href="https://doi.org/10.1023/B:APIN.0000027769.48098.91">10.1023/B:APIN.0000027769.48098.91</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC779">OV2004LSGAFTJSSP</a></li>
<dt id="P">P</dt><dd>Pongchairerks P (2014). “Variable Neighbourhood Search Algorithms Applied to Job-Shop Scheduling Problems.” International Journal of Mathematics in Operational Research (IJMOR), 6(6), 752-774. doi:<a href="https://doi.org/10.1504/IJMOR.2014.065421">10.1504/IJMOR.2014.065421</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC792">P2014VNSAATJSSP</a></li>
<dt id="P2">P2</dt><dd>Pongchairerks P (2019). “A Two-Level Metaheuristic Algorithm for the Job-Shop Scheduling Problem.” Complexity, 2019(8683472), 1-11. doi:<a href="https://doi.org/10.1155/2019/8683472">10.1155/2019/8683472</a>, <a href="http://www.hindawi.com/journals/complexity/2019/8683472/">http://www.hindawi.com/journals/complexity/2019/8683472/</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC804">P2019ATLMAFTJSSP</a></li>
<dt id="PLC">PLC</dt><dd>Peng B, Lü Z, Cheng TCE (2015). “A Tabu Search/Path Relinking Algorithm to Solve the Job Shop Scheduling Problem.” Computers & Operations Research, 53, 154-164. doi:<a href="https://doi.org/10.1016/j.cor.2014.08.006">10.1016/j.cor.2014.08.006</a>, A February 2014 preprint is available as arXiv:1402.5613v1 [cs.DS], <a href="http://arxiv.org/abs/1402.5613">http://arxiv.org/abs/1402.5613</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC817">PLC2015ATSPRATSTJSSP</a></li>
<dt id="PM">PM</dt><dd>Pezzella F, Merelli E (2000). “A Tabu Search Method Guided by Shifting Bottleneck for the Job Shop Scheduling Problem.” European Journal of Operational Research (EJOR), 120(2), 297-310. doi:<a href="https://doi.org/10.1016/S0377-2217(99">10.1016/S0377-2217(99)00158-7</a>00158-7), <a href="https://www2.cs.sfu.ca/CourseCentral/827/havens/papers/topic%2310(JobShop)/Tabu%20With%20Shifting.pdf">https://www2.cs.sfu.ca/CourseCentral/827/havens/papers/topic%2310(JobShop)/Tabu%20With%20Shifting.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC831">PM2000ATSMGBSBFTJSSP</a></li>
<dt id="PPH">PPH</dt><dd>Pérez E, Posada M, Herrera F (2012). “Analysis of New Niching Genetic Algorithms for Finding Multiple Solutions in the Job Shop Scheduling.” Journal of Intelligent Manufacturing, 23(3), 341-356. doi:<a href="https://doi.org/10.1007/s10845-010-0385-4">10.1007/s10845-010-0385-4</a>, reports result 595.97 for la03, which is below the lower bound of 597 and thus not included in our data set. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC845">PPH2012AONNGAFMSITJSS</a></li>
<dt id="PSV">PSV</dt><dd>Pardalos PM, Shylo OV, Vazacopoulos A (2010). “Solving Job Shop Scheduling Problems Utilizing the Properties of Backbone and "Big Valley".” Computational Optimization and Applications, 47(1), 61-76. doi:<a href="https://doi.org/10.1007/s10589-008-9206-5">10.1007/s10589-008-9206-5</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC859">PSV2010SJSSPUTPOBABV</a></li>
<dt id="QL">QL</dt><dd>Qiu X, Lau HYK (2014). “An AIS-based Hybrid Algorithm for Static Job Shop Scheduling Problem.” Journal of Intelligent Manufacturing, 25(3), 489-503. doi:<a href="https://doi.org/10.1007/s10845-012-0701-2">10.1007/s10845-012-0701-2</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC872">QL2014AABHAFSSSP</a></li>
<dt id="RNK">RNK</dt><dd>Raeesi N. MR, Kobti Z (2012). “A Knowledge-Migration-Based Multi-Population Cultural Algorithm to Solve Job Shop Scheduling.” In Youngblood GM, McCarthy PM (eds.), Proceedings of the Twenty-Fifth International Florida Artificial Intelligence Research Society Conference (FLAIRS'12), May 23-25, 2012, Marco Island, FL, USA. ISBN 978-1-57735-558-8, <a href="http://www.aaai.org/ocs/index.php/FLAIRS/FLAIRS12/paper/view/4378/4768">http://www.aaai.org/ocs/index.php/FLAIRS/FLAIRS12/paper/view/4378/4768</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC885">RNK2012AKMBMPCATSJSS</a></li>
<dt id="S">S</dt><dd>Schilham R (2000). “Results listed on Éric Taillard's Page.” see also http://jobshop.jjvh.nl/, <a href="http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html">http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC907">S200RLOETP</a></li>
<dt id="S2">S2</dt><dd>Shylo OV (2019). “Job Shop Scheduling (Personal Homepage).” <a href="http://optimizizer.com/jobshop.php">http://optimizizer.com/jobshop.php</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC897">S2019JSSPH</a></li>
<dt id="SB">SB</dt><dd>Sabuncuoğlu İ, Bayiz M (1999). “Job Shop Scheduling with Beam Search.” European Journal of Operational Research (EJOR), 118(2), 390-412. doi:<a href="https://doi.org/10.1016/S0377-2217(98">10.1016/S0377-2217(98)00319-1</a>00319-1), <a href="http://yoksis.bilkent.edu.tr/doi_getpdf/articles/10.1016-S0377-2217(98)00319-1.pdf">http://yoksis.bilkent.edu.tr/doi_getpdf/articles/10.1016-S0377-2217(98)00319-1.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC916">SB1999JSSWBS</a></li>
<dt id="SIS">SIS</dt><dd>Shi G, Iima H, Sannomiya N (1997). “New Encoding Scheme for Solving Job Shop Problems by Genetic Algorithm.” In Proceedings of the 35th IEEE Conference on Decision and Control (CDC'96), December 11-13, 1996, Kobe, Japan, volume 4, 4395-4400. ISBN 0-7803-3590-2, doi:<a href="https://doi.org/10.1109/CDC.1996.577484">10.1109/CDC.1996.577484</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC930">SIS1997NESFSJSPBGA</a></li>
<dt id="SK">SK</dt><dd>Sakuma J, Kobayashi S (2000). “Extrapolation-Directed Crossover for Job-Shop Scheduling Problems: Complementary Combination with JOX.” In Whitley LD, Goldberg DE, Cantú-Paz E, Spector L, Parmee IC, Beyer H (eds.), Proceedings of the Genetic and Evolutionary Computation Conference (GECCO'00), July 8-12, 2000, Las Vegas, NV, USA, 973-980. ISBN 1-55860-708-0. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC943">SK2000EDCFJSSPCCWJ</a></li>
<dt id="SMM">SMM</dt><dd>Sahana SK, Mukherjee I, Mahanti PK (2018). “Parallel Artificial Bee Colony (PABC) for Job Shop Scheduling Problems.” Advances in Information Sciences and Service Sciences (AISS), 10(3), 1-11. reports 661 as result for abz9 which is below the lower bound 678 and thus not included in our data set, <a href="http://www.globalcis.org/aiss/ppl/AISS3877PPL.pdf">http://www.globalcis.org/aiss/ppl/AISS3877PPL.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC955">SMM2018PABCPFJSSP</a></li>
<dt id="SS">SS</dt><dd>Shylo OV, Shams H (2018). “Boosting Binary Optimization via Binary Classification: A Case Study of Job Shop Scheduling.” cs.AI/math.OC abs/1808.10813, arXiv. Many results are available in the GitHub repository https://github.com/quasiquasar/gta-jobshop-data. We just use a subset (namely, samples after 3, 5, 30, and 60 minutes, and the end results) to compute statistics. The paper reports some new bks for which the creating runs are not contained in the GitHub repository, verified via email with the authors, as well as bound 6196 for both dmu74 and dmu75. Other results have been published on Prof. Shylo's website http://optimizizer.com/DMU.php for the same paper (including dmu17), <a href="https://arxiv.org/pdf/1808.10813">https://arxiv.org/pdf/1808.10813</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC969">SS2018BBOVBCACSOJSS</a></li>
<dt id="SSS">SSS</dt><dd>Sharma N, Sharma H, Sharma A (2018). “Beer Froth Artificial Bee Colony Algorithm for Job-Shop Scheduling Problem.” Applied Soft Computing Journal (ASOC), 68, 507-524. doi:<a href="https://doi.org/10.1016/j.asoc.2018.04.001">10.1016/j.asoc.2018.04.001</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC982">SSS2018BFABCAFJSSP</a></li>
<dt id="SWV">SWV</dt><dd>Storer RH, Wu SD, Vaccari R (1992). “New Search Spaces for Sequencing Problems with Application to Job Shop Scheduling.” Management Science, 38(10), 1495-1509. doi:<a href="https://doi.org/10.1287/mnsc.38.10.1495">10.1287/mnsc.38.10.1495</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC993">SWV1992NSSFSPWATJSS</a></li>
<dt id="T">T</dt><dd>Taillard ÉD (1993). “Benchmarks for Basic Scheduling Problems.” European Journal of Operational Research (EJOR), 64(2), 278-285. doi:<a href="https://doi.org/10.1016/0377-2217(93">10.1016/0377-2217(93)90182-M</a>90182-M). BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1005">T199BFBSP</a></li>
<dt id="V">V</dt><dd>Vaessens RJM (1995). “Results listed on Éric Taillard's Page.” see also http://jobshop.jjvh.nl/, <a href="http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html">http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1027">V1995RLOETP</a></li>
<dt id="V1">V1</dt><dd>Vaessens RJM (1996). “Addition to John Edward Beasley's OR Library.” see also http://jobshop.jjvh.nl/, <a href="http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/jobshop1.txt">http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/jobshop1.txt</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1018">V1996ATJEBOL</a></li>
<dt id="VAL">VAL</dt><dd>Vaessens RJM, Aarts EHL, Lenstra JK (1996). “Job Shop Scheduling by Local Search.” INFORMS Journal on Computing, 8(3), 302-317. doi:<a href="https://doi.org/10.1287/ijoc.8.3.302">10.1287/ijoc.8.3.302</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1036">VAL1996JSSBLS</a></li>
<dt id="vH">vH</dt><dd>van Hoorn JJ (2015). “Job Shop Instances and Solutions.” <a href="http://jobshop.jjvh.nl">http://jobshop.jjvh.nl</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1049">vH2015JSIAS</a></li>
<dt id="vH2">vH2</dt><dd>van Hoorn JJ (2016). Dynamic Programming for Routing and Scheduling: Optimizing Sequences of Decisions. Ph.D. thesis, Vrije Universiteit Amsterdam, Amsterdam, The Netherlands. <a href="http://jobshop.jjvh.nl/dissertation">http://jobshop.jjvh.nl/dissertation</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1057">vH2016DPFRASOSOD</a></li>
<dt id="VLS">VLS</dt><dd>Vilím P, Laborie P, Shaw P (2015). “Failure-Directed Search for Constraint-Based Scheduling.” In Michel L (ed.), International Conference Integration of AI and OR Techniques in Constraint Programming: Proceedings of 12th International Conference on AI and OR Techniques in Constriant Programming for Combinatorial Optimization Problems (CPAIOR'2015), May 18-22, 2015, Barcelona, Spain, volume 9075 series Lecture Notes in Computer Science (LNCS) and Theoretical Computer Science and General Issues book sub series (LNTCS), 437-453. ISBN 978-3-319-18007-6, doi:<a href="https://doi.org/10.1007/978-3-319-18008-3_30">10.1007/978-3-319-18008-3_30</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1070">VLS2015FDSFCBS</a></li>
<dt id="VLS2">VLS2</dt><dd>Vilím P, Laborie P, Shaw P (2015). “Failure-Directed Search for Constraint-Based Scheduling - Detailed Experimental Results.” The detailed experimental results of the paper "Failure-Directed Search for Constraint-Based Scheduling" by the same authors, in International Conference Integration of AI and OR Techniques in Constraint Programming: Proceedings of 12th International Conference on AI and OR Techniques in Constriant Programming for Combinatorial Optimization Problems (CPAIOR'2015), May 18-22, 2015, Barcelona, Spain, pages 437-453, doi:10.1007/978-3-319-18008-3_30., <a href="http://vilim.eu/petr/cpaior2015-results.pdf">http://vilim.eu/petr/cpaior2015-results.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1086">VLS2015FDSFCBSDER</a></li>
<dt id="W">W</dt><dd>Weise T (2019-2020). “jsspInstancesAndResults: Results, Data, and Instances of the Job Shop Scheduling Problem.” A GitHub repository with the common benchmark instances for the Job Shop Scheduling Problem as well as results from the literature, both in form of CSV files as well as R program code to access them., <a href="https://github.com/thomasWeise/jsspInstancesAndResults">https://github.com/thomasWeise/jsspInstancesAndResults</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1096">W2019JRDAIOTJSSP</a></li>
<dt id="WCL">WCL</dt><dd>Wang L, Cai J, Li M (2016). “An Adaptive Multi-Population Genetic Algorithm for Job-Shop Scheduling Problem.” Advances in Manufacturing, 4(2), 142-149. doi:<a href="https://doi.org/10.1007/s40436-016-0140-y">10.1007/s40436-016-0140-y</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1107">WCL2016AAMPGAFJSSP</a></li>
<dt id="WD">WD</dt><dd>Wang X, Duan H (2014). “A Hybrid Biogeography-based Optimization Algorithm for Job Shop Scheduling Problem.” Computers & Industrial Engineering, 73, 96-114. doi:<a href="https://doi.org/10.1016/j.cie.2014.04.006">10.1016/j.cie.2014.04.006</a>, <a href="http://hbduan.buaa.edu.cn/papers/2014CAIE_Wang_Duan.pdf">http://hbduan.buaa.edu.cn/papers/2014CAIE_Wang_Duan.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1120">WD2014AHBBOAFJSSP</a></li>
<dt id="WGK">WGK</dt><dd>Weckman GR, Ganduri CV, Koonce DA (2008). “A Neural Network Job-Shop Scheduler.” Journal of Intelligent Manufacturing, 19, 191-201. doi:<a href="https://doi.org/10.1007/s10845-008-0073-9">10.1007/s10845-008-0073-9</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1133">WGK2008ANNJSS</a></li>
<dt id="WTC">WTC</dt><dd>Wang S, Tsai C, Chiang M (2018). “A High Performance Search Algorithm for Job-Shop Scheduling Problem.” In Shakshuki EM, Yasar A (eds.), The 9th International Conference on Emerging Ubiquitous Systems and Pervasive Networks (EUSPN'18) / The 8th International Conference on Current and Future Trends of Information and Communication Technologies in Healthcare (ICTH'18) / Affiliated Workshops, November 5-8, 2018, Leuven, Belgium, volume 141 series Procedia Computer Science, 119-126. doi:<a href="https://doi.org/10.1016/j.procs.2018.10.157">10.1016/j.procs.2018.10.157</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1146">WTC2018AHPSAFJSSP</a></li>
<dt id="YN">YN</dt><dd>Yamada T, Nakano R (1992). “A Genetic Algorithm Applicable to Large-Scale Job-Shop Instances.” In Männer R, Manderick B (eds.), Proceedings of Parallel Problem Solving from Nature 2 (PPSN II), September 28-30, 1992, Brussels, Belgium, 281-290. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1160">YN1992AGAATLSJSI</a></li>
<dt id="YN1">YN1</dt><dd>Yamada T, Nakano R (1997). “Genetic Algorithms for Job-Shop Scheduling Problems.” In Proceedings of Modern Heuristic for Decision Support, March18-19, 1997, London, England, UK, 67-81. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1172">YN1997GAFJSSP</a></li>
<dt id="ZHZ">ZHZ</dt><dd>Zupan H, Herakovič N, Žerovnik J (2016). “A Heuristic for the Job Shop Scheduling Problem.” In Papa G, Mernik M (eds.), The 7th International Conference on Bioinspired Optimization Methods and their Application (BIOMA'16), May 18-20, 2016, Bled, Slovenia, 187-198. ISBN 978-961-264-093-4, <a href="http://bioma.ijs.si/conference/BIOMA2016Proceedings.pdf">http://bioma.ijs.si/conference/BIOMA2016Proceedings.pdf</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1182">ZHZ2016AHFTJSSP</a></li>
<dt id="ZLR">ZLR</dt><dd>Zhang C, Li P, Rao Y, Guan Z (2008). “A Very Fast TS/SA Algorithm for the Job Shop Scheduling Problem.” Computers & Operations Research, 35(1), 282-294. doi:<a href="https://doi.org/10.1016/j.cor.2006.02.024">10.1016/j.cor.2006.02.024</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1197">ZLRG2008AVFTAFTJSSP</a></li>
<dt id="ZRL">ZRL</dt><dd>Zhang C, Rao Y, Li P (2008). “An Effective Hybrid Genetic Algorithm for the Job Shop Scheduling Problem.” International Journal of Advanced Manufacturing Technology (JAMT), 39, 965-974. doi:<a href="https://doi.org/10.1007/s00170-007-1354-8">10.1007/s00170-007-1354-8</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1210">ZRL2008AEHGAFTJSSP</a></li>
<dt id="ZSR">ZSR</dt><dd>Zhang C, Shao X, Rao Y, Qiu H (2008). “Some New Results on Tabu Search Algorithm Applied to the Job-Shop Scheduling Problem.” In Jaziri W (ed.), Tabu Search. IntechOpen, London, England, UK. ISBN 978-3-902613-34-9, doi:<a href="https://doi.org/10.5772/5593">10.5772/5593</a>, <a href="http://www.intechopen.com/books/tabu_search/some_new_results_on_tabu_search_algorithm_applied_to_the_job-shop_scheduling_problem">http://www.intechopen.com/books/tabu_search/some_new_results_on_tabu_search_algorithm_applied_to_the_job-shop_scheduling_problem</a>. BibTeX:<a href="data-raw/bibliography/bibliography.bib#LC1222">ZSRQ2008SNROTSAATTJSSP</a></li>
</dl>
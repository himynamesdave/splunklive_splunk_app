#Splunk>live! App

##Overview:

![SplunkLive App Twitter](https://raw.githubusercontent.com/himynamesdave/splunklive_splunk_app/master/static/screenshot-twitter.jpg)

![SplunkLive App Instagram](https://raw.githubusercontent.com/himynamesdave/splunklive_splunk_app/master/static/screenshot-instagram.jpg)

An app that visualises Tweets / Instagram images containing #splunklive & #splunk.

##Instructions:

**Get the app**

[Download and install the Splunk>live! App](https://splunk.box.com/s/kg0fg64w48k4plj05s4v3ngrvi8x9clv) (Splunkers only) onto your Splunk Instance.

If you are not a Splunker, you can copy this repository into your Splunk Instances app directory: $SPLUNK HOME > etc > apps

**Install the "REST API Modular Input app**

Copy the folder SPLUNK HOME/etc/apps/splunklive_splunk_app/install/rest_ta to SPLUNK HOME/etc/apps/

This will install the official REST API modular input created by Damien Dallimore that is used for connecting to the Instagram API. This version of rest_ta includes some custom python response handlers to handle the Instagram API json format. These are not included in the REST API Modular input app that can be found on Splunkbase.

If you have downloaded the app from the Box link above, all you need to do now is "Enable Inputs" in: Settings > Data Inputs > REST. Config is now complete.

If you did not download the app from the Box link above, follow the instructions below.

##Configure Twitter Feed

**Get your Twitter API keys**

[Instructions on how to do this here: steps 1-2](http://blogs.splunk.com/2014/07/03/splunking-social-media-tracking-tweets/).

[You can also use these keys (Splunkers only)](https://splunk.box.com/s/qkjsk55anrswmkmthhavuhgtwv1b5520)

**Add your Twitter API kets to the to the "SplunkLiveTwitterFeed" REST input**

To do this navigate to Settings > Data Inputs > REST > "SplunkLiveTwitterFeed".

Replace the missing API keys with the ones you have just generated during step 2, then hit "save". Note: you can also change the tweets collected on this page. By default the app will track all tweets with the hashtag #splunklive. If you want to change the hashtag, or add others, simply change the URL arguments field.

e.g:
URL Arguments: track=#splunk,#bigdata,#mytag^stall_warnings=true

**Enable input**

To do this navigate to Settings > Data Inputs > REST. For the "SplunkLiveTwitterFeed" select "Enable".

##Configure Instagram Feed

**Get your Instagram API keys**

[Instructions on how to do this here: steps 1-2](http://blogs.splunk.com/2015/05/15/instasplunk/).

[You can also use these keys (Splunkers only)](https://splunk.box.com/s/qkjsk55anrswmkmthhavuhgtwv1b5520)

**Add your Instagram API kets to the to the "SplunkInstagramFeed" / "SplunkInstagramFeed" REST input**

Add your Instagram API kets to the to the "SplunkInstagramFeed" and "SplunkInstagramFeed" REST input. To do this navigate to Settings > Data Inputs > REST > "SplunkInstagramFeed" / "SplunkInstagramFeed".

Replace the access token, client ID and client secret for these Instagram REST Inputs with those just created.

**Enable inputs**

To do this navigate to Settings > Data Inputs > REST. For the "SplunkInstagramFeed" / "SplunkInstagramFeed" select "Enable".

##Final (important) step

**Restart Splunk**

**Profit**

##Top tip:

Do all these steps 2 hours before the event begins to allow the index to populate with some tweets and images.

##Say hi (or help!):

dgreenwood@splunk.com

p.s You can contribute to this app here: https://github.com/himynamesdave/splunklive_splunk_app

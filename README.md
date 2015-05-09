Splunk>live! App
===

Overview:
---

![SplunkLive App](https://raw.githubusercontent.com/himynamesdave/splunklive_splunk_app/master/static/screenshot.jpeg)

An app that visualises tweets containing #splunklive.

Instructions:
---

1. Download and install the Splunk>live! App (https://github.com/himynamesdave/splunklive_splunk_app/raw/master/splunklive_splunk_app.tar.gz) onto your Splunk Instance.

2. Download and install the Splunk REST API Modular Input (https://splunkbase.splunk.com/app/1546/) onto your Splunk Instance.

3. Get your Twitter API keys. [Instructions on how to do this here: steps 1-2](http://blogs.splunk.com/2014/07/03/splunking-social-media-tracking-tweets/).

4. Add your Twitter API kets to the to the "SplunkLiveTwitterFeed" REST input. To do this navigate to Settings > Data Inputs > REST > "SplunkLiveTwitterFeed". Replace the missing API keys with the ones you have just generated during step 2, then hit "save". Note: you can also change the tweets collected on this page. By default the app will track all tweets with the hashtag #splunklive. If you want to change the hashtag, or add others, simply change the URL arguments field. e.g:
URL Arguments: track=#splunk,#bigdata,#mytag^stall_warnings=true

5. Enable input. To do this navigate to Settings > Data Inputs > REST. For the "SplunkLiveTwitterFeed" select "Enable".

6. Restart Splunk.

7. Profit.

More info:
---

Ideally do all these steps 2 hours before the event begins to allow the index to populate with some tweets.

There is one dashboard in this app: #SplunkLive Twitter Stream. This is automatically configured to only show tweets for "today".

Say hi (or help!):
---

dgreenwood@splunk.com

p.s You can contribute to this app here: https://github.com/himynamesdave/splunklive_splunk_app

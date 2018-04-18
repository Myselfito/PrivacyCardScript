# PrivacyCardScript
Privacy Card Script by chexmdc

This script allows you to bulk create, close, pause and resume your Privacy cards. All you need configure to run it properly is a token, a session id and etag string that you can find on Chrome developer tools in your Privacy account.

To get this token just log in to your Privacy account, open the Network tab through developer tools, go to one of your Privacy cards and do an action such as Pause or Resume. You will see the API post session for that action appear in the Network log. Click the request and look for the "token", "etag", and "sessionid" string in the cookies of that request. Copy each string and put it in config.py before running. Those are basically your API keys. They change about every couple hours.

I made config a py file as I got lazy to make a real config file. If anyone wants to add anything to the script feel free.

Any questions you may dm me on twitter @chexmdc

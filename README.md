# InstaScope 🔎📸

InstaScope is an **OSINT** tool on Instagram to collect, analyze, and run reconnaissance.

Disclaimer: **FOR EDUCATIONAL PURPOSE ONLY! The contributors do not assume any responsibility for the use of this tool.**

Warning: It is advisable to **not** use your own/primary account when using this tool.

## Tools and Commands 🧰

InstaScope offers an interactive shell to perform analysis on Instagram account of any users by its nickname. You can get:

```text
- addrs           Get all registered addressed by target photos
- captions        Get user's photos captions
- comments        Get total comments of target's posts
- followers       Get target followers
- followings      Get users followed by target
- fwersemail      Get email of target followers
- fwingsemail     Get email of users followed by target
- fwersnumber     Get phone number of target followers
- fwingsnumber    Get phone number of users followed by target
- hashtags        Get hashtags used by target
- info            Get target info
- likes           Get total likes of target's posts
- mediatype       Get user's posts type (photo or video)
- photodes        Get description of target's photos
- photos          Download user's photos in output folder
- propic          Download user's profile picture
- stories         Download user's stories  
- tagged          Get list of users tagged by target
- wcommented      Get a list of user who commented target's photos
- wtagged         Get a list of user who tagged target
```

You can find detailed commands usage [here](doc/COMMANDS.md).|
[Commands](doc/COMMANDS.md) |
## FAQ
1. **Can I access the contents of a private profile?** No, you cannot get information on private profiles. You can only get information from a public profile or a profile you follow. The tools that claim to be successful are scams!
2. **What is and how I can bypass the `challenge_required` error?** The `challenge_required` error means that Instagram notice a suspicious behavior on your profile, so needs to check if you are a real person or a bot. To avoid this you should follow the suggested link and complete the required operation (insert a code, confirm email, etc)


## Installation ⚙️

1. Fork/Clone/Download this repo

    `git clone https://github.com/letchupkt/InstaScope.git`

2. Navigate to the directory

    `cd InstaScope`
  
3. Run `pip install -r requirements.txt`

4. Run the main.py script in one of two ways

    * As an interactive prompt `python3 main.py `
    * Or execute your command straight away `python main.py `


## Developer 👨‍💻

Developed by [@letchupkt](https://github.com/letchupkt)

## External library 🔗

[Instagram API](https://github.com/ping/instagram_private_api)

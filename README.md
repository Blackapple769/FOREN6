
```
-------------------------------------------------------------
$$$$$$$$\  $$$$$$\  $$$$$$$\  $$$$$$$$\ $$\   $$\  $$$$$$\  
$$  _____|$$  __$$\ $$  __$$\ $$  _____|$$$\  $$ |$$  __$$\ 
$$ |      $$ /  $$ |$$ |  $$ |$$ |      $$$$\ $$ |$$ /  \__|
$$$$$\    $$ |  $$ |$$$$$$$  |$$$$$\    $$ $$\$$ |$$$$$$$\  
$$  __|   $$ |  $$ |$$  __$$< $$  __|   $$ \$$$$ |$$  __$$\ 
$$ |      $$ |  $$ |$$ |  $$ |$$ |      $$ |\$$$ |$$ /  $$ |        
$$ |       $$$$$$  |$$ |  $$ |$$$$$$$$\ $$ | \$$ | $$$$$$  |        
\__|       \______/ \__|  \__|\________|\__|  \__| \______/         
-------------------------------------------------------------
```

Author: Jon47

Please consider donating!
Bitcoin Address: bc1qdwcfrgzwdcsn52937nf5f4vwcam9tn89kyye3y

The configuration information is in 
the `foren6.py` file in the data.

## About FOREN6
This is a forensics program. Designed to be 
downloaded onto a remote device (Windows) 
to glean information.The program has multiple 
ways of getting data such as a keylogger, 
screenshots and system/wifi information including 
wifi passwords.

Cooldowns for gathering data in the configuration file are listed in seconds.
It is recomended to have over 60 seconds for screenshots.

## Disclaimer
**Jon47 does not condone any malicious action carried out 
using this program. It is for educational purposes only
and should NOT be used to carry out attacks on machines you 
do not have explicit permission to get access.**

## Important Configuration Information
The `info_email_receiver` configuration option needs to be set to an email address you wish to recieve the data from. The `sender_email_address` and
`sender_email_password` should be a burner account that you 
will not care about if it is lost. 

If you are using an email platform such as Gmail for your burner account (`sender_email_address`), you will need to enable an option to let "less secure apps" access your account. This allows a 3rd-party program to connect with the account.

## Manually Building FOREN6
If you are building FOREN6 from source, you will need to ensure Python 3 is added to your PATH, as well as installing the following dependencies:

- emails
- pyinput==1.6.8
- pyautogui
- requests
- nuitka
- secure-smtplib

To convert to an EXE file, run the following in your terminal:

`nuitka --mingw64 --windows-disable-console foren6.py`




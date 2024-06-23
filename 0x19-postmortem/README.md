# June 21st Major outage postmortem; Tale of a Typographical Terror
First practice postmortem ..(Based on a web stack debugging task).. mostly made-up, thankfully!

## Issue summary:
As of June 21st 2:55 PM GMT untill June 22nd 10:21 GMT, The time when the Word Press went scilent 100% of users faced a downtime in the entire wordpress service as a result of a internal server issue caused by.. ...
a typo in file extention in one of the major configuration files. 
Rings a bell?

## Timeline
- **June 21st 2:51 PM GMT:** Alert raised about a downtime.
- **Detection:** The responsible monitoring system smelled the smoke of downtime.
- **Initial Assumptions:** Configuration bugs in PHP or Apache2, potential database issues.
- **Misleading Investigations:** checking goasts of network issues and the daemons of the server.
- **Escalation:** Incident was escalated to the DevOps team, led by Loay Al-Said.
- **Resolution:** Issue resolved by fixing the typo in the configuration file name.


## Root cause and solution
- Using strace to trace the process uid of apache. This line here
```
	open("/var/www/html/wp-includes/class-wp-locale.phpp", O_RDONLY) = -1 ENOENT (No such file or directory)
```
shows that the server is trying to get the class-wp-locale code from a file exists only on fairy tale. Ever seen a server look for "class-wp-locale.phpp"? Yeah, neither had we. 😅

- The issue was solved by removing the trailing 'P' in the file name in wp-settings.php file

## Corrective and Preventative Measures:
- **Immediate Actions:**
	* Having On-call team for resolutoin once issues detected
	* Having a policy to avoid direct changes  on the production branch.
- **Preventative Measures:**
	* Ensure updates happen with a time span in day to test and rollback
	* Schedule regular testing sessions following system changes.
	* Implement automated tests to check for common configuration errors.
	* Code reviews are your friend: Double (or triple) checking code can help identify typos and other errors before deployment.
	* Broadly testing the system after upgrades

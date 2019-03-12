## Terminologies
----
* Source: Where an attacker can inject payload. ex: input field  
* Sink: Where the payload will arrive or reflected. ex: insecure code

* Direct attack: 
  * Where we target the application directly for DB takeover,data leakage.
  * Example: SQL Injection, SSRF, RCE, LFI.
* Indirect Attack:
  * Where we target the application users for stealing session,passwords.
  * In this case, the attacker needs to rely on user browser's features.
  * Example: XSS, Clickjacking, Address Spoofing.

## Charset and URL's
----
* Earlier there was ASCII which only supported 128 character out of which 95 were human readable character including A through Z, digits from 0 to 9 and couple of punctuations and special characters.
  Since it included characters limited to only one language(english), different countries started to introduce their own standards specifications for thier own eg: `ISO 8859-*, CP720, CP875 etc.`
  Finally Unicode was introduced which has 1,114,112 code points which can be used to form all kind of letter and symbols.
  
#### Common Parts of an URL

>http :// user:pass@ www . foo . de : port / folder / file.ext ? x=y & y=z # frag-id

* Protocol / Scheme ➔ http 
* Optional HTTP Auth information ➔ user:pass
* Sub-Domain(s) ➔ www
* Domain ➔ foo
* Top-Level Domain ➔ de
* Port
* Folder
* Filename and -extension
* GET / CGI Parameters
* Fragment identifier


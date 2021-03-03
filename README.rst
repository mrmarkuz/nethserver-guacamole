====================
nethserver-guacamole
====================

Apache Guacamole is a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH.

LDAP Properties
===============

Nethserver-guacamole tries to guess the right settings.

For custom ldap encryption (none, ssl or starttls):

  config setprop guacd Encryption none

For use a custom ldap port (usually 389 or 636):

  config setprop guacd ldapPort 389

For changing the LDAP username attribute:

  config setprop guacd usernameAttribute samaccountname,userprincipalname

Links
=====

https://community.nethserver.org/t/howto-install-guacamole/9047

# Author: David Samuel

# Add user on ad

import ldap
import ldap.modlist as modlist

try:

    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    l = ldap.initialize("ldaps://0.0.0.0:636/")

    l.simple_bind_s("user@domain.com", "password")

    dn="cn=John,ou=Users,dc=domain,dc=com"

    # A dict to help build the "body" of the object
    attrs = {}
    attrs['objectclass'] = ['User']
    attrs['cn'] = 'John'
    attrs['sAMAccountname'] = 'John Tiger'
    attrs['userPassword'] = 'password'
    attrs['mail'] = 'tiger@domain.com'

    ldif = modlist.addModlist(attrs)

    l.add_s(dn,ldif)

    l.unbind_s()

except ldap.INVALID_CREDENTIALS, e:
    print e
except ldap.LDAPError, e:
    print e
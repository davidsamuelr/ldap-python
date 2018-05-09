# Author: David Samuel

# Delete user on ad

import ldap

try:

    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    l = ldap.initialize("ldaps://0.0.0.0:636/")

    l.simple_bind_s("user@domain.com", "password")

    dn="cn=user,ou=Users,dc=domain,dc=com"

    l.delete_s(dn)

    l.unbind_s()

except ldap.INVALID_CREDENTIALS, e:
    print e
except ldap.LDAPError, e:
    print e
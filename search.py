# Author: David Samuel

import ldap

try:

    l = ldap.initialize("ldap://0.0.0.0")

    l.protocol_version = ldap.VERSION3

    l.simple_bind_s("user@domain.com", "password")

    print "Conexao estabelecida."

    # only users
    # ldap_result = l.search_s('ou=USERS, dc=domain,dc=com', ldap.SCOPE_SUBTREE, '(objectclass=person)',['cn', 'mail'])

    ldap_result = l.search_s('ou=USERS, dc=domain,dc=com', ldap.SCOPE_SUBTREE, '(cn=David Samuel)',['cn', 'mail'])

    print ldap_result

except ldap.INVALID_CREDENTIALS, e:
    print e

except ldap.LDAPError, e:
    print e

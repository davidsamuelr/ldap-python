# Author: David Samuel

import ldap
import ldap.modlist as modlist

ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

l = ldap.initialize("ldaps://0.0.0.0:636/")

l.simple_bind_s("user@domain.com", "password")

dn = "cn=David Samuel,ou=Users,dc=domain,dc=com"

old = {'mail':['david@gmail.com']}
new = {'mail':['davidsamuel@gmail.com']}

ldif = modlist.modifyModlist(old,new)

l.modify_s(dn,ldif)

l.unbind_s()
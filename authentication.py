# Author: David Samuel

# Authentication in AD with ldap

import ldap

try:

	l = ldap.initialize("ldap://0.0.0.0")
	l.protocol_version = ldap.VERSION3
	l.simple_bind_s("user@domain.com", "password")

	print "Conexao estabelecida."

except ldap.INVALID_CREDENTIALS, e:
	print e
except ldap.LDAPError, e:
	print e
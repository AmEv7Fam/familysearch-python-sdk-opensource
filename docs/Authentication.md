* `login(self, username, password)`
Log into FamilySearch using Basic Authentication.
This mechanism is available only to approved developer keys.

* `oauth_desktop_login(self, ruri=None)`
Log into FamilySearch using OAuth2 Authentication.
This is primarily a convenience function for desktop apps.
Not normally intended for production apps, but should
work while waiting for approval for password login.
Default Redirect URI is "http://localhost:63342/fslogin",
but you can set your own as a paramater.

* `oauth_code_login(self, code)`
Convenience function for Web servers to log into FamilySearch
with the token code FamilySearch hands you.

* `unauthenticated_login(self, ip_address)`
Log into FamilySearch without authenticating.
Has very limited read-only access.
Not intended for general use.

* `logout(self)`
Log the current session out of FamilySearch.

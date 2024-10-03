# How session is handled?

The game server continues to push three (3) `Set-Cookie` headers.

```http
Set-Cookie: cv=1727151169 // Time? it never changes during requests
Set-Cookie: sk=<token> // This is the session key (token)
Set-Cookie: rc=1 // Request count (auto-increments by 1 server-side)
```

Client will send back those cookies like this:

```http
Cookie: rc=1; sk=<token>; cv=1727151169; 
```

However, sending `Set-Cookie` is mandatory since client tends to forget everything (bruh).
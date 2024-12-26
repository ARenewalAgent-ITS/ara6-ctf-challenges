# QR Note PoC

There is **CSRF** and **XSS**. Then you must bypass the DOMPurify check in the source code using the **htmx**, because the source code is use **htmx** to fetch some api data, so we can use it. Also try to bypass the parser link check up content using regex to string in js.

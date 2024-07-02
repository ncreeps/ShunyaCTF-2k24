## Solution:

Directory Traversal

You can perform a directory traversal attack through the /download.php endpoint by manipulating the ?file parameter. For example, you can access ../index.php by crafting the right request.

---

Service Overview

The given webapp is a service that converts your uploaded file into a .tar.gz archive. Here's how it works:

- You upload a file through a form.
- The service processes the file and creates a tar.gz archive.
- If the upload is successful, you get a link to download the archive.

Here's a bit of the PHP code that handles this:

php
```
function tar($file) {
    // Process the file and create a tar.gz archive
}
```

```
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $file = $_FILES['file'];
    // Handle file upload and archive creation
```
To get the flag, you need to execute remote code on the server. It's located in the root directory.

Accessing the Downloaded File

You can retrieve the uploaded and archived file using the /download.php endpoint:

php
```
if ($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['file'])) {
    // Decode and serve the requested file
```
Again, by manipulating the ?file parameter, you can access other files on the server.

Command Injection

There is a command injection vulnerability in the index.php file at line 24. The filename parameter is user-controlled, which allows you to inject arbitrary commands. 

For example, you can list files in the directory:

1. ls   
2. ls ..

To execute commands at the root level, you can use base64 encoding to bypass restrictions:
```
ls / -> ls $(echo Lwo= | base64 -d)
```

```
cat /badmosi_k4rk3_fl4g_m1lg4y4.txt -> cat $(echo L2JhZG1vc2lfazRyazNfZmw0Z19tMWxnNHk0LnR4dA== | base64 -d)
```

This way, you can access and read the contents of sensitive files.
flag: 0CTF{b4dm0s_bh4y_k4_fl4g}

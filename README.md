# Galeria
Un proyecto simple de una galeria usando Django :) 
Link del proyecto, por si gustas verlo: https://gallery.jackcloudman.me/
# 2 Instalando galeria
## 1 Instalar nginx  
Ubuntu/Debian: <code>sudo apt-get install nginx</code>  
ArchLinux/Manjaro: <code>sudo pacman -S nginx</code>  
CentOS: <code>sudo yum install nginx</code>
## 2 Descargar el repositorio  
<code>cd /usr/share/nginx/html/</code><br>
<code>sudo git clone https://github.com/JackCloudman/galeria.git</code>
## 3 Instalar virtualenv
Usa el siguiente comando:
<code>sudo python3 -m pip install virtualenv</code>  
NOTA: Si no tienes pip instalalo -w- (<code>sudo apt-get install python3-pip</code>)
## 4 Crear entorno virtual
* Ve a la carpeta donde quieras crearlo, yo lo haré en la carpeta principal  
<code>cd ~</code><br>
<code>  virtualenv Django --python=python3</code>
## 5 Instalar bibliotecas
<code>source ~/Django/bin/activate</code><br>
<code>cd /usr/share/nginx/html/galeria/</code><br>
<code>pip install -r requirements.txt</code><br>
## 6 Configurar nginx
* Edita el archivo /etc/nginx/nginx.conf
* Eliminar todo y pegar lo que hay en: https://github.com/JackCloudman/galeria/blob/master/nginx.conf
## Editar settings.py
* Editar /usr/share/nginx/html/galeria/Galeria/settings.py
* El la linea 28 cambiar ALLOWED_HOSTS = ['localhost'] por tu IP(puedes dejar localhost)
# Arrancando el servidor
<code>cd /usr/share/nginx/html/galeria/</code><br>
<code>gunicorn Galeria.wsgi</code><br>

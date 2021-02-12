# app-with-magiclinks
<h2>About</h2>
<div>
Simple app doesn`t require user to input email/password to have access.

</div>
 <h2>Getting Started</h2>
<h3>PREREQUISITES</h3>
<ul>
    <li>Python 3</li>
    <li>pip3 to install dependencies</li>
 </ul>
<h3>INSTALLING PACKAGES</h3>
<div>
  Open terminal in the directory with project and write there:
<h4>Mac OS:</h4>
<ol>
 <li>Run <code>virtualenv name_of_virtual_env_dir</code> to make virtual environment </li>
 <li>Activate it by <code>source name_of_virtual_env_dir/bin/activate</code></li>
 <li>Run <code>pip3 install -r requirements.txt</code></li>
 </ol>
 <h4>Windows:</h4>
<ol>
 <li>Run <code>python3 -m venv name_of_virtual_env_dir</code> to make virtual environment </li>
 <li>Activate it by <code>name_of_virtual_env_dir\Scripts\activate.bat</code></li>
 <li>Run <code>pip3 install -r requirements.txt</code></li>
 </ol>

<p><i>then in your terminal u'll see:
  <code>(name_of_virtual_env_dir) c:\path\to\working\directory</code></i></p>
</div>

<h3>SET CONGIG</h3>
<div>
Change EMAIL_HOST_USER and EMAIL_HOST_PASSWORD into settings.py on email from which you want to send letters
</div>
<h3>RUN</h3>
<div>
  <ol>
<li>CD into project directory: <code>cd magic_progect</code></li>
<li>Run <code>python3 manage.py runserver</code></li>
<li>Enjoy!</li>
    </ol>
</div>

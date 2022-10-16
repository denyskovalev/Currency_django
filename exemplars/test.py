def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3

#
# # mysite_nginx.conf
#
# # the upstream component nginx needs to connect to
# upstream django {
#     # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
#     server 127.0.0.1:8001; # for a web port socket (we'll use this first)
# }
#
# # configuration of the server
# server {
#     # the port your site will be served on
#     listen      8000;
#     # the domain name it will serve for
#     server_name example.com; # substitute your machine's IP address or FQDN
#     charset     utf-8;
#
#     # max upload size
#     client_max_body_size 75M;   # adjust to taste
#
#     # Django media
#     location /media  {
#         alias /home/den/PycharmProjects/currency_django/app/static;  # your Django project's media files - amend as required
#     }
#
#     location /static {
#         alias /home/den/PycharmProjects/currency_django/app/static; # your Django project's static files - amend as required
#     }
#
#     # Finally, send all non-media requests to the Django server.
#     location / {
#         uwsgi_pass  django;
#         include     /home/den/PycharmProjects/currency_django/app/settings/uwsgi_params; # the uwsgi_params file you installed
#     }
# }
#
# # mysite_uwsgi.ini file
# [uwsgi]
#
# # Django-related settings
# # the base directory (full path)
# chdir           = /home/den/PycharmProjects/currency_django/app
# # Django's wsgi file
# module          = settings.wsgi
# # the virtualenv (full path)
# home            = /home/den/PycharmProjects/currency_django/venv
#
# # process-related settings
# # master
# master          = true
# # maximum number of worker processes
# processes       = 10
# # the socket (use the full path to be safe
# socket          = 0.0.0.0:8001
# # ... with appropriate permissions - may be needed
# # chmod-socket    = 664
# # clear environment on exit
# vacuum          = true

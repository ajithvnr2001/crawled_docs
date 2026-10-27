---
url: https://docs.cloud.google.com/appengine/docs/standard/tools/local-devserver-command/
title: Local development server options \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:40:20.178170+00:00
---

# Local development server options  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/tools/local-devserver-command/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Local development server options Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby

**Note:** The local development server supports only the runtimes that include legacy bundled services: Go, Java, PHP, and Python runtimes.

The local development server (`dev_appserver.py`) is part of the App Engine components of the [gcloud CLI](https://docs.cloud.google.com/sdk/docs). This topic provides advanced information about the `dev_appserver.py` usage.

We recommend that you use standard Python tools, such as `virtualenv` to create isolated environments and `pytest` to run unit tests and integration tests, rather than depending on `dev_appserver`, the local development server provided with the [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs). 

See [Using the Local development server](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#local-dev-server) for more information about local testing.

## Set up the local development server tool

**Important:** Before running the local development server, follow the [setup instructions](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server#set-up).

A sample `dev_appserver.py` command might look as follows:
    
    
    python3 CLOUD_SDK_ROOT/bin/dev_appserver.py OPTION yaml_path FILES
    

Replace the following:

  * CLOUD_SDK_ROOT with the path to the root directory where you installed Google Cloud CLI. The default directory is `./google-cloud-sdk/`.
  * OPTION with a flag supported by the local development server.
  * FILES specifies one or more `app.yaml` files, one per service, for the positional argument `yaml_path`.



For a complete list of options, run the following:
    
    
    python3 CLOUD_SDK_ROOT/bin/dev_appserver.py -h
    

## Common options

The most common options are as follows:

`--admin_host=ADMIN_HOST`
    Host name to which the local development server's administration console should bind (default: localhost).
`--admin_port=ADMIN_PORT`
    Port to which the local development server's administration console should bind (default: 8000).
`--addn_host=ADDN_HOST`
    This argument allows you to allowlist additional HTTP Host header values, so that the server might be made accessible behind a proxy, without having to disable host checking (see `--enable_host_checking`). Additional hosts starting with `*.` allow all subdomains. For example, `*.example.org` allows `host.example.org` but not `sub.host.example.org` or `example.org`. Hosts starting with `**.` allow subdomains of any depth. For example, `**.example.com` allows `host.example.com` and `sub.host.example.com`, but not `example.com`. (default: [])
`--allow_skipped_files=...`
    Make files specified in the `app.yaml` `skip_files` or `static` handles readable by the application (default: False).
`-A APP_ID, --application=...`
    Set the application, overriding the application value from the `app.yaml` file (default: None).
`--appidentity_email_address=...`
    Email address associated with a service account that has a downloadable key. May be `None` for no local application identity (default: None).
`--appidentity_private_key_path=...`
    Path to private key file associated with service account (`.pem` format). Must be set if `appidentity_email_address` is set (default: None).
`--api_host=API_HOST`
    Host name to which the API server should bind (default: localhost).
`--api_port=API_PORT`
    Port to which the server for API calls should bind (default: 0).
`--auth_domain=...`
    Name of the authorization domain to use (default: `gmail.com`).
`--auto_id_policy=...`
    Deprecated. How the local datastore assigns automatic IDs. Options are `sequential` or `scattered` (default: `scattered`).
`--automatic_restart=...`
    Restart instances automatically when files relevant to their module are changed (default: True).
`--blobstore_path=...`
    Path to directory used to store blob contents (defaults to a subdirectory of `--storage_path` if not set) (default: None).
`--clear_datastore=yes|no`
    Clears the datastore data and history files before starting the web server (default: `no`).
`--clear_search_indexes...`
    Clear the search indexes (default: False).
`--custom_entrypoint=...`
    

Specify an entrypoint for custom runtime modules. This is required when such modules are present. Include `{port}` in the string (without quotes) to pass the port number in as an argument (default: ). For instance:
    
    
    --custom_entrypoint="gunicorn -b localhost:{port}
      mymodule:application"
    

`--datastore_consistency_policy {consistent,random,time}`
    

The policy to apply when deciding whether a datastore write should appear in global queries (default: time).

`--datastore_emulator_cmd=...`
    

The path to a script that invokes cloud datastore emulator. If left empty, `dev_appserver` will try to find datastore emulator in the Google Cloud SDK (default: None).

`--datastore_emulator_port=...`
    

The port number that dev_appserver should launch Cloud Datastore emulator on (default: 0).

`--datastore_path=...`
    

The path to use for the local datastore data file. The server creates this file if it does not exist.

`--default_gcs_bucket_name=...`
    

Default Cloud Storage bucket name (default: None).

`--dev_appserver_log_level {debug,info,warning,critical,error}`
    

The log level below which logging messages generated by the development server will not be displayed on the console (this flag is more useful for diagnosing problems in `dev_appserver.py` rather than in application code) (default: info).

`--enable_host_checking=yes|no`
    

Determines whether to enforce `HTTP` Host checking for application modules, API server, and admin server. Host checking protects against DNS rebinding attacks, only disable after understanding the security implications (default: True).

`--enable_console=yes|no`
    

Enable interactive console in admin view (default: False).

`--enable_sendmail=yes|no`
    

Uses the local computer's `Sendmail` installation for sending email messages.

`--enable_task_running=yes|no`
    

Enables the development server to run push tasks (default: `yes`). If you specify `no`, the server will not run push tasks.

`--env_var=...`
    

User defined environment variable for the local runtime process. Each `env_var` is in the format of `key=value`, and you can define multiple environment variables. In addition to `env_variables` in the `app.yaml`, this flag allows setting extra environment variables for local processes.

For example:`--env_var KEY_1=val1 --env_var KEY_2=val2`

`--grpc_api_port...`
    

Port on which the `gRPC` API server listens (default:0).

`--help`
    

Prints a helpful message then quits.

`--host=...`
    

The host address to use for the server. You may need to set this to be able to access the development server from another computer on your network. An address of `0.0.0.0` allows both localhost access and IP or hostname access (default: `localhost`).

`--log_level=...`
    

The lowest logging level at which logging messages will be written to the console; messages of the specified logging level or higher will be output. Possible values are `debug`, `info`, `warning`, `error`, and `critical`.

`--logs_path=...`
    

By default, the logs for the local development server are stored in memory only. Specify this option when you run the local development server to store the logs into a file, which makes the logs available across server restarts. You must specify the directory path and name to a SQLite database file. A SQLite database file is created with the specified name if the file does not already exist.

For example: `--logs_path=/home/logs/boglogs.db`

`--max_module_instances=...`
    

The maximum number of runtime instances that can be started for a particular module. The value can be an integer, in which case all modules are limited to the number of instances or a comma-separated list of `module:max_instances` (default: None). For Example: `default:5,backend:3`

`--mysql_host=MYSQL_HOST`
    

Host name of a running MySQL server used for simulated Cloud SQL storage (default: localhost).

`--mysql_port=MYSQL_PORT`
    

Port number of a running MySQL server used for simulated Cloud SQL storage (default: 3306).

`--mysql_user=MYSQL_USER`
    

Username to use when connecting to the MySQL server specified in `--mysql_host` and `--mysql_port` or `--mysql_socket` (default: ).

`--mysql_password=MYSQL_PASSWORD`
    

Password to use when connecting to the MySQL server specified in `--mysql_host` and `--mysql_port` or `--mysql_socket` (default: ).

`--mysql_socket=MYSQL_SOCKET`
    

Path to a Unix socket file to use when connecting to a running MySQL server used for simulated Cloud SQL storage (default: None).

`--port=...`
    

The port number to use for the server. Default is `8080`. If multiple servers are launched such as for services, they will be assigned subsequent ports, such as `8081`, `8082`.

`--require_indexes=yes|no`
    

Disables automatic generation of entries in the `index.yaml` file. Instead, when the application makes a query that requires that its index be defined in the file and the index definition is not found, an exception will be raised, similar to what would happen when running on App Engine (default: `no`).

`--runtime=...`
    

Specify the default runtimes you would like to use. For the list of supported runtimes, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule).

`--running_datastore_emulator_host=...`
    

Overrides the environment variable DATASTORE_EMULATOR_HOST, which means the `hostname:port` of a running Cloud Datastore emulator that `dev_appserver` can connect to (default: None).

`--search_indexes_path=...`
    

Path to a file used to store search indexes (defaults to a file in `--storage_path` if not set) (default:None).

`--skip_sdk_update_check=...`
    

Skip checking for SDK updates (if false, use `.appcfg_nag` to decide) (default: False).

`--show_mail_body=...`
    

Logs the contents of e-mails sent using the Mail API (default: False).

`--smtp_allow_tls...`
    

Allow TLS to be used when the SMTP server announces TLS support (ignored if --smtp_host is not set) (default: True).

`--smtp_host=...`
    

The hostname of the SMTP server to use for sending email messages.

`--smtp_port=...`
    

The port number of the SMTP server to use for sending email messages.

`--smtp_user=...`
    

The username to use with the SMTP server for sending email messages.

`--smtp_password=...`
    

The password to use with the SMTP server for sending email messages.

`--storage_path=...`
    

Path at which all local files, such as the Datastore, Blobstore, Cloud Storage files and logs, will be stored, unless overridden by `--datastore_path`, `--blobstore_path`, or `--logs_path`.

`--support_datastore_emulator=yes|no`
    

Use the Cloud Datastore Emulator (beta) for local datastore emulation.

`--ssl_certificate_path=...`
    

Path to SSL certificate. Must also provide `--ssl_certificate_key_path` if using this option (default: None).

`--ssl_certificate_key_path=...`
    

Path to corresponding SSL private key. Must also provide `--ssl_certificate_path` if using this option (default: None).

`--threadsafe_override=...`
    

Override the application's threadsafe configuration. The value can be a boolean, in which case all modules threadsafe setting will be overridden or a comma-separated list of `module:threadsafe_override` (default: None).

For example: `default:False,backend:True`

`--use_mtime_file_watcher=...`
    

Use mtime polling for detecting source code changes - useful if modifying code from a remote machine using a distributed file system (default: False).

`--watcher_ignore_re=...`
    

Regex string to specify files to be ignored by the filewatcher. (default: None)

## Python-specific options

Python runtime specific command options:

`--python_startup_script`
    The script to run at the startup of new Python runtime instances (useful for tools such as debuggers) (default: None).
`--python_startup_args`
    The arguments made available to the script specified in `python_startup_script` (default: None).
`--python27_executable_path=...`
    The path to the python27 executable for python27 runtime instances (default: None).
`--python_virtualenv_path`
    The path to the directory that is used to setup a Python 3 virtual environment for the local devappserver execution environment for Python 3 applications. If the path does not exist, the directory is created, but won't be cleaned up at the end of the devappserver execution, allowing for caching between invocations. If not defined, a temporary directory will be used and cleaned up at the end of the execution.
`--runtime_python_path=...`
    The path to your Python binary. To run a Python app on the `dev_appserver`, specify this flag.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

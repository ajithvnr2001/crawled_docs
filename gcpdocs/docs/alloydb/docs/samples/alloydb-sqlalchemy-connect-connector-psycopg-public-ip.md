---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/
title: Connect with SQLAlchemy and a public IP \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:29:55.043698+00:00
---

# Connect with SQLAlchemy and a public IP  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fdocs%2Fsamples%2Falloydb-sqlalchemy-connect-connector-psycopg-public-ip%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/docs)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Code sample](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/#code-sample)
  * [What's next](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)


Was this helpful?
#  Connect with SQLAlchemy and a public IP Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Code sample](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/#code-sample)
  * [What's next](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/#whats-next)


This snippet shows how to create a SQLAlchemy connection pool to connect to your database instance using a public IP address. Use this approach to securely connect from an application using the AlloyDB Python Connector without needing a sidecar proxy.
## Code sample
[Python](https://docs.cloud.google.com/alloydb/docs/samples/alloydb-sqlalchemy-connect-connector-psycopg-public-ip/#python) More
To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
import sqlalchemy

from google.cloud.alloydbconnector import Connector


def create_sqlalchemy_engine(
    inst_uri: str,
    user: str,
    password: str,
    db: str,
) -> tuple[sqlalchemy.engine.Engine, Connector]:
    """Creates a connection pool for an AlloyDB instance and returns the pool
    and the connector. Callers are responsible for closing the pool and the
    connector.

    A sample invocation looks like:

        engine, connector = create_sqlalchemy_engine(
                inst_uri,
                user,
                password,
                db,
        )
        with engine.connect() as conn:
            time = conn.execute(sqlalchemy.text("SELECT NOW()")).fetchone()
            conn.commit()
            curr_time = time[0]
            # do something with query result
            connector.close()

    Args:
        instance_uri (str):
            The instance URI specifies the instance relative to the project,
            region, and cluster. For example:
            "projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance"
        user (str):
            The database user name, e.g., postgres
        password (str):
            The database user's password, e.g., secret-password
        db (str):
            The name of the database, e.g., mydb
    """
    connector = Connector()

    # create SQLAlchemy connection pool
    engine = sqlalchemy.create_engine(
        "postgresql+psycopg://",
        creator=lambda: connector.connect(
            inst_uri,
            "psycopg",
            user=user,
            password=password,
            db=db,
            ip_type="PUBLIC",
        ),
    )
    return engine, connector


```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

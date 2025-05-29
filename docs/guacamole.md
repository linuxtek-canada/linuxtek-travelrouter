# Apache Guacamole Setup and Configuration

## Introduction

[Apache Guacamole](https://guacamole.apache.org/) is an open-source project which allows saving and using remote access to Windows and Linux machines using multiple protocols. For graphical environments, RDP and VNC are both supported.  This functionality is included in the deployment to provide an additional method for navigating captive portals, if it cannot be handled by RaspAP.

## Configuration

* Setting the manual path for the directories needed by the 3 containers - guacd, guacamole, and postgres: init, data, record, and drive.
* The username for PostgreSQL is `guacamole_user`.
* The PostgreSQL password is set via environment variables.

## References

Based on the following video from Lawrence Systems: 
* [Secure Remote Access to SSH & RDP From Your Browser](https://www.youtube.com/watch?v=GX53C80c05k)

This will use the official Apache Docker image for Guacamole, but the following repository is referenced for how to configure the deployment with Docker Compose:
* [GitHub Project - Docker Compose Example](https://github.com/boschkundendienst/guacamole-docker-compose)
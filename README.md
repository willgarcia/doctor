# Doctor

A small utility providing an extensible system to check your server's health.

Doctor can be used:
* to detect potential issues on a server / in combination with alert monitoring tools
* for analysis purposes: eg. in a webapp to display the server services' statuses via the JSON output

My special thanks to [Julien Bianchi](https://twitter.com/jubianchi) for his original idea and write-up of Doctor.
At first, Julien has imagined this tool to guide/help the developers to investigate environment problems on their local VM setups.

Following the same idea, I have refactored the code in order to extend the system and suit new needs/options.

Doctor provides:
* a configurable way to define what is called a "check" - see [configuration](#configuration);
* a JSON output;
* a RPM package via via [PackageCloud.io](https://packagecloud.io/willgarcia/doctor).

## RPM Build (optional)

```bash
$ ./build.sh
```

From here, the generated is available in `rpmbuild/RPMS/x86_64`.

## Installation

See the [Packagecloud instructions](https://packagecloud.io/willgarcia/doctor/install) to setup the RPM repository in your system

```bash
$ yum install doctor-X.X.X
```

## Usage

```bash
$ doctor -h
/usr/bin/doctor [-q query] [-l] [-h]

  -l List of existing checks

  -q Query mode
     Values: grep rule for check filtering
     Default: All checks

  -h Help
```

## Configuration

Add your own check in `/etc/doctor/conf.d/*.doctor`.

A check is basically a call to a bash function with the following arguments:

```bash
 # ID=$1
 # MSG=$2
 # CMD=$3
 # LEVEL=$4
 # SUGGEST=$5
 # GROUP=$6
```
Example:

```bash
add_check \
"uptime_last_update" \
"Uptime" \
"date '+%Y-%m-%d %H:%M:%S' -d \"`cut -f1 -d. /proc/uptime` seconds ago\"" \
"INFO" \
"Rebooting is evil" \
"system"
```

See examples here:
* [File check](samples/files.doctor)
* [Hostname check](samples/hostname.doctor)
* [HTTP check](samples/http.doctor)
* [Service check](samples/services.doctor)

It's up to you to define both the checks' groups and levels.

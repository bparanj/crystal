How to check the current timezone on the Ubuntu server?

To check the current timezone on an Ubuntu server, you can use the `timedatectl` command. This command displays information about the system clock and timezone among other details. Here's how you can use it:

1. Open a terminal or connect to your server via SSH.
2. Run the following command:

```bash
timedatectl
```

This command will output several pieces of information about your system time settings, including the local time, universal time, RTC time, time zone, and the status of the NTP synchronization. Look for the line that starts with `Time zone:` to find out the current timezone set on your server.

Here is an example of what the output might look like:

```
               Local time: Thu 2024-03-17 12:34:56 EDT
           Universal time: Thu 2024-03-17 16:34:56 UTC
                 RTC time: Thu 2024-03-17 16:34:57
                Time zone: America/New_York (EDT, -0400)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

In this example, the timezone is `America/New_York` with EDT (Eastern Daylight Time) being the current time adjustment.

The timezone by default is UTC on EC2 instances.

```
ubuntu@ip-172-31-44-28:~$ timedatectl
               Local time: Tue 2024-03-19 13:57:22 UTC
           Universal time: Tue 2024-03-19 13:57:22 UTC
                 RTC time: Tue 2024-03-19 13:57:22
                Time zone: Etc/UTC (UTC, +0000)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

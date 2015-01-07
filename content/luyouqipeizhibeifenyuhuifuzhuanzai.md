Title: 路由器配置备份与恢复（转载）
Date: 2010-06-28 03:02
Author: lmatt wang
Slug: luyouqipeizhibeifenyuhuifuzhuanzai

<a name="intro">Introduction</a>
--------------------------------

Routers often get upgraded or swapped out for a number of reasons. This
document provides the user with some basic steps to migrate the
configuration from an existing router to a new router.\

<a name="prereq">Prerequisites</a>
----------------------------------

### <a name="req">Requirements</a>

Before you use the information in this document, make sure that you meet
these requirements:

-   Access to a Trivial File Transfer Protocol (TFTP) or File Transfer
    Protocol (FTP) server.
-   Connectivity - Routers must be able to access the FTP or TFTP
    server. Use the **ping** command to verify connectivity.

### <a name="hw">Components Used</a>

This document is not restricted to specific software and hardware
versions.

The information in this document was created from the devices in a
specific lab environment. All of the devices used in this document
started with a cleared (default) configuration. If your network is live,
make sure that you understand the potential impact of any command.\

### <a name="conventions">Conventions</a>

Refer to [Cisco Technical Tips
Conventions](http://www.cisco.com/en/US/tech/tk801/tk36/technologies_tech_note09186a0080121ac5.shtml)
for more information on document conventions.\

<a name="backup">Make a Backup of the Configuration</a>
-------------------------------------------------------

There are several methods to choose from in order to back up and restore
a configuration:

-   [Use a TFTP
    server](http://www.cisco.com/en/US/products/sw/iosswrel/ps1835/products_tech_note09186a008020260d.shtml#tftp)
-   [Use an FTP
    server](http://www.cisco.com/en/US/products/sw/iosswrel/ps1835/products_tech_note09186a008020260d.shtml#ftp)
-   [Use a Terminal Emulation
    Program](http://www.cisco.com/en/US/products/sw/iosswrel/ps1835/products_tech_note09186a008020260d.shtml#em-prog)
-   [Automatic Backup of Configuration using the Kron
    Method](http://www.cisco.com/en/US/products/sw/iosswrel/ps1835/products_tech_note09186a008020260d.shtml#ab)
-   [Backup Configuration to a TFTP
    Server](http://www.cisco.com/en/US/products/sw/iosswrel/ps1835/products_tech_note09186a008020260d.shtml#bcb)

### <a name="tftp">Use a TFTP Server to Backup and Restore a Configuration</a>

This is a step-by-step approach to copy a configuration from a router to
a TFTP server, and back to another router. Before you proceed with this
method, make sure you have a TFTP server on the network to which you
have IP connectivity.

1.  At the `Router>` prompt, issue the **enable** command, and provide
    the required password when prompted.
    </p>
    <p>
    The prompt changes to `Router#`, which indicates that the router is
    now in privileged mode.
2.  Copy the running configuration file to the TFTP server:\

    >     CE_2#copy running-config tftp:
    >     Address or name of remote host []? 64.104.207.171
    >     Destination filename [ce_2-confg]? backup_cfg_for_my_router
    >     !!
    >     1030 bytes copied in 2.489 secs (395 bytes/sec)
    >     CE_2#

    <p>
3.  Open the configuration file with a text editor. Search for and
    remove any line that starts with "AAA".
    </p>
    <p>
    **Note:** This step is to remove any security commands that can lock
    you out of the router.
4.  Copy the configuration file from the TFTP server to a new router in
    privileged (enable) mode which has a basic configuration.\

    >     Router#copy tftp: running-config
    >     Address or name of remote host []? 64.104.207.171
    >     Source filename []? backup_cfg_for_my_router
    >     Destination filename [running-config]?
    >     Accessing tftp://10.66.64.10/backup_cfg_for_my_router...
    >     Loading backup_cfg_for_router from 64.104.207.171 (via FastEthernet0/0): !
    >     [OK - 1030 bytes]
    >
    >     1030 bytes copied in 9.612 secs (107 bytes/sec)
    >     CE_2#

    <p>

### <a name="ftp">Use an FTP Server to Backup and Restore a Configuration</a>

In this procedure, an FTP server can be used in place of a TFTP server.

1.  At the `Router>` prompt, issue the **enable** command, and provide
    the required password when prompted.
    </p>
    <p>
    The prompt changes to `Router#`, which indicates that the router is
    now in privileged mode.
2.  Configure the FTP username and password.\

    >     CE_2#config terminal
    >     CE_2(config)#ip ftp username cisco
    >     CE_2(config)#ip ftp password cisco123
    >     CE_2(config)#end
    >     CE_2#

    <p>
3.  Copy the configuration to the FTP server.\

    >     CE_2#copy running-config ftp:
    >     Address or name of remote host []? 10.66.64.10
    >     Destination filename [ce_2-confg]? backup_cfg_for_router
    >     Writing backup_cfg_for_router !
    >     1030 bytes copied in 3.341 secs (308 bytes/sec)
    >     CE_2#

    <p>
4.  Open the configuration file with a text editor. Search for and
    remove any line that starts with "AAA".
    </p>
    <p>
    **Note:** This step is to remove any security commands that can lock
    you out of the router.
5.  Copy the configuration file from the FTP server to a router in
    privileged (enable) mode which has a basic configuration.\

    >     Router#copy ftp: running-config
    >     Address or name of remote host [10.66.64.10]?
    >     Source filename [backup_cfg_for_router]?
    >     Destination filename [running-config]?
    >     Accessing ftp://10.66.64.10/backup_cfg_for_router...
    >     Loading backup_cfg_for_router !
    >     [OK - 1030/4096 bytes]
    >     1030 bytes copied in 13.213 secs (78 bytes/sec)
    >     CE_2#

    <p>

### <a name="em-prog">Use a Terminal Emulation Program to Backup and Restore a Configuration</a>

A terminal emualation program can be used to back up and restore a
configuration. This is a description of the procedure using Microsoft
Hyperterminal Terminal Emulation software:

1.  If the configuration needs to be copied from another router, connect
    to that router through the console or Telnet.
2.  At the `Router>` prompt, issue the **enable** command, and provide
    the required password when prompted.
    </p>
    <p>
    The prompt changes to `Router#`, which indicates that the router is
    now in privileged mode.
3.  Issue the **terminal length 0** command in order to force the router
    to return the entire response at once, rather than one screen at a
    time.
    </p>
    <p>
    This allows you to capture the configuration without extraneous
    `--more--` prompts generated when the router responds one screen at
    a time.
4.  On the HyperTerminal menu, choose **Transfer \> Capture Text**.
    </p>
    <p>
    The Capture Text window appears.
5.  Name this file "config.txt."
6.  Click **Start** in order to dismiss the Capture Text window and
    begin the capture.
7.  Issue the **show running-config** command, and allow time for the
    router to complete its response. You will see:\

    >     Building configuration...

    <p>
    followed by the configuration.

8.  On the HyperTerminal menu, choose **Transfer \> Capture Text \>
    Stop** in order to end the screen capture.
9.  Open the config.txt file you created in any text editor, such as
    Notepad or Wordpad.
10. Search for and remove any line that starts with "AAA".
    </p>
    <p>
    **Note:** This step is to remove any security commands that could
    lock you out of the router.
11. Save the file.
12. Connect to the router that needs the configuration.
13. Open the config.txt file.
14. Highlight the entire contents of the config.txt file.
    </p>
    <p>
    You can do this by dragging the cursor from before the first
    character to after the last character in the file while holding down
    the left mouse button. Alternatively, if you use Notepad, you can
    choose **Edit \> Select All** from the menu.
15. Copy the selected text to the Windows clipboard.
    </p>
    <p>
    You can either choose **Edit \> Copy** from the text editor menu, or
    hold down the **CTRL** key and simultaneously press the **C** key in
    order to perform the copy.
16. Switch to the HyperTerminal window, and issue the **configure
    terminal** command at the `Router#` prompt. Then press **Enter**.
17. Paste the configuration file into the router by selecting **Edit \>
    Paste to Host** on the HyperTerminal menu.
18. After the configuration has finished pasting and the router brings
    you back to the configuration prompt, issue the **copy
    running-config startup-config** command in order to write the
    configuration into memory.
19. Issue the **exit** command in order to return to the `Router#`
    prompt.

### <a name="ab">Automatic Backup of Configuration using the Kron Method</a>

In order to get a router to copy the running-config to startup-config,
for example every Sunday at 23:00, complete these steps:

1.  **Create a kron policy list**—This is the script that lists what
    commands the router should run at the scheduled time.\

    >     Router(config)#kron policy-list SaveConfig
    >
    >             Router(config-kron-policy)#cli write
    >             Router(config-kron-policy)#exit

    -   **cli**—Specifies EXEC CLI commands within a Command Scheduler
        policy list.
    -   **Policy-list**—Specifies the policy list associated with a
        Command Scheduler occurrence.

    <p>
    **Note:** The reason why **write** was used rather than **copy
    running-config startup-config** is because kron does not support
    interactive prompts and the **copy running-config startup-config**
    command requires interaction. It is important to remember this when
    you create commands. Also, note that kron does not support
    configuration commands.

2.  **Create a kron occurrence**—This informs the router when and how
    often the policy should run.\

    >     Router(config)#kron occurrence SaveConfigSchedule
    >      at 23:00 Sun recurring
    >             Router(config-kron-occurrence)#policy-list SaveConfig

    -   **SaveConfigSchedule**—This is the name of occurrence. Length of
        occurrence-name is from 1 to 31 characters. If the
        occurrence-name is new, an occurrence structure will be created.
        If the occurrence-name is not new, the existing occurrence will
        be edited.
    -   **at**—Identifies that the occurrence is to run at a specified
        calendar date and time.
    -   **recurring**—Identifies that the occurrence is to run on a
        recurring basis.

    <p>
3.  Verify the kron configuration by using the **show** command.\

    >     Router#sh kron schedule
    >              Kron Occurrence Schedule
    >              SaveConfigSchedule inactive, will run again in 1 days 12:37:47 at 23:00 on Sun

    -   **inactive**—Means that kron is not running the command(s) at
        present.
    -   **Active**—Means that kron is running the current command(s).

    >     Router#show running-configuration
    >               kron occurrence SaveConfigSchedule at 23:00 Sun recurring
    >                 policy-list SaveConfig
    >                 kron policy-list SaveConfig
    >                 cli write

    <p>

### <a name="bcb">Backup Configuration to a TFTP Server</a>

This example is to save the running config to a TFTP server (10.1.1.1)
every Sunday at 23:00:\

>     Router(config)#kron policy-list Backup
>
>              Router(config-kron-policy)#cli show run | redirect
>        tftp://10.1.1.1/test.cfg
>              Router(config-kron-policy)#exit
>              !
>              Router(config)#kron occurrence Backup at 23:00 Sun recurring
>              Router(config-kron-occurrence)#policy-list Backup

<a name="verify">Verify</a>
---------------------------

Use the **show running-config** command to confirm that the
configuration file has been copied to the destination router.\

<a name="NetPro">Cisco Support Community - Featured Conversations</a>
---------------------------------------------------------------------

<!--googleoff: all-->[Cisco Support
Community](https://supportforums.cisco.com/index.jspa) is a forum for
you to ask and answer questions, share suggestions, and collaborate with
your peers. Below are just some of the most recent and relevant
conversations happening right now.

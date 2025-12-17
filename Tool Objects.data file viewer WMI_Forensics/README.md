# WMI_Forensics

This repo is a clone of the official repo made by David Pany (see credits sections at the end of the page)

This repository contains scripts used to find evidence in WMI repositories, specifically OBJECTS.DATA files located at:

- C:\WINDOWS\system32\wbem\Repository\OBJECTS.DATA
- C:\WINDOWS\system32\wbem\Repository\FS\OBJECTS.DATA

## CCM_RUA_Finder.py
CCM_RUA_finder.py extracts SCCM software metering RecentlyUsedApplication logs from OBJECTS.DATA files.

### Usage
```
CCM_RUA_Finder.py -i path\to\OBJECTS.DATA -o path\to\output.xls
```

The output file will be TSV formatted. Excel will automatically parse TSV files with .xls extensions.

## PyWMIPersistenceFinder.py
PyWMIPersistenceFinder.py is designed to find WMI persistence via FitlerToConsumerBindings
solely by keyword searching the OBJECTS.DATA file without parsing the full WMI repository.

In testing, this script has found the exact same data as python-cim's
show_FilterToConsumerBindings.py without requiring the setup. Only further testing will
indicate if this script misses any data that python-cim can find.

In theory, this script will detect FilterToConsumerBindings that are deleted and remain
in unallocated WMI space, but I haven't had a chance to test yet.

### Usage
```PyWMIPersistenceFinder.py <OBJECTS.DATA file>```

The output is text based in the following format for each binding:
```
<consumer name>-<filter name>
            <optional notes>
        Consumer: <consumer name><consumer execution details>
        Filter: <filter name><filter listener details>
```

# Credits to the Author
David Pany - Mandiant (FireEye) - 2017

Twitter: @DavidPany

Please send him comments, bug reports, and questions to his official github repo


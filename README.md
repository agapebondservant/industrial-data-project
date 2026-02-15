# Industrial Data Platform

(Testing change here again)

This is an industrial sensor data collection and processing platform which supports reporting, email alerts, and a web dashboard.
It integrates with SCADA systems, mainframes and other data sources.

(Forked from <a href="https://github.com/rdwj/py2to3-example-project" target="_blank">this repo</a> authored by Wes Jackson)

INSTALLATION

  1. Download and unpack the source archive, then cd into the root directory:
       cd industrial-data-project

  2. Install dependencies:
       pip install -r requirements.txt

  3. Install the platform:
       python setup.py install

  4. Copy configuration:
       cp config/platform.ini /etc/platform/platform.ini 

     Edit the file to match your plant's network layout.


USAGE

  Interactive mode:
      python scripts/run_platform.py

  Batch mode (for cron):
      python scripts/run_platform.py --batch

  Mainframe import:
      python scripts/batch_import.py /opt/platform/incoming/mainframe

  Sensor monitoring daemon:
      python scripts/sensor_monitor.py --serial /dev/ttyS0 --mqtt 10.1.40.200:1883

[MIT](LICENSE)

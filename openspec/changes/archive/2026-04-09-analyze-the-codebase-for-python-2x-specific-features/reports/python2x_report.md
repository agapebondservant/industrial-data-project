# Python 2x-Specific Syntax Report

## Findings

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/setup.py
#### Pattern: python2_imports
#### Matches:
- from distutils.core import setup

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/scripts/run_platform.py
#### Pattern: print_statements
#### Matches:
- print "Unknown option: %s" % argv[i]
- print "Initialising platform..."
- print "Platform subsystems ready"

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/scripts/run_platform.py
#### Pattern: except_syntax
#### Matches:
- except (EOFError, KeyboardInterrupt):
- except Exception, e:
- except Exception, e:

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/scripts/batch_import.py
#### Pattern: print_statements
#### Matches:
- print "=" * 60
- print "Processing: %s" % file_path
- print "Started:    %s" % time.strftime("%Y-%m-%d %H:%M:%S")

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/scripts/sensor_monitor.py
#### Pattern: print_statements
#### Matches:
- print "MONITOR: serial poll thread started on %s" % reader.port_path
- print "MONITOR: reading queue full, dropping serial packet"
- print "MONITOR: serial thread error: %s" % str(e)

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/automation/script_runner.py
#### Pattern: print_statements
#### Matches:
- print "ScriptRunner initialised, dir: %s" % self.script_directory
- print "WARNING: bad argument type: %s" % type(args)
- print "Loaded script: %s (%d bytes)" % (filename, len(source))

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/automation/scheduler.py
#### Pattern: print_statements
#### Matches:
- print "Task stream shutting down"
- print "Task stream cancellation: %s" % e
- print "Worker %d started" % self.worker_id

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/reporting/email_sender.py
#### Pattern: print_statements
#### Matches:
- print "Distribution list '%s': %d recipients" % (name, len(recipients))
- print "Loaded %d distribution lists" % len(self._distribution_lists)
- print "Alert sent to %d recipients: %s" % (len(alert.recipients), alert.subject)

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/io_protocols/modbus_client.py
#### Pattern: print_statements
#### Matches:
- print "MODBUS: connecting to %s:%d unit %d" % (self.host, self.port, self.unit_id)
- print "MODBUS: connected"
- print "MODBUS: disconnect warning -- %s" % e

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/io_protocols/serial_sensor.py
#### Pattern: print_statements
#### Matches:
- print "SERIAL: unknown type 0x%02X sensor %04X" % (
- print "SERIAL: chksum error 0x%04X (exp %02X got %02X)" % (
- print "SERIAL: pkt #%d sensor 0x%04X (%s) %d bytes" % (

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/io_protocols/opcua_client.py
#### Pattern: print_statements
#### Matches:
- print "OPC-UA: monitoring %s (item %d)" % (node_id, iid)
- print "OPC-UA: connecting to %s" % self.endpoint
- print "OPC-UA: session %s" % self._sid

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/io_protocols/mqtt_listener.py
#### Pattern: print_statements
#### Matches:
- print "MQTT: JSON error on %s -- %s" % (self.topic, e)
- print "MQTT: connecting to %s:%d" % (self.host, self.port)
- print "MQTT: connected"

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/data_processing/mainframe_parser.py
#### Pattern: print_statements
#### Matches:
- print "Loaded %d cached records for %s" % (len(cached), file_path)
- print "Parsing mainframe file: %s" % file_path
- print "WARNING: Truncated record #%d (%d bytes, expected %d)" % (

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/data_processing/text_analyzer.py
#### Pattern: print_statements
#### Matches:
- print for duplicate detection.
- print are considered duplicates even if they
- print for duplicate detection."

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/data_processing/xml_transformer.py
#### Pattern: print_statements
#### Matches:
- print "Loading XML from %s" % xml_path
- print "Detected SCADA namespace: %s" % namespace
- print "Transformed %d records from %s" % (len(records), xml_path)

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/data_processing/log_parser.py
#### Pattern: print_statements
#### Matches:
- print "Parsing log file: %s" % file_path
- print "WARNING: Could not detect log format from line %d" % line_num
- print "Parsed %d entries from %d lines in %.2f seconds" % (

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/storage/file_store.py
#### Pattern: print_statements
#### Matches:
- print "Created directory: %s" % d
- print "Wrote report: %s (%d bytes)" % (dest, os.path.getsize(dest))
- print "Wrote binary: %s (%d bytes)" % (dest, len(data))

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/storage/cache.py
#### Pattern: print_statements
#### Matches:
- print = self._compute_fingerprint(value)
- print "  [cache] MISS: %s" % key
- print "  [cache] HIT: %s (bucket %d)" % (key, self._bucket_for_key(key))

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/storage/database.py
#### Pattern: print_statements
#### Matches:
- print "  [txn] BEGIN"
- print "  [txn] COMMIT"
- print "  [txn] ROLLBACK (%s)" % exc_type.__name__

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/tests/test_core_types.py
#### Pattern: print_statements
#### Matches:
- print "cmp() ordering verified"
- print "Py2 integer division: 7/2 = 3"
- print "TypeError raised for bad input"

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/tests/test_csv_processor.py
#### Pattern: print_statements
#### Matches:
- print "UTF-8 CSV: %d rows" % len(rows)
- print "CSV written"
- print "UTF-8 roundtrip OK"

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/core/utils.py
#### Pattern: python2_imports
#### Matches:
- from sets import Set as OrderedSet   # pre-2.6 habit; used for dedup w/ order

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/core/string_helpers.py
#### Pattern: python2_imports
#### Matches:
- from StringIO import StringIO
- from cStringIO import StringIO as FastStringIO

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/core/exceptions.py
#### Pattern: except_syntax
#### Matches:
- except PlatformError, e:
- except StandardError, e:
- except ProtocolError, e:

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/core/config_loader.py
#### Pattern: print_statements
#### Matches:
- print "Loading config from", self._path
- print "Found config at", candidate
- print "WARNING: no configuration file found; using defaults"

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/storage/file_store.py
#### Pattern: except_syntax
#### Matches:
- except IOError, e:
- except IOError, e:
- except (IOError, struct.error), e:

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/storage/cache.py
#### Pattern: except_syntax
#### Matches:
- except StandardError, e:
- except StandardError, e:
- except OSError, e:

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/storage/database.py
#### Pattern: except_syntax
#### Matches:
- except StandardError, e:
- except StandardError, e:
- except Exception, e:

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/io_protocols/opcua_client.py
#### Pattern: division_behavior
#### Matches:
- 2008/02

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/src/data_processing/log_parser.py
#### Pattern: division_behavior
#### Matches:
- 6/2

### File: /opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp/tests/test_core_types.py
#### Pattern: division_behavior
#### Matches:
- 7/2
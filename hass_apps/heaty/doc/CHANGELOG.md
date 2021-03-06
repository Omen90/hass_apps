# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## Unreleased

### Fixed
* Fixed error when turning master switch off due to a wrong default
  value for off_temp.

### Security

### Added

### Changed

### Deprecated

### Removed


## 0.10.1 - 2018-03-05

### Fixed
* Fixed issue that lead to endless re-sending with AppDaemon 3.
* thermostat_defaults and window_sensor_defaults are now handled correctly.


## 0.10.0 - 2018-03-05

### Added
* Added appdaemon 3 support alongside the old appdaemon 2


## 0.9.4 - 2018-02-03

### Added
* Added ``start_date`` and ``end_date`` constraints for schedule rules.


## 0.9.3 - 2018-02-02

### Fixed
* Fixed wrong version number


## 0.9.2 - 2018-02-02

### Fixed
* Fixed error when not setting ``schedule:``, ``schedule_prepend:`` and
  ``schedule_append:`` due to voluptuous not validating default values.


## 0.9.1 - 2018-02-01

### Added
- Begin using CHANGELOG.md

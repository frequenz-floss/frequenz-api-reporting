# Frequenz Reporting API Release Notes

## Summary

- Added sensor-ID based RPCs

## Upgrading

- The minimum allowed version of `protobuf` and `grpcio` has been updated to 6.31.1 and 1.72.1 respectively, you might also need to bump your dependencies accordingly.

## New Features
- Two new RPCs have been added to support sensor data:
  - `ReceiveMicrogridSensorsDataStream`
  - `ReceiveAggregatedMicrogridSensorsDataStream`

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->

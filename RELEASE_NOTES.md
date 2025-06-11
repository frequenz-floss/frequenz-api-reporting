# Frequenz Reporting API Release Notes

## Summary

- Dependency versions have been bumped, see "Upgrading" for specifics
- Renaming of time filter fields, see "Upgrading" for specifics

## Upgrading

- The minimum allowed version of `protobuf` and `grpcio` has been updated to 6.31.1 and 1.72.1 respectively, you might also need to bump your dependencies accordingly.
- The fields `start` and `end` in `TimeFilter` have been renamed to `start_time` and `end_time` respectively. Apps that implement this API should take care.

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->

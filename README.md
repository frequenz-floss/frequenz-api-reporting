# Frequenz Reporting API

[![Build Status](https://github.com/frequenz-floss/frequenz-api-reporting/actions/workflows/ci.yaml/badge.svg)](https://github.com/frequenz-floss/frequenz-api-reporting/actions/workflows/ci.yaml)
[![PyPI Package](https://img.shields.io/pypi/v/frequenz-api-reporting)](https://pypi.org/project/frequenz-api-reporting/)
[![Docs](https://img.shields.io/badge/docs-latest-informational)](https://frequenz-floss.github.io/frequenz-api-reporting/)

## Introduction

Frequenz gRPC API to aggregate component data from microgrids.

## Supported Platforms

The following platforms are officially supported (tested):

- **Python:** 3.11
- **Operating System:** Ubuntu Linux 20.04
- **Architectures:** amd64, arm64

## Overview
The Microgrid Reporting API serves as an interface for obtaining detailed insights into
microgrid operations and metrics. Unlike general telemetry APIs, this API specializes in
generating reports based on complex, user-defined aggregations of microgrid data. It
provides both historical and real-time reporting capabilities.

## Objective
The primary objective of the Microgrid Reporting API is to furnish a robust foundation for
building data-driven applications that optimize microgrid performance, enable efficient
power trading strategies, and facilitate intelligent decision-making across multiple
operational scenarios. By aggregating and streamlining access to key metrics and data,
this API not only aids in conducting in-depth performance analysis but also supports the
development of algorithms and strategies for real-time and future power trading. This dual
focus ensures that the API serves as a versatile tool for both operational and financial
optimization within the microgrid ecosystem.

## Key Features
- Real-time and Historical Reporting: Supports both real-time reporting through data
   streams and historical data retrieval, offering comprehensive analytical capabilities.
- Custom Aggregation: Support for user-defined aggregation formulas for microgrid
   component metrics like power, voltage, and more.
- Multiple Microgrid Support: Allows users to aggregate data from multiple microgrids
   in a single request, providing a holistic view of operations.

## Scope and Limitations
The Microgrid Reporting API is designed to offer extensive reporting capabilities, allowing
for both simple and complex data aggregations across multiple microgrids. It provides
granular insights on a per-component basis as well as an overarching view of entire microgrid
operations.  The scope of the API is limited by the types of aggregation formulas it supports,
potentially constraining its utility in highly specialized analytical scenarios.

## Target Audience
The Microgrid Reporting API is tailored for a broad audience, including performance analysts,
trading strategists, and cloud application developers. Whether the aim is to perform in-depth
performance analysis, devise trading strategies based on microgrid data, or build applications
that capitalize on real-time and historical data, this API serves as a comprehensive data source.
By providing an array of key metrics and aggregation features, it accommodates various
use-cases and empowers users to make well-informed decisions in different operational
contexts.

## Contributing

If you want to know how to build this project and contribute to it, please
check out the [Contributing Guide](CONTRIBUTING.md).

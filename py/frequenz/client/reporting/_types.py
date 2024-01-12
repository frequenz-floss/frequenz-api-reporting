# License: MIT
# Copyright © 2024 Frequenz Energy-as-a-Service GmbH

"""Module to define the types used with the reporting client"""

from __future__ import annotations  # required for constructor type hinting

import enum
import logging
from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

from frequenz.api.reporting.v1 import reporting_pb2
from frequenz.api.common.v1.metrics import metric_sample_pb2, bounds_pb2
from frequenz.api.common.v1.microgrid import (
    microgrid_components_components_pb2,
    microgrid_pb2,
)
from frequenz.api.common.v1.pagination import (
    pagination_params_pb2,
    pagination_info_pb2,
)
from google.protobuf import timestamp_pb2

# Set up logging
_logger = logging.getLogger(__name__)


# # From common metric api


class Metric(enum.Enum):
    """
    List of supported metrics.
    """

    # Default value
    UNSPECIFIED = metric_sample_pb2.Metric.UNSPECIFIED

    # DC electricity metrics
    DC_VOLTAGE = metric_sample_pb2.Metric.METRIC_DC_VOLTAGE
    DC_CURRENT = metric_sample_pb2.Metric.METRIC_DC_CURRENT
    DC_POWER = metric_sample_pb2.Metric.METRIC_DC_POWER

    # General AC electricity metrics
    AC_FREQUENCY = metric_sample_pb2.Metric.METRIC_AC_FREQUENCY
    AC_VOLTAGE = metric_sample_pb2.Metric.METRIC_AC_VOLTAGE
    AC_VOLTAGE_PHASE_1 = metric_sample_pb2.Metric.METRIC_AC_VOLTAGE_PHASE_1
    AC_VOLTAGE_PHASE_2 = metric_sample_pb2.Metric.METRIC_AC_VOLTAGE_PHASE_2
    AC_VOLTAGE_PHASE_3 = metric_sample_pb2.Metric.METRIC_AC_VOLTAGE_PHASE_3
    AC_APPARENT_CURRENT = metric_sample_pb2.Metric.METRIC_AC_APPARENT_CURRENT
    AC_APPARENT_CURRENT_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_CURRENT_PHASE_1
    )
    AC_APPARENT_CURRENT_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_CURRENT_PHASE_2
    )
    AC_APPARENT_CURRENT_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_CURRENT_PHASE_3
    )

    # AC power metrics
    AC_APPARENT_POWER = metric_sample_pb2.Metric.METRIC_AC_APPARENT_POWER
    AC_APPARENT_POWER_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_POWER_PHASE_1
    )
    AC_APPARENT_POWER_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_POWER_PHASE_2
    )
    AC_APPARENT_POWER_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_POWER_PHASE_3
    )
    AC_ACTIVE_POWER = metric_sample_pb2.Metric.METRIC_AC_ACTIVE_POWER
    AC_ACTIVE_POWER_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_POWER_PHASE_1
    )
    AC_ACTIVE_POWER_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_POWER_PHASE_2
    )
    AC_ACTIVE_POWER_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_POWER_PHASE_3
    )
    AC_REACTIVE_POWER = metric_sample_pb2.Metric.METRIC_AC_REACTIVE_POWER
    AC_REACTIVE_POWER_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_REACTIVE_POWER_PHASE_1
    )
    AC_REACTIVE_POWER_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_REACTIVE_POWER_PHASE_2
    )
    AC_REACTIVE_POWER_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_REACTIVE_POWER_PHASE_3
    )

    # AC power factor
    AC_POWER_FACTOR = metric_sample_pb2.Metric.METRIC_AC_POWER_FACTOR
    AC_POWER_FACTOR_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_POWER_FACTOR_PHASE_1
    )
    AC_POWER_FACTOR_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_POWER_FACTOR_PHASE_2
    )
    AC_POWER_FACTOR_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_POWER_FACTOR_PHASE_3
    )

    # AC energy metrics
    AC_APPARENT_ENERGY = metric_sample_pb2.Metric.METRIC_AC_APPARENT_ENERGY
    AC_APPARENT_ENERGY_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_ENERGY_PHASE_1
    )
    AC_APPARENT_ENERGY_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_ENERGY_PHASE_2
    )
    AC_APPARENT_ENERGY_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_APPARENT_ENERGY_PHASE_3
    )
    AC_ACTIVE_ENERGY = metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY
    AC_ACTIVE_ENERGY_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_PHASE_1
    )
    AC_ACTIVE_ENERGY_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_PHASE_2
    )
    AC_ACTIVE_ENERGY_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_PHASE_3
    )
    AC_ACTIVE_ENERGY_CONSUMED = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_CONSUMED
    )
    AC_ACTIVE_ENERGY_CONSUMED_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_CONSUMED_PHASE_1
    )
    AC_ACTIVE_ENERGY_CONSUMED_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_CONSUMED_PHASE_2
    )
    AC_ACTIVE_ENERGY_CONSUMED_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_CONSUMED_PHASE_3
    )
    AC_ACTIVE_ENERGY_DELIVERED = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_DELIVERED
    )
    AC_ACTIVE_ENERGY_DELIVERED_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_DELIVERED_PHASE_1
    )
    AC_ACTIVE_ENERGY_DELIVERED_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_DELIVERED_PHASE_2
    )
    AC_ACTIVE_ENERGY_DELIVERED_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_ACTIVE_ENERGY_DELIVERED_PHASE_3
    )
    AC_REACTIVE_ENERGY = metric_sample_pb2.Metric.METRIC_AC_REACTIVE_ENERGY
    AC_REACTIVE_ENERGY_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_REACTIVE_ENERGY_PHASE_1
    )
    AC_REACTIVE_ENERGY_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_REACTIVE_ENERGY_PHASE_2
    )
    AC_REACTIVE_ENERGY_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_REACTIVE_ENERGY_PHASE_3
    )

    # AC harmonics
    AC_THD_CURRENT = metric_sample_pb2.Metric.METRIC_AC_THD_CURRENT
    AC_THD_CURRENT_PHASE_1 = (
        metric_sample_pb2.Metric.METRIC_AC_THD_CURRENT_PHASE_1
    )
    AC_THD_CURRENT_PHASE_2 = (
        metric_sample_pb2.Metric.METRIC_AC_THD_CURRENT_PHASE_2
    )
    AC_THD_CURRENT_PHASE_3 = (
        metric_sample_pb2.Metric.METRIC_AC_THD_CURRENT_PHASE_3
    )

    # General BMS metrics
    BATTERY_CAPACITY = metric_sample_pb2.Metric.METRIC_BATTERY_CAPACITY
    BATTERY_SOC_PCT = metric_sample_pb2.Metric.METRIC_BATTERY_SOC_PCT
    BATTERY_TEMPERATURE = metric_sample_pb2.Metric.METRIC_BATTERY_TEMPERATURE

    # General inverter metrics
    INVERTER_TEMPERATURE = metric_sample_pb2.Metric.METRIC_INVERTER_TEMPERATURE

    # EV charging station metrics
    EV_CHARGING_TEMPERATURE = (
        metric_sample_pb2.Metric.METRIC_EV_CHARGING_TEMPERATURE
    )

    # General sensor metrics
    SENSOR_WIND_SPEED = metric_sample_pb2.Metric.METRIC_SENSOR_WIND_SPEED
    SENSOR_WIND_DIRECTION = (
        metric_sample_pb2.Metric.METRIC_SENSOR_WIND_DIRECTION
    )
    SENSOR_TEMPERATURE = metric_sample_pb2.Metric.METRIC_SENSOR_TEMPERATURE
    SENSOR_RELATIVE_HUMIDITY = (
        metric_sample_pb2.Metric.METRIC_SENSOR_RELATIVE_HUMIDITY
    )
    SENSOR_DEW_POINT = metric_sample_pb2.Metric.METRIC_SENSOR_DEW_POINT
    SENSOR_AIR_PRESSURE = metric_sample_pb2.Metric.METRIC_SENSOR_AIR_PRESSURE
    SENSOR_IRRADIANCE = metric_sample_pb2.Metric.METRIC_SENSOR_IRRADIANCE

    @classmethod
    def from_pb(cls, metric: metric_sample_pb2.Metric.ValueType) -> Metric:
        """Convert a protobuf Metric value to Metric enum.
        Args:
            metric: Metric to convert.
        Returns:
            Enum value corresponding to the protobuf message.
        """
        if not any(m.value == metric for m in cls):
            _logger.warning(
                "Unknown metric %s. Returning UNSPECIFIED.", metric
            )
            return cls.UNSPECIFIED

        return cls(metric)

    def to_pb(self) -> metric_sample_pb2.Metric.ValueType:
        """Convert a Metric object to protobuf Metric.
        Returns:
            Protobuf message corresponding to the Metric object.
        """
        return metric_sample_pb2.Metric.ValueType(self.value)


@dataclass(frozen=True)
class MetricSampleVariant:
    """
    MetricSampleVariant serves as a union type that can encapsulate either a
    `SimpleMetricSample` or an `AggregatedMetricSample`. Setting one will
    nullify the other.

    Args:
        simple_metric: Simple metric sample.
        aggregated_metric: Aggregated metric sample.

    """

    simple_metric: SimpleMetricSample | None = None
    aggregated_metric: AggregatedMetricSample | None = None

    @classmethod
    def from_pb(
        cls, metric_sample_variant: metric_sample_pb2.MetricSampleVariant
    ) -> MetricSampleVariant:
        """Convert a protobuf MetricSampleVariant to MetricSampleVariant object.
        Args:
            metric_sample_variant: MetricSampleVariant to convert.
        Returns:
            MetricSampleVariant object corresponding to the protobuf message.
        """
        return cls(
            simple_metric=SimpleMetricSample.from_pb(
                metric_sample_variant.simple_metric_sample
            )
            if metric_sample_variant.HasField("simple_metric_sample")
            else None,
            aggregated_metric=AggregatedMetricSample.from_pb(
                metric_sample_variant.aggregated_metric_sample
            )
            if metric_sample_variant.HasField("aggregated_metric_sample")
            else None,
        )

    def to_pb(self) -> metric_sample_pb2.MetricSampleVariant:
        """Convert a MetricSampleVariant object to protobuf MetricSampleVariant.
        Returns:
            Protobuf message corresponding to the MetricSampleVariant object.
        """

        metric_sample_variant = metric_sample_pb2.MetricSampleVariant()

        if self.simple_metric is not None:
            metric_sample_variant.simple_metric_sample.CopyFrom(
                self.simple_metric.to_pb()
            )
        if self.aggregated_metric is not None:
            metric_sample_variant.aggregated_metric_sample.CopyFrom(
                self.aggregated_metric.to_pb()
            )
        return metric_sample_variant


@dataclass(frozen=True)
class MetricSample:
    """
    Representation of a sampled metric along with its value.

    Args:
        sampled_at: Time at which metric was sampled.
        metric: Metric that was sampled.
        sample: Value of the sampled metric.
        bounds: List of bounds that apply to the metric sample.
    """

    sampled_at: datetime
    metric: Metric
    sample: MetricSampleVariant
    bounds: List[bounds_pb2.Bounds]

    @classmethod
    def from_pb(
        cls, metric_sample: metric_sample_pb2.MetricSample
    ) -> MetricSample:
        """Convert a protobuf MetricSample to MetricSample object.
        Args:
            metric_sample: MetricSample to convert.
        Returns:
            MetricSample object corresponding to the protobuf message.
        """
        return cls(
            sampled_at=metric_sample.sampled_at.ToDatetime(),
            metric=Metric.from_pb(metric_sample.metric),
            sample=MetricSampleVariant.from_pb(metric_sample.sample),
            bounds=[bounds_pb2.Bounds.from_pb(bound) for bound in metric_sample.bounds],
        )

    def to_pb(self) -> metric_sample_pb2.MetricSample:
        """Convert a MetricSample object to protobuf MetricSample.
        Returns:
           Protobuf message corresponding to the MetricSample object.
        """
        return metric_sample_pb2.MetricSample(
            sampled_at=timestamp_pb2.Timestamp().FromDatetime(self.sampled_at),
            metric=self.metric.to_pb(),
            sample=self.sample.to_pb(),
            bounds=[bounds_pb2.Bounds.ValueType(bound.value) for bound in self.bounds] if self.bounds else None,
        )


@dataclass(frozen=True)
class SimpleMetricSample:
    """
    Simple metric sample, the value of which is either measured or derived at a particular time.

    Args:
        value: Value of the sample.
    """

    value: float

    @classmethod
    def from_pb(
        cls, simple_metric_sample: metric_sample_pb2.SimpleMetricSample
    ) -> SimpleMetricSample:
        """Convert a protobuf SimpleMetricSample to SimpleMetricSample object.
        Args:
            simple_metric_sample: SimpleMetricSample to convert.
        Returns:
            SimpleMetricSample object corresponding to the protobuf message.
        """
        return cls(
            value=simple_metric_sample.value,
        )

    def to_pb(self) -> metric_sample_pb2.SimpleMetricSample:
        """Convert a SimpleMetricSample object to protobuf SimpleMetricSample.
        Returns:
            Protobuf message corresponding to the SimpleMetricSample object.
        """
        return metric_sample_pb2.SimpleMetricSample(
            value=self.value,
        )


@dataclass(frozen=True)
class AggregatedMetricSample:
    """
    Encapsulates derived statistical summaries of a single metric.

    Args:
        avg_value: Derived average value of the metric.
        min_value: Minimum value of the metric.
        max_value: Maximum value of the metric.
        raw_values: Array of all the raw individual values.
    """

    avg_value: float
    min_value: float
    max_value: float
    raw_values: List[float]

    @classmethod
    def from_pb(
        cls, aggregated_metric_sample: metric_sample_pb2.AggregatedMetricSample
    ) -> AggregatedMetricSample:
        """Convert a protobuf AggregatedMetricSample to AggregatedMetricSample object.
        Args:
            aggregated_metric_sample: AggregatedMetricSample to convert.
        Returns:
            AggregatedMetricSample object corresponding to the protobuf message.
        """
        return cls(
            avg_value=aggregated_metric_sample.avg_value,
            min_value=aggregated_metric_sample.min_value,
            max_value=aggregated_metric_sample.max_value,
            raw_values=aggregated_metric_sample.raw_values,
        )

    def to_pb(self) -> metric_sample_pb2.AggregatedMetricSample:
        """Convert a AggregatedMetricSample object to protobuf AggregatedMetricSample.
        Returns:
            Protobuf message corresponding to the AggregatedMetricSample object.
        """
        return metric_sample_pb2.AggregatedMetricSample(
            avg_value=self.avg_value,
            min_value=self.min_value,
            max_value=self.max_value,
            raw_values=self.raw_values,
        )


# # From common microgrid api


@dataclass(frozen=True)
class MicrogridComponentIDs:
    """
    IDs of microgrid components.

    Args:
        microgrid_id: ID of the microgrid.
        component_ids: IDs of the components.
    """

    microgrid_id: int
    component_ids: List[int]

    @classmethod
    def from_pb(
        cls, microgrid_component_ids: microgrid_pb2.MicrogridComponentIDs
    ) -> MicrogridComponentIDs:
        """Convert a protobuf MicrogridComponentIDs to MicrogridComponentIDs object.
        Args:
            microgrid_component_ids: MicrogridComponentIDs to convert.
        Returns:
            MicrogridComponentIDs object corresponding to the protobuf message.
        """
        return cls(
            microgrid_id=microgrid_component_ids.microgrid_id,
            component_ids=microgrid_component_ids.component_ids,
        )

    def to_pb(self) -> microgrid_pb2.MicrogridComponentIDs:
        """Convert a MicrogridComponentIDs object to protobuf MicrogridComponentIDs.
        Returns:
            Protobuf message corresponding to the MicrogridComponentIDs object.
        """
        return microgrid_pb2.MicrogridComponentIDs(
            microgrid_id=self.microgrid_id,
            component_ids=self.component_ids,
        )


# # From common component api


@dataclass(frozen=True)
class ComponentData:
    """
    Data of a microgrid component which aggregates multiple metrics,
    operational states, and errors.

    Args:
        component_id: ID of the component.
        metric_samples: Measurements of a metric of the specified component.
        states: Operational states of the specified component.
    """

    component_id: int
    metric_samples: List[MetricSample]
    states: List[ComponentState]

    @classmethod
    def from_pb(
        cls, component_data: microgrid_components_components_pb2.ComponentData
    ) -> ComponentData:
        """Convert a protobuf ComponentData to ComponentData object.
        Args:
            component_data: ComponentData to convert.
        Returns:
            ComponentData object corresponding to the protobuf message.
        """
        return cls(
            component_id=component_data.component_id,
            metric=[MetricSample.from_pb(metric_sample) for metric_sample in component_data.metric_samples],
            states=[ComponentState.from_pb(state) for state in component_data.states],
        )

    def to_pb(self) -> microgrid_components_components_pb2.ComponentData:
        """Convert a ComponentData object to protobuf ComponentData.
        Returns:
            Protobuf message corresponding to the ComponentData object.
        """
        return microgrid_components_components_pb2.ComponentData(
            component_id=self.component_id.states,
            metric=[microgrid_components_components_pb2.MetricSample.ValueType(metric_sample.value) for metric_sample in self.metric_samples] if self.metric_samples else None,
            states=[microgrid_components_components_pb2.ComponentState.ValueType(state.value) for state in self.states] if self.states else None,
        )


class ComponentStateCode(enum.Enum):
    """
    List of component state codes.
    """

    # Default value
    UNSPECIFIED = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_UNSPECIFIED
    )

    # Component is in unknonwn or undefined condition
    UNKNOWN = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_UNKNOWN
    )

    # Component is temporarily unavailable
    UNAVAILABLE = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_UNAVAILABLE
    )

    # Component is switching off
    SWITCHING_OFF = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_SWITCHING_OFF
    )

    # Component has sucessfully switched off
    OFF = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_OFF
    )

    # Component is switching on
    SWITCHING_ON = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_SWITCHING_ON
    )

    # Component is in standby mode
    STANDBY = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_STANDBY
    )

    # Component is fully operational and ready
    READY = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_READY
    )

    # Component is actively consuming energy
    CHARGING = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_CHARGING
    )

    # Component is actively releasing energy
    DISCHARGING = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_DISCHARGING
    )

    # Component is in error state and may need attention
    ERROR = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_ERROR
    )

    # EV charging cable unplugged
    EV_CHARGING_CABLE_UNPLUGGED = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_UNPLUGGED
    )

    # EV charging cable plugged into charging station
    EV_CHARGING_CABLE_PLUGGED_AT_STATION = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_PLUGGED_AT_STATION
    )

    # EV charging cable plugged into vehicle
    EV_CHARGING_CABLE_PLUGGED_AT_EV = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_PLUGGED_AT_EV
    )

    # EV charging cable locked at charging station
    EV_CHARGING_CABLE_LOCKED_AT_STATION = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_LOCKED_AT_STATION
    )

    # EV charging cable locked at vehicle
    EV_CHARGING_CABLE_LOCKED_AT_EV = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_EV_CHARGING_CABLE_LOCKED_AT_EV
    )

    # Relay is in open state
    RELAY_OPEN = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_RELAY_OPEN
    )

    # Relay is in closed state
    RELAY_CLOSED = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_RELAY_CLOSED
    )

    # Precharger circuit is open
    PRECHARGER_OPEN = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_PRECHARGER_OPEN
    )

    # Precharger in precharging state
    PRECHARGER_PRECHARGING = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_PRECHARGER_PRECHARGING
    )

    # Precharger circuit is closed
    PRECHARGER_CLOSED = (
        microgrid_components_components_pb2.ComponentStateCode.COMPONENT_STATE_CODE_PRECHARGER_CLOSED
    )

    @classmethod
    def from_pb(
        cls,
        component_state_code: microgrid_components_components_pb2.ComponentStateCode.ValueType,
    ) -> ComponentStateCode:
        """Convert a protobuf ComponentStateCode value to ComponentStateCode enum.
        Args:
            component_category: ComponentStateCode to convert.
        Returns:
            Enum value corresponding to the protobuf message.
        """
        if not any(s.value == component_state_code for s in cls):
            _logger.warning(
                "Unknown component state code %s. Returning UNSPECIFIED.",
                component_state_code,
            )
            return cls.UNSPECIFIED

        return cls(component_state_code)

    def to_pb(
        self,
    ) -> microgrid_components_components_pb2.ComponentStateCode.ValueType:
        """Convert a ComponentStateCode object to protobuf ComponentStateCode.
        Returns:
            Protobuf message corresponding to the ComponentStateCode object.
        """
        return (
            microgrid_components_components_pb2.ComponentStateCode.ValueType(
                self.value
            )
        )


class ComponentErrorCode(enum.Enum):
    """
    List of component error codes.
    """

    # Default value
    UNSPECIFIED = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_UNSPECIFIED
    )

    # Component is reporting unknonwn or undefined error
    UNKNOWN = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_UNKNOWN
    )

    # Component should not be switched on
    SWITCH_ON_FAULT = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_SWITCH_ON_FAULT
    )

    # Component is operating under the minimum rated voltage
    UNDERVOLTAGE = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_UNDERVOLTAGE
    )

    # Component is operating above the maximum rated voltage
    OVERVOLTAGE = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_OVERVOLTAGE
    )

    # Component's consumption current is above the maximum rated value during charging
    OVERCURRENT_CHARGING = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_OVERCURRENT_CHARGING
    )

    # Component's consumption current is above the maximum rated value during discharging
    OVERCURRENT_DISCHARGING = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_OVERCURRENT_DISCHARGING
    )

    # Component is operating above maximum rated temperature
    OVERTEMPERATURE = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_OVERTEMPERATURE
    )

    # Component is operating below minimum rated temperature
    UNDERTEMPERATURE = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_UNDERTEMPERATURE
    )

    # Component is exposed to high humity above maximum rated value
    HIGH_HUMIDITY = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_HIGH_HUMIDITY
    )

    # Component's fuse has blown
    FUSE_ERROR = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_FUSE_ERROR
    )

    # Component's precharge unit has failed
    PRECHARGE_ERROR = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_PRECHARGE_ERROR
    )

    # Plausibility issues within the system involving this component
    PLAUSIBILITY_ERROR = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_PLAUSIBILITY_ERROR
    )

    # System shutdown due to undervolatge involving this component
    UNDERVOLTAGE_SHUTDOWN = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_UNDERVOLTAGE_SHUTDOWN
    )

    # Unexpected pilot failure in EV
    UNEXPECTED_PILOT_FAILURE = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_UNEXPECTED_PILOT_FAILURE
    )

    # Fault current detected in component
    FAULT_CURRENT = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_FAULT_CURRENT
    )

    # Short circuit detected in component
    SHORT_CIRCUIT = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_SHORT_CIRCUIT
    )

    # Configuration error related to component
    CONFIG_ERROR = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_CONFIG_ERROR
    )

    # Illegal state requested for component
    ILLEGAL_COMPONENT_STATE_CODE_REQUESTED = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_ILLEGAL_COMPONENT_STATE_CODE_REQUESTED
    )

    # Hardware of component inaccessible
    HARDWARE_INACCESSIBLE = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_HARDWARE_INACCESSIBLE
    )

    # Internal error in component
    INTERNAL = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_INTERNAL
    )

    # Component is unauthorized to perform the last requested action
    UNAUTHORIZED = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_UNAUTHORIZED
    )

    # EV cable was abruptly unplugged from charging station
    EV_CHARGING_CABLE_UNPLUGGED_FROM_STATION = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_EV_CHARGING_CABLE_UNPLUGGED_FROM_STATION
    )

    # EV cable was abruptly unplugged from vehicle
    EV_CHARGING_CABLE_UNPLUGGED_FROM_EV = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_EV_CHARGING_CABLE_UNPLUGGED_FROM_EV
    )

    # EV cable lock failure
    EV_CHARGING_CABLE_LOCK_FAILED = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_EV_CHARGING_CABLE_LOCK_FAILED
    )

    # EV cable invalid
    EV_CHARGING_CABLE_INVALID = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_EV_CHARGING_CABLE_INVALID
    )

    # Incompatible EV plug
    EV_CONSUMER_INCOMPATIBLE = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_EV_CONSUMER_INCOMPATIBLE
    )

    # Battery system imbalance
    BATTERY_IMBALANCE = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_BATTERY_IMBALANCE
    )

    # Battery low state of health (SOH)
    BATTERY_LOW_SOH = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_BATTERY_LOW_SOH
    )

    # Battery block error
    BATTERY_BLOCK_ERROR = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_BATTERY_BLOCK_ERROR
    )

    # Battery relay error
    BATTERY_RELAY_ERROR = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_BATTERY_RELAY_ERROR
    )

    # Indicating that battery calibration is needed
    BATTERY_CALIBRATION_NEEDED = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_BATTERY_CALIBRATION_NEEDED
    )

    # Relays have reached cycle limit
    RELAY_CYCLE_LIMIT_REACHED = (
        microgrid_components_components_pb2.ComponentErrorCode.COMPONENT_ERROR_CODE_RELAY_CYCLE_LIMIT_REACHED
    )

    @classmethod
    def from_pb(
        cls,
        component_error_code: microgrid_components_components_pb2.ComponentErrorCode.ValueType,
    ) -> ComponentErrorCode:
        """Convert a protobuf ComponentErrorCode value to ComponentErrorCode enum.
        Args:
            component_category: ComponentErrorCode to convert.
        Returns:
            Enum value corresponding to the protobuf message.
        """
        if not any(e.value == component_error_code for e in cls):
            _logger.warning(
                "Unknown component error code %s. Returning UNSPECIFIED.",
                component_error_code,
            )
            return cls.UNSPECIFIED

        return cls(component_error_code)

    def to_pb(
        self,
    ) -> microgrid_components_components_pb2.ComponentErrorCode.ValueType:
        """Convert a ComponentErrorCode object to protobuf ComponentErrorCode.
        Returns:
            Protobuf message corresponding to the ComponentErrorCode object.
        """
        return (
            microgrid_components_components_pb2.ComponentErrorCode.ValueType(
                self.value
            )
        )


@dataclass(frozen=True)
class ComponentState:
    """
    Operational states and errors of a microgrid component.

    Args:
        sampled_at: Time at which state was sampled
        states: List of states of the component.
        warnings: List of warnings of the component.
        errors: List of errors of the component.
    """

    sampled_at: datetime
    states: List[ComponentStateCode]
    warnings: List[ComponentErrorCode]
    errors: List[ComponentErrorCode]

    @classmethod
    def from_pb(
        cls,
        component_state: microgrid_components_components_pb2.ComponentState,
    ) -> ComponentState:
        """Convert a protobuf ComponentState to ComponentState object.
        Args:
            component_state: ComponentState to convert.
        Returns:
            ComponentState object corresponding to the protobuf message.
        """
        return cls(
            sampled_at=component_state.sampled_at.ToDatetime(),
            states=[
                ComponentStateCode.from_pb(state)
                for state in component_state.states
            ],
            warnings=[
                ComponentErrorCode.from_pb(warning)
                for warning in component_state.warnings
            ],
            errors=[
                ComponentErrorCode.from_pb(error)
                for error in component_state.errors
            ],
        )

    def to_pb(self) -> microgrid_components_components_pb2.ComponentState:
        """Convert a ComponentState object to protobuf ComponentState.
        Returns:
            Protobuf message corresponding to the ComponentState object.
        """
        return microgrid_components_components_pb2.ComponentState(
            sampled_at=timestamp_pb2.Timestamp().FromDatetime(self.sampled_at),
            states=[microgrid_components_components_pb2.ComponentStateCode.ValueType(state.value) for state in self.states] if self.states else None,
            warnings=[microgrid_components_components_pb2.ComponentErrorCode.ValueType(warning.value) for warning in self.warnings] if self.warnings else None,
            errors=[microgrid_components_components_pb2.ComponentErrorCode.ValueType(error.value) for error in self.errors] if self.errors else None,
        )


# # From common pagination api


@dataclass(frozen=True)
class PaginationParams:
    """
    Parameters for paginating list requests.
    Args:
        page_size: The maximum number of results to be returned per request.
        page_token: The token identifying a specific page of the list results.
    """

    page_size: int | None = None
    page_token: str | None = None

    @classmethod
    def from_pb(
        cls, pagination_params: pagination_params_pb2.PaginationParams
    ) -> PaginationParams:
        """Convert a protobuf PaginationParams to PaginationParams object.
        Args:
            pagination_params: PaginationParams to convert.
        Returns:
            PaginationParams object corresponding to the protobuf message.
        """
        return cls(
            page_size=pagination_params.page_size,
            page_token=pagination_params.page_token,
        )

    def to_pb(self) -> pagination_params_pb2.PaginationParams:
        """Convert a PaginationParams object to protobuf PaginationParams.
        Returns:
            Protobuf message corresponding to the PaginationParams object.
        """
        return pagination_params_pb2.PaginationParams(
            page_size=self.page_size,
            page_token=self.page_token,
        )


@dataclass(frozen=True)
class PaginationInfo:
    """
    Information about the pagination of a list request.
    Args:
        total_items: The total number of items that match the request.
        next_page_token: The token identifying the next page of results.
    """

    total_items: int
    next_page_token: str | None = None

    @classmethod
    def from_pb(
        cls, pagination_info: pagination_info_pb2.PaginationInfo
    ) -> PaginationInfo:
        """Convert a protobuf PaginationInfo to PaginationInfo object.
        Args:
            pagination_info: PaginationInfo to convert.
        Returns:
            PaginationInfo object corresponding to the protobuf message.
        """
        return cls(
            total_items=pagination_info.total_items,
            next_page_token=pagination_info.next_page_token,
        )

    def to_pb(self) -> pagination_info_pb2.PaginationInfo:
        """Convert a PaginationInfo object to protobuf PaginationInfo.
        Returns:
            Protobuf message corresponding to the PaginationInfo object.
        """
        return pagination_params_pb2.PaginationInfo(
            total_items=self.total_items,
            next_page_token=self.next_page_token,
        )


# # From reporting api


@dataclass(frozen=True)
class TimeFilter:
    """
    Time-based filter for querying aggregated microgrid components data.
    This timestamp will be >= start and < end.

    Args:
        start: Optional UTC start time for the query.
        end: Optional UTC end time for the query.
    """

    start: Optional[datetime]
    end: Optional[datetime]

    def __post_init__(self) -> None:
        """Validate the parameters."""
        if self.start is not None and not isinstance(self.start, datetime):
            raise ValueError("Start must be a datetime object or None.")
        if self.end is not None and not isinstance(self.end, datetime):
            raise ValueError("End must be a datetime object or None.")

    @classmethod
    def from_pb(cls, time_filter: reporting_pb2.TimeFilter) -> TimeFilter:
        """Convert a protobuf TimeFilter to TimeFilter object.
        Args:
            start: Optional UCT start.
            end: Optional UTC end.
        Returns:
            TimeFilter object corresponding to the protobuf message.
        """
        return cls(
            start=time_filter.start.ToDatetime()
            if time_filter.HasField("start")
            else None,
            end=time_filter.end.ToDatetime()
            if time_filter.HasField("end")
            else None,
        )

    def to_pb(self) -> reporting_pb2.TimeFilter:
        """Convert a TimeFilter object to protobuf TimeFilter.
        Returns:
            Protobuf message corresponding to the TimeFilter object.
        """
        time_filter_pb = reporting_pb2.TimeFilter()

        if self.start is not None:
            start = timestamp_pb2.Timestamp()
            start.FromDatetime(self.start)
            time_filter_pb.start.CopyFrom(start)
        if self.end is not None:
            end = timestamp_pb2.Timestamp()
            end.FromDatetime(self.end)
            time_filter_pb.end.CopyFrom(end)
        return time_filter_pb


@dataclass(frozen=True)
class ResamplingOptions:
    """
    Options for resampling aggregated microgrid components data.
    Args:
        resolution: Optional resampling resolution, represented in seconds.
    """

    resolution: Optional[int]

    @classmethod
    def from_pb(
        cls, resampling_options: reporting_pb2.ResamplingOptions
    ) -> ResamplingOptions:
        """Convert a protobuf ResamplingOptions to ResamplingOptions object.
        Args:
            resampling_options: ResamplingOptions to convert.
        Returns:
            ResamplingOptions object corresponding to the protobuf message.
        """
        return cls(
            resolution=resampling_options.resolution
            if resampling_options.HasField("resolution")
            else None,
        )

    def to_pb(self) -> reporting_pb2.ResamplingOptions:
        """Convert a ResamplingOptions object to protobuf ResamplingOptions.
        Returns:
            Protobuf message corresponding to the ResamplingOptions object.
        """
        return reporting_pb2.ResamplingOptions(
            resolution=self.resolution,
        )


class FilterOption(enum.Enum):
    """
    List of filter options.
    """

    # Default value
    UNSPECIFIED = reporting_pb2.FilterOption.FILTER_OPTION_UNSPECIFIED

    # Filter by microgrid ID
    EXCLUDE = reporting_pb2.FilterOption.FILTER_OPTION_EXCLUDE

    # Filter by component ID
    INCLUDE = reporting_pb2.FilterOption.FILTER_OPTION_INCLUDE

    @classmethod
    def from_pb(
        cls, filter_option: reporting_pb2.FilterOption.ValueType
    ) -> FilterOption:
        """Convert a protobuf FilterOption value to FilterOption enum.
        Args:
            filter_option: FilterOption to convert.
        Returns:
            Enum value corresponding to the protobuf message.
        """
        if not any(f.value == filter_option for f in cls):
            _logger.warning(
                "Unknown filter option %s. Returning UNSPECIFIED.",
                filter_option,
            )
            return cls.UNSPECIFIED

        return cls(filter_option)

    def to_pb(self) -> reporting_pb2.FilterOption.ValueType:
        """Convert a FilterOption object to protobuf FilterOption.
        Returns:
            Protobuf message corresponding to the FilterOption object.
        """
        return reporting_pb2.FilterOption.ValueType(self.value)


@dataclass(frozen=True)
class IncludeOptions:
    """
    Options for including microgrid components data.
    Args:
        filter_option: Filter option for including results in repsonse message.
        bounds: Optional bounds for filtering results.
        states: Optional states for filtering results.
    """

    filter_option: FilterOption
    bounds: Optional[FilterOption]
    states: Optional[FilterOption]

    @classmethod
    def from_pb(
        cls, include_options: reporting_pb2.IncludeOptions
    ) -> IncludeOptions:
        """Convert a protobuf IncludeOptions to IncludeOptions object.
        Args:
            include_options: IncludeOptions to convert.
        Returns:
            IncludeOptions object corresponding to the protobuf message.
        """
        return cls(
            filter_option=FilterOption.from_pb(include_options.filter_option),
            bounds=FilterOption.from_pb(include_options.bounds)
            if include_options.HasField("bounds")
            else None,
            states=FilterOption.from_pb(include_options.states)
            if include_options.HasField("states")
            else None,
        )

    def to_pb(self) -> reporting_pb2.IncludeOptions:
        """Convert a IncludeOptions object to protobuf IncludeOptions.
        Returns:
            Protobuf message corresponding to the IncludeOptions object.
        """
        return reporting_pb2.IncludeOptions(
            filter_option=self.filter_option.to_pb(),
            bounds=self.bounds.to_pb() if self.bounds is not None else None,
            states=self.states.to_pb() if self.states is not None else None,
        )


@dataclass(frozen=True)
class AggregationConfig:
    """
    Configuration for aggregating microgrid components data.
    Args:
        microgrid_id: ID of the microgrid for which the data is aggregated.
        metric: Metric for which the data is aggregated.
        aggregation_formula: Optional aggregation formula for aggregating the metric.
    """

    microgrid_id: int
    metric: Metric
    aggreation_formula: str

    @classmethod
    def from_pb(
        cls, aggregation_config: reporting_pb2.AggregationConfig
    ) -> AggregationConfig:
        """Convert a protobuf AggregationConfig to AggregationConfig object.
        Args:
            aggregation_config: AggregationConfig to convert.
        Returns:
            AggregationConfig object corresponding to the protobuf message.
        """
        return cls(
            microgrid_id=aggregation_config.microgrid_id,
            metric=Metric.from_pb(aggregation_config.metric),
            aggregation_formula=aggregation_config.aggregation_formula,
        )

    def to_pb(self) -> reporting_pb2.AggregationConfig:
        """Convert a AggregationConfig object to protobuf AggregationConfig.
        Returns:
            Protobuf message corresponding to the AggregationConfig object.
        """
        return reporting_pb2.AggregationConfig(
            microgrid_id=self.microgrid_id,
            metric=self.metric.to_pb(),
            aggregation_formula=self.aggregation_formula,
        )


@dataclass(frozen=True)
class SimpleAggregatedMetricSample:
    """
    Aggregated metric sample with a single value.
    Args:
        sampled_at: Time at which metric was sampled.
        sample: Aggregated value of the metric.
    """

    sampled_at: datetime
    sample: SimpleMetricSample

    @classmethod
    def from_pb(
        cls,
        simple_aggregated_metric_sample: reporting_pb2.SimpleAggregatedMetricSample,
    ) -> SimpleAggregatedMetricSample:
        """Convert a protobuf SimpleAggregatedMetricSample to SimpleAggregatedMetricSample object.
        Args:
            simple_aggregated_metric_sample: SimpleAggregatedMetricSample to convert.
        Returns:
            SimpleAggregatedMetricSample object corresponding to the protobuf message.
        """
        return cls(
            sampled_at=simple_aggregated_metric_sample.sampled_at.ToDatetime(),
            sample=SimpleMetricSample.from_pb(
                simple_aggregated_metric_sample.sample
            ),
        )

    def to_pb(self) -> reporting_pb2.SimpleAggregatedMetricSample:
        """Convert a SimpleAggregatedMetricSample object to protobuf SimpleAggregatedMetricSample.
        Returns:
            Protobuf message corresponding to the SimpleAggregatedMetricSample object.
        """
        return reporting_pb2.SimpleAggregatedMetricSample(
            sampled_at=timestamp_pb2.Timestamp().FromDatetime(self.sampled_at),
            sample=self.sample.to_pb(),
        )


@dataclass(frozen=True)
class ListFilter:
    """
    Filter for querying microgrid components data.
    Args:
        resampling_options: Optional resampling options. If ommited, no resampling will be performed.
        time_filter: Optional time filter for querying data.
        include_options: Optional include options for querying data.
    """

    resampling_options: Optional[ResamplingOptions]
    time_filter: Optional[TimeFilter]
    include_options: Optional[IncludeOptions]

    @classmethod
    def from_pb(cls, list_filter: reporting_pb2.ListFilter) -> ListFilter:
        """Convert a protobuf ListFilter to ListFilter object.
        Args:
            list_filter: ListFilter to convert.
        Returns:
            ListFilter object corresponding to the protobuf message.
        """
        return cls(
            resampling_options=ResamplingOptions.from_pb(
                list_filter.resampling_options
            )
            if list_filter.HasField("resampling_options")
            else None,
            time_filter=TimeFilter.from_pb(list_filter.time_filter)
            if list_filter.HasField("time_filter")
            else None,
            include_options=IncludeOptions.from_pb(list_filter.include_options)
            if list_filter.HasField("include_options")
            else None,
        )

    def to_pb(self) -> reporting_pb2.ListFilter:
        """Convert a ListFilter object to protobuf ListFilter.
        Returns:
            Protobuf message corresponding to the ListFilter object.
        """
        return reporting_pb2.ListFilter(
            resampling_options=self.resampling_options.to_pb()
            if self.resampling_options is not None
            else None,
            time_filter=self.time_filter.to_pb()
            if self.time_filter is not None
            else None,
            include_options=self.include_options.to_pb()
            if self.include_options is not None
            else None,
        )


@dataclass(frozen=True)
class MicrogridData:
    """
    Microgrid data report with metric samples for a single microgrid organised by components.
    Args:
        microgrid_id: Microgrid ID for which the data is reported.
        components: List of components within this microgrid.
    """

    microgrid_id: int
    components: List[ComponentData]

    @classmethod
    def from_pb(
        cls, microgrid_data: reporting_pb2.MicrogridData
    ) -> MicrogridData:
        """Convert a protobuf MicrogridData to MicrogridData object.
        Args:
            microgrid_data: MicrogridData to convert.
        Returns:
            MicrogridData object corresponding to the protobuf message.
        """
        return cls(
            microgrid_id=microgrid_data.microgrid_id,
            components=[
                ComponentData.from_pb(component)
                for component in microgrid_data.components
            ],
        )

    def to_pb(self) -> reporting_pb2.MicrogridData:
        """Convert a MicrogridData object to protobuf MicrogridData.
        Returns:
            Protobuf message corresponding to the MicrogridData object.
        """
        return reporting_pb2.MicrogridData(
            microgrid_id=self.microgrid_id,
            components=[microgrid_components_components_pb2.ComponentData.ValueType(component.value) for component in self.components] if self.components else None,
        )


@dataclass(frozen=True)
class StreamFilter:
    """
    Filter for querying live microgrid components data.
    Args:
       resampling_options: Optional resampling options. If ommited, no resampling will be performed.
       include_options: Optional include options for querying data.
    """

    resampling_options: Optional[ResamplingOptions]
    include_options: Optional[IncludeOptions]

    @classmethod
    def from_pb(
        cls, stream_filter: reporting_pb2.StreamFilter
    ) -> StreamFilter:
        """Convert a protobuf StreamFilter to StreamFilter object.
        Args:
            stream_filter: StreamFilter to convert.
        Returns:
            StreamFilter object corresponding to the protobuf message.
        """
        return cls(
            resampling_options=ResamplingOptions.from_pb(
                stream_filter.resampling_options
            )
            if stream_filter.HasField("resampling_options")
            else None,
            include_options=IncludeOptions.from_pb(
                stream_filter.include_options
            )
            if stream_filter.HasField("include_options")
            else None,
        )

    def to_pb(self) -> reporting_pb2.StreamFilter:
        """Convert a StreamFilter object to protobuf StreamFilter.
        Returns:
            Protobuf message corresponding to the StreamFilter object.
        """
        return reporting_pb2.StreamFilter(
            resampling_options=self.resampling_options.to_pb()
            if self.resampling_options is not None
            else None,
            include_options=self.include_options.to_pb()
            if self.include_options is not None
            else None,
        )


@dataclass(frozen=True)
class AggregationListFilter:
    """General filter for querying aggregated microgrid components data.
    Args:
        resampling_options: Optional resampling options. If ommited, no resampling will be performed.
        time_filter: Optional time filter for querying data.
    """

    resampling_options: Optional[ResamplingOptions]
    time_filter: Optional[TimeFilter]

    @classmethod
    def from_pb(
        cls, aggregation_list_filter: reporting_pb2.AggregationListFilter
    ) -> AggregationListFilter:
        """Convert a protobuf AggreagtionListFilter to AggreagtionListFilter object.
        Args:
            aggregation_list_filter: AggreagtionListFilter to convert.
        Returns:
            AggreagtionListFilter object corresponding to the protobuf message.
        """
        return cls(
            resampling_options=ResamplingOptions.from_pb(
                aggregation_list_filter.resampling_options
            )
            if aggregation_list_filter.HasField("resampling_options")
            else None,
            time_filter=TimeFilter.from_pb(aggregation_list_filter.time_filter)
            if aggregation_list_filter.HasField("time_filter")
            else None,
        )

    def to_pb(self) -> reporting_pb2.AggregationListFilter:
        """Convert a AggreagtionListFilter object to protobuf AggreagtionListFilter.
        Returns:
            Protobuf message corresponding to the AggreagtionListFilter object.
        """
        return reporting_pb2.AggregationListFilter(
            resampling_options=self.resampling_options.to_pb()
            if self.resampling_options is not None
            else None,
            time_filter=self.time_filter.to_pb()
            if self.time_filter is not None
            else None,
        )


@dataclass(frozen=True)
class AggregatedResult:
    """Aggregated metric sample with a single value.
    Args:
        aggregation_config: Configuration for aggregating microgrid components data.
        samples: List of aggregated metric samples.
    """

    aggregation_config: AggregationConfig
    samples: List[SimpleAggregatedMetricSample]

    @classmethod
    def from_pb(
        cls, aggregated_result: reporting_pb2.AggregatedResult
    ) -> AggregatedResult:
        """Convert a protobuf AggregatedResult to AggregatedResult object.
        Args:
            aggregated_result: AggregatedResult to convert.
        Returns:
            AggregatedResult object corresponding to the protobuf message.
        """
        return cls(
            aggregation_config=AggregationConfig.from_pb(
                aggregated_result.aggregation_config
            ),
            samples=[
                SimpleAggregatedMetricSample.from_pb(sample)
                for sample in aggregated_result.samples
            ],
        )

    def to_pb(self) -> reporting_pb2.AggregatedResult:
        """Convert a AggregatedResult object to protobuf AggregatedResult.
        Returns:
            Protobuf message corresponding to the AggregatedResult object.
        """
        return reporting_pb2.AggregatedResult(
            aggregation_config=self.aggregation_config.to_pb(),
            samples=[reporting_pb2.SimpleAggregatedMetricSample.ValueType(sample.value) for sample in self.samples] if self.samples else None,
        )


@dataclass(frozen=True)
class AggregatedStreamFilter:
    """Filter for querying live aggregated microgrid components data.
    Args:
        resampling_options: Optional resampling options. If ommited, no resampling will be performed.
    """

    resampling_options: Optional[ResamplingOptions]

    @classmethod
    def from_pb(
        cls, aggregated_stream_filter: reporting_pb2.AggregatedStreamFilter
    ) -> AggregatedStreamFilter:
        """Convert a protobuf AggregatedStreamFilter to AggregatedStreamFilter object.
        Args:
            aggregated_stream_filter: AggregatedStreamFilter to convert.
        Returns:
            AggregatedStreamFilter object corresponding to the protobuf message.
        """
        return cls(
            resampling_options=ResamplingOptions.from_pb(
                aggregated_stream_filter.resampling_options
            )
            if aggregated_stream_filter.HasField("resampling_options")
            else None,
        )

    def to_pb(self) -> reporting_pb2.AggregatedStreamFilter:
        """Convert a AggregatedStreamFilter object to protobuf AggregatedStreamFilter.
        Returns:
            Protobuf message corresponding to the AggregatedStreamFilter object.
        """
        return reporting_pb2.AggregatedStreamFilter(
            resampling_options=self.resampling_options.to_pb()
            if self.resampling_options is not None
            else None,
        )

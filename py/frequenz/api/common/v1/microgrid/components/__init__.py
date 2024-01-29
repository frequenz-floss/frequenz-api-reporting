# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: frequenz/api/common/v1/microgrid/components/battery.proto, frequenz/api/common/v1/microgrid/components/components.proto, frequenz/api/common/v1/microgrid/components/ev_charger.proto, frequenz/api/common/v1/microgrid/components/fuse.proto, frequenz/api/common/v1/microgrid/components/grid.proto, frequenz/api/common/v1/microgrid/components/inverter.proto, frequenz/api/common/v1/microgrid/components/transformer.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from datetime import datetime
from typing import List

import betterproto

from ... import (
    metrics as __metrics__,
    microgrid as __microgrid__,
)


class BatteryType(betterproto.Enum):
    """Enumerated battery types."""

    BATTERY_TYPE_UNSPECIFIED = 0
    """Unspecified."""

    BATTERY_TYPE_LI_ION = 1
    """Li-ion batteries."""

    BATTERY_TYPE_NA_ION = 2
    """Sodium-ion batteries"""


class EvChargerType(betterproto.Enum):
    """Enumerated EV charger types."""

    EV_CHARGER_TYPE_UNSPECIFIED = 0
    """Default type."""

    EV_CHARGER_TYPE_AC = 1
    """The EV charging station supports AC charging only."""

    EV_CHARGER_TYPE_DC = 2
    """The EV charging station supports DC charging only."""

    EV_CHARGER_TYPE_HYBRID = 3
    """The EV charging station supports both AC and DC."""


class InverterType(betterproto.Enum):
    """Enumerated inverter types."""

    INVERTER_TYPE_UNSPECIFIED = 0
    """Unspecified."""

    INVERTER_TYPE_BATTERY = 1
    """Battery inverter."""

    INVERTER_TYPE_SOLAR = 2
    """Solar inverter."""

    INVERTER_TYPE_HYBRID = 3
    """Hybrid inverter."""


class ComponentCategory(betterproto.Enum):
    """Enumrated component categories."""

    COMPONENT_CATEGORY_UNSPECIFIED = 0
    """
    An unknown component categories, useful for error handling, and marking
    unknown components in a list of components with otherwise known categories.
    """

    COMPONENT_CATEGORY_GRID = 1
    """The point where the local microgrid is connected to the grid."""

    COMPONENT_CATEGORY_METER = 2
    """
    A meter, for measuring electrical metrics, e.g., current, voltage, etc.
    """

    COMPONENT_CATEGORY_INVERTER = 3
    """An electricity generator, with batteries or solar energy."""

    COMPONENT_CATEGORY_CONVERTER = 4
    """A DC-DC converter."""

    COMPONENT_CATEGORY_BATTERY = 5
    """A storage system for electrical energy, used by inverters."""

    COMPONENT_CATEGORY_EV_CHARGER = 6
    """A station for charging electrical vehicles."""

    COMPONENT_CATEGORY_CRYPTO_MINER = 8
    """A crypto miner."""

    COMPONENT_CATEGORY_ELECTROLYZER = 9
    """An electrolyzer for converting water into hydrogen and oxygen."""

    COMPONENT_CATEGORY_CHP = 10
    """
    A heat and power combustion plant (CHP stands for combined heat and power).
    """

    COMPONENT_CATEGORY_RELAY = 11
    """
    A relay. Relays generally have two states: open (connected) and closed
    (disconnected). They are generally placed in front of a component, e.g., an
    inverter, to control whether the component is connected to the grid or not.
    """

    COMPONENT_CATEGORY_PRECHARGER = 12
    """
    A precharge module. Precharging involves gradually ramping up the DC
    voltage to prevent any potential damage to sensitive electrical components
    like capacitors. While many inverters and batteries come equipped with in-
    built precharging mechanisms, some may lack this feature. In such cases, we
    need to use external precharging modules.
    """

    COMPONENT_CATEGORY_FUSE = 13
    """
    A fuse. Fuses are used to protect electrical components from overcurrents.
    """

    COMPONENT_CATEGORY_VOLTAGE_TRANSFORMER = 14
    """
    A voltage transformer. Voltage transformers are used to step up or step
    down the voltage, keeping the power somewhat constant by increasing or
    decreasing the current. If voltage is stepped up, current is stepped down,
    and vice versa. Note that voltage transformers have efficiency losses, so
    the output power is always less than the input power.
    """


class ComponentStatus(betterproto.Enum):
    """
    ComponentStatus defines the possible statuses for a component. !!! note
    The status indicates the status set by the user via the user interface.
    The status is not yet included in the Component messages and should be
    added.
    """

    COMPONENT_STATUS_UNSPECIFIED = 0
    """The status is unspecified. This should not be used."""

    COMPONENT_STATUS_ACTIVE = 1
    """The component is active."""

    COMPONENT_STATUS_INACTIVE = 2
    """The component is inactive."""


class ComponentStateCode(betterproto.Enum):
    """
    Enum to represent the various states that a component can be in. This enum
    is unified across all component categories for consistency.
    """

    COMPONENT_STATE_CODE_UNSPECIFIED = 0
    """
    Default value when the component state is not explicitly set. This is the
    zero value of the enum.
    """

    COMPONENT_STATE_CODE_UNKNOWN = 1
    """
    State when the component is in an unknown or undefined condition. This is
    used when the sender is unable to classify the component into any other
    state.
    """

    COMPONENT_STATE_CODE_UNAVAILABLE = 2
    """State when the component is temporarily unavailable for operation."""

    COMPONENT_STATE_CODE_SWITCHING_OFF = 3
    """State when the component is in the process of switching off."""

    COMPONENT_STATE_CODE_OFF = 4
    """State when the component has successfully switched off."""

    COMPONENT_STATE_CODE_SWITCHING_ON = 5
    """
    State when the component is in the process of switching on from an off
    state.
    """

    COMPONENT_STATE_CODE_STANDBY = 6
    """
    State when the component is in standby mode, and not immediately ready for
    immediate operations.
    """

    COMPONENT_STATE_CODE_READY = 7
    """State when the component is fully operational and ready for use."""

    COMPONENT_STATE_CODE_CHARGING = 8
    """State when the component is actively consuming energy."""

    COMPONENT_STATE_CODE_DISCHARGING = 9
    """State when the component is actively producing or releasing energy."""

    COMPONENT_STATE_CODE_ERROR = 10
    """
    State when the component is in an error state and may need attention.
    """

    COMPONENT_STATE_CODE_EV_CHARGING_CABLE_UNPLUGGED = 20
    """
    The Electric Vehicle (EV) charging cable is unplugged from the charging
    station.
    """

    COMPONENT_STATE_CODE_EV_CHARGING_CABLE_PLUGGED_AT_STATION = 21
    """The EV charging cable is plugged into the charging station."""

    COMPONENT_STATE_CODE_EV_CHARGING_CABLE_PLUGGED_AT_EV = 22
    """The EV charging cable is plugged into the vehicle."""

    COMPONENT_STATE_CODE_EV_CHARGING_CABLE_LOCKED_AT_STATION = 23
    """
    The EV charging cable is locked at the charging station end, indicating
    readiness for charging.
    """

    COMPONENT_STATE_CODE_EV_CHARGING_CABLE_LOCKED_AT_EV = 24
    """
    The EV charging cable is locked at the vehicle end, indicating that
    charging is active.
    """

    COMPONENT_STATE_CODE_RELAY_OPEN = 30
    """The relay is in an open state, meaning no current can flow through."""

    COMPONENT_STATE_CODE_RELAY_CLOSED = 31
    """The relay is in a closed state, allowing current to flow."""

    COMPONENT_STATE_CODE_PRECHARGER_OPEN = 40
    """The precharger circuit is open, meaning it's not currently active."""

    COMPONENT_STATE_CODE_PRECHARGER_PRECHARGING = 41
    """
    The precharger is in a precharging state, preparing the main circuit for
    activation.
    """

    COMPONENT_STATE_CODE_PRECHARGER_CLOSED = 42
    """
    The precharger circuit is closed, allowing full current to flow to the main
    circuit.
    """


class ComponentErrorCode(betterproto.Enum):
    """
    A representation of all possible errors that can occur across all component
    categories.
    """

    COMPONENT_ERROR_CODE_UNSPECIFIED = 0
    """Default value. No specific error is specified."""

    COMPONENT_ERROR_CODE_UNKNOWN = 1
    """
    The component is reporting an unknown or an undefined error, and the sender
    cannot parse the component error to any of the variants below.
    """

    COMPONENT_ERROR_CODE_SWITCH_ON_FAULT = 2
    """Error indicating that the component could not be switched on."""

    COMPONENT_ERROR_CODE_UNDERVOLTAGE = 3
    """
    Error indicating that the component is operating under the minimum rated
    voltage.
    """

    COMPONENT_ERROR_CODE_OVERVOLTAGE = 4
    """
    Error indicating that the component is operating over the maximum rated
    voltage.
    """

    COMPONENT_ERROR_CODE_OVERCURRENT = 5
    """
    Error indicating that the component is drawing more current than the
    maximum rated value.
    """

    COMPONENT_ERROR_CODE_OVERCURRENT_CHARGING = 6
    """
    Error indicating that the component's consumption current is over the
    maximum rated value during charging.
    """

    COMPONENT_ERROR_CODE_OVERCURRENT_DISCHARGING = 7
    """
    Error indicating that the component's production current is over the
    maximum rated value during discharging.
    """

    COMPONENT_ERROR_CODE_OVERTEMPERATURE = 8
    """
    Error indicating that the component is operating over the maximum rated
    temperature.
    """

    COMPONENT_ERROR_CODE_UNDERTEMPERATURE = 9
    """
    Error indicating that the component is operating under the minimum rated
    temperature.
    """

    COMPONENT_ERROR_CODE_HIGH_HUMIDITY = 10
    """
    Error indicating that the component is exposed to high humidity levels over
    the maximum rated value.
    """

    COMPONENT_ERROR_CODE_FUSE_ERROR = 11
    """Error indicating that the component's fuse has blown."""

    COMPONENT_ERROR_CODE_PRECHARGE_ERROR = 12
    """Error indicating that the component's precharge unit has failed."""

    COMPONENT_ERROR_CODE_PLAUSIBILITY_ERROR = 13
    """
    Error indicating plausibility issues within the system involving this
    component.
    """

    COMPONENT_ERROR_CODE_UNDERVOLTAGE_SHUTDOWN = 14
    """
    Error indicating system shutdown due to undervoltage involving this
    component.
    """

    COMPONENT_ERROR_CODE_EV_UNEXPECTED_PILOT_FAILURE = 15
    """
    Error indicating unexpected pilot failure in an electric vehicle (EV)
    component.
    """

    COMPONENT_ERROR_CODE_FAULT_CURRENT = 16
    """Error indicating fault current detected in the component."""

    COMPONENT_ERROR_CODE_SHORT_CIRCUIT = 17
    """Error indicating a short circuit detected in the component."""

    COMPONENT_ERROR_CODE_CONFIG_ERROR = 18
    """Error indicating a configuration error related to the component."""

    COMPONENT_ERROR_CODE_ILLEGAL_COMPONENT_STATE_CODE_REQUESTED = 19
    """Error indicating an illegal state requested for the component."""

    COMPONENT_ERROR_CODE_HARDWARE_INACCESSIBLE = 20
    """Error indicating that the hardware of the component is inaccessible."""

    COMPONENT_ERROR_CODE_INTERNAL = 21
    """Error indicating an internal error within the component."""

    COMPONENT_ERROR_CODE_UNAUTHORIZED = 22
    """
    Error indicating that the component is unauthorized to perform the last
    requested action.
    """

    COMPONENT_ERROR_CODE_EV_CHARGING_CABLE_UNPLUGGED_FROM_STATION = 40
    """
    Error indicating electric vehicle (EV) cable was abruptly unplugged from
    the charging station.
    """

    COMPONENT_ERROR_CODE_EV_CHARGING_CABLE_UNPLUGGED_FROM_EV = 41
    """
    Error indicating electric vehicle (EV) cable was abruptly unplugged from
    the vehicle.
    """

    COMPONENT_ERROR_CODE_EV_CHARGING_CABLE_LOCK_FAILED = 42
    """Error indicating electric vehicle (EV) cable lock failure."""

    COMPONENT_ERROR_CODE_EV_CHARGING_CABLE_INVALID = 43
    """Error indicating an invalid electric vehicle (EV) cable."""

    COMPONENT_ERROR_CODE_EV_CONSUMER_INCOMPATIBLE = 44
    """Error indicating an incompatible electric vehicle (EV) plug."""

    COMPONENT_ERROR_CODE_BATTERY_IMBALANCE = 50
    """Error indicating a battery system imbalance."""

    COMPONENT_ERROR_CODE_BATTERY_LOW_SOH = 51
    """
    Error indicating a low state of health (SOH) detected in the battery.
    """

    COMPONENT_ERROR_CODE_BATTERY_BLOCK_ERROR = 52
    """Error indicating a battery block error."""

    COMPONENT_ERROR_CODE_BATTERY_CONTROLLER_ERROR = 53
    """Error indicating a battery controller error."""

    COMPONENT_ERROR_CODE_BATTERY_RELAY_ERROR = 54
    """Error indicating a battery relay error."""

    COMPONENT_ERROR_CODE_BATTERY_CALIBRATION_NEEDED = 56
    """Error indicating that battery calibration is needed."""

    COMPONENT_ERROR_CODE_RELAY_CYCLE_LIMIT_REACHED = 60
    """
    Error indicating that the relays have been cycled for the maximum number of
    times.
    """


@dataclass(eq=False, repr=False)
class Battery(betterproto.Message):
    """A representation of a battery."""

    type: "BatteryType" = betterproto.enum_field(1)
    """The battery type."""


@dataclass(eq=False, repr=False)
class EvCharger(betterproto.Message):
    """A representation of an EV chaging station."""

    type: "EvChargerType" = betterproto.enum_field(1)
    """The EV charger type."""


@dataclass(eq=False, repr=False)
class Fuse(betterproto.Message):
    """
    A representation of a fuse. The fuse component represents a fuse in the
    microgrid. It is used to protect components from overcurrents.
    """

    rated_current: int = betterproto.uint32_field(1)
    """
    The rated current of the fuse in amperes. This is the maximum current that
    the fuse can withstand for a long time. This limit applies to currents both
    flowing in or out of each of the 3 phases individually. In other words, a
    current _i_ A at one of the phases of the node must comply with the
    following constraint: `-rated_fuse_current <= i <= rated_fuse_current`
    """


@dataclass(eq=False, repr=False)
class GridConnectionPoint(betterproto.Message):
    """
    A representation of a grid connection point. This is the point where a
    microgrid connects to the grid. The terms "Grid Connection Point" and
    "Point of Common Coupling" (PCC) are commonly used in the context. While
    both terms describe a connection point to the grid, the
    `GridConnectionPoint` is specifically the physical connection point of the
    generation facility to the grid, often concerned with the technical and
    ownership aspects of the connection. In contrast, the PCC is is more
    specific in terms of electrical engineering. It refers to the point where a
    customer's local electrical system (such as a microgrid) connects to the
    utility distribution grid in such a way that it can affect other customers’
    systems connected to the same network. It is the point where the grid and
    customer's electrical systems interface and where issues like power quality
    and supply regulations are assessed. The term `GridConnectionPoint` is used
    to make it clear that what is referred to here is the physical connection
    point of the local facility to the grid. Note that this may also be the PCC
    in some cases.
    """

    rated_fuse_current: int = betterproto.uint32_field(1)
    """
    This refers to the maximum amount of electrical current, in amperes, that a
    fuse at the grid connection point is designed to safely carry under normal
    operating conditions. This limit applies to currents both flowing in or out
    of each of the 3 phases individually. In other words, a current _i_ A at
    one of the phases of the grid connection point must comply with the
    following constraint: `-rated_fuse_current <= i <= rated_fuse_current`
    """


@dataclass(eq=False, repr=False)
class Inverter(betterproto.Message):
    """A representation of an inverter. The inverter metadata."""

    type: "InverterType" = betterproto.enum_field(1)
    """The inverter type."""


@dataclass(eq=False, repr=False)
class VoltageTransformer(betterproto.Message):
    """
    A representation of a voltage transformer. Voltage transformers are used to
    step up or step down the voltage, keeping the power somewhat constant by
    increasing or decreasing the current. If voltage is stepped up, current is
    stepped down, and vice versa. Note that voltage transformers have
    efficiency losses, so the output power is always less than the input power.
    """

    primary: float = betterproto.float_field(1)
    """
    The primary voltage of the transformer. This is the input voltage that is
    stepped up or down.
    """

    secondary: float = betterproto.float_field(2)
    """
    The secondary voltage of the transformer. This is the output voltage that
    is the result of stepping the primary voltage up or down.
    """


@dataclass(eq=False, repr=False)
class ComponentCategoryMetadataVariant(betterproto.Message):
    """Metadata specific to a microgrid component."""

    battery: "Battery" = betterproto.message_field(1, group="metadata")
    ev_charger: "EvCharger" = betterproto.message_field(2, group="metadata")
    fuse: "Fuse" = betterproto.message_field(3, group="metadata")
    grid: "GridConnectionPoint" = betterproto.message_field(4, group="metadata")
    inverter: "Inverter" = betterproto.message_field(5, group="metadata")
    voltage_transformer: "VoltageTransformer" = betterproto.message_field(
        6, group="metadata"
    )


@dataclass(eq=False, repr=False)
class Component(betterproto.Message):
    """Microgrid electrical component details."""

    id: int = betterproto.uint64_field(1)
    """The component ID."""

    microgrid_id: int = betterproto.uint64_field(2)
    """Unique identifier of the parent microgrid_id."""

    name: str = betterproto.string_field(3)
    """The component name."""

    category: "ComponentCategory" = betterproto.enum_field(4)
    """The component category. E.g., Inverter, Battery, etc."""

    category_type: "ComponentCategoryMetadataVariant" = betterproto.message_field(5)
    """The metadata specific to the component category type."""

    manufacturer: str = betterproto.string_field(6)
    """The component manufacturer."""

    model_name: str = betterproto.string_field(7)
    """The model name of the component."""

    status: "ComponentStatus" = betterproto.enum_field(8)
    """The status of the component."""

    operational_lifetime: "__microgrid__.Lifetime" = betterproto.message_field(9)
    """The operational lifetime of the component."""


@dataclass(eq=False, repr=False)
class ComponentConnection(betterproto.Message):
    """
    ComponentConnection describes a single electrical link between two
    components within a microgrid, effectively representing the physical wiring
    as viewed from the grid connection point, if one exists, or from the
    islanding point, in case of an islanded microgrids. !!! note "Physical
    Representation"     This message is not about data flow but rather about
    the physical     electrical connections between components. Therefore, the
    IDs for the     source and destination components correspond to the actual
    setup within     the microgrid. !!! note "Direction"     The direction of
    the connection follows the flow of current away from the     grid
    connection point, or in case of islands, away from the islanding     point.
    This direction is aligned with positive current according to the
    [Passive Sign Convention]
    (https://en.wikipedia.org/wiki/Passive_sign_convention). !!! info
    "Historical Data"     The timestamps of when a connection was created and
    terminated allows for     tracking the changes over time to a microgrid,
    providing insights into     when and how the microgrid infrastructure has
    been modified.
    """

    source_component_id: int = betterproto.uint64_field(1)
    """
    Unique identifier of the component where the connection originates. This is
    aligned with the direction of current flow away from the grid connection
    point, or in case of islands, away from the islanding point.
    """

    destination_component_id: int = betterproto.uint64_field(2)
    """
    Unique ID of the component where the connection terminates. This is the
    component towards which the current flows.
    """

    operational_lifetime: "__microgrid__.Lifetime" = betterproto.message_field(3)
    """The operational lifetime of the connection."""


@dataclass(eq=False, repr=False)
class ComponentData(betterproto.Message):
    """
    ComponentData message aggregates multiple metrics, operational states, and
    errors, related to a specific microgrid component. !!! example   Example
    output of a component data message:   ```    {      component_id: 13,
    metric_samples: [        /* list of metrics for multiple timestamps */
    {          sampled_at: "2023-10-01T00:00:00Z",          metric:
    "DC_VOLTAGE_V",          sample: {},          bounds: {},        },
    {          sampled_at: "2023-10-01T00:00:00Z",          metric:
    "DC_VOLTAGE_V",          sample: {},          bounds: {},        }      ],
    states: [        /* list of states for multiple timestamps */        {
    sampled_at: "2023-10-01T00:00:00Z",          states: [],          errors:
    [],        },        {          sampled_at: "2023-10-01T00:00:00Z",
    states: [],          errors: [],        },      ]    }  ```
    """

    component_id: int = betterproto.uint64_field(1)
    """The ID of the microgrid component."""

    metric_samples: List["__metrics__.MetricSample"] = betterproto.message_field(2)
    """
    List of measurements for a metric of the specific microgrid component.
    """

    states: List["ComponentState"] = betterproto.message_field(3)
    """List of states of a specific microgrid component."""


@dataclass(eq=False, repr=False)
class ComponentState(betterproto.Message):
    """Representation of a component state and errors."""

    sampled_at: datetime = betterproto.message_field(1)
    """The time at which the state was sampled."""

    states: List["ComponentStateCode"] = betterproto.enum_field(2)
    """
    List of states of the microgrid component. !!! note    The list will
    contain unique members. No state will exist twice in    this list.
    """

    warnings: List["ComponentErrorCode"] = betterproto.enum_field(3)
    """
    List of warnings for the microgrid component. !!! note    This list may
    have warnings even if the component state is not in an    error state. !!!
    note    The list will contain unique members. No warning will exist twice
    in    this list.
    """

    errors: List["ComponentErrorCode"] = betterproto.enum_field(4)
    """
    List of errors for the microgrid component. !!! note    This list is
    expected to have errors if and only if the component is in    an error
    state. !!! note    The list will contain unique members. No error will
    exist twice in    this list.
    """
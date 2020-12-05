"""ENum values dictionary for the Home Connect integration."""

enum_list = {
    "BSH.Common.Status.OperationState" : "Operation State",

    "BSH.Common.EnumType.OperationState.Inactive" : "Inactive",
    "BSH.Common.EnumType.OperationState.Ready" : "Ready",
    "BSH.Common.EnumType.OperationState.DelayedStart" : "Delayed Start",
    "BSH.Common.EnumType.OperationState.Run" : "Run",
    "BSH.Common.EnumType.OperationState.Pause" : "Pause",
    "BSH.Common.EnumType.OperationState.ActionRequired" : "Action Required",
    "BSH.Common.EnumType.OperationState.Finished" : "Finished",
    "BSH.Common.EnumType.OperationState.Error" : "Error",
    "BSH.Common.EnumType.OperationState.Aborting" : "Aborting",

    "BSH.Common.Setting.PowerState" : "Power State",

    "BSH.Common.EnumType.PowerState.Off" : "Off",
    "BSH.Common.EnumType.PowerState.On" : "On",
    "BSH.Common.EnumType.PowerState.Standby" : "Standby",

    "BSH.Common.Setting.TemperatureUnit" : "Temperature Units",

    "BSH.Common.EnumType.TemperatureUnit.Celsius" : "Celsius",
    "BSH.Common.EnumType.TemperatureUnit.Fahrenheit" : "Fahrenheit",

    "BSH.Common.Status.DoorState" : "Door State",

    "BSH.Common.EnumType.DoorState.Open" : "Open",
    "BSH.Common.EnumType.DoorState.Closed" : "Closed",
    "BSH.Common.EnumType.DoorState.Locked" : "Locked",

    "BSH.Common.Status.LocalControlActive" : "Local Control Activation",
    "BSH.Common.Status.RemoteControlActive": "Remote Control Activation",
    "BSH.Common.Status.RemoteControlStartAllowed" : "Remote Control Allowed",

    "BSH.Common.Root.ActiveProgram" : "Active Program",
    "BSH.Common.Root.SelectedProgram" : "Selected Program",

    "BSH.Common.Option.RemainingProgramTime" : "Remaining Program Time",
    "BSH.Common.Option.ElapsedProgramTime" : "Elapsed Program Time",
    "BSH.Common.Option.ProgramProgress" : "Program Progress",
    "BSH.Common.Option.Duration" : "Program Duration",

    "BSH.Common.Event.ProgramFinished" : "Program Finished",
    "BSH.Common.Event.AlarmClockElapsed" : "Alarm Clock Elapsed",
    "LaundryCare.Dryer.Event.DryingProcessFinished" : "Drying Process Finished",

    "BSH.Common.EnumType.EventPresentState.Present" : "Event Present",
    "BSH.Common.EnumType.EventPresentState.Off" : "Event Off",
    "BSH.Common.EnumType.EventPresentState.Confirmed" : "Event Confirmed",

    "LaundryCare.Dryer.Program.Cotton" : "Cotton",
    "LaundryCare.Dryer.Program.Synthetic" : "Synthetic",
    "LaundryCare.Dryer.Program.Mix" : "Mix Textiles",
    "LaundryCare.Dryer.Program.Blankets" : "Blankets",
    "LaundryCare.Dryer.Program.BusinessShirts" : "Business Shirts",
    "LaundryCare.Dryer.Program.DownFeathers" : "Down Feathers",
    "LaundryCare.Dryer.Program.Hygiene" : "Hygiene",
    "LaundryCare.Dryer.Program.Jeans" : "Jeans",
    "LaundryCare.Dryer.Program.Outdoor" : "Outdoor",
    "LaundryCare.Dryer.Program.SyntheticRefresh" : "Synthetic Refresh",
    "LaundryCare.Dryer.Program.Towels" : "Towels",
    "LaundryCare.Dryer.Program.Delicates" : "Delicates",
    "LaundryCare.Dryer.Program.Super40" : "Super 40'",
    "LaundryCare.Dryer.Program.Shirts15" : "Shirts 15'",
    "LaundryCare.Dryer.Program.Pillow" : "Pillow",
    "LaundryCare.Dryer.Program.AntiShrink" : "Anti-Shrink",
    "LaundryCare.Dryer.Program.WoolFinish" : "Wool",

    "LaundryCare.Dryer.Program.MyTime.MyDryingTime" : "Variable Time",
    "LaundryCare.Dryer.Program.TimeCold" : "Variable Time - Cold",
    "LaundryCare.Dryer.Program.TimeWarm" : "Variable Time - Warm",
    "LaundryCare.Dryer.Program.InBasket" : "Variable Time - In Basket",

    "LaundryCare.Dryer.Program.TimeColdFix.TimeCold20" : "Fix Time 20'- Cold",
    "LaundryCare.Dryer.Program.TimeColdFix.TimeCold30" : "Fix Time 30'- Cold",
    "LaundryCare.Dryer.Program.TimeColdFix.TimeCold60" : "Fix Time 60'- Cold",
    "LaundryCare.Dryer.Program.TimeWarmFix.TimeWarm30" : "Fix Time 30'- Warm",
    "LaundryCare.Dryer.Program.TimeWarmFix.TimeWarm40" : "Fix Time 40'- Warm",
    "LaundryCare.Dryer.Program.TimeWarmFix.TimeWarm60" : "Fix Time 60'- Warm",
    "LaundryCare.Dryer.Program.Dessous" : "Dessous",

    "LaundryCare.Dryer.Option.DryingTarget" : "Drying Target",

    "LaundryCare.Dryer.EnumType.DryingTarget.IronDry" : "Iron Dry",
    "LaundryCare.Dryer.EnumType.DryingTarget.CupboardDry" : "Cupboard Dry",
    "LaundryCare.Dryer.EnumType.DryingTarget.CupboardDryPlus" : "Cupboard Dry Plus",

}

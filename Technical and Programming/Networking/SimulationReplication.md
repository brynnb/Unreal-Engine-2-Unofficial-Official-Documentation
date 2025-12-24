# Simulation Replication

*Document Summary: a bit about replication and simulation.**Document Changelog: Created by Michiel Hendriks, to extend the [NetworkingTome](https://udn.epicgames.com/Two/NetworkingTome).*

* [Simulation Replication](#simulation-replication)
  + [Overview](#overview)
  + [Simulated function](#simulated-function)

## Overview

Simulated functions are used to help the client simulate the behavior of a given actor on the client. These simulated functions are executed both on the server and on the client. For example, a rocket's HitWall function is simulated so that it will explode both on the server and on the client. The client will then be able to simulate the explosion when the client sees it happen, and not have to wait an additional 300 ms for the server to notify the client of what to do.This document is part of the [NetworkingTome](https://udn.epicgames.com/Two/NetworkingTome).More information about function replication can be found in the [FunctionReplication](FunctionReplication.md#function_replication_and_simulat) document.

## Simulated function

Variables can be replicated simply by adding a replication statement for them, this is not the case for functions. Only in case when the `RemoteRole` is `ROLE_AutonomousProxy` functions can be replicated when there's a replication statement for them. When the `RemoteRole` is `ROLE_SimulatedProxy` the functions also have to be declared with the keyword `simulated`.For example:

```

replication
{
   reliable if (Something == true)
      func1, func2;
}

simulated function func1(int arg);

function func2(int arg);

defaultproperties
{
   RemoteRole=ROLE_SimulatedProxy
}
```

In the above function only *func1* will be replicated. *func2* will only be replicated when `RemoteRole` is set to `ROLE_AutonomousProxy`.If the function is not simulated or native and the `RemoteRole` is `ROLE_SimulatedProxy` or less then it will be absorbed and never executed locally. So in the above example *func2* will never execute when it is called. *func1* will always be executed, if the it passes the replication conditions it will be executed remotely otherwise it will be executed locally. The replication conditions that will have to be met for functions to be replicated are:

1. the `Role` is `ROLE_Authority` and the actor this function is called in is owned by the replication destination (which would be a `PlayerController` class)
2. the replication expression results in true


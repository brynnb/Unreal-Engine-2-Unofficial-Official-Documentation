# Saving Object Configurations to ini Files

*Last updated by Richard 'vajuras' Osborne ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)) for document creation.*

* [Saving Object Configurations to ini Files](SaveConfiguration.md#Saving Object Configurations to ini Files)
  + [Save Object Configurations](SaveConfiguration.md#Save Object Configurations)
  + [Declaring the Ini Filename](SaveConfiguration.md#Declaring the Ini Filename)
  + [Ini Configurations and Inheritance](SaveConfiguration.md#Ini Configurations and Inheritance)
  + [Dynamic vs Static Configuration](SaveConfiguration.md#Dynamic vs Static Configuration)

## Save Object Configurations

The unreal engine has the ability to save the configuration of an object to any desired ini file. The syntax of an unrealscript/engine ini file is very straight forward and easily traceable to the Object that created the entry (the IniFilesTutorial? reviews how the *tags* in ini files work and traces many of the engine entries).

## Declaring the Ini Filename

The class declaration contains the filename of the new ini file. For example, the following example class declares that it's variables will be saved to User.ini file:

```

class MyController extends Controller
   config(user);
```

If you do not declare a filename for the ini file, the engine will simply store the contents to UW.ini by default. The following example code demonstrates this:

```

class TestConfig extends Actor
   config;

var config int X;

function postbeginplay()
{
   X=5;
   SaveConfig();
}
```

When the *TestConfig* actor is created, it will set the value of X and save it's configuration. The UW.ini file will be updated with the following:

```

[UDN.TestConfig]
X=5
```

The next time the *TestConfig* actor is created, the default value of X will equal 5. Even if you were to remove the **PostBeginPlay** function from the actor, X will be set to equal the value 5.If you declare a new ini filename, then that file will be created. The example below shows an object that declares a new ini file:

```

class TestConfig extends Actor
   config(UDN);
```

## Ini Configurations and Inheritance

Configuration variables are inherited by subclasses. However, if SaveConfig() is called on a child of TestConfig, the value of X is stored for the child class. The example below extends TestConfig:

```

class TestConfigChild extends TestConfig;

function postbeginplay()
{
   X=15;
   SaveConfig();
}
```

When the TestConfigChild actor is spawned, the configuration for this object is saved:

```

[UDN.TestConfigChild]
X=15
```

## Dynamic vs Static Configuration

There are two different methods programmers can use to save an object's configuration to an ini file: dynamic and static. Basically, this simply means the runtime variables are saved if you call SaveConfig() on an instance of an object. Calling StaticSaveConfig() on a class variable will write the objects *default* values to the ini file. The examples above all covered saving the configuration of a runtime object. The following snippet saves the default value of X.

```

class'TestConfigChild'.default.X = 30;
class'TestConfigChild'.static.StaticSaveConfig();
```

The default value of X is written to the ini file.

```

[UDN.TestConfigChild]
X=30
```
